# Generated by Sandhiya
# Generated on 20210407 at 08:28:22
# Version v2.4.3rc5


# Step1: HARD Reset
time.sleep(0.001)
# GENERIC : begin
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x01)
i2c.i2cw(0x5b, 0x23, 0x03)
i2c.i2cw(0x5b, 0x24, 0x0e)
i2c.i2cw(0x5b, 0x25, 0xf8)
i2c.i2cw(0x5b, 0x28, 0x42)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2c, 0xa4)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x32, 0x1f)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x20)
i2c.i2cw(0x5b, 0x40, 0x42)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x79)
i2c.i2cw(0x5b, 0x11, 0x79)
i2c.i2cw(0x5b, 0x16, 0x30)
i2c.i2cw(0x5b, 0x17, 0x45)
i2c.i2cw(0x5b, 0x18, 0x22)
i2c.i2cw(0x5b, 0x19, 0x22)
i2c.i2cw(0x5b, 0x1a, 0x22)
i2c.i2cw(0x5b, 0x1b, 0x22)
i2c.i2cw(0x5b, 0x1c, 0x34)
i2c.i2cw(0x5b, 0x1d, 0x52)
i2c.i2cw(0x5b, 0x1e, 0x22)
i2c.i2cw(0x5b, 0x1f, 0x22)
i2c.i2cw(0x5b, 0x20, 0x22)
i2c.i2cw(0x5b, 0x21, 0x22)
i2c.i2cw(0x5b, 0x22, 0x34)
i2c.i2cw(0x5b, 0x23, 0x52)
i2c.i2cw(0x5b, 0x24, 0x22)
i2c.i2cw(0x5b, 0x25, 0x22)
i2c.i2cw(0x5b, 0x26, 0x22)
i2c.i2cw(0x5b, 0x27, 0x22)
i2c.i2cw(0x5b, 0x28, 0x34)
i2c.i2cw(0x5b, 0x29, 0x52)
i2c.i2cw(0x5b, 0x2a, 0x22)
i2c.i2cw(0x5b, 0x2b, 0x22)
i2c.i2cw(0x5b, 0x2c, 0x22)
i2c.i2cw(0x5b, 0x2d, 0x22)

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
i2c.i2cw(0x5b, 0x10, 0x28)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x20)
i2c.i2cw(0x5b, 0x1c, 0x20)
i2c.i2cw(0x5b, 0x30, 0x32)
i2c.i2cw(0x5b, 0x36, 0xff)
i2c.i2cw(0x5b, 0x37, 0xff)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0x28)
i2c.i2cw(0x5b, 0x3b, 0x20)
i2c.i2cw(0x5b, 0x3c, 0x20)
i2c.i2cw(0x5b, 0x40, 0x2c)
i2c.i2cw(0x5b, 0x46, 0xff)
i2c.i2cw(0x5b, 0x47, 0xff)
i2c.i2cw(0x5b, 0x48, 0xff)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0x28)
i2c.i2cw(0x5b, 0x4b, 0x20)
i2c.i2cw(0x5b, 0x4c, 0x20)
i2c.i2cw(0x5b, 0x50, 0x26)
i2c.i2cw(0x5b, 0x56, 0xff)
i2c.i2cw(0x5b, 0x57, 0xff)
i2c.i2cw(0x5b, 0x58, 0xff)
i2c.i2cw(0x5b, 0x59, 0xff)
i2c.i2cw(0x5b, 0x5a, 0x28)
i2c.i2cw(0x5b, 0x5b, 0x20)
i2c.i2cw(0x5b, 0x5c, 0x20)
i2c.i2cw(0x5b, 0x60, 0x28)
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
i2c.i2cw(0x5b, 0x10, 0x97)
i2c.i2cw(0x5b, 0x11, 0x05)
i2c.i2cw(0x5b, 0x12, 0x04)
i2c.i2cw(0x5b, 0x14, 0x64)
i2c.i2cw(0x5b, 0x17, 0xc5)
i2c.i2cw(0x5b, 0x1a, 0x30)
i2c.i2cw(0x5b, 0x1b, 0x0a)
i2c.i2cw(0x5b, 0x1c, 0x01)
i2c.i2cw(0x5b, 0x1d, 0x07)
i2c.i2cw(0x5b, 0x1f, 0xd2)
i2c.i2cw(0x5b, 0x30, 0x97)
i2c.i2cw(0x5b, 0x31, 0x05)
i2c.i2cw(0x5b, 0x32, 0x04)
i2c.i2cw(0x5b, 0x34, 0x64)
i2c.i2cw(0x5b, 0x37, 0xc5)
i2c.i2cw(0x5b, 0x3a, 0x30)
i2c.i2cw(0x5b, 0x3b, 0x0a)
i2c.i2cw(0x5b, 0x3c, 0x01)
i2c.i2cw(0x5b, 0x3d, 0x07)
i2c.i2cw(0x5b, 0x3f, 0xd2)
i2c.i2cw(0x5b, 0x40, 0x97)
i2c.i2cw(0x5b, 0x41, 0x05)
i2c.i2cw(0x5b, 0x42, 0x04)
i2c.i2cw(0x5b, 0x44, 0x64)
i2c.i2cw(0x5b, 0x47, 0xc5)
i2c.i2cw(0x5b, 0x4a, 0x30)
i2c.i2cw(0x5b, 0x4b, 0x0a)
i2c.i2cw(0x5b, 0x4c, 0x01)
i2c.i2cw(0x5b, 0x4d, 0x07)
i2c.i2cw(0x5b, 0x4f, 0xd2)
i2c.i2cw(0x5b, 0x50, 0x97)
i2c.i2cw(0x5b, 0x51, 0x05)
i2c.i2cw(0x5b, 0x52, 0x04)
i2c.i2cw(0x5b, 0x54, 0x64)
i2c.i2cw(0x5b, 0x57, 0xc5)
i2c.i2cw(0x5b, 0x5a, 0x30)
i2c.i2cw(0x5b, 0x5b, 0x0a)
i2c.i2cw(0x5b, 0x5c, 0x01)
i2c.i2cw(0x5b, 0x5d, 0x07)
i2c.i2cw(0x5b, 0x5f, 0xd2)
i2c.i2cw(0x5b, 0x60, 0x97)
i2c.i2cw(0x5b, 0x61, 0x05)
i2c.i2cw(0x5b, 0x62, 0x04)
i2c.i2cw(0x5b, 0x64, 0x64)
i2c.i2cw(0x5b, 0x67, 0x65)
i2c.i2cw(0x5b, 0x6a, 0x30)
i2c.i2cw(0x5b, 0x6b, 0x0a)
i2c.i2cw(0x5b, 0x6c, 0x01)
i2c.i2cw(0x5b, 0x6d, 0x07)
i2c.i2cw(0x5b, 0x6f, 0xd2)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x8f, 0x06)


