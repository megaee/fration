# Generated by Sandhiya
# Generated on 20210401 at 11:19:26
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
i2c.i2cw(0x5b, 0x24, 0x09)
i2c.i2cw(0x5b, 0x25, 0x08)
i2c.i2cw(0x5b, 0x28, 0x40)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2c, 0xa0)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x32, 0x1e)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x60)
i2c.i2cw(0x5b, 0x40, 0x18)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x11, 0x59)
i2c.i2cw(0x5b, 0x12, 0x09)
i2c.i2cw(0x5b, 0x16, 0x66)
i2c.i2cw(0x5b, 0x17, 0x66)
i2c.i2cw(0x5b, 0x18, 0x66)
i2c.i2cw(0x5b, 0x19, 0x66)
i2c.i2cw(0x5b, 0x1a, 0x66)
i2c.i2cw(0x5b, 0x1b, 0x66)
i2c.i2cw(0x5b, 0x22, 0x12)
i2c.i2cw(0x5b, 0x23, 0x22)
i2c.i2cw(0x5b, 0x24, 0x22)
i2c.i2cw(0x5b, 0x25, 0x22)
i2c.i2cw(0x5b, 0x26, 0x22)
i2c.i2cw(0x5b, 0x27, 0x22)
i2c.i2cw(0x5b, 0x28, 0x66)
i2c.i2cw(0x5b, 0x29, 0x66)
i2c.i2cw(0x5b, 0x2a, 0x66)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x66)
i2c.i2cw(0x5b, 0x2d, 0x66)

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
i2c.i2cw(0x5b, 0x10, 0x01)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x38)
i2c.i2cw(0x5b, 0x1b, 0x23)
i2c.i2cw(0x5b, 0x1c, 0x10)
i2c.i2cw(0x5b, 0x1d, 0x01)
i2c.i2cw(0x5b, 0x20, 0x0a)
i2c.i2cw(0x5b, 0x26, 0xff)
i2c.i2cw(0x5b, 0x27, 0xff)
i2c.i2cw(0x5b, 0x28, 0xff)
i2c.i2cw(0x5b, 0x29, 0xff)
i2c.i2cw(0x5b, 0x2a, 0x28)
i2c.i2cw(0x5b, 0x2b, 0x20)
i2c.i2cw(0x5b, 0x2c, 0x20)
i2c.i2cw(0x5b, 0x30, 0x01)
i2c.i2cw(0x5b, 0x36, 0xff)
i2c.i2cw(0x5b, 0x37, 0xff)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0x38)
i2c.i2cw(0x5b, 0x3b, 0x21)
i2c.i2cw(0x5b, 0x61, 0xf8)
i2c.i2cw(0x5b, 0x66, 0xff)
i2c.i2cw(0x5b, 0x67, 0xff)
i2c.i2cw(0x5b, 0x68, 0xff)
i2c.i2cw(0x5b, 0x69, 0xff)
i2c.i2cw(0x5b, 0x6a, 0x08)
i2c.i2cw(0x5b, 0x6b, 0x09)
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
i2c.i2cw(0x5b, 0x14, 0x5f)
i2c.i2cw(0x5b, 0x15, 0x5e)
i2c.i2cw(0x5b, 0x16, 0x10)
i2c.i2cw(0x5b, 0x17, 0xd4)
i2c.i2cw(0x5b, 0x19, 0x60)
i2c.i2cw(0x5b, 0x1a, 0x2d)
i2c.i2cw(0x5b, 0x1b, 0x08)
i2c.i2cw(0x5b, 0x1d, 0x4f)
i2c.i2cw(0x5b, 0x1f, 0x3f)
i2c.i2cw(0x5b, 0x20, 0x43)
i2c.i2cw(0x5b, 0x21, 0x05)
i2c.i2cw(0x5b, 0x22, 0x04)
i2c.i2cw(0x5b, 0x24, 0x50)
i2c.i2cw(0x5b, 0x27, 0xca)
i2c.i2cw(0x5b, 0x29, 0x10)
i2c.i2cw(0x5b, 0x2a, 0x30)
i2c.i2cw(0x5b, 0x2b, 0x06)
i2c.i2cw(0x5b, 0x2c, 0x01)
i2c.i2cw(0x5b, 0x2d, 0xa4)
i2c.i2cw(0x5b, 0x2f, 0xfc)
i2c.i2cw(0x5b, 0x30, 0x43)
i2c.i2cw(0x5b, 0x31, 0x05)
i2c.i2cw(0x5b, 0x32, 0x04)
i2c.i2cw(0x5b, 0x34, 0x50)
i2c.i2cw(0x5b, 0x37, 0xca)
i2c.i2cw(0x5b, 0x39, 0x10)
i2c.i2cw(0x5b, 0x3a, 0x30)
i2c.i2cw(0x5b, 0x3b, 0x06)
i2c.i2cw(0x5b, 0x3c, 0x01)
i2c.i2cw(0x5b, 0x3d, 0xa4)
i2c.i2cw(0x5b, 0x3e, 0x01)
i2c.i2cw(0x5b, 0x3f, 0x50)
i2c.i2cw(0x5b, 0x60, 0x43)
i2c.i2cw(0x5b, 0x61, 0x05)
i2c.i2cw(0x5b, 0x62, 0x04)
i2c.i2cw(0x5b, 0x64, 0x5f)
i2c.i2cw(0x5b, 0x65, 0x5e)
i2c.i2cw(0x5b, 0x66, 0x10)
i2c.i2cw(0x5b, 0x67, 0x74)
i2c.i2cw(0x5b, 0x69, 0x60)
i2c.i2cw(0x5b, 0x6a, 0x2d)
i2c.i2cw(0x5b, 0x6b, 0x08)
i2c.i2cw(0x5b, 0x6d, 0x4f)
i2c.i2cw(0x5b, 0x6f, 0x3f)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x74, 0x75)
i2c.i2cw(0x5b, 0x8f, 0x06)
i2c.i2cw(0x5b, 0xa0, 0x43)
i2c.i2cw(0x5b, 0xa1, 0x05)
i2c.i2cw(0x5b, 0xa2, 0x04)
i2c.i2cw(0x5b, 0xa4, 0x5f)
i2c.i2cw(0x5b, 0xa5, 0x5e)
i2c.i2cw(0x5b, 0xa6, 0x10)
i2c.i2cw(0x5b, 0xa7, 0xf4)
i2c.i2cw(0x5b, 0xa9, 0x60)
i2c.i2cw(0x5b, 0xaa, 0x2d)
i2c.i2cw(0x5b, 0xab, 0x08)
i2c.i2cw(0x5b, 0xad, 0x4f)
i2c.i2cw(0x5b, 0xaf, 0x3f)


