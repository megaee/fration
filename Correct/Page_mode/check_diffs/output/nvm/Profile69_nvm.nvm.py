# Generated by Auraauro
# Generated on 20210215 at 22:40:03
# Version v2.4rc3


# Step1: HARD Reset
# Step2: Wait for CPU to reach Active State
time.sleep(0.02)
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
i2c.i2cw(0x5b, 0x2c, 0xe2)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0x99)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x76)
i2c.i2cw(0x5b, 0x40, 0x40)
i2c.i2cw(0x5b, 0x50, 0x08)
i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x16, 0x71)
i2c.i2cw(0x5b, 0x17, 0x82)
i2c.i2cw(0x5b, 0x18, 0x93)
i2c.i2cw(0x5b, 0x19, 0xa4)
i2c.i2cw(0x5b, 0x1a, 0xb5)

# Update NVM Bank
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0x29, 0x00)
i2c.i2cw(0x5b, 0xc5, 0x01)
i2c.i2cw(0x5b, 0xc4, 0x01)
time.sleep(0.015)
i2c.i2cw(0x5b, 0xc5, 0x00)
i2c.i2cw(0x5b, 0xc4, 0x00)

# Disabling CPU PLL
i2c.i2cw(0x5b, 0xec, 0x10)
# GENERIC : end