i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x11)
i2c.i2cw(0x5b, 0x2a, 0xaa)
i2c.i2cw(0x5b, 0x2b, 0xaa)
i2c.i2cw(0x5b, 0x2c, 0xaa)
i2c.i2cw(0x5b, 0x2d, 0xaa)
i2c.i2cw(0x5b, 0x2e, 0x16)
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
i2c.i2cw(0x5b, 0x14, 0x0d)
i2c.i2cw(0x5b, 0x15, 0x40)
i2c.i2cw(0x5b, 0x17, 0x04)
i2c.i2cw(0x5b, 0x18, 0xc2)
i2c.i2cw(0x5b, 0x19, 0xc2)
i2c.i2cw(0x5b, 0x1a, 0x17)
i2c.i2cw(0x5b, 0x1c, 0x29)
i2c.i2cw(0x5b, 0x1e, 0x60)
i2c.i2cw(0x5b, 0x1f, 0x01)
i2c.i2cw(0x5b, 0x24, 0x0a)
i2c.i2cw(0x5b, 0x25, 0x40)
i2c.i2cw(0x5b, 0x27, 0x04)
i2c.i2cw(0x5b, 0x28, 0x93)
i2c.i2cw(0x5b, 0x29, 0xe2)
i2c.i2cw(0x5b, 0x2a, 0x17)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2e, 0x60)
i2c.i2cw(0x5b, 0x2f, 0x01)
i2c.i2cw(0x5b, 0x34, 0x0e)
i2c.i2cw(0x5b, 0x35, 0x40)
i2c.i2cw(0x5b, 0x37, 0x06)
i2c.i2cw(0x5b, 0x38, 0x68)
i2c.i2cw(0x5b, 0x39, 0xa2)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3c, 0x33)
i2c.i2cw(0x5b, 0x3e, 0x60)
i2c.i2cw(0x5b, 0x3f, 0x02)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x34, 0x18)
i2c.i2cw(0x5b, 0x35, 0x40)
i2c.i2cw(0x5b, 0x37, 0x06)
i2c.i2cw(0x5b, 0x38, 0x97)
i2c.i2cw(0x5b, 0x39, 0x82)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3c, 0x31)
i2c.i2cw(0x5b, 0x3e, 0x60)
i2c.i2cw(0x5b, 0x3f, 0x01)

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
i2c.i2cw(0x5b, 0x10, 0x8d)
i2c.i2cw(0x5b, 0x11, 0x67)
i2c.i2cw(0x5b, 0x12, 0x8c)
i2c.i2cw(0x5b, 0x13, 0x09)
i2c.i2cw(0x5b, 0x14, 0x56)
i2c.i2cw(0x5b, 0x15, 0xc7)
i2c.i2cw(0x5b, 0x16, 0x01)
i2c.i2cw(0x5b, 0x17, 0x18)
i2c.i2cw(0x5b, 0x18, 0x06)
i2c.i2cw(0x5b, 0x19, 0x60)
i2c.i2cw(0x5b, 0x1f, 0xb2)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x25, 0x88)
i2c.i2cw(0x5b, 0x26, 0x44)
i2c.i2cw(0x5b, 0x29, 0x0f)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x4e)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x51)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x32, 0xb9)
i2c.i2cw(0x5b, 0x33, 0x31)
i2c.i2cw(0x5b, 0x34, 0x33)
i2c.i2cw(0x5b, 0x35, 0xb3)
i2c.i2cw(0x5b, 0x38, 0x01)
i2c.i2cw(0x5b, 0x39, 0x6b)
i2c.i2cw(0x5b, 0x3a, 0x66)
i2c.i2cw(0x5b, 0x3b, 0xe6)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x90)
i2c.i2cw(0x5b, 0x3f, 0x01)
i2c.i2cw(0x5b, 0x42, 0x40)
i2c.i2cw(0x5b, 0x43, 0x77)
i2c.i2cw(0x5b, 0x44, 0x01)
i2c.i2cw(0x5b, 0x48, 0x03)
i2c.i2cw(0x5b, 0x4c, 0xf0)
i2c.i2cw(0x5b, 0x4d, 0x80)
i2c.i2cw(0x5b, 0x4e, 0x0f)
i2c.i2cw(0x5b, 0x4f, 0xdf)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLE : end
time.sleep(0.02061961)


