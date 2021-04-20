#!/usr/bin/python3
import logging
import math
from pathlib import Path
from . import gvalid
from .. import math_wrappers
from fractions import Fraction
from .. import readonly as ro
from ..readonly import INPUT_ID, PLL_ID, PLL_INDEX, OUTPUT_ID, PLL_OUTPUT
from ..readonly import PHASESYNC_NEUTRAL, FLEXIO_ID, FLEXIO_MONITORING, OUTPUT_DE_SWING, INPUT_special_intsync
from ..utilities import format_frequency, is_emptydir
from .. import arithmetic_parser
from ..backend import pll_order_selection
import pprint
# Frequency Planning Modules
from ..realtime.Output_Delay_Driver import program_delay_PLL
from ..freqplan.Zeus_freq_planning_V1_4 import report_err_fvco_fref_clash, report_warn_fvco_fvco_clash, report_warn_clash_adj_sync_fout_freerun

logger = logging.getLogger(__name__)
def get_gui_state(state):
    #read
    fr = open("number.txt",'r')
    numb = fr.read()
    fr.close()
    #write
    fw = open("number.txt",'w')
    new_num = int(numb)+1
    fw.write(str(new_num))
    print(numb)
    fw.close()
    
    ############# create_py file ############
    formate = pprint.pformat(state)
    num = numb
    no = "Profile"+num
    nme="test"
    ash = "\n\n############################################################# "+no+" #############################################################\n\n"
    imp = "from fractions import Fraction\n"
    f = open(no+".py",'w')
    f.write(imp+ash+nme+" = "+str(formate))
    f.close()