# INPUT_SYS: begin
i2c.i2cw(0x5b, 0xff, 0x02)
i2c.i2cw(0x5b, 0xbd, 0xc3)
# Ecsape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)
i2c.i2cw(0x5b, 0x10, 0x07)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x23)
i2c.i2cw(0x5b, 0x1c, 0xc1)
i2c.i2cw(0x5b, 0x1d, 0x0e)
i2c.i2cw(0x5b, 0x20, 0x15)
i2c.i2cw(0x5b, 0x26, 0xff)
i2c.i2cw(0x5b, 0x27, 0xff)
i2c.i2cw(0x5b, 0x28, 0xff)
i2c.i2cw(0x5b, 0x29, 0xff)
i2c.i2cw(0x5b, 0x2a, 0x28)
i2c.i2cw(0x5b, 0x2b, 0x23)
i2c.i2cw(0x5b, 0x2c, 0xc0)
i2c.i2cw(0x5b, 0x2d, 0x07)
i2c.i2cw(0x5b, 0x30, 0x07)
i2c.i2cw(0x5b, 0x36, 0xff)
i2c.i2cw(0x5b, 0x37, 0xff)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0x28)
i2c.i2cw(0x5b, 0x3b, 0x23)
i2c.i2cw(0x5b, 0x3c, 0xc1)
i2c.i2cw(0x5b, 0x3d, 0x0e)
i2c.i2cw(0x5b, 0x40, 0x15)
i2c.i2cw(0x5b, 0x46, 0xff)
i2c.i2cw(0x5b, 0x47, 0xff)
i2c.i2cw(0x5b, 0x48, 0xff)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0x28)
i2c.i2cw(0x5b, 0x4b, 0x23)
i2c.i2cw(0x5b, 0x4c, 0xc1)
i2c.i2cw(0x5b, 0x4d, 0x07)
i2c.i2cw(0x5b, 0x50, 0x1c)
i2c.i2cw(0x5b, 0x56, 0xff)
i2c.i2cw(0x5b, 0x57, 0xff)
i2c.i2cw(0x5b, 0x58, 0xff)
i2c.i2cw(0x5b, 0x59, 0xff)
i2c.i2cw(0x5b, 0x5a, 0x28)
i2c.i2cw(0x5b, 0x5b, 0x23)
i2c.i2cw(0x5b, 0x5c, 0xc1)
i2c.i2cw(0x5b, 0x5d, 0x0e)
i2c.i2cw(0x5b, 0x60, 0x07)
i2c.i2cw(0x5b, 0x66, 0xff)
i2c.i2cw(0x5b, 0x67, 0xff)
i2c.i2cw(0x5b, 0x68, 0xff)
i2c.i2cw(0x5b, 0x69, 0xff)
i2c.i2cw(0x5b, 0x6a, 0x28)
i2c.i2cw(0x5b, 0x6b, 0x29)
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
# Ecsape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)
i2c.i2cw(0x5b, 0x10, 0xfe)
i2c.i2cw(0x5b, 0x11, 0x80)
i2c.i2cw(0x5b, 0x12, 0x6c)
i2c.i2cw(0x5b, 0x14, 0x46)
i2c.i2cw(0x5b, 0x17, 0x05)
i2c.i2cw(0x5b, 0x1a, 0x2c)
i2c.i2cw(0x5b, 0x1b, 0x08)
i2c.i2cw(0x5b, 0x1d, 0xff)
i2c.i2cw(0x5b, 0x1f, 0xef)
i2c.i2cw(0x5b, 0x20, 0xb1)
i2c.i2cw(0x5b, 0x21, 0x1e)
i2c.i2cw(0x5b, 0x22, 0x02)
i2c.i2cw(0x5b, 0x24, 0x46)
i2c.i2cw(0x5b, 0x27, 0x05)
i2c.i2cw(0x5b, 0x2a, 0x2c)
i2c.i2cw(0x5b, 0x2b, 0x08)
i2c.i2cw(0x5b, 0x2d, 0xdf)
i2c.i2cw(0x5b, 0x2f, 0x80)
i2c.i2cw(0x5b, 0x30, 0xd7)
i2c.i2cw(0x5b, 0x31, 0x28)
i2c.i2cw(0x5b, 0x32, 0x02)
i2c.i2cw(0x5b, 0x34, 0x46)
i2c.i2cw(0x5b, 0x37, 0x05)
i2c.i2cw(0x5b, 0x3a, 0x2c)
i2c.i2cw(0x5b, 0x3b, 0x08)
i2c.i2cw(0x5b, 0x3d, 0x8f)
i2c.i2cw(0x5b, 0x3f, 0x40)
i2c.i2cw(0x5b, 0x40, 0xb2)
i2c.i2cw(0x5b, 0x41, 0x23)
i2c.i2cw(0x5b, 0x42, 0x03)
i2c.i2cw(0x5b, 0x44, 0x46)
i2c.i2cw(0x5b, 0x47, 0x05)
i2c.i2cw(0x5b, 0x4a, 0x2c)
i2c.i2cw(0x5b, 0x4b, 0x08)
i2c.i2cw(0x5b, 0x4d, 0x8f)
i2c.i2cw(0x5b, 0x4f, 0x40)
i2c.i2cw(0x5b, 0x50, 0xc5)
i2c.i2cw(0x5b, 0x51, 0x0d)
i2c.i2cw(0x5b, 0x52, 0x06)
i2c.i2cw(0x5b, 0x54, 0x46)
i2c.i2cw(0x5b, 0x57, 0x05)
i2c.i2cw(0x5b, 0x5a, 0x2c)
i2c.i2cw(0x5b, 0x5b, 0x08)
i2c.i2cw(0x5b, 0x5d, 0xbf)
i2c.i2cw(0x5b, 0x5f, 0xaf)
i2c.i2cw(0x5b, 0x60, 0x10)
i2c.i2cw(0x5b, 0x61, 0x1c)
i2c.i2cw(0x5b, 0x62, 0x05)
i2c.i2cw(0x5b, 0x64, 0x46)
i2c.i2cw(0x5b, 0x67, 0x05)
i2c.i2cw(0x5b, 0x6a, 0x2c)
i2c.i2cw(0x5b, 0x6b, 0x08)
i2c.i2cw(0x5b, 0x6d, 0xcf)
i2c.i2cw(0x5b, 0x6f, 0x80)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x71, 0xff)
i2c.i2cw(0x5b, 0x72, 0xfc)
i2c.i2cw(0x5b, 0x73, 0xff)
i2c.i2cw(0x5b, 0x88, 0x54)
i2c.i2cw(0x5b, 0x89, 0x66)
i2c.i2cw(0x5b, 0x8a, 0x02)
i2c.i2cw(0x5b, 0x8b, 0x30)
i2c.i2cw(0x5b, 0x8c, 0x05)
i2c.i2cw(0x5b, 0x8d, 0x36)
i2c.i2cw(0x5b, 0x8f, 0x02)
i2c.i2cw(0x5b, 0xa0, 0x92)
i2c.i2cw(0x5b, 0xa1, 0x47)
i2c.i2cw(0x5b, 0xa2, 0x22)
i2c.i2cw(0x5b, 0xa4, 0x46)
i2c.i2cw(0x5b, 0xa7, 0x25)
i2c.i2cw(0x5b, 0xaa, 0x2c)
i2c.i2cw(0x5b, 0xab, 0x08)
i2c.i2cw(0x5b, 0xad, 0xcf)
i2c.i2cw(0x5b, 0xaf, 0x80)
i2c.i2cw(0x5b, 0xb0, 0xb3)
i2c.i2cw(0x5b, 0xb1, 0x1e)
i2c.i2cw(0x5b, 0xbf, 0x10)
i2c.i2cw(0x5b, 0xc0, 0xe2)
i2c.i2cw(0x5b, 0xc1, 0x41)
i2c.i2cw(0x5b, 0xc2, 0x40)
i2c.i2cw(0x5b, 0xc4, 0x46)
i2c.i2cw(0x5b, 0xc7, 0x25)
i2c.i2cw(0x5b, 0xca, 0x2c)
i2c.i2cw(0x5b, 0xcb, 0x08)
i2c.i2cw(0x5b, 0xcd, 0xef)
i2c.i2cw(0x5b, 0xcf, 0x60)
i2c.i2cw(0x5b, 0xd2, 0x06)
i2c.i2cw(0x5b, 0xd4, 0x46)
i2c.i2cw(0x5b, 0xd7, 0x25)
i2c.i2cw(0x5b, 0xda, 0x2c)
i2c.i2cw(0x5b, 0xdb, 0x08)
i2c.i2cw(0x5b, 0xdd, 0xdf)
i2c.i2cw(0x5b, 0xdf, 0x80)
i2c.i2cw(0x5b, 0xe0, 0x82)
i2c.i2cw(0x5b, 0xe1, 0x23)
i2c.i2cw(0x5b, 0xe2, 0x04)
i2c.i2cw(0x5b, 0xe4, 0x46)
i2c.i2cw(0x5b, 0xe7, 0x25)
i2c.i2cw(0x5b, 0xea, 0x2c)
i2c.i2cw(0x5b, 0xeb, 0x08)
i2c.i2cw(0x5b, 0xed, 0xef)
i2c.i2cw(0x5b, 0xef, 0x70)
i2c.i2cw(0x5b, 0xf0, 0xc3)
i2c.i2cw(0x5b, 0xf1, 0x13)
i2c.i2cw(0x5b, 0xf2, 0x06)
i2c.i2cw(0x5b, 0xf4, 0x46)
i2c.i2cw(0x5b, 0xf7, 0x25)
i2c.i2cw(0x5b, 0xfa, 0x2c)
i2c.i2cw(0x5b, 0xfb, 0x08)
i2c.i2cw(0x5b, 0xfc, 0x08)



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
# Escape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x34, 0x19)
i2c.i2cw(0x5b, 0x35, 0x60)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3b, 0x22)
i2c.i2cw(0x5b, 0x3c, 0x30)
i2c.i2cw(0x5b, 0x3e, 0xa0)
i2c.i2cw(0x5b, 0x3f, 0x40)

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
i2c.i2cw(0x5b, 0x10, 0x6c)
i2c.i2cw(0x5b, 0x11, 0x4e)
i2c.i2cw(0x5b, 0x12, 0x90)
i2c.i2cw(0x5b, 0x13, 0x6c)
i2c.i2cw(0x5b, 0x14, 0x4e)
i2c.i2cw(0x5b, 0x15, 0xcd)
i2c.i2cw(0x5b, 0x16, 0x3f)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0d)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0xc7)
i2c.i2cw(0x5b, 0x26, 0xa2)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x7c)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x4d)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2e)
i2c.i2cw(0x5b, 0x32, 0xf7)
i2c.i2cw(0x5b, 0x33, 0x12)
i2c.i2cw(0x5b, 0x34, 0xda)
i2c.i2cw(0x5b, 0x35, 0x4b)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xbc)
i2c.i2cw(0x5b, 0x3f, 0x02)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x47, 0x68)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xd5)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLA : end


# Disable the Outputs from CPU PLL
i2c.i2cw(0x5b, 0xff, 0x0d)
i2c.i2cw(0x5b, 0x27, 0x00)
i2c.i2cw(0x5b, 0x28, 0x00)
i2c.i2cw(0x5b, 0x0f, 0x02)
# NVM END HERE
