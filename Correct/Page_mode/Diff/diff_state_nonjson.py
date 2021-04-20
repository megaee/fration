# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:02:17 2020

@author: Dell
"""

from fractions import Fraction
# dict1={
#   "_appversion": None,
#   "_variant": "au5315",
#   "_version": 1,
#   "algorithm": {
#     "INPUT": {
#       "0P": {
#         "bypass": True,
#         "divn1": {
#           "denominator": 4294967295,
#           "int": 1,
#           "numerator": 0
#         },
#         "doubler": False,
#         "fin_int": 100.0
#       }
#     },
#     "OUTPUT": {
#       "11": {
#         "coarse": 0,
#         "fine": 0
#       }
#     }}}

# dict2={
#   "_appversion": None,
#   "_variant": "au5518",
#   "_version": 1,
#   "algorithm": {
#     "INPUT": {
#       "0P": {
#         "bypass": True,
#         "divn1": {
#           "denominator": 4294967295,
#           "int": 1,
#           "numerator": 0
#         },
#         "doubler": False,
#         "fin_int": 100.0
#       }
#     },
#     "OUTPUT": {
#       "11": {
#         "coarse": 0,
#         "fine": 1
#       }
#     }}}

# dict1={}
# dict2={'acg': {'enabled': False, 'value': {'clock_mode': {'parsed': None, 'valid': True, 'value': ''}}}, 'comms': {'i2c': {'address': {'parsed': 91, 'valid': True, 'value': '0x5B'}}, 'spi': {'wires': 4}, 'type': 'i2c'}, 'crystal': {'doubler': True, 'freq': {'parsed': Fraction(54000000, 1), 'valid': True, 'value': '54 MHz'}, 'mode': 'LFF CL=8pF'}, 'eeprom': {'addr': {'parsed': 0, 'valid': True, 'value': '0'}, 'ibus': None, 'type': 64, 'verify': {'block': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'golden_clock': 'xtal', 'gpio': {'gpio': {'valid': True, 'value': {'0': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '1': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '2': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '3': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '4': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '5': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}, '9': {'configuration': {'clock_disqualification': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'OCXO': False}, 'value': {'parsed': 'general_purpose_inp', 'valid': True, 'value': 'General Purpose Input'}}, 'input': {'state': 'input', 'value': {'configuration': {'features': False}, 'pll': {'A': False, 'B': False, 'C': False, 'D': False}}}, 'inversion': False, 'output': {'state': 'input', 'value': {'configuration': {'clkmon': False, 'eeprom': False, 'general': False, 'pll:A': False, 'pll:B': False, 'pll:C': False, 'pll:D': False, 'pll:FT': False}, 'open_drain': False}}}}}, 'vdd': '1.8V'}, 'inputs': {'0N': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '0P': {'enabled': True, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': Fraction(5000000, 1), 'valid': True, 'value': '5M'}, 'plls': {'A': True, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '1N': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '1P': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '2N': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '2P': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '3N': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '3P': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '4N': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, '4P': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, 'INTSYNC': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}, 'OCXO': {'enabled': False, 'value': {'clock_couple': 'dc', 'clock_gap': False, 'clock_inversion': False, 'clock_loss': {'enabled': True, 'valid': True, 'value': {'edge_clear': {'parsed': 4, 'valid': True, 'value': '4'}, 'edge_trigger': {'parsed': 5, 'valid': True, 'value': '5'}}}, 'clock_switch': {'clock_loss': True, 'fd_coarse': False, 'fd_fine': False}, 'drift_coarse': {'enabled': False, 'value': {'clr': '400', 'set': '500'}, 'warn': True}, 'drift_fine': {'enabled': False, 'value': {'clr': '8', 'set': '10'}, 'warn': True}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'plls': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'valid_timer': {'parsed': Fraction(16, 125), 'valid': True, 'value': '128 ms'}}}}, 'inputs_diff': {'0P': False, '1P': False, '2P': False, '3P': False, '4P': False}, 'inputtdc': {'edge': {'0N': 'Rising', '0P': 'Rising', '1N': 'Rising', '1P': 'Rising', '2N': 'Rising', '2P': 'Rising', '3N': 'Rising', '3P': 'Rising', '4N': 'Rising', '4P': 'Rising'}, 'tdcs': {'0': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '1': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '2': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '3': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '4': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '5': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '6': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '7': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '8': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}, '9': {'enabled': False, 'valid': True, 'value': {'clk1': {'parsed': None, 'valid': True, 'value': ''}, 'clk2': {'parsed': None, 'valid': True, 'value': ''}, 'nsamples': {'parsed': 11, 'valid': True, 'value': '11'}}}}}, 'interrupt': {'eeprom': {'defect_interrupt': False}, 'input_closs': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'INTSYNC': False, 'OCXO': False}, 'input_coarse_drift': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'INTSYNC': False, 'OCXO': False}, 'input_fine_drift': {'0N': False, '0P': False, '1N': False, '1P': False, '2N': False, '2P': False, '3N': False, '3P': False, '4N': False, '4P': False, 'INTSYNC': False, 'OCXO': False}, 'pll_ho_freeze': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'pll_inner_lol': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False, 'common': False}, 'pll_outer_lol': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'pll_phase_lol': {'A': False, 'B': False, 'C': False, 'D': False, 'FT': False}, 'tdc': {'A': False, 'B': False, 'C': False, 'D': False}}, 'on_the_fly': {'enabled': False, 'value': {'multi': [], 'single': []}}, 'outputs': {'valid': True, 'value': {'0': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '1': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '10': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '11': {'enabled': True, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': Fraction(5000000, 1), 'valid': True, 'value': '5M'}, 'm_de': {'state': 'de', 'value': {'it': False, 'submode': 'LVPECL', 'swing': {'parsed': Fraction(1, 2), 'valid': True, 'value': '0.5 V'}}}, 'm_se': {'state': 'de', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': True, 'value': 'A'}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '2': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '3': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '4': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '5': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '6': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '7': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '8': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}, '9': {'enabled': False, 'valid': True, 'value': {'delay': {'parsed': Fraction(0, 1), 'valid': True, 'value': '0 s'}, 'freq': {'parsed': None, 'valid': True, 'value': ''}, 'm_de': {'state': '', 'value': {'it': False, 'submode': '', 'swing': {'parsed': None, 'valid': True, 'value': ''}}}, 'm_se': {'state': '', 'value': {'on': {'enabled': False, 'value': ''}, 'op': {'enabled': False, 'value': ''}}}, 'phfl': False, 'pll': {'enabled': False, 'value': ''}, 'syncb': False, 'sys_ref': {'enabled': False, 'value': {'continuous': '', 'pulser': {'state': '', 'value': {'count': {'parsed': None, 'valid': True, 'value': ''}}}}}, 'vddo': '3.3V'}}}}, 'phase_sync': {'enabled': False, 'value': {'A': False, 'B': False, 'C': False, 'D': False}}, 'plls': {'A': {'enabled': True, 'value': {'free_running': {'enabled': True, 'value': {'clock_switch': {'frequency_ramp': {'enabled': False, 'value': {'slope': {'parsed': None, 'valid': True, 'value': ''}}}, 'hitless': {'ph_bout': 'propagation', 'ph_prop': {'state': 'propagation', 'value': {'slope': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}}}}}, 'dco': False, 'fast_lock_ho': True, 'freq_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'ppm': {'valid': True, 'value': {'clr': {'parsed': Fraction(1, 500000), 'value': '2 ppm'}, 'set': {'parsed': Fraction(1, 250000), 'value': '4 ppm'}}}, 'timer': True}}, 'holdover': {'average': {'parsed': Fraction(547, 500), 'valid': True, 'value': '1.094 s'}, 'delay': {'parsed': Fraction(547, 1000), 'valid': True, 'value': '547 ms'}}, 'ip_clock': {'revertive': True, 'select': 'Auto'}, 'mode': {'o:phfl': {'state': '', 'value': {'delta': {'parsed': Fraction(1, 10000000), 'valid': True, 'value': '100 ns'}}}, 'value': ''}, 'phase_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'phase_delta': {'parsed': Fraction(1, 500000000), 'valid': True, 'value': '2 ns'}, 'timer': True}}, 'sw_ext': {'state': 'oc', 'value': {'decimation': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'sw_oc': {'state': 'oc', 'value': {'fast': {'parsed': Fraction(100, 1), 'value': '100', 'warn': True}, 'normal': {'parsed': Fraction(100, 1), 'value': '100', 'warn': True}}}, 'zdm': {'external': {'feedback': {'parsed': None, 'valid': True, 'value': ''}, 'output': {'parsed': None, 'valid': True, 'value': ''}}, 'state': ''}}}, 'fuse_lock': {'enabled': False, 'value': {'fvco': {'parsed': None, 'valid': True, 'value': ''}}}, 'in3_sync': False, 'lwm': False, 'order_in': ['0P'], 'ptp': {'enabled': False, 'value': {'bw': {'parsed': None, 'valid': False, 'value': ''}, 'ipath': True, 'phase_sl': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}, 'phase_ur': {'parsed': None, 'valid': False, 'value': ''}, 'ppath': True}}, 'smartdco': {'receiver': {'valid': True, 'value': {'rx1': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'rx2': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'sl': {'parsed': Fraction(1, 1000), 'valid': True, 'value': '1000 ppm/s'}}}, 'transmitter': {'tx1': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}, 'tx2': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}}}}}, 'B': {'enabled': False, 'value': {'free_running': {'enabled': False, 'value': {'clock_switch': {'frequency_ramp': {'enabled': False, 'value': {'slope': {'parsed': None, 'valid': True, 'value': ''}}}, 'hitless': {'ph_bout': 'propagation', 'ph_prop': {'state': 'propagation', 'value': {'slope': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}}}}}, 'dco': False, 'fast_lock_ho': True, 'freq_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'ppm': {'valid': True, 'value': {'clr': {'parsed': Fraction(1, 500000), 'value': '2 ppm'}, 'set': {'parsed': Fraction(1, 250000), 'value': '4 ppm'}}}, 'timer': True}}, 'holdover': {'average': {'parsed': Fraction(547, 500), 'valid': True, 'value': '1.094 s'}, 'delay': {'parsed': Fraction(547, 1000), 'valid': True, 'value': '547 ms'}}, 'ip_clock': {'revertive': True, 'select': 'Auto'}, 'mode': {'o:phfl': {'state': '', 'value': {'delta': {'parsed': Fraction(1, 10000000), 'valid': True, 'value': '100 ns'}}}, 'value': ''}, 'phase_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'phase_delta': {'parsed': Fraction(1, 500000000), 'valid': True, 'value': '2 ns'}, 'timer': True}}, 'sw_ext': {'state': 'oc', 'value': {'decimation': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'sw_oc': {'state': 'oc', 'value': {'fast': {'parsed': None, 'value': '', 'warn': True}, 'normal': {'parsed': None, 'value': '', 'warn': True}}}, 'zdm': {'external': {'feedback': {'parsed': None, 'valid': True, 'value': ''}, 'output': {'parsed': None, 'valid': True, 'value': ''}}, 'state': ''}}}, 'fuse_lock': {'enabled': False, 'value': {'fvco': {'parsed': None, 'valid': True, 'value': ''}}}, 'in3_sync': False, 'lwm': False, 'order_in': [], 'ptp': {'enabled': False, 'value': {'bw': {'parsed': None, 'valid': False, 'value': ''}, 'ipath': True, 'phase_sl': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}, 'phase_ur': {'parsed': None, 'valid': False, 'value': ''}, 'ppath': True}}, 'smartdco': {'receiver': {'valid': True, 'value': {'rx1': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'rx2': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'sl': {'parsed': Fraction(1, 1000), 'valid': True, 'value': '1000 ppm/s'}}}, 'transmitter': {'tx1': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}, 'tx2': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}}}}}, 'C': {'enabled': False, 'value': {'free_running': {'enabled': False, 'value': {'clock_switch': {'frequency_ramp': {'enabled': False, 'value': {'slope': {'parsed': None, 'valid': True, 'value': ''}}}, 'hitless': {'ph_bout': 'propagation', 'ph_prop': {'state': 'propagation', 'value': {'slope': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}}}}}, 'dco': False, 'fast_lock_ho': True, 'freq_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'ppm': {'valid': True, 'value': {'clr': {'parsed': Fraction(1, 500000), 'value': '2 ppm'}, 'set': {'parsed': Fraction(1, 250000), 'value': '4 ppm'}}}, 'timer': True}}, 'holdover': {'average': {'parsed': Fraction(547, 500), 'valid': True, 'value': '1.094 s'}, 'delay': {'parsed': Fraction(547, 1000), 'valid': True, 'value': '547 ms'}}, 'ip_clock': {'revertive': True, 'select': 'Auto'}, 'mode': {'o:phfl': {'state': '', 'value': {'delta': {'parsed': Fraction(1, 10000000), 'valid': True, 'value': '100 ns'}}}, 'value': ''}, 'phase_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'phase_delta': {'parsed': Fraction(1, 500000000), 'valid': True, 'value': '2 ns'}, 'timer': True}}, 'sw_ext': {'state': 'oc', 'value': {'decimation': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'sw_oc': {'state': 'oc', 'value': {'fast': {'parsed': None, 'value': '', 'warn': True}, 'normal': {'parsed': None, 'value': '', 'warn': True}}}, 'zdm': {'external': {'feedback': {'parsed': None, 'valid': True, 'value': ''}, 'output': {'parsed': None, 'valid': True, 'value': ''}}, 'state': ''}}}, 'fuse_lock': {'enabled': False, 'value': {'fvco': {'parsed': None, 'valid': True, 'value': ''}}}, 'in3_sync': False, 'lwm': False, 'order_in': [], 'ptp': {'enabled': False, 'value': {'bw': {'parsed': None, 'valid': False, 'value': ''}, 'ipath': True, 'phase_sl': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}, 'phase_ur': {'parsed': None, 'valid': False, 'value': ''}, 'ppath': True}}, 'smartdco': {'receiver': {'valid': True, 'value': {'rx1': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'rx2': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'sl': {'parsed': Fraction(1, 1000), 'valid': True, 'value': '1000 ppm/s'}}}, 'transmitter': {'tx1': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}, 'tx2': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}}}}}, 'D': {'enabled': False, 'value': {'free_running': {'enabled': False, 'value': {'clock_switch': {'frequency_ramp': {'enabled': False, 'value': {'slope': {'parsed': None, 'valid': True, 'value': ''}}}, 'hitless': {'ph_bout': 'propagation', 'ph_prop': {'state': 'propagation', 'value': {'slope': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}}}}}, 'dco': False, 'fast_lock_ho': True, 'freq_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'ppm': {'valid': True, 'value': {'clr': {'parsed': Fraction(1, 500000), 'value': '2 ppm'}, 'set': {'parsed': Fraction(1, 250000), 'value': '4 ppm'}}}, 'timer': True}}, 'holdover': {'average': {'parsed': Fraction(547, 500), 'valid': True, 'value': '1.094 s'}, 'delay': {'parsed': Fraction(547, 1000), 'valid': True, 'value': '547 ms'}}, 'ip_clock': {'revertive': True, 'select': 'Auto'}, 'mode': {'o:phfl': {'state': '', 'value': {'delta': {'parsed': Fraction(1, 10000000), 'valid': True, 'value': '100 ns'}}}, 'value': ''}, 'phase_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'phase_delta': {'parsed': Fraction(1, 500000000), 'valid': True, 'value': '2 ns'}, 'timer': True}}, 'sw_ext': {'state': 'oc', 'value': {'decimation': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'sw_oc': {'state': 'oc', 'value': {'fast': {'parsed': None, 'value': '', 'warn': True}, 'normal': {'parsed': None, 'value': '', 'warn': True}}}, 'zdm': {'external': {'feedback': {'parsed': None, 'valid': True, 'value': ''}, 'output': {'parsed': None, 'valid': True, 'value': ''}}, 'state': ''}}}, 'fuse_lock': {'enabled': False, 'value': {'fvco': {'parsed': None, 'valid': True, 'value': ''}}}, 'in3_sync': False, 'lwm': False, 'order_in': [], 'ptp': {'enabled': False, 'value': {'bw': {'parsed': None, 'valid': False, 'value': ''}, 'ipath': True, 'phase_sl': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}, 'phase_ur': {'parsed': None, 'valid': False, 'value': ''}, 'ppath': True}}, 'smartdco': {'receiver': {'valid': True, 'value': {'rx1': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'rx2': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'sl': {'parsed': Fraction(1, 1000), 'valid': True, 'value': '1000 ppm/s'}}}, 'transmitter': {'tx1': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}, 'tx2': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}}}}}, 'FT': {'enabled': True, 'value': {'free_running': {'enabled': False, 'value': {'clock_switch': {'frequency_ramp': {'enabled': False, 'value': {'slope': {'parsed': None, 'valid': True, 'value': ''}}}, 'hitless': {'ph_bout': 'propagation', 'ph_prop': {'state': 'propagation', 'value': {'slope': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}}}}}, 'dco': False, 'fast_lock_ho': True, 'freq_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'ppm': {'valid': True, 'value': {'clr': {'parsed': Fraction(1, 500000), 'value': '2 ppm'}, 'set': {'parsed': Fraction(1, 250000), 'value': '4 ppm'}}}, 'timer': True}}, 'holdover': {'average': {'parsed': Fraction(547, 500), 'valid': True, 'value': '1.094 s'}, 'delay': {'parsed': Fraction(547, 1000), 'valid': True, 'value': '547 ms'}}, 'ip_clock': {'revertive': True, 'select': 'Auto'}, 'mode': {'o:phfl': {'state': '', 'value': {'delta': {'parsed': Fraction(1, 10000000), 'valid': True, 'value': '100 ns'}}}, 'value': ''}, 'phase_lock_loss': {'enabled': True, 'value': {'delay': {'parsed': Fraction(1, 250), 'valid': True, 'value': '4 ms'}, 'phase_delta': {'parsed': Fraction(1, 500000000), 'valid': True, 'value': '2 ns'}, 'timer': True}}, 'sw_ext': {'state': 'oc', 'value': {'decimation': {'parsed': 1, 'valid': True, 'value': '1'}}}, 'sw_oc': {'state': 'oc', 'value': {'fast': {'parsed': None, 'value': '', 'warn': True}, 'normal': {'parsed': None, 'value': '', 'warn': True}}}, 'zdm': {'external': {'feedback': {'parsed': None, 'valid': True, 'value': ''}, 'output': {'parsed': None, 'valid': True, 'value': ''}}, 'state': ''}}}, 'fuse_lock': {'enabled': False, 'value': {'fvco': {'parsed': None, 'valid': True, 'value': ''}}}, 'in3_sync': False, 'lwm': False, 'order_in': [], 'ptp': {'enabled': False, 'value': {'bw': {'parsed': None, 'valid': False, 'value': ''}, 'ipath': True, 'phase_sl': {'parsed': None, 'valid': True, 'value': 'Bandwidth'}, 'phase_ur': {'parsed': None, 'valid': False, 'value': ''}, 'ppath': True}}, 'smartdco': {'receiver': {'valid': True, 'value': {'rx1': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'rx2': {'enabled': False, 'value': {'pll': '', 'tx': 'tx1'}}, 'sl': {'parsed': Fraction(1, 1000), 'valid': True, 'value': '1000 ppm/s'}}}, 'transmitter': {'tx1': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}, 'tx2': {'enabled': False, 'value': {'ipath': True, 'ppath': False, 'rx1': True, 'rx2': True}}}}}}}}

nvm_list=['Profile1_nvm.nvm.py.nvm.py', 'Profile3_nvm.nvm.py.nvm.py', 'Profile4_nvm.nvm.py.nvm.py', 'Profile5_nvm.nvm.py.nvm.py', 'Profile6_nvm.nvm.py.nvm.py', 'Profile8_nvm.nvm.py.nvm.py', 'Profile9_nvm.nvm.py.nvm.py', 'Profile10_nvm.nvm.py.nvm.py', 'Profile11_nvm.nvm.py.nvm.py', 'Profile15_nvm.nvm.py.nvm.py', 'Profile16_nvm.nvm.py.nvm.py', 'Profile17_nvm.nvm.py.nvm.py', 'Profile19_nvm.nvm.py.nvm.py', 'Profile20_nvm.nvm.py.nvm.py', 'Profile21_nvm.nvm.py.nvm.py', 'Profile22_nvm.nvm.py.nvm.py', 'Profile23_nvm.nvm.py.nvm.py', 'Profile24_nvm.nvm.py.nvm.py', 'Profile25_nvm.nvm.py.nvm.py', 'Profile26_nvm.nvm.py.nvm.py', 'Profile27_nvm.nvm.py.nvm.py', 'Profile28_nvm.nvm.py.nvm.py', 'Profile29_nvm.nvm.py.nvm.py', 'Profile30_nvm.nvm.py.nvm.py', 'Profile31_nvm.nvm.py.nvm.py', 'Profile32_nvm.nvm.py.nvm.py', 'Profile33_nvm.nvm.py.nvm.py', 'Profile34_nvm.nvm.py.nvm.py', 'Profile35_nvm.nvm.py.nvm.py', 'Profile36_nvm.nvm.py.nvm.py', 'Profile37_nvm.nvm.py.nvm.py', 'Profile38_nvm.nvm.py.nvm.py', 'Profile39_nvm.nvm.py.nvm.py', 'Profile40_nvm.nvm.py.nvm.py', 'Profile41_nvm.nvm.py.nvm.py', 'Profile42_nvm.nvm.py.nvm.py', 'Profile43_nvm.nvm.py.nvm.py', 'Profile44_nvm.nvm.py.nvm.py', 'Profile45_nvm.nvm.py.nvm.py', 'Profile46_nvm.nvm.py.nvm.py', 'Profile47_nvm.nvm.py.nvm.py', 'Profile48_nvm.nvm.py.nvm.py', 'Profile49_nvm.nvm.py.nvm.py', 'Profile50_nvm.nvm.py.nvm.py', 'Profile51_nvm.nvm.py.nvm.py', 'Profile52_nvm.nvm.py.nvm.py', 'Profile53_nvm.nvm.py.nvm.py', 'Profile54_nvm.nvm.py.nvm.py', 'Profile55_nvm.nvm.py.nvm.py', 'Profile56_nvm.nvm.py.nvm.py', 'Profile57_nvm.nvm.py.nvm.py', 'Profile58_nvm.nvm.py.nvm.py', 'Profile59_nvm.nvm.py.nvm.py', 'Profile60_nvm.nvm.py.nvm.py', 'Profile61_nvm.nvm.py.nvm.py', 'Profile62_nvm.nvm.py.nvm.py', 'Profile64_nvm.nvm.py.nvm.py', 'Profile65_nvm.nvm.py.nvm.py', 'Profile66_nvm.nvm.py.nvm.py', 'Profile67_nvm.nvm.py.nvm.py', 'Profile68_nvm.nvm.py.nvm.py', 'Profile69_nvm.nvm.py.nvm.py', 'Profile70_nvm.nvm.py.nvm.py', 'Profile71_nvm.nvm.py.nvm.py', 'Profile72_nvm.nvm.py.nvm.py', 'Profile73_nvm.nvm.py.nvm.py', 'Profile74_nvm.nvm.py.nvm.py', 'Profile75_nvm.nvm.py.nvm.py', 'Profile76_nvm.nvm.py.nvm.py', 'Profile77_nvm.nvm.py.nvm.py', 'Profile78_nvm.nvm.py.nvm.py', 'Profile79_nvm.nvm.py.nvm.py', 'Profile80_nvm.nvm.py.nvm.py', 'Profile81_nvm.nvm.py.nvm.py', 'Profile83_nvm.nvm.py.nvm.py', 'Profile84_nvm.nvm.py.nvm.py', 'Profile85_nvm.nvm.py.nvm.py', 'Profile87_nvm.nvm.py.nvm.py', 'Profile88_nvm.nvm.py.nvm.py', 'Profile89_nvm.nvm.py.nvm.py', 'Profile90_nvm.nvm.py.nvm.py', 'Profile91_nvm.nvm.py.nvm.py', 'Profile92_nvm.nvm.py.nvm.py', 'Profile93_nvm.nvm.py.nvm.py', 'Profile94_nvm.nvm.py.nvm.py', 'Profile95_nvm.nvm.py.nvm.py', 'Profile96_nvm.nvm.py.nvm.py', 'Profile97_nvm.nvm.py.nvm.py', 'Profile98_nvm.nvm.py.nvm.py', 'Profile99_nvm.nvm.py.nvm.py', 'Profile100_nvm.nvm.py.nvm.py', 'Profile101_nvm.nvm.py.nvm.py', 'Profile102_nvm.nvm.py.nvm.py', 'Profile103_nvm.nvm.py.nvm.py', 'Profile105_nvm.nvm.py.nvm.py', 'Profile106_nvm.nvm.py.nvm.py', 'Profile107_nvm.nvm.py.nvm.py', 'Profile108_nvm.nvm.py.nvm.py', 'Profile109_nvm.nvm.py.nvm.py', 'Profile110_nvm.nvm.py.nvm.py', 'Profile111_nvm.nvm.py.nvm.py', 'Profile112_nvm.nvm.py.nvm.py', 'Profile113_nvm.nvm.py.nvm.py', 'Profile114_nvm.nvm.py.nvm.py', 'Profile115_nvm.nvm.py.nvm.py', 'Profile116_nvm.nvm.py.nvm.py', 'Profile117_nvm.nvm.py.nvm.py', 'Profile118_nvm.nvm.py.nvm.py', 'Profile119_nvm.nvm.py.nvm.py', 'Profile121_nvm.nvm.py.nvm.py', 'Profile122_nvm.nvm.py.nvm.py', 'Profile123_nvm.nvm.py.nvm.py', 'Profile124_nvm.nvm.py.nvm.py', 'Profile125_nvm.nvm.py.nvm.py', 'Profile126_nvm.nvm.py.nvm.py', 'Profile127_nvm.nvm.py.nvm.py', 'Profile128_nvm.nvm.py.nvm.py', 'Profile129_nvm.nvm.py.nvm.py', 'Profile130_nvm.nvm.py.nvm.py', 'Profile131_nvm.nvm.py.nvm.py', 'Profile132_nvm.nvm.py.nvm.py', 'Profile133_nvm.nvm.py.nvm.py', 'Profile134_nvm.nvm.py.nvm.py', 'Profile135_nvm.nvm.py.nvm.py', 'Profile136_nvm.nvm.py.nvm.py', 'Profile137_nvm.nvm.py.nvm.py', 'Profile138_nvm.nvm.py.nvm.py', 'Profile139_nvm.nvm.py.nvm.py', 'Profile140_nvm.nvm.py.nvm.py', 'Profile141_nvm.nvm.py.nvm.py', 'Profile142_nvm.nvm.py.nvm.py', 'Profile143_nvm.nvm.py.nvm.py', 'Profile144_nvm.nvm.py.nvm.py', 'Profile145_nvm.nvm.py.nvm.py', 'Profile146_nvm.nvm.py.nvm.py', 'Profile147_nvm.nvm.py.nvm.py', 'Profile148_nvm.nvm.py.nvm.py', 'Profile149_nvm.nvm.py.nvm.py', 'Profile150_nvm.nvm.py.nvm.py', 'Profile151_nvm.nvm.py.nvm.py', 'Profile152_nvm.nvm.py.nvm.py', 'Profile153_nvm.nvm.py.nvm.py', 'Profile154_nvm.nvm.py.nvm.py', 'Profile155_nvm.nvm.py.nvm.py', 'Profile156_nvm.nvm.py.nvm.py', 'Profile157_nvm.nvm.py.nvm.py', 'Profile158_nvm.nvm.py.nvm.py', 'Profile159_nvm.nvm.py.nvm.py', 'Profile160_nvm.nvm.py.nvm.py', 'Profile161_nvm.nvm.py.nvm.py', 'Profile163_nvm.nvm.py.nvm.py', 'Profile164_nvm.nvm.py.nvm.py', 'Profile165_nvm.nvm.py.nvm.py', 'Profile166_nvm.nvm.py.nvm.py', 'Profile167_nvm.nvm.py.nvm.py', 'Profile168_nvm.nvm.py.nvm.py', 'Profile169_nvm.nvm.py.nvm.py', 'Profile170_nvm.nvm.py.nvm.py', 'Profile171_nvm.nvm.py.nvm.py', 'Profile172_nvm.nvm.py.nvm.py', 'Profile173_nvm.nvm.py.nvm.py', 'Profile174_nvm.nvm.py.nvm.py', 'Profile176_nvm.nvm.py.nvm.py', 'Profile177_nvm.nvm.py.nvm.py', 'Profile178_nvm.nvm.py.nvm.py', 'Profile179_nvm.nvm.py.nvm.py', 'Profile180_nvm.nvm.py.nvm.py', 'Profile181_nvm.nvm.py.nvm.py', 'Profile182_nvm.nvm.py.nvm.py', 'Profile183_nvm.nvm.py.nvm.py', 'Profile184_nvm.nvm.py.nvm.py', 'Profile185_nvm.nvm.py.nvm.py', 'Profile186_nvm.nvm.py.nvm.py', 'Profile187_nvm.nvm.py.nvm.py', 'Profile188_nvm.nvm.py.nvm.py', 'Profile189_nvm.nvm.py.nvm.py', 'Profile191_nvm.nvm.py.nvm.py', 'Profile192_nvm.nvm.py.nvm.py', 'Profile193_nvm.nvm.py.nvm.py', 'Profile194_nvm.nvm.py.nvm.py', 'Profile195_nvm.nvm.py.nvm.py', 'Profile196_nvm.nvm.py.nvm.py', 'Profile197_nvm.nvm.py.nvm.py', 'Profile198_nvm.nvm.py.nvm.py', 'Profile199_nvm.nvm.py.nvm.py', 'Profile200_nvm.nvm.py.nvm.py', 'Profile201_nvm.nvm.py.nvm.py', 'Profile202_nvm.nvm.py.nvm.py', 'Profile203_nvm.nvm.py.nvm.py', 'Profile204_nvm.nvm.py.nvm.py', 'Profile205_nvm.nvm.py.nvm.py', 'Profile208_nvm.nvm.py.nvm.py', 'Profile209_nvm.nvm.py.nvm.py', 'Profile210_nvm.nvm.py.nvm.py', 'Profile211_nvm.nvm.py.nvm.py', 'Profile212_nvm.nvm.py.nvm.py', 'Profile214_nvm.nvm.py.nvm.py', 'Profile215_nvm.nvm.py.nvm.py', 'Profile216_nvm.nvm.py.nvm.py', 'Profile217_nvm.nvm.py.nvm.py', 'Profile218_nvm.nvm.py.nvm.py', 'Profile219_nvm.nvm.py.nvm.py', 'Profile220_nvm.nvm.py.nvm.py', 'Profile221_nvm.nvm.py.nvm.py', 'Profile223_nvm.nvm.py.nvm.py', 'Profile224_nvm.nvm.py.nvm.py', 'Profile225_nvm.nvm.py.nvm.py', 'Profile227_nvm.nvm.py.nvm.py', 'Profile228_nvm.nvm.py.nvm.py', 'Profile229_nvm.nvm.py.nvm.py']

dict1 = {'acg': {'enabled': False,
          'value': {'clock_mode': {'parsed': None, 'valid': True, 'value': ''}}},
  'comms': {'i2c': {'address': {'parsed': 91, 'valid': True, 'value': '0x5B'}},
            'spi': {'wires': 4},
            'type': 'spi'},
  'eeprom': {'addr': {'parsed': 0, 'valid': True, 'value': '0'},
            'ibus': None,
            'type': 64,
            'verify': {'block': {'parsed': 0, 'valid': True, 'value': '1'}}},
  'golden_clock': 'xtal'}

dict2 = {'acg': {'enabled': False,
          'value': {'clock_mode': {'parsed': None, 'valid': True, 'value': ''}}},
  'comms': {'i2c': {'address': {'parsed': 91, 'valid': True, 'value': '0x5B'}},
            'spi': {'wires': 3},
            'type': 'spi'},
  'crystal': {'doubler': True,
              'freq': {'parsed': '',
                      'valid': True,
                      'value': '59 MHz'},
              'mode': 'LFF CL=8pF'},
  'eeprom': {'addr': {'parsed': 0, 'valid': True, 'value': '0'},
            'ibus': None,
            'type': 64,
            'verify': {'block': {'parsed': 1, 'valid': True, 'value': '1'}}},
  'golden_clock': 'A'}

DEBUG=2
import sys
sys.stdout = open("output_inputpy.txt", "w")

def get_only_files(path, include_str=''):
    global onlyfiles
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f)) and include_str in f]
    return onlyfiles
    

def pairs(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield from pairs(v)
        else:
            yield '{}={}'.format(k, v)

def nested_keys(d):
    for k, v in d.items():
        if isinstance(v, dict):
            yield '{}'.format(k)
            yield from nested_keys(v)
        else:
            yield '{}'.format(k)


def recursive_items(dictionary):
    for key, value in dictionary.items():
        if type(value) is dict:
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)
    
    
# step 0: Compare 2 dictionaries
    # If same return Null and quit
# step 1: Find if any keys are different
 # - report the keys and no further processing of these keys
 # We will only compare the key that are in both
# If I have a difference then run the recursive function. Rem state will help to remeber the hierarchy
    # - If a key is missing or different I report straight away saying key is missing ---
    # - Then look for values that are different if keys are same
# If keys are same compare two dictionaries with given keys
    # - If key value pairs are same

    
# dict2={
#   "_appversion": None,
#   "_variant": "au5518",
#   "_version": 1,
#   "algorithm": {
#     "INPUT": {
#       "0P": {
#         "bypass": True,
#         "divn1": {
#           "denominator": 4294967295,
#           "int": 1,
#           "numerator": 0
#         },
#         "doubler": False,
#         "fin_int": 100.0
#       }
#     },
#     "OUTPUT": {
#       "11": {
#         "coarse": 0,
#         "fine": 1
#       }
#     }}}

def diff_dic(state1, state2, new_state_added,rem_path=""):
    diff_output =[]
    for k in state1:
        if (k not in state2):
            if DEBUG>0:
                print (rem_path, ":")
            if new_state_added:
                if DEBUG>0:
                    print (k + " key newly added in state2", "\n")
            else:
                if DEBUG>0:
                    print (k + " key not in state2", "\n")
            diff_output.append(k)
        else:
            if type(state1[k]) is dict:
                if rem_path == "":
                    new_path = k
                else:
                    new_path = rem_path + "->" + k
                # myfirsttime=True
                #     rem_list.append(k)
                    
                diff_ret = diff_dic(state1[k],state2[k],new_state_added, new_path)
                diff_output.extend(diff_ret)
            else:
                if state1[k] != state2[k]:
                    if DEBUG>0:
                        print (rem_path, ":")
                        print (" - ", k," : ", state1[k])
                        print (" + ", k," : ", state2[k])
                    diff_output.extend([rem_path+'->' if rem_path!= '' else '' +k])
    return diff_output

# diff_dic(dict1, dict2, new_state_added=False)

def compare_state(dict1, dict2, rem_path=""):
    

    # step 0: Compare 2 dictionaries
        # If same return Null and quit
    # step 1: Find if any keys are different
      # - report the keys and no further processing of these keys
      # We will only compare the key that are in both
    if dict1==dict2:
        return
    else:
        
        keys_state1=list(nested_keys(dict1)) # Get keys of state1
        keys_state2=list(nested_keys(dict2)) # Get keys of state2
        
        # step 1: Find if any keys are different
          # - report the keys and no further processing of these keys
        if len(keys_state2)>len(keys_state1):
            new_state_added=True
        if len(keys_state2)<len(keys_state1):
            new_state_added=False
        if len(keys_state2)==len(keys_state1):
            new_state_added=False
            
        if not(new_state_added):
            a = diff_dic(dict1, dict2, new_state_added,rem_path="")
            if DEBUG>3:
                print(f'Final a = {a}')
        else:
            a = diff_dic(dict2, dict1, new_state_added,rem_path="")
            if DEBUG>3:
                print(f'Final a = {a}')
    return a

# compare_state(dict1, dict2)            
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

import os
working_dir=os.getcwd()




# def my_import(name):
#     m = _import_(name.split(".")[0])
#     for n in name.split(".")[1:]:
#         m = getattr(m, n)
#     return m
# m = my_import("xml.etree.ElementTree")

import importlib
import base64
import re

def slugify(value):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    # ...
    return value


def json_load():
    ''' Function used to load json'''
    import json 
  
    input_file_path     = r'input'
    output_file_path    = r'output'
    
    input_files     = get_only_files(input_file_path)
    input_files.sort(key=natural_keys)
    output_files    = get_only_files(output_file_path)
    output_files.sort(key=natural_keys)
    
    json_needed=[]
    dummy_nvm_list=[]
    in_files=[]
    out_files=[]
    
    for file in nvm_list:
        dummy_nvm_list.append(file.split('_')[0])

    for i in range (len(input_files)):
        if input_files[i].split('.')[0] in dummy_nvm_list:
            in_files.append(input_files[i])
    in_files.remove(in_files[-1:][0])
    
    for i in range (len(output_files)):
        if output_files[i].split('.')[0] in dummy_nvm_list:
            out_files.append(output_files[i])
    # out_files.append('Profile247.py')

    

    if len(in_files)==len(out_files):
        for i in range(len(in_files)):
            # # sys.path.insert(1, working_dir+'//'+'input')
            # sys.path.insert(1,'input')
            # # import importlib
            # a=input_files[i].replace('.py','')
            # ip55_in = importlib.import_module(a)

            # sys.path.append('../..')
            # sys.path.insert(1,'output')
            # # import importlib
            # b=output_files[i].replace('.py','')
            # ip55_out = importlib.import_module(b)
            

            # import importlib
            
            # Contrived example of generating a module named as a string
            full_module_name1 = "input." + in_files[i].replace('.py','')
            
            # The file gets executed upon import, as expected.
            mymodule1 = importlib.import_module(full_module_name1)
            full_module_name2 = "output." + out_files[i].replace('.py','')
            
            # The file gets executed upon import, as expected.
            mymodule2 = importlib.import_module(full_module_name2)

            # exec('from input.'+input_files[i].replace('.py','')+' import test as test1')
            # exec('from output.'+output_files[i].replace('.py','')+' import test as test2')
            


            # # JSON file 
            print('#############################################################################################')
            print('Processing file %s vs %s'%(in_files[i],out_files[i]))
            # f1 = open (input_file_path+'//'+input_files[i]) 
            # f2 = open (output_file_path+'//'+output_files[i]) 
              
            # # Reading from file 
            # data1 = json.load(f1) 
            # data2 = json.load(f2) 
            compare_state(mymodule1.test, mymodule2.test)
            print('#############################################################################################')
            print("\n")
            # f1.close() 
            # f2.close() 
    else:
        print("Number of files in input vs output directories are not same")
        print("Please have the same number of files")
json_load()        
sys.stdout.close()
      
        
# def compare_state(state1, state2, rem_path=""):
    

#     # step 0: Compare 2 dictionaries
#         # If same return Null and quit
#     # step 1: Find if any keys are different
#      # - report the keys and no further processing of these keys
#      # We will only compare the key that are in both
#     if dict1==dict2:
#         return
#     else:
#         for k in state1:
#             if (k not in state2):
#                 print (rem_path, ":")
#                 print (k + " key not in state2", "\n")
#             else:
#                 if type(state1[k]) is dict:
#                     if rem_path == "":
#                         rem_path = k
#                     else:
#                         rem_path = rem_path + "->" + k
#                     compare_state(state1[k],state2[k], rem_path)
#                 else:
#                     if state1[k] != state2[k]:
#                         print (rem_path, ":")
#                         print (" - ", k," : ", state1[k])
#                         print (" + ", k," : ", state2[k])

    
    
