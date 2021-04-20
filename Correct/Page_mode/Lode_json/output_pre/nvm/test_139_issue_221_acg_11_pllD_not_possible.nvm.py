# Generated by Sandhiya
# Generated on 20210401 at 11:05:36
# Version v2.4.3rc1


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
i2c.i2cw(0x5b, 0x25, 0xfe)
i2c.i2cw(0x5b, 0x28, 0x40)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2c, 0xa5)
i2c.i2cw(0x5b, 0x2d, 0xbf)
i2c.i2cw(0x5b, 0x32, 0x1f)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x77)
i2c.i2cw(0x5b, 0x40, 0x6e)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x28, 0x44)
i2c.i2cw(0x5b, 0x29, 0x44)
i2c.i2cw(0x5b, 0x2a, 0x44)
i2c.i2cw(0x5b, 0x2b, 0x44)
i2c.i2cw(0x5b, 0x2c, 0x44)
i2c.i2cw(0x5b, 0x2d, 0x44)

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
i2c.i2cw(0x5b, 0x10, 0x14)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x21)
i2c.i2cw(0x5b, 0x50, 0x01)
i2c.i2cw(0x5b, 0x56, 0xff)
i2c.i2cw(0x5b, 0x57, 0xff)
i2c.i2cw(0x5b, 0x58, 0xff)
i2c.i2cw(0x5b, 0x59, 0xff)
i2c.i2cw(0x5b, 0x5a, 0x38)
i2c.i2cw(0x5b, 0x5b, 0x21)
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
i2c.i2cw(0x5b, 0x14, 0x50)
i2c.i2cw(0x5b, 0x17, 0xc4)
i2c.i2cw(0x5b, 0x1a, 0x2c)
i2c.i2cw(0x5b, 0x1b, 0x06)
i2c.i2cw(0x5b, 0x1d, 0x69)
i2c.i2cw(0x5b, 0x1f, 0x54)
i2c.i2cw(0x5b, 0x50, 0x43)
i2c.i2cw(0x5b, 0x51, 0x05)
i2c.i2cw(0x5b, 0x52, 0x04)
i2c.i2cw(0x5b, 0x54, 0x4c)
i2c.i2cw(0x5b, 0x55, 0x4b)
i2c.i2cw(0x5b, 0x56, 0x40)
i2c.i2cw(0x5b, 0x57, 0xd5)
i2c.i2cw(0x5b, 0x59, 0x40)
i2c.i2cw(0x5b, 0x5a, 0x2e)
i2c.i2cw(0x5b, 0x5b, 0x06)
i2c.i2cw(0x5b, 0x5d, 0xc9)
i2c.i2cw(0x5b, 0x5f, 0xa1)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x8b, 0x10)
i2c.i2cw(0x5b, 0x8d, 0x10)
i2c.i2cw(0x5b, 0x8f, 0x06)


i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x1c)
i2c.i2cw(0x5b, 0x2a, 0x96)
i2c.i2cw(0x5b, 0x2b, 0x11)
i2c.i2cw(0x5b, 0x2c, 0xa7)
i2c.i2cw(0x5b, 0x2d, 0xb9)
i2c.i2cw(0x5b, 0x2e, 0x38)

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
i2c.i2cw(0x5b, 0x14, 0xc6)
i2c.i2cw(0x5b, 0x15, 0x41)
i2c.i2cw(0x5b, 0x16, 0xa8)
i2c.i2cw(0x5b, 0x17, 0xdc)
i2c.i2cw(0x5b, 0x18, 0xa6)
i2c.i2cw(0x5b, 0x19, 0x02)
i2c.i2cw(0x5b, 0x1a, 0x17)
i2c.i2cw(0x5b, 0x1c, 0x31)
i2c.i2cw(0x5b, 0x1e, 0x60)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x34, 0xd8)
i2c.i2cw(0x5b, 0x35, 0x61)
i2c.i2cw(0x5b, 0x36, 0xa8)
i2c.i2cw(0x5b, 0x37, 0xdc)
i2c.i2cw(0x5b, 0x38, 0xa6)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3c, 0x30)
i2c.i2cw(0x5b, 0x3e, 0xa0)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x03)
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# OUTSYS : end


# PLLD : begin
i2c.i2cw(0x5b, 0xff, 0x0d)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xe1)
i2c.i2cw(0x5b, 0x11, 0x2f)
i2c.i2cw(0x5b, 0x12, 0x81)
i2c.i2cw(0x5b, 0x13, 0x80)
i2c.i2cw(0x5b, 0x14, 0x2f)
i2c.i2cw(0x5b, 0x15, 0xbe)
i2c.i2cw(0x5b, 0x16, 0x31)
i2c.i2cw(0x5b, 0x17, 0x18)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x7e)
i2c.i2cw(0x5b, 0x1f, 0xb0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x3f)
i2c.i2cw(0x5b, 0x25, 0xd7)
i2c.i2cw(0x5b, 0x26, 0xa5)
i2c.i2cw(0x5b, 0x27, 0x20)
i2c.i2cw(0x5b, 0x28, 0x03)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x19)
i2c.i2cw(0x5b, 0x2e, 0x2b)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x31)
i2c.i2cw(0x5b, 0x32, 0x93)
i2c.i2cw(0x5b, 0x33, 0x5d)
i2c.i2cw(0x5b, 0x34, 0x9b)
i2c.i2cw(0x5b, 0x35, 0x28)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x14)
i2c.i2cw(0x5b, 0x3e, 0x80)
i2c.i2cw(0x5b, 0x3f, 0xa5)
i2c.i2cw(0x5b, 0x40, 0x3f)
i2c.i2cw(0x5b, 0x41, 0x04)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4e, 0x04)
i2c.i2cw(0x5b, 0x4f, 0x64)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLD : end
time.sleep(0.81210855)


# NVM END HERE