def common_validations(gui_state, *, variant, batch):
    '''
    These are GUI validations, too complex to be implemented on the widgets
    themselves. Maybe they depend on too many widget values.

    Some are pure lazyness, and could (technically) be moved to the widgets.

    `batch`: Run some validations that only make sense on the batch mode.
             Re-implements the GUI validations. See #551
    '''
    result = gvalid.Results()
    get_gui_state(gui_state)
    crystal = gui_state['crystal']
    inputs = gui_state['inputs']
    outputs = gui_state['outputs']['value']
    plls = gui_state['plls']
    gpio = gui_state['gpio']

    # Inputs -> PLL
    inputs_pll = {i: [] for i in INPUT_ID}
    for i in INPUT_ID:
        if inputs[i]['enabled']:
            inputs_pll[i] = [p for p, pi in inputs[i]['value']['plls'].items() if pi is True]
    # PLL -> Outputs
    pll_outputs = {p: [] for p in PLL_ID}
    for o in OUTPUT_ID:
        output_pll = outputs[o]['value']['pll']['value']
        if output_pll != '':
            pll_outputs[output_pll].append(o)
    pll_mode = {p: plls[p]['value']['free_running']['value']['mode']['value'] for p in PLL_ID}

    # TODO: Harmonise with GUI `validate_fxtal`
    if crystal['freq']['valid']:
        frequency = crystal['freq']['parsed']
        if crystal['doubler']:
            frequency = frequency * 2
        if gvalid.range(*ro.CRYSTAL_MODE_RANGE[crystal['mode']], fn=arithmetic_parser.parser_Hz)(frequency):
            # Inside the valid range, validate the warning range
            for rwarn in ro.CRYSTAL_MODE_RANGES_WARN:
                if not crystal['doubler'] and gvalid.range(*rwarn, fn=arithmetic_parser.parser_Hz)(frequency):
                    if rwarn[0] is None:
                        mdelta = 'less than %s' % format_frequency(rwarn[1])
                    elif rwarn[1] is None:
                        mdelta = 'more than %s' % format_frequency(rwarn[0])
                    message = 'Doubler is recommended to be enabled for references %s' % mdelta
                    # Inside the warning range
                    result.add_warning('crystal_warn_doubler',
                                       message=message,
                                       rargs=rwarn
                                       )
        else:
            # Outside the valid range
            result.add_error('crystal_freq_error',
                             message='Invalid Crystal Frequency')

    FOUT_ADJACENT_VALUE_MIN = arithmetic_parser.parser_Hz('12kHz')
    FOUT_ADJACENT_VALUE_MAX = arithmetic_parser.parser_Hz('20MHz')
    FOUT_ADJACENT_SEDE_VALUE_MIN = arithmetic_parser.parser_Hz('100kHz')
    FOUT_ADJACENT_SEDE_VALUE_MAX = arithmetic_parser.parser_Hz('20MHz')
    for x in range(len(OUTPUT_ID) - 1):
        oname1, oname2 = OUTPUT_ID[x], OUTPUT_ID[x + 1]
        o1, o2 = outputs[oname1], outputs[oname2]
        # Check that both outputs are enabled, and from different PLL
        if o1['enabled'] and o2['enabled'] and o1['value']['pll'] != o2['value']['pll']:
            # Check that both outputs are valid
            if o1['value']['freq']['valid'] and o2['value']['freq']['valid']:
                # Implements:: fout_adjacent_value_checker
                # TODO: Implement this in the output widgets
                delta = abs(o1['value']['freq']['parsed'] - o2['value']['freq']['parsed'])
                if FOUT_ADJACENT_VALUE_MIN <= delta <= FOUT_ADJACENT_VALUE_MAX:
                    result.add_warning('fout_adjacent_value_checker',
                                       message='%s|%s: Adjacent outputs are within [%s to %s] and will result in jitter degradation. It is recommended to space the outputs for best jitter performance\n' % (oname1, oname2, '12kHz', '20MHz'),
                                       delta=delta,
                                       outputs=(oname1, oname2),
                                       )
                # Implements:: fout_SE_DE_adjacent_value_checker
                states = (o1['value']['m_se']['state'], o2['value']['m_se']['state'])
                if 'se' in states and 'de' in states:
                    # SE and DE outputs side by side
                    if states == ('se', 'de'):
                        o_se = o1
                        oname_se = oname1
                        o_de = o2
                        oname_de = oname2
                    else:
                        o_se = o2
                        oname_se = oname2
                        o_de = o1
                        oname_de = oname1
                    for n, n_name in [(2, '2nd'), (3, '3rd')]:
                        delta = abs(n * o_se['value']['freq']['parsed'] - o_de['value']['freq']['parsed'])
                        if FOUT_ADJACENT_SEDE_VALUE_MIN < delta < FOUT_ADJACENT_SEDE_VALUE_MAX:
                            msg = 'There might be a in-band spur due to the %s harmonic of SE Output %s (%s) coupling with DE Output %s (%s); Spacing out the outputs is recommended for low jitter application' % (
                                n_name,
                                oname_se,
                                format_frequency(o_se['value']['freq']['parsed']),
                                oname_de,
                                format_frequency(o_de['value']['freq']['parsed'])
                            )
                            result.add_warning('fout_SE_DE_adjacent_value_checker',
                                               message=msg,
                                               harmonic=n,
                                               delta=delta,
                                               outputs=(oname_se, oname_de),
                                               )

    # Implements:: SE_type_outputs_complementary_format_checker
    # TODO: Implement this in the output widgets
    for o in OUTPUT_ID:
        se = outputs[o]['value']['m_se']
        if se['state'] == 'se':
            value = se['value']
            value_enabled = [value[v]['enabled'] for v in list(value.keys())]
            acceptable_values = [
                {
                    'on': {'enabled': True, 'value': 'clkn'},
                    'op': {'enabled': True, 'value': 'clkp'},
                },
                {
                    'on': {'enabled': True, 'value': 'clkp'},
                    'op': {'enabled': True, 'value': 'clkn'},
                },
            ]
            # If both are enabled, check if their values are different
            if False not in value_enabled and value not in acceptable_values:
                result.add_warning('SE_type_outputs_complementary_format_checker',
                                   message='It is recommended to select complimentary (out of phase) output format for "Output %s > SE" to minimize output cross-talk' % o,
                                   output=o,
                                   )
            if True not in value_enabled:
                result.add_error('SE_type_outputs_OP_ON',
                                 output=o,
                                 message='For "Output %s > SE" , OP or ON is mandatory' % o,
                                 )
    # On the Fly error messages
    if gui_state['on_the_fly']['enabled'] is True:
        logger.debug('Checking messages for ON THE FLY CHANGE')
        if gui_state['on_the_fly']['value']['single'] == []:
            result.add_error('On the Fly mode:Frequencies',
                             message='No output frequencies specified for On the Fly Mode',
                             )
        fouts = [outputs[x]['value']['freq']['parsed'] for x in OUTPUT_ID if outputs[x]['enabled'] is True]
        frac_fout_fly = [arithmetic_parser.parser_Hz(x) for x in gui_state['on_the_fly']['value']['single']]
        for fout in fouts:
            if fout not in frac_fout_fly:
                result.add_error('On the Fly mode:Fout Valid',
                                 message='%s does not match the fouts in the fouts list' % fout,
                                 )
        logger.debug('PLL Outputs')
        for p, p_outputs in pll_outputs.items():
            logger.debug('  %r|%r', p, p_outputs)
            output_freqs = [outputs[o]['value']['freq']['parsed'] for o in p_outputs]
            if len(set(output_freqs)) > 1 and len(set(output_freqs)) == len(output_freqs):
                result.add_error('On the Fly mode:PLL outputs',
                                 message='PLLs should have outputs at the same frequency in on the fly mode. Check PLL%s' % p,
                                 )
    # FVCO fuse lock error message
    # TODO: Move this to the widget itself
    for p in PLL_ID:
        # Check whether fuselock is enabled
        # get fuse_fvco parced value = Fraction(25000000, 1)
        # get output frequencies of each PLL
        # Check whether fuse lock fvco is an integer multiple of output frequency
        # If not print error message
        if plls[p]['value']['fuse_lock']['enabled'] is True:
            fvco = plls[p]['value']['fuse_lock']['value']['fvco']['parsed']
            for o in OUTPUT_ID:
                output_obj = outputs[o]['value']
                if p == output_obj['pll']['value']:
                    output_freq = output_obj['freq']['parsed']
                    if output_freq:
                        integer = (fvco / output_freq)
                        if int(integer) != integer:
                            result.add_error('Fuse FVCO',
                                             message='Fuse lock FVCO %s for PLL %s should be an integer multiple of Output %s with frequency %s' % (format_frequency(fvco), p, o, format_frequency(output_freq)),
                                             )

    # Implements:: https://support.powertools-tech.com/PowertoolsTech/Support/AuraAuro_GUI/issues/184#note_5850
    if set([outputs[o]['value']['pll']['value'] for o in OUTPUT_ID]) == set(['']):
        result.add_error('check::pll-output',
                         message='There should be at least one PLL with an output.',
                         )
    # Validate "Input #3 Sync"
    for p in PLL_ID:
        if plls[p]['value']['in3_sync'] is True:
            i = '3P'
            if not inputs[i]['enabled']:
                result.add_error('in3_sync:pll:enabled',
                                 message='PLL %s: "Input #3 Sync" requires input %s to be enabled.' % (p, i),
                                 input=i,
                                 pll=p,
                                 )

    # PLL PTP / Filtering interaction
    for p in PLL_ID:
        if plls[p]['value']['ptp']['enabled'] and plls[p]['value']['free_running']['enabled']:
            if plls[p]['value']['free_running']['value']['sw_oc']['state'] == 'ext':
                result.add_error('ptp:pll:filter_external',
                                 message='PLL %s: External Filter and PTP are incompatible' % p,
                                 pll=p,
                                 )

    # TODO: Implement this on the GUI itself
    if gui_state['phase_sync']['enabled']:
        synced_pll = [p for p in PLL_ID if p!=PHASESYNC_NEUTRAL and gui_state['phase_sync']['value'].get(p, False)]
        if len(set([tuple(plls[p]['value']['order_in']) for p in synced_pll])) != 1:
            result.add_error('phase_sync:input_order',
                             message='Phase Sync: All Input Order for all Synced PLL must be the same.',
                             pll=synced_pll,
                             )
        if synced_pll == [PHASESYNC_NEUTRAL]:
            result.add_error('phase_sync:empty',
                             message='Phase Sync: There must be at least one PLL selected other than PLL A.',
                             )

    # Implements:: https://support.powertools-tech.com/PowertoolsTech/Support/AuraAuro_GUI/issues/521
    # TODO: Implement this on the GUI itself
    if gui_state['golden_clock'] in INPUT_ID:
        i = gui_state['golden_clock']
        ivalue = inputs[i]['value']
        values = [
            ivalue['clock_switch']['fd_coarse'],
            ivalue['clock_switch']['fd_fine'],
            ivalue['drift_coarse']['enabled'],
            ivalue['drift_fine']['enabled']
        ]
        if False in values:
            result.add_error('golden_clock:input',
                             message='Input %s: Golden Clock requires Drift Monitor and Clock Switch (Coarse and Fine)' % i,
                             input=i,
                             )

    ext_zdm_feedback_unique = []
    ext_zdm_output_unique = []
    for p in PLL_ID:
        if plls[p]['enabled'] and plls[p]['value']['free_running']['enabled']:
            inputs_to_pll = plls[p]['value']['order_in']
            # Phase hopping fastlock and ZDB None not possible together
            if plls[p]['value']['free_running']['value']['mode']['value'] == 'phfl':
                # Issue warning if CL thresholds>=2 when PLL is in Phase Hopping fast lock
                for inp in INPUT_ID:  # TODO: Maybe `inputs_to_pll`
                    if inputs[inp]['enabled']:
                        if inputs[inp]['value']['clock_loss']['value']['edge_clear']['parsed'] < 2:
                            result.add_warning('clock_loss_Clear',
                                               message='Input %s > Clock loss > Clear edge :Clear edge can not be < 2 edges when Phase Hopping FastLock is enabled for PLL%s.' % (inp, p),
                                               pll=p,
                                               input=inp,
                                               )
                        if inputs[inp]['value']['clock_loss']['value']['edge_trigger']['parsed'] < 2:
                            result.add_warning('clock_loss_Trigger',
                                               message='Input %s > Clock loss > Trigger edge :Triggr edge can not be < 2 edges when Phase Hopping FastLock is enabled for PLL%s.' % (inp, p),
                                               pll=p,
                                               input=inp,
                                               )
                if plls[p]['value']['free_running']['value']['zdm']['state'] == '':
                    result.add_error('pll_zdm_phfl',
                                     message='PLL %s > ZDM: Internal or external mode required for Phase Hopping FastLock.' % p,
                                     pll=p,
                                     )
            # ZDM Validations
            p_zdm = plls[p]['value']['free_running']['value']['zdm']
            if p_zdm['state'] == 'external':
                if p_zdm['external']['feedback']['valid'] and p_zdm['external']['output']['valid']:
                    zdm_feedback = p_zdm['external']['feedback']['parsed']
                    zbm_out = p_zdm['external']['output']['value']
                    ext_zdm_feedback_unique.append(zdm_feedback)
                    ext_zdm_output_unique.append(zbm_out)
                    if zdm_feedback in inputs_to_pll:
                        result.add_error('pll_zdm_efeedback',
                                         message='PLL %s > ZDM: Invalid External Feedback "%s"' % (p, zdm_feedback),
                                         pll=p,
                                         input=zdm_feedback,
                                         )

                    if not inputs[zdm_feedback]['enabled']:
                        result.add_error('pll_zdm_ext_feedback_enable',
                                         message='PLL %s > ZDM: External feedback "%s" must be enabled' % (p, zdm_feedback),
                                         pll=p,
                                         input=zdm_feedback,
                                         )

                    # For ext zdm, input and output freq must be same
                    zdm_input_freq = inputs[zdm_feedback]['value']['freq']['parsed']
                    if outputs[zbm_out]['value']['freq']['parsed'] != zdm_input_freq:
                        result.add_error('pll_zdm_ext_output_enable',
                                         message='PLL %s > ZDM: External feedback "%s" frequency and External Output "%s" frequency must be same.' % (p, zdm_feedback, zbm_out),
                                         pll=p,
                                         )
                    # Output selected in Ext ZDB output dropdown must be enabled
                    if not outputs[zbm_out]['enabled']:
                        result.add_error('pll_zdm_ext_output_enable',
                                         message='PLL %s > ZDM: External Output "%s" must be enabled' % (p, zbm_out),
                                         pll=p,
                                         input=zbm_out,
                                         )
                    if outputs[zbm_out]['enabled'] and outputs[zbm_out]['value']['pll']['value'] != p:
                        result.add_error('pll_zdm_ext_output_match',
                                         message='PLL %s > ZDM: Selected external Output "%s" must be connected to PLL %s' % (p, zbm_out, p),
                                         pll=p,
                                         input=zbm_out,
                                         )
                    for inp_pll in inputs_to_pll:
                        if zdm_input_freq != inputs[inp_pll]['value']['freq']['parsed']:
                            result.add_warning('pll_zdm_same_freq',
                                               message='PLL %s > ZDM: When ZDM external is enabled, it is recommended to have same input frequency as External feedback "%s" for all inputs.' % (p, zdm_feedback),
                                               pll=p,
                                               input=zdm_feedback,
                                               )

            if p_zdm['state'] != '':
                if plls[p]['value']['free_running']['value']['clock_switch']['hitless']['ph_bout'] == 'buildout':
                    result.add_error('pll_zdm_phaseBO',
                                     message='PLL %s > ZDM: When ZDM external or internal is enabled, Phase Build Out is not supported.' % p,
                                     pll=p,
                                     )

                if plls[p]['value']['in3_sync']:
                    result.add_error('pll_zdm_and_in3sync',
                                     message='PLL %s > ZDM: ZDM & "Input #3 Sync" cannot be enabled for same PLL' % p,
                                     pll=p,
                                     )

        # If in3sync enabled, input 3P cannot go to that PLL 3P or diff
        if plls[p]['value']['in3_sync']:
            i3s = ['3P']
            assert set(i3s).issubset(set(INPUT_ID))  # Guarantee that these inputs exist
            for i in i3s:
                if i in plls[p]['value']['order_in']:
                    result.add_error('pll_in3sync_3p',
                                     message='PLL %s > Input #3 Sync: When enabled, input %s cannot be active clock to that PLL' % (p, i),
                                     input=i,
                                     pll=p,
                                     )

    if len(ext_zdm_feedback_unique) != len(set(ext_zdm_feedback_unique)):
        result.add_error('multiple_pll_zdm_ext',
                         message='Same ZDM external feedback clock cannot be used across multiple PLLs.',
                         plls=list(sorted(set(ext_zdm_feedback_unique))),
                         )
    if len(ext_zdm_output_unique) != len(set(ext_zdm_output_unique)):
        result.add_error('multiple_pll_zdm_ext',
                         message='Same ZDM external output clock cannot be used across multiple PLLs.',
                         plls=list(sorted(set(ext_zdm_output_unique))),
                         )

    # Input TDC requires only active clocks
    iTDC = False
    ITDC_INPUT_MAX = arithmetic_parser.parser_Hz('250 MHz')
    for itdc in ro.INPUTTDC_ID:
        itdc_channel = gui_state['inputtdc']['tdcs'][itdc]
        if itdc_channel['enabled']:
            clks = ['clk1', 'clk2']
            tdc_clks = [itdc_channel['value'][clk]['value'] for clk in clks]
            for clkn, tpl in enumerate(zip(clks, tdc_clks)):
                clk, tdc_clk = tpl
                if tdc_clk in INPUT_ID:
                    iTDC = True
                    if inputs[tdc_clk]['enabled']:
                        # Check input frequency
                        clk_freq = inputs[tdc_clk]['value']['freq']['parsed']
                        if inputs[tdc_clk]['value']['freq']['valid']:
                            if clk_freq > ITDC_INPUT_MAX:
                                msg = 'Input TDC > Channel %s > Clock #%d: "%s" frequency cannot exceed %s.' % (
                                    itdc,
                                    clkn,
                                    tdc_clk,
                                    format_frequency(ITDC_INPUT_MAX)
                                )
                                result.add_error('itdc_active_clk_freq',
                                                 message=msg,
                                                 itdc=itdc,
                                                 clk=clk,
                                                 input=tdc_clk,
                                                 )
                    else:
                        # Input is disabled
                        result.add_error('itdc_active_clk',
                                         message='Input TDC > Channel %s > Clock #%d: "%s" input clock must be enabled.' % (i, clkn, tdc_clk),
                                         itdc=itdc,
                                         clk=clk,
                                         input=tdc_clk,
                                         )
            tdc_clk1, tdc_clk2 = tdc_clks
            valid_tdcs = tdc_clk1 in INPUT_ID and tdc_clk2 in INPUT_ID
            # Reimplements `InputTDCSpec.setup_containervalid`, sort of
            if valid_tdcs and inputs[tdc_clk1]['enabled'] and inputs[tdc_clk2]['enabled']:
                clk1_freq = inputs[tdc_clk1]['value']['freq']['parsed']
                clk2_freq = inputs[tdc_clk2]['value']['freq']['parsed']
                if None not in (clk1_freq, clk2_freq) and clk1_freq != clk2_freq:
                    if not (clk2_freq % clk1_freq == 0 or clk1_freq % clk2_freq == 0):
                        msg = 'Input TDC > Channel %s: Clock #1 and #2 ("%s" and "%s") frequencies must be same or integer related.' % (
                            itdc,
                            tdc_clk1,
                            tdc_clk2,
                        )
                        result.add_warning('itdc_clk_integer_relation',
                                           message=msg,
                                           itdc=itdc,
                                           )

    if iTDC:
        special_pll = 'FT'
        assert special_pll in PLL_ID
        if not plls[special_pll]['enabled']:
            result.add_error('itdc_FTpll',
                             message='Input TDC requires PLL %s to be enabled. Please add at least one input clock to enable PLL %s.' % (special_pll, special_pll),
                             p=special_pll,
                             )

    # checker to avoid SDCO loop
    SDCO_info = {}  # TODO: {p: {'tx': [], 'rx': []} for p in ro.PLL_ID if p not in ro.PLL_special}
    SDCO_mult_pll_enabled = []
    for p in PLL_ID:
        receiver_rx1 = plls[p]['value']['smartdco']['receiver']['value']['rx1']
        receiver_rx2 = plls[p]['value']['smartdco']['receiver']['value']['rx2']
        receiver_rx1_pll = [receiver_rx1['value']['pll']['parsed']] if receiver_rx1['enabled'] else []
        receiver_rx2_pll = [receiver_rx2['value']['pll']['parsed']] if receiver_rx2['enabled'] else []
        if receiver_rx1['enabled'] or receiver_rx2['enabled']:
            SDCO_mult_pll_enabled.append(p)
        SDCO_info[p] = {
            "tx": [
                *receiver_rx1_pll,
                *receiver_rx2_pll
            ],
            "rx": [],
        }
        special_pll = 'FT'
        assert special_pll in PLL_ID
        if (receiver_rx1_pll or receiver_rx2_pll) == special_pll:
            if not plls[special_pll]['enabled']:
                result.add_error('sdco_FTpll',
                                 message='SDCO requires PLLFT to be enabled.',
                                 )

    if len(SDCO_mult_pll_enabled) > 1:
        try:
            pll_order_selection.PLL_ORDER(SDCO_info).final_order
        except pll_order_selection.TxRxLoopingError as e:
            result.add_error('sdco_loop',
                             message=f'SmartDCO > {e.error}',
                             plls=SDCO_mult_pll_enabled,
                             )

    # INTSYNC clock cannot be floating
    if inputs[ro.INPUT_special_intsync]['enabled']:
        if not (True in [inputs[ro.INPUT_special_intsync]['value']['plls'][p] for p in PLL_ID]):
            result.add_error('Intsync_floating_ip',
                             message='INTSYNC clock is enabled, but not connected to any PLL.',
                             )

    for o in OUTPUT_ID:
        omodes = {
            'sys_ref': outputs[o]['value']['sys_ref']['enabled'],
            'syncb': outputs[o]['value']['syncb'],
            'phfl': outputs[o]['value']['phfl'],
        }
        if True in omodes.values():
            # At least one mode configured
            opll = outputs[o]['value']['pll']['value']
            if opll in PLL_ID:
                opll_mode = pll_mode[opll]
                if True in (v for k, v in omodes.items() if k != opll_mode):
                    result.add_error('output_pllmode',
                                     message='Output %s: Invalid setup for PLL %s Mode %s' % (o, opll, opll_mode),
                                     output=o,
                                     pll=opll,
                                     pll_mode=opll_mode,
                                     )

    if gui_state['acg']['enabled']:
        clock_mode = gui_state['acg']['value']['clock_mode']
        if clock_mode['parsed']:
            # Input 4N
            # Input 4 Single Ended
            # PLL D
            # Output 5
            # Output 6
            # Output 7
            i_4N, i_4_se, p_D, o_5, o_6, o_7 = {
                0b00: (True, True, True, True, True, True),
                0b01: (False, False, False, False, False, False),
                0b10: (False, False, False, False, True, False),
                0b11: (False, False, False, False, False, False),
            }[clock_mode['parsed']]
            if '4N' in ro.INPUT_ID:
                if i_4N is False and inputs['4N']['enabled']:
                    result.add_error('acg:inputs:4N',
                                     message='ACG "%s" is incompatible with Input 4N' % clock_mode['value'],
                                     acg=clock_mode['parsed'],
                                     input='4N',
                                     )
                if i_4_se is False and gui_state['inputs_diff'][ro.INPUT_DIFFERENTIAL.master('4N')]:
                    result.add_error('acg:inputs:4_SingleEnded',
                                     message='ACG "%s" is incompatible with differential Input 4' % clock_mode['value'],
                                     acg=clock_mode['parsed'],
                                     input='4N',
                                     )
            if p_D is False:
                if plls['D']['enabled']:
                    result.add_error('acg:plls:D',
                                     message='ACG "%s" is incompatible with PLL D' % clock_mode['value'],
                                     acg=clock_mode['parsed'],
                                     pll='D',
                                     )
            for o, o_state in [('5', o_5), ('6', o_6), ('7', o_7)]:
                if o_state is False and outputs[o]['enabled']:
                    result.add_error('acg:outputs:%s' % o,
                                     message='ACG "%s" is incompatible with Output %s' % (clock_mode['value'], o),
                                     acg=clock_mode['parsed'],
                                     output=o,
                                     )

    if batch is True:
        for p in PLL_ID:
            # Pll_SmartDCO
            smartdco = plls[p]['value']['smartdco']
            for tx, smartdco_tx in smartdco['transmitter']:
                if smartdco_tx['ppath'] is True and smartdco_tx['ipath'] is False:
                    result.add_error('batch::pll_smartdco::tx',
                                     message='PLL {p}: Invalid Transmitter {tx}: P-Path requires I-Path',
                                     pll=p,
                                     tx=tx,
                                     )
        # Output_DE
        # TODO: Reimplement `calc_validation__vddo_type`
        for o in OUTPUT_ID:
            de = outputs[o]['value']['m_de']
            if de['state'] == 'de':
                swing_values, it = OUTPUT_DE_SWING.get(de['value']['submode']) or ([], False)
                if len(swing_values) > 0:
                    if de['value']['swing']['parsed'] not in swing_values:
                        result.add_error('batch::output_de:swing',
                                         message=f'Output {o}: Invalid Swing for submode',
                                         output=o,
                                         )
                if it is False and de['value']['it'] is True:
                    result.add_error('batch::output_de:it',
                                     message=f'Output {o}: Invalid Internal Termination for submode',
                                     output=o,
                                     )

        # Implemented on the GUI side already
        if INPUT_special_intsync in inputs:
            super_special_pll = 'B'
            if inputs[INPUT_special_intsync]['enabled'] and plls[super_special_pll]['enabled']:
                result.add_error('intsync_pllB',
                                 message='Input %s requires PLL %s to be enabled' % (INPUT_special_intsync, super_special_pll),
                                 input=INPUT_special_intsync,
                                 pll=super_special_pll,
                                 )

    for g in ro.GPIO_ID:
        for p in [p for p in PLL_ID if p not in ro.PLL_special]:
            if gpio['gpio']['value'][g]['input']['value']['pll']['value'][p]:
                if not plls[p]['enabled']:
                    result.add_warning('gpio_pll',
                                       message='GPIO%s > Input: PLL %s is not an active PLL' % (g, p),
                                       gpio=g,
                                       p=p,
                                       )

    pll_dco_select_bit = []
    manual_input_clock_select_bit = []
    pll_syncb_select_bit = []
    for g in ro.GPIO_ID:
        gpio_val = gpio['gpio']['value'][g]['configuration']['value']['value']
        # pll_dco_select_bit
        if gpio_val.startswith('PLL DCO Select Bit'):
            pll_dco_select_bit.append(int(gpio_val[-1]))
        # manual_input_clock_select_bit
        if gpio_val.startswith('Manual Input Clock Select Bit'):
            manual_input_clock_select_bit.append(int(gpio_val[-1]))
        # pll_syncb_select_bit
        if gpio_val.startswith('PLL SyncB Select Bit'):
            pll_syncb_select_bit.append(int(gpio_val[-1]))
        # pll enable
        if gpio_val.endswith('Manual Input Spare Clock Select'):
            pll = gpio_val[4]
            if not plls[pll]['enabled']:
                result.add_warning('manual_input_spare_clock_select',
                                   message='GPIO > Config > Selection:PLL %s is not an active PLL' % pll,
                                   pll=pll,
                                   )
            else:
                if plls[pll]['value']['free_running']['value']['ip_clock']['select'] == 'Auto':
                    msg = 'GPIO: PLL %s IP clock selction has highest priorty over GPIO selection: %s' % (
                        pll,
                        gpio_val,
                    )
                    result.add_warning('manual_input_spare_clock_select_ip_clock',
                                       message=msg,
                                       pll=pll,
                                       gpio=gpio_val
                                       )
    # pll_dco_select_bit
    if len(pll_dco_select_bit) > 0:
        pll_dco_select_bit_max = max(pll_dco_select_bit)
        for pll_dco_select_bit_i in range(pll_dco_select_bit_max):
            if pll_dco_select_bit_i not in pll_dco_select_bit:
                msg = 'GPIO: PLL DCO Select Bit %d is selected, so PLL DCO Select Bit %d must be selected in any of the other GPIOs' % (
                    pll_dco_select_bit_max,
                    pll_dco_select_bit_i,
                )
                result.add_error('gpio_selection_pll_DCO_bit',
                                 message=msg,
                                 )

    # manual_input_clock_select_bit
    if len(manual_input_clock_select_bit) > 0:
        manual_input_clock_select_bit_max = max(manual_input_clock_select_bit)
        for manual_input_clock_select_bit_i in range(manual_input_clock_select_bit_max):
            if manual_input_clock_select_bit_i not in manual_input_clock_select_bit:
                msg = 'GPIO: Manual Input Clock Select Bit %d is selected, so Manual Input Clock Select Bit %d must be selected in any of the other GPIOs' % (
                    manual_input_clock_select_bit_max,
                    manual_input_clock_select_bit_i,
                )
                result.add_error('gpio_manual_input_clock_select_bit',
                                 message=msg,
                                 )

    # pll_syncb_select_bit
    if len(pll_syncb_select_bit) > 0:
        pll_syncb_select_bit_max = max(pll_syncb_select_bit)
        for pll_syncb_select_bit_i in range(pll_syncb_select_bit_max):
            if pll_syncb_select_bit_i not in pll_syncb_select_bit:
                msg = 'GPIO: PLL SyncB Select Bit %d is selected, so Pll SyncB Select Bit %d must be selected in any of the other GPIOs' % (
                    pll_syncb_select_bit_max,
                    pll_syncb_select_bit_i,
                )
                result.add_error('gpio_pll_syncb_select_bit',
                                 message=msg,
                                 )

    # SDCO PLL Tx checker
    for p in PLL_ID:
        rx1 = plls[p]['value']['smartdco']['receiver']['value']['rx1']
        rx2 = plls[p]['value']['smartdco']['receiver']['value']['rx2']
        if rx1['enabled']:
            rxpll = rx1['value']['pll']['parsed']
            txl = rx1['value']['tx']
            if rx1['value']['pll']['valid']:
                if not plls[rxpll]['enabled']:
                    result.add_warning('smartdco_pll_active',
                                       message='PLL%s > SmartDCO: Enable PLL %s which is selected as Rx1 PLL in Smart DCO' % (p, rxpll),
                                       pll=p,
                                       rxpll=rxpll,
                                       )
                if not plls[rxpll]['value']['smartdco']['transmitter'][txl]['enabled']:
                    result.add_warning('smartdco_pll_rxtx',
                                       message='PLL%s > SmartDCO > Rx1 > Tx: %s of PLL %s is not enabled' % (p, txl, rxpll),
                                       pll=p,
                                       rxpll=rxpll,
                                       )
        if rx2['enabled']:
            rxpll = rx2['value']['pll']['parsed']
            txl = rx2['value']['tx']
            if rx2['value']['pll']['valid']:
                if not plls[rxpll]['enabled']:
                    result.add_warning('smartdco_pll',
                                       message='PLL%s > SmartDCO > Enable PLL %s which is selected as Rx2 PLL in Smart DCO' % (p, rxpll),
                                       pll=p,
                                       rxpll=rxpll,
                                       )
                if not plls[rxpll]['value']['smartdco']['transmitter'][txl]['enabled']:
                    result.add_warning('smartdco_pll',
                                       message='PLL%s > SmartDCO > Rx2 > Tx: %s of PLL %s is not enabled' % (p, txl, rxpll),
                                       pll=p,
                                       rxpll=rxpll,
                                       )

    return result