i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x43)
i2c.i2cw(0x5b, 0x11, 0x05)
i2c.i2cw(0x5b, 0x12, 0x04)
i2c.i2cw(0x5b, 0x14, 0x4a)
i2c.i2cw(0x5b, 0x15, 0x67)
i2c.i2cw(0x5b, 0x16, 0x9e)
i2c.i2cw(0x5b, 0x17, 0x65)
i2c.i2cw(0x5b, 0x1a, 0x2e)
i2c.i2cw(0x5b, 0x1b, 0x06)
i2c.i2cw(0x5b, 0x1d, 0xc4)
i2c.i2cw(0x5b, 0x1f, 0x9d)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x28)
i2c.i2cw(0x5b, 0x2e, 0x18)

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
i2c.i2cw(0x5b, 0x14, 0x0e)
i2c.i2cw(0x5b, 0x15, 0x60)
i2c.i2cw(0x5b, 0x19, 0x02)
i2c.i2cw(0x5b, 0x1a, 0x0f)
i2c.i2cw(0x5b, 0x1c, 0x20)
i2c.i2cw(0x5b, 0x1e, 0xa0)
i2c.i2cw(0x5b, 0x1f, 0x05)
i2c.i2cw(0x5b, 0x24, 0x0e)
i2c.i2cw(0x5b, 0x25, 0x60)
i2c.i2cw(0x5b, 0x29, 0x02)
i2c.i2cw(0x5b, 0x2a, 0x0f)
i2c.i2cw(0x5b, 0x2c, 0x20)
i2c.i2cw(0x5b, 0x2e, 0xa0)
i2c.i2cw(0x5b, 0x2f, 0x05)
i2c.i2cw(0x5b, 0x34, 0x71)
i2c.i2cw(0x5b, 0x35, 0x40)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0xcf)
i2c.i2cw(0x5b, 0x3c, 0x20)
i2c.i2cw(0x5b, 0x3e, 0x6c)
i2c.i2cw(0x5b, 0x54, 0x2a)
i2c.i2cw(0x5b, 0x55, 0x60)
i2c.i2cw(0x5b, 0x59, 0x02)
i2c.i2cw(0x5b, 0x5a, 0x0f)
i2c.i2cw(0x5b, 0x5c, 0x20)
i2c.i2cw(0x5b, 0x5e, 0xa0)
i2c.i2cw(0x5b, 0x5f, 0x05)
i2c.i2cw(0x5b, 0x64, 0x1f)
i2c.i2cw(0x5b, 0x65, 0x60)
i2c.i2cw(0x5b, 0x69, 0x02)
i2c.i2cw(0x5b, 0x6a, 0x17)
i2c.i2cw(0x5b, 0x6c, 0x30)
i2c.i2cw(0x5b, 0x6e, 0xa0)
i2c.i2cw(0x5b, 0x6f, 0x07)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x14, 0x1c)
i2c.i2cw(0x5b, 0x15, 0x60)
i2c.i2cw(0x5b, 0x19, 0x02)
i2c.i2cw(0x5b, 0x1a, 0x0f)
i2c.i2cw(0x5b, 0x1c, 0x20)
i2c.i2cw(0x5b, 0x1e, 0xa0)
i2c.i2cw(0x5b, 0x1f, 0x05)
i2c.i2cw(0x5b, 0x24, 0x2a)
i2c.i2cw(0x5b, 0x25, 0x60)
i2c.i2cw(0x5b, 0x29, 0x02)
i2c.i2cw(0x5b, 0x2a, 0x0f)
i2c.i2cw(0x5b, 0x2c, 0x20)
i2c.i2cw(0x5b, 0x2e, 0xa0)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x40, 0x01)
i2c.i2cw(0x5b, 0x41, 0x9d)
i2c.i2cw(0x5b, 0x42, 0xd1)
i2c.i2cw(0x5b, 0x43, 0x80)
i2c.i2cw(0x5b, 0x45, 0x40)
i2c.i2cw(0x5b, 0x49, 0x02)
i2c.i2cw(0x5b, 0x4a, 0xcf)
i2c.i2cw(0x5b, 0x4c, 0x20)
i2c.i2cw(0x5b, 0x4e, 0x6c)
i2c.i2cw(0x5b, 0x50, 0x01)
i2c.i2cw(0x5b, 0x51, 0x9d)
i2c.i2cw(0x5b, 0x52, 0xd1)
i2c.i2cw(0x5b, 0x53, 0x80)
i2c.i2cw(0x5b, 0x55, 0x40)
i2c.i2cw(0x5b, 0x59, 0x02)
i2c.i2cw(0x5b, 0x5a, 0xcf)
i2c.i2cw(0x5b, 0x5c, 0x20)
i2c.i2cw(0x5b, 0x5e, 0x6c)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x03)
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# OUTSYS : end


