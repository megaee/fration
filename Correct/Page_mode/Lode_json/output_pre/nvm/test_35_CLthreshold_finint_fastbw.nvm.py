# Generated by Sandhiya
# Generated on 20210401 at 11:19:12
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
i2c.i2cw(0x5b, 0x25, 0xff)
i2c.i2cw(0x5b, 0x28, 0x40)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2c, 0xa2)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x32, 0x18)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x7e)
i2c.i2cw(0x5b, 0x40, 0x78)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x16, 0x99)
i2c.i2cw(0x5b, 0x17, 0x99)
i2c.i2cw(0x5b, 0x18, 0x99)
i2c.i2cw(0x5b, 0x19, 0x99)
i2c.i2cw(0x5b, 0x1a, 0x99)
i2c.i2cw(0x5b, 0x1b, 0x99)

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
i2c.i2cw(0x5b, 0x1b, 0x23)
i2c.i2cw(0x5b, 0x1c, 0x10)
i2c.i2cw(0x5b, 0x1d, 0x01)
i2c.i2cw(0x5b, 0x2b, 0x23)
i2c.i2cw(0x5b, 0x2c, 0x10)
i2c.i2cw(0x5b, 0x2d, 0x01)
i2c.i2cw(0x5b, 0x3b, 0x23)
i2c.i2cw(0x5b, 0x3c, 0x10)
i2c.i2cw(0x5b, 0x3d, 0x01)
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
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x88, 0x11)
i2c.i2cw(0x5b, 0x89, 0x10)
i2c.i2cw(0x5b, 0x8f, 0x06)
i2c.i2cw(0x5b, 0xa0, 0x43)
i2c.i2cw(0x5b, 0xa1, 0x05)
i2c.i2cw(0x5b, 0xa2, 0x04)
i2c.i2cw(0x5b, 0xa4, 0x6b)
i2c.i2cw(0x5b, 0xa5, 0x05)
i2c.i2cw(0x5b, 0xa6, 0x43)
i2c.i2cw(0x5b, 0xa7, 0xeb)
i2c.i2cw(0x5b, 0xa9, 0x20)
i2c.i2cw(0x5b, 0xaa, 0x2c)
i2c.i2cw(0x5b, 0xab, 0x09)
i2c.i2cw(0x5b, 0xad, 0x47)
i2c.i2cw(0x5b, 0xaf, 0x39)
i2c.i2cw(0x5b, 0xb0, 0x43)
i2c.i2cw(0x5b, 0xb1, 0x05)
i2c.i2cw(0x5b, 0xc0, 0x43)
i2c.i2cw(0x5b, 0xc1, 0x05)
i2c.i2cw(0x5b, 0xc2, 0x04)
i2c.i2cw(0x5b, 0xc4, 0x4b)
i2c.i2cw(0x5b, 0xc5, 0x1e)
i2c.i2cw(0x5b, 0xc6, 0xc5)
i2c.i2cw(0x5b, 0xc7, 0xee)
i2c.i2cw(0x5b, 0xc9, 0x20)
i2c.i2cw(0x5b, 0xca, 0x30)
i2c.i2cw(0x5b, 0xcb, 0x06)
i2c.i2cw(0x5b, 0xcc, 0x01)
i2c.i2cw(0x5b, 0xcd, 0x8b)
i2c.i2cw(0x5b, 0xce, 0x01)
i2c.i2cw(0x5b, 0xcf, 0x3c)
i2c.i2cw(0x5b, 0xd2, 0x04)
i2c.i2cw(0x5b, 0xd4, 0x6c)
i2c.i2cw(0x5b, 0xd5, 0x81)
i2c.i2cw(0x5b, 0xd6, 0xc7)
i2c.i2cw(0x5b, 0xd7, 0xee)
i2c.i2cw(0x5b, 0xd9, 0x20)
i2c.i2cw(0x5b, 0xda, 0x32)
i2c.i2cw(0x5b, 0xdb, 0x09)
i2c.i2cw(0x5b, 0xdc, 0x02)
i2c.i2cw(0x5b, 0xdd, 0x3a)
i2c.i2cw(0x5b, 0xde, 0x01)
i2c.i2cw(0x5b, 0xdf, 0xc8)


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
i2c.i2cw(0x5b, 0x33, 0x01)
i2c.i2cw(0x5b, 0x34, 0x75)
i2c.i2cw(0x5b, 0x35, 0x40)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3c, 0x31)
i2c.i2cw(0x5b, 0x3e, 0x60)

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
i2c.i2cw(0x5b, 0x10, 0xc1)
i2c.i2cw(0x5b, 0x11, 0x2f)
i2c.i2cw(0x5b, 0x12, 0x62)
i2c.i2cw(0x5b, 0x13, 0x66)
i2c.i2cw(0x5b, 0x14, 0x36)
i2c.i2cw(0x5b, 0x15, 0x64)
i2c.i2cw(0x5b, 0x16, 0x31)
i2c.i2cw(0x5b, 0x17, 0x18)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x19, 0x4e)
i2c.i2cw(0x5b, 0x1f, 0xb0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0xbf)
i2c.i2cw(0x5b, 0x25, 0x90)
i2c.i2cw(0x5b, 0x26, 0xa2)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x1c)
i2c.i2cw(0x5b, 0x2e, 0xc6)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2d)
i2c.i2cw(0x5b, 0x32, 0x7b)
i2c.i2cw(0x5b, 0x33, 0x09)
i2c.i2cw(0x5b, 0x34, 0xed)
i2c.i2cw(0x5b, 0x35, 0xe5)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x9a)
i2c.i2cw(0x5b, 0x3f, 0x38)
i2c.i2cw(0x5b, 0x40, 0x08)
i2c.i2cw(0x5b, 0x43, 0xc8)
i2c.i2cw(0x5b, 0x44, 0x71)
i2c.i2cw(0x5b, 0x45, 0x1c)
i2c.i2cw(0x5b, 0x46, 0xc7)
i2c.i2cw(0x5b, 0x49, 0xfc)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4e, 0x08)
i2c.i2cw(0x5b, 0x4f, 0x9f)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0x90, 0x05)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLA : end
time.sleep(0.61300855)


# NVM END HERE