def freqplan_validations(global_variables, gui_state, result, *, freqplan, variant):
    '''
    Validate the global state after `api_backend.stage_one`.
    '''
    outputs = gui_state['outputs']['value']

    if global_variables.frequency_planning_error:
        # Special Case: Stage 1 (Frequency Planning) was unsuccessful, don't validate anything else
        result.add_error('frequency_planning_error', message=global_variables.frequency_planning_error)
    else:
        # Implements:: delay_write_fn
        # global array_out_global
        # logger.debug('Array Out Global: %r', array_out_global)
        logger.debug('Implements:: delay_write_fn: %r', global_variables.Pll_fvcos_for_delay)
        for p in PLL_ID:
            outputs_pll = [o for o in PLL_OUTPUT[p] if outputs[o]['value']['pll']['value'] == p]
            logger.debug('PLL %s: %r', p, outputs_pll)
            _fvco = freqplan['fvco_for_delay'][p]
            if _fvco == (0, 0):
                pll_fvco = 0
            else:
                pll_fvco = Fraction(*_fvco)
            logger.debug('|  FVCO: %r', pll_fvco)
            # Check if there is only one fout (this means disabling delay)
            if len(outputs_pll) > 1:
                # Remove 'OUT' prefix
                for o in outputs_pll:
                    delay = outputs[o]['value']['delay']['parsed'] or 0.0
                    logger.debug('| Delay[%s]: %r', o, delay)
                    coarse, fine, range_max = program_delay_PLL(pll_fvco, delay)
                    logger.debug('| RangeMax[%r]', range_max)
                    if delay >= range_max:
                        result.add_warning('delay_write_fn',
                                           message='Output %s: Delay should be < %s' % (o, range_max),
                                           output=o,
                                           )

        # Frequency Plan Validations
        report_err_fvco_fref_clash(result)
        report_warn_fvco_fvco_clash(result)
        report_warn_clash_adj_sync_fout_freerun(result)

        # Implements:: bandwidth_checker
        internal_freqs = {p: Fraction(global_variables.global_pll_internal[PLL_INDEX[p]]) for p in PLL_ID}
        outputs_pll = [outputs[o]['value']['pll']['value'] for o in OUTPUT_ID]
        logger.debug('Internal Frequencies')
        for p in PLL_ID:
            if p in outputs_pll:  # Don't check PLL without outputs
                internal_freq = internal_freqs[p]
                logger.debug('  PLL %s: %s', p, format_frequency(internal_freq))
                if internal_freq != 0:
                    bw = gui_state['plls'][p]['value']['sw_oc']
                    bw_fast = bw['fast']['parsed']
                    if bw_fast is not None:
                        limit = min(internal_freq / 100, ro.CHECKER_BW_MAX_LIMIT)
                        if bw_fast > limit:
                            result.add_warning('bandwidth_checker:fast',
                                               message='The Fast Bandwidth for PLL %s is high, please lower it to meet the constraint of "(fin_PLL / Fast Bandwidth) >= 100" to ensure PLL stabilty' % p,
                                               pll=p,
                                               limit=limit,
                                               )
                    bw_normal = bw['normal']['parsed']
                    if bw_normal is not None:
                        limit = min(internal_freq / 500, ro.CHECKER_BW_MAX_LIMIT)
                        if bw_normal > limit:
                            result.add_warning('bandwidth_checker:normal',
                                               message='The Normal Bandwidth for PLL %s is high, please lower it to meet the constraint of "(fin_PLL / Normal Bandwidth) >= 500" to ensure good jitter attenuation performance' % p,
                                               pll=p,
                                               limit=limit,
                                               )
    return result