# PLLE : begin
i2c.i2cw(0x5b, 0xff, 0x0e)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x76)
i2c.i2cw(0x5b, 0x11, 0x2f)
i2c.i2cw(0x5b, 0x12, 0x97)
i2c.i2cw(0x5b, 0x13, 0x74)
i2c.i2cw(0x5b, 0x14, 0x2f)
i2c.i2cw(0x5b, 0x15, 0xb2)
i2c.i2cw(0x5b, 0x16, 0x01)
i2c.i2cw(0x5b, 0x18, 0x08)
i2c.i2cw(0x5b, 0x19, 0x78)
i2c.i2cw(0x5b, 0x1f, 0xb2)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x03)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0x7d)
i2c.i2cw(0x5b, 0x26, 0x80)
i2c.i2cw(0x5b, 0x27, 0x30)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x30)
i2c.i2cw(0x5b, 0x2d, 0x19)
i2c.i2cw(0x5b, 0x2e, 0x86)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x27)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x32, 0xcd)
i2c.i2cw(0x5b, 0x33, 0xcc)
i2c.i2cw(0x5b, 0x34, 0xcc)
i2c.i2cw(0x5b, 0x35, 0xcc)
i2c.i2cw(0x5b, 0x38, 0xfe)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x14)
i2c.i2cw(0x5b, 0x3f, 0x0d)
i2c.i2cw(0x5b, 0x40, 0xa2)
i2c.i2cw(0x5b, 0x41, 0x73)
i2c.i2cw(0x5b, 0x42, 0x48)
i2c.i2cw(0x5b, 0x48, 0x01)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0x80)
i2c.i2cw(0x5b, 0x4f, 0x35)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLE : end
time.sleep(6.74857755)