# PLLD : begin
i2c.i2cw(0x5b, 0xff, 0x0d)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x89)
i2c.i2cw(0x5b, 0x11, 0x1c)
i2c.i2cw(0x5b, 0x12, 0xeb)
i2c.i2cw(0x5b, 0x13, 0x8b)
i2c.i2cw(0x5b, 0x14, 0x2c)
i2c.i2cw(0x5b, 0x15, 0x89)
i2c.i2cw(0x5b, 0x16, 0xbf)
i2c.i2cw(0x5b, 0x17, 0x1a)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x54)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x25, 0x85)
i2c.i2cw(0x5b, 0x26, 0x64)
i2c.i2cw(0x5b, 0x28, 0x08)
i2c.i2cw(0x5b, 0x29, 0x0f)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x54)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x3a)
i2c.i2cw(0x5b, 0x32, 0x55)
i2c.i2cw(0x5b, 0x33, 0x55)
i2c.i2cw(0x5b, 0x34, 0x55)
i2c.i2cw(0x5b, 0x35, 0x55)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x78)
i2c.i2cw(0x5b, 0x3f, 0x05)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xd5)
i2c.i2cw(0x5b, 0x57, 0x52)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLD : end
time.sleep(0.05917065)


# PLLA : begin
i2c.i2cw(0x5b, 0xff, 0x0a)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x69)
i2c.i2cw(0x5b, 0x11, 0x1c)
i2c.i2cw(0x5b, 0x12, 0xeb)
i2c.i2cw(0x5b, 0x13, 0x6b)
i2c.i2cw(0x5b, 0x14, 0x2c)
i2c.i2cw(0x5b, 0x15, 0x89)
i2c.i2cw(0x5b, 0x16, 0xb8)
i2c.i2cw(0x5b, 0x17, 0x1a)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1a, 0x10)
i2c.i2cw(0x5b, 0x1b, 0x04)
i2c.i2cw(0x5b, 0x1e, 0x30)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x20, 0x21)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x0c)
i2c.i2cw(0x5b, 0x24, 0x30)
i2c.i2cw(0x5b, 0x25, 0x85)
i2c.i2cw(0x5b, 0x26, 0x64)
i2c.i2cw(0x5b, 0x27, 0x04)
i2c.i2cw(0x5b, 0x29, 0x4f)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x76)
i2c.i2cw(0x5b, 0x2c, 0x72)
i2c.i2cw(0x5b, 0x2d, 0x60)
i2c.i2cw(0x5b, 0x2e, 0x54)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2b)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x32, 0x55)
i2c.i2cw(0x5b, 0x33, 0x55)
i2c.i2cw(0x5b, 0x34, 0x55)
i2c.i2cw(0x5b, 0x35, 0x55)
i2c.i2cw(0x5b, 0x36, 0x44)
i2c.i2cw(0x5b, 0x38, 0xfe)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x10)
i2c.i2cw(0x5b, 0x3f, 0x04)
i2c.i2cw(0x5b, 0x42, 0xe0)
i2c.i2cw(0x5b, 0x47, 0x80)
i2c.i2cw(0x5b, 0x48, 0x01)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xe0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xd5)
i2c.i2cw(0x5b, 0x57, 0x52)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLA : end
time.sleep(0.06467065)