def stage3_otf_checks(gui_state, directory: Path):
    """
    Set `directory` to None so skip validation (if it's unknown yet)
    """
    result = gvalid.Results()
    otf_state = gui_state['on_the_fly']

    if otf_state['enabled'] is True:
        if otf_state['value']['single'] == []:
            result.add_error('OTF:Frequencies',
                             message='No output frequencies specified for On the Fly Mode')

    if gui_state['phase_sync']['enabled']:
        # Go through the PLL enabled for Phase Sync
        for p in [p for p in PLL_ID if gui_state['phase_sync']['value'][p]]:
            bw = gui_state['plls'][p]['sw_oc']
            if None in (bw['fast']['parsed'], bw['normal']['parsed']):
                result.add_error('OTF:PLL:BW',
                                 message='Missing Bandwidth for Phase Sync PLL %s' % p,
                                 pll=p)

    if directory:
        if not validate_OTF_overwrite(directory):
            result.add_warning('OTF:overwrite',
                               message='Overwriting a non-empty directory')

    return result


def pll_fout_not_possible(p, pll_fout, *, config):
    fvco_min = config.fvco_pll_limits['PLL%s' % p]['min'] * 1e6
    fvco_max = config.fvco_pll_limits['PLL%s' % p]['max'] * 1e6
    lcm = math_wrappers.lcm_multipledecimal(*pll_fout)
    min_freq = math.ceil(fvco_min / lcm) * lcm
    max_freq = math.floor(fvco_max / lcm) * lcm
    return not(fvco_max >= min_freq >= fvco_min or fvco_max >= max_freq >= fvco_min)