# PLLC : begin
i2c.i2cw(0x5b, 0xff, 0x0c)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x86)
i2c.i2cw(0x5b, 0x11, 0x33)
i2c.i2cw(0x5b, 0x12, 0xa9)
i2c.i2cw(0x5b, 0x13, 0x44)
i2c.i2cw(0x5b, 0x14, 0x2c)
i2c.i2cw(0x5b, 0x15, 0xe4)
i2c.i2cw(0x5b, 0x16, 0x31)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x4e)
i2c.i2cw(0x5b, 0x1f, 0xb0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x03)
i2c.i2cw(0x5b, 0x24, 0x23)
i2c.i2cw(0x5b, 0x25, 0xac)
i2c.i2cw(0x5b, 0x26, 0x40)
i2c.i2cw(0x5b, 0x27, 0x01)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x6f)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x61)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x32, 0x01)
i2c.i2cw(0x5b, 0x35, 0xe0)
i2c.i2cw(0x5b, 0x38, 0xf7)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x14)
i2c.i2cw(0x5b, 0x3e, 0xe0)
i2c.i2cw(0x5b, 0x3f, 0x60)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4e, 0x09)
i2c.i2cw(0x5b, 0x4f, 0xc7)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLC : end
time.sleep(0.021821294)


# PLLA : begin
i2c.i2cw(0x5b, 0xff, 0x0a)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xad)
i2c.i2cw(0x5b, 0x11, 0x2d)
i2c.i2cw(0x5b, 0x12, 0xad)
i2c.i2cw(0x5b, 0x13, 0x8b)
i2c.i2cw(0x5b, 0x14, 0x1d)
i2c.i2cw(0x5b, 0x15, 0xe8)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1b, 0x03)
i2c.i2cw(0x5b, 0x1e, 0x30)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0xc2)
i2c.i2cw(0x5b, 0x26, 0x40)
i2c.i2cw(0x5b, 0x28, 0x16)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x76)
i2c.i2cw(0x5b, 0x2c, 0x72)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x3e)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x67)
i2c.i2cw(0x5b, 0x32, 0xbf)
i2c.i2cw(0x5b, 0x33, 0x7d)
i2c.i2cw(0x5b, 0x34, 0x1d)
i2c.i2cw(0x5b, 0x35, 0x38)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3f, 0x03)
i2c.i2cw(0x5b, 0x42, 0xe8)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
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


# PLLB : begin
i2c.i2cw(0x5b, 0xff, 0x0b)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x16, 0x31)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x1f, 0xb8)
i2c.i2cw(0x5b, 0x20, 0x47)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x24, 0x33)
i2c.i2cw(0x5b, 0x27, 0x01)
i2c.i2cw(0x5b, 0x28, 0x60)
i2c.i2cw(0x5b, 0x29, 0x10)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x58)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x8b)
i2c.i2cw(0x5b, 0x31, 0x60)
i2c.i2cw(0x5b, 0x32, 0x97)
i2c.i2cw(0x5b, 0x33, 0xf5)
i2c.i2cw(0x5b, 0x34, 0xb9)
i2c.i2cw(0x5b, 0x35, 0xda)
i2c.i2cw(0x5b, 0x38, 0x5a)
i2c.i2cw(0x5b, 0x39, 0xfe)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x14)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x49, 0x01)
i2c.i2cw(0x5b, 0x4d, 0x80)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLB : end
time.sleep(0.03214336845238095)


# PLLD : begin
i2c.i2cw(0x5b, 0xff, 0x0d)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xcd)
i2c.i2cw(0x5b, 0x11, 0x2d)
i2c.i2cw(0x5b, 0x12, 0xad)
i2c.i2cw(0x5b, 0x13, 0xab)
i2c.i2cw(0x5b, 0x14, 0x1d)
i2c.i2cw(0x5b, 0x15, 0xe8)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1b, 0x04)
i2c.i2cw(0x5b, 0x1e, 0x30)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0xc2)
i2c.i2cw(0x5b, 0x26, 0x40)
i2c.i2cw(0x5b, 0x28, 0x06)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x76)
i2c.i2cw(0x5b, 0x2c, 0x72)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x3f)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x8a)
i2c.i2cw(0x5b, 0x32, 0x54)
i2c.i2cw(0x5b, 0x33, 0x52)
i2c.i2cw(0x5b, 0x34, 0x27)
i2c.i2cw(0x5b, 0x35, 0xa0)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3f, 0x04)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
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
# PLLD : end
time.sleep(0.03214336845238095)


# NVM END HERE