# PLLB : begin
i2c.i2cw(0x5b, 0xff, 0x0b)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xea)
i2c.i2cw(0x5b, 0x11, 0x1c)
i2c.i2cw(0x5b, 0x12, 0xeb)
i2c.i2cw(0x5b, 0x13, 0x09)
i2c.i2cw(0x5b, 0x14, 0x2c)
i2c.i2cw(0x5b, 0x15, 0x89)
i2c.i2cw(0x5b, 0x16, 0xbf)
i2c.i2cw(0x5b, 0x17, 0x1a)
i2c.i2cw(0x5b, 0x18, 0x4f)
i2c.i2cw(0x5b, 0x19, 0x54)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x0c)
i2c.i2cw(0x5b, 0x24, 0x30)
i2c.i2cw(0x5b, 0x25, 0x85)
i2c.i2cw(0x5b, 0x26, 0x64)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x29, 0x0f)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x56)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x3c)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x38, 0xfe)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xa0)
i2c.i2cw(0x5b, 0x3f, 0x05)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xd5)
i2c.i2cw(0x5b, 0x57, 0x52)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLB : end


# PLLC : begin
i2c.i2cw(0x5b, 0xff, 0x0c)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xaa)
i2c.i2cw(0x5b, 0x11, 0x1c)
i2c.i2cw(0x5b, 0x12, 0x8a)
i2c.i2cw(0x5b, 0x13, 0xac)
i2c.i2cw(0x5b, 0x14, 0x2c)
i2c.i2cw(0x5b, 0x15, 0xa9)
i2c.i2cw(0x5b, 0x16, 0xbf)
i2c.i2cw(0x5b, 0x17, 0x1a)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x54)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x8c)
i2c.i2cw(0x5b, 0x25, 0x85)
i2c.i2cw(0x5b, 0x26, 0x66)
i2c.i2cw(0x5b, 0x28, 0x04)
i2c.i2cw(0x5b, 0x29, 0x0f)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x66)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x20)
i2c.i2cw(0x5b, 0x32, 0x3b)
i2c.i2cw(0x5b, 0x33, 0xb1)
i2c.i2cw(0x5b, 0x34, 0x13)
i2c.i2cw(0x5b, 0x35, 0xbb)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xe8)
i2c.i2cw(0x5b, 0x3f, 0x03)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xd7)
i2c.i2cw(0x5b, 0x57, 0x52)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLC : end
time.sleep(0.06467065)


# INPUT_TDC : begin
i2c.i2cw(0x5b, 0xff, 0x05)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xee)
i2c.i2cw(0x5b, 0x11, 0xc3)
i2c.i2cw(0x5b, 0x13, 0x01)
i2c.i2cw(0x5b, 0x14, 0x04)
i2c.i2cw(0x5b, 0x1e, 0xb0)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# INPUT_TDC : end


# NVM END HERE