def validate_OTF_overwrite(fpath: Path):
    if fpath.exists():
        if fpath.is_dir():
            return is_emptydir(fpath)
        else:
            return False
    else:
        return True


# Widget validations
# | Return `True` if its valid, `'valid'` otherwise

# TODO: Migrate this to Output container validations

def validate_OutputFrame(value, *, config):
    pll_ofreqs = {p: [] for p in PLL_ID}
    pll_choices = {p: [] for p in PLL_ID}  # TODO: Unused, remove
    for o in OUTPUT_ID:
        pll = value[o]['value']['pll']['value']
        if pll in PLL_ID:
            pll_choices[pll].append(o)
    pll_errors = []
    for p, pll_fout in pll_ofreqs.items():
        for o in pll_choices[p]:
            pll_ofreqs[p].append(value[o]['value']['freq']['parsed'])
        if len(pll_fout) > 0:
            if None in pll_fout or 0 in pll_fout:
                # Catastrophic Error
                return None
            elif pll_fout_not_possible(p, pll_fout, config=config):
                # Error here
                pll_errors.append(p)
    return pll_errors


def v_OutputFrame(value, *, config):
    result, message = True, None  # Default to no error
    pll_errors = validate_OutputFrame(value, config=config)
    if pll_errors is None:
        logger.debug('PLL Errors: %r', pll_errors)
        result = 'valid'  # Error
    elif len(pll_errors) > 0:
        result = 'valid'
        message = 'PLL %s cannot be synthesized' % ', '.join(sorted(pll_errors))
    return result, message


