# Generated by Sandhiya
# Generated on 20210407 at 08:33:19
# Version v2.4.3rc5


# Step1: HARD Reset
time.sleep(0.001)
# GENERIC : begin
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x01)
i2c.i2cw(0x5b, 0x1a, 0x1f)
i2c.i2cw(0x5b, 0x1b, 0x1f)
i2c.i2cw(0x5b, 0x1c, 0x1f)
i2c.i2cw(0x5b, 0x1d, 0xff)
i2c.i2cw(0x5b, 0x1e, 0xff)
i2c.i2cw(0x5b, 0x1f, 0xff)
i2c.i2cw(0x5b, 0x20, 0xff)
i2c.i2cw(0x5b, 0x21, 0xff)
i2c.i2cw(0x5b, 0x22, 0xdf)
i2c.i2cw(0x5b, 0x23, 0x03)
i2c.i2cw(0x5b, 0x24, 0x0e)
i2c.i2cw(0x5b, 0x25, 0xff)
i2c.i2cw(0x5b, 0x28, 0x40)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2c, 0xa2)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x32, 0x1e)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x7e)
i2c.i2cw(0x5b, 0x40, 0x7e)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x16, 0x07)
i2c.i2cw(0x5b, 0x17, 0x77)
i2c.i2cw(0x5b, 0x18, 0x77)
i2c.i2cw(0x5b, 0x19, 0x77)
i2c.i2cw(0x5b, 0x1a, 0x77)
i2c.i2cw(0x5b, 0x1b, 0x77)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# force wakeup the slaves
i2c.i2cw(0x5b, 0xe1, 0xff)
i2c.i2cw(0x5b, 0xe0, 0xff)
i2c.i2cw(0x5b, 0xef, 0x05)
i2c.i2cw(0x5b, 0xee, 0x05)
time.sleep(0.0004)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# GENERIC : end


# INPUT_SYS : begin
i2c.i2cw(0x5b, 0xff, 0x02)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x17)
i2c.i2cw(0x5b, 0x12, 0x30)
i2c.i2cw(0x5b, 0x13, 0xf7)
i2c.i2cw(0x5b, 0x14, 0x34)
i2c.i2cw(0x5b, 0x15, 0xc2)
i2c.i2cw(0x5b, 0x16, 0xf0)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x24)
i2c.i2cw(0x5b, 0x1b, 0x23)
i2c.i2cw(0x5b, 0x1d, 0x03)
i2c.i2cw(0x5b, 0x6c, 0x0a)
i2c.i2cw(0x5b, 0x90, 0x0c)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
time.sleep(0.005)
# INPUT_SYS : end


# CLOCK_MON : begin
i2c.i2cw(0x5b, 0xff, 0x06)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x43)
i2c.i2cw(0x5b, 0x11, 0x05)
i2c.i2cw(0x5b, 0x12, 0x04)
i2c.i2cw(0x5b, 0x14, 0x67)
i2c.i2cw(0x5b, 0x15, 0x72)
i2c.i2cw(0x5b, 0x16, 0xc2)
i2c.i2cw(0x5b, 0x17, 0xc4)
i2c.i2cw(0x5b, 0x1a, 0x2e)
i2c.i2cw(0x5b, 0x1b, 0x09)
i2c.i2cw(0x5b, 0x1d, 0x88)
i2c.i2cw(0x5b, 0x1f, 0x6d)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x88, 0x10)
i2c.i2cw(0x5b, 0x8b, 0x10)
i2c.i2cw(0x5b, 0x8f, 0x06)
i2c.i2cw(0x5b, 0xa0, 0x43)
i2c.i2cw(0x5b, 0xa1, 0x05)
i2c.i2cw(0x5b, 0xa2, 0x04)
i2c.i2cw(0x5b, 0xa4, 0x67)
i2c.i2cw(0x5b, 0xa5, 0x72)
i2c.i2cw(0x5b, 0xa6, 0xc2)
i2c.i2cw(0x5b, 0xa7, 0xe4)
i2c.i2cw(0x5b, 0xaa, 0x2e)
i2c.i2cw(0x5b, 0xab, 0x09)
i2c.i2cw(0x5b, 0xad, 0x88)
i2c.i2cw(0x5b, 0xaf, 0x6d)


i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x13)
i2c.i2cw(0x5b, 0x2a, 0x84)
i2c.i2cw(0x5b, 0x2b, 0xbd)
i2c.i2cw(0x5b, 0x2c, 0xa1)
i2c.i2cw(0x5b, 0x2d, 0x2f)
i2c.i2cw(0x5b, 0x2e, 0x17)
i2c.i2cw(0x5b, 0x2f, 0x01)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x06)
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# CLOCK_MON : end


# OUTSYS : begin
i2c.i2cw(0x5b, 0xff, 0x03)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x32, 0x7b)
i2c.i2cw(0x5b, 0x33, 0x32)
i2c.i2cw(0x5b, 0x34, 0x0d)
i2c.i2cw(0x5b, 0x35, 0x61)
i2c.i2cw(0x5b, 0x36, 0x20)
i2c.i2cw(0x5b, 0x37, 0xbd)
i2c.i2cw(0x5b, 0x38, 0x4e)
i2c.i2cw(0x5b, 0x39, 0x7a)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3c, 0x30)
i2c.i2cw(0x5b, 0x3e, 0xa0)
i2c.i2cw(0x5b, 0x3f, 0x02)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x03)
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# OUTSYS : end


# PLLA : begin
i2c.i2cw(0x5b, 0xff, 0x0a)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xad)
i2c.i2cw(0x5b, 0x11, 0x1b)
i2c.i2cw(0x5b, 0x12, 0x6b)
i2c.i2cw(0x5b, 0x13, 0x92)
i2c.i2cw(0x5b, 0x14, 0x4e)
i2c.i2cw(0x5b, 0x15, 0x6d)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0x1a)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0xbc)
i2c.i2cw(0x5b, 0x25, 0x81)
i2c.i2cw(0x5b, 0x26, 0xa2)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x72)
i2c.i2cw(0x5b, 0x2d, 0x1c)
i2c.i2cw(0x5b, 0x2e, 0x46)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2d)
i2c.i2cw(0x5b, 0x32, 0xce)
i2c.i2cw(0x5b, 0x33, 0x63)
i2c.i2cw(0x5b, 0x34, 0xa7)
i2c.i2cw(0x5b, 0x35, 0xda)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xf5)
i2c.i2cw(0x5b, 0x3f, 0x01)
i2c.i2cw(0x5b, 0x43, 0xa4)
i2c.i2cw(0x5b, 0x44, 0xbd)
i2c.i2cw(0x5b, 0x45, 0xf5)
i2c.i2cw(0x5b, 0x46, 0x20)
i2c.i2cw(0x5b, 0x49, 0x20)
i2c.i2cw(0x5b, 0x4a, 0xf9)
i2c.i2cw(0x5b, 0x4b, 0xfe)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xdf)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLA : end
time.sleep(0.5998421189655171)


# NVM END HERE