def validate_FlexIO(value):
    '''
    Validates:
    1. FlexIO selected has a Defect/Notify/Interrupt
    2. All notify/PLL notify/clckmon notify requires atleast one option to be selected
    '''
    messages = []  # Default to no error
    monitors = []
    for fid in FLEXIO_ID:
        if value['flexio'][fid]['enabled']:
            monitors.append(value['flexio'][fid]['value'])
    all_notify = 'all_not' in monitors
    if all_notify or 'pll_not' in monitors:
        if True not in [b for t, obj in value['pll_not'].items() for p, b in obj.items()]:
            messages.append(f'{FLEXIO_MONITORING["all_not"]}/{FLEXIO_MONITORING["pll_not"]} requires at least one {FLEXIO_MONITORING["pll_not"]} Option to be selected.')
    if all_notify or 'clkmon_not' in monitors:
        if True not in [b for t, obj in value['clkmon_not'].items() for i, b in obj.items()]:
            messages.append(f'{FLEXIO_MONITORING["all_not"]}/{FLEXIO_MONITORING["clkmon_not"]} requires at least one {FLEXIO_MONITORING["clkmon_not"]} Option to be selected.')
    return messages


def v_FlexIO(value):
    result, message = True, None  # Default to no error
    flexio_errors = validate_FlexIO(value)
    if len(flexio_errors) > 0:
        result = 'valid'
        message = '\n'.join(flexio_errors)
    return result, message
