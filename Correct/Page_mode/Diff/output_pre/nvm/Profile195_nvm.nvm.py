# Generated by megan
# Generated on 20201229 at 20:15:30
# Version v2.3.2rc3


# Step1: HARD Reset
# Step2: Wait for CPU to reach Active State
time.sleep(0.02)
# GENERIC : begin
time.sleep(1e-06)
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x01)
i2c.i2cw(0x5b, 0x11, 0x00)
i2c.i2cw(0x5b, 0x12, 0x00)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x00)
i2c.i2cw(0x5b, 0x15, 0x00)
i2c.i2cw(0x5b, 0x16, 0x00)
i2c.i2cw(0x5b, 0x17, 0x00)
i2c.i2cw(0x5b, 0x18, 0x00)
i2c.i2cw(0x5b, 0x19, 0x00)
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
i2c.i2cw(0x5b, 0x24, 0x00)
i2c.i2cw(0x5b, 0x25, 0x00)
i2c.i2cw(0x5b, 0x26, 0x00)
i2c.i2cw(0x5b, 0x27, 0x00)
i2c.i2cw(0x5b, 0x28, 0x40)
i2c.i2cw(0x5b, 0x29, 0x28)
i2c.i2cw(0x5b, 0x2a, 0x60)
i2c.i2cw(0x5b, 0x2b, 0x00)
i2c.i2cw(0x5b, 0x2c, 0xe2)
i2c.i2cw(0x5b, 0x2d, 0x3f)
i2c.i2cw(0x5b, 0x2e, 0x00)
i2c.i2cw(0x5b, 0x2f, 0x00)
i2c.i2cw(0x5b, 0x30, 0x00)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0x00)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0x99)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3d, 0x00)
i2c.i2cw(0x5b, 0x3f, 0x70)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x50, 0x08)
i2c.i2cw(0x5b, 0x64, 0x00)
i2c.i2cw(0x5b, 0xbf, 0x00)
i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x00)
i2c.i2cw(0x5b, 0x11, 0x00)
i2c.i2cw(0x5b, 0x12, 0x00)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x00)
i2c.i2cw(0x5b, 0x15, 0x00)
i2c.i2cw(0x5b, 0x16, 0x08)
i2c.i2cw(0x5b, 0x17, 0x19)
i2c.i2cw(0x5b, 0x18, 0x2a)
i2c.i2cw(0x5b, 0x19, 0x3b)
i2c.i2cw(0x5b, 0x1a, 0x45)
i2c.i2cw(0x5b, 0x1b, 0x77)
i2c.i2cw(0x5b, 0x1c, 0x08)
i2c.i2cw(0x5b, 0x1d, 0x19)
i2c.i2cw(0x5b, 0x1e, 0x2a)
i2c.i2cw(0x5b, 0x1f, 0x3b)
i2c.i2cw(0x5b, 0x20, 0x45)
i2c.i2cw(0x5b, 0x21, 0x77)
i2c.i2cw(0x5b, 0x22, 0x08)
i2c.i2cw(0x5b, 0x23, 0x19)
i2c.i2cw(0x5b, 0x24, 0x2a)
i2c.i2cw(0x5b, 0x25, 0x3b)
i2c.i2cw(0x5b, 0x26, 0x45)
i2c.i2cw(0x5b, 0x27, 0x77)
i2c.i2cw(0x5b, 0x28, 0x08)
i2c.i2cw(0x5b, 0x29, 0x19)
i2c.i2cw(0x5b, 0x2a, 0x2a)
i2c.i2cw(0x5b, 0x2b, 0x3b)
i2c.i2cw(0x5b, 0x2c, 0x45)
i2c.i2cw(0x5b, 0x2d, 0x77)
i2c.i2cw(0x5b, 0x2e, 0x00)
i2c.i2cw(0x5b, 0x2f, 0x00)
# Update Small Change
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0x0f, 0x02)
# GENERIC : end


# INPUT_SYS: begin
i2c.i2cw(0x5b, 0xff, 0x02)
i2c.i2cw(0x5b, 0xbd, 0xc3)
# Ecsape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)
i2c.i2cw(0x5b, 0x10, 0x07)
i2c.i2cw(0x5b, 0x11, 0x00)
i2c.i2cw(0x5b, 0x12, 0x00)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x00)
i2c.i2cw(0x5b, 0x15, 0x00)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x23)
i2c.i2cw(0x5b, 0x1c, 0xc1)
i2c.i2cw(0x5b, 0x1d, 0x0e)
i2c.i2cw(0x5b, 0x20, 0x15)
i2c.i2cw(0x5b, 0x21, 0x00)
i2c.i2cw(0x5b, 0x22, 0x00)
i2c.i2cw(0x5b, 0x23, 0x00)
i2c.i2cw(0x5b, 0x24, 0x00)
i2c.i2cw(0x5b, 0x25, 0x00)
i2c.i2cw(0x5b, 0x26, 0xff)
i2c.i2cw(0x5b, 0x27, 0xff)
i2c.i2cw(0x5b, 0x28, 0xff)
i2c.i2cw(0x5b, 0x29, 0xff)
i2c.i2cw(0x5b, 0x2a, 0x28)
i2c.i2cw(0x5b, 0x2b, 0x23)
i2c.i2cw(0x5b, 0x2c, 0xc0)
i2c.i2cw(0x5b, 0x2d, 0x07)
i2c.i2cw(0x5b, 0x30, 0x07)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0x00)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x00)
i2c.i2cw(0x5b, 0x35, 0x00)
i2c.i2cw(0x5b, 0x36, 0xff)
i2c.i2cw(0x5b, 0x37, 0xff)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0x28)
i2c.i2cw(0x5b, 0x3b, 0x23)
i2c.i2cw(0x5b, 0x3c, 0xc1)
i2c.i2cw(0x5b, 0x3d, 0x0e)
i2c.i2cw(0x5b, 0x40, 0x15)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x00)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x00)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0xff)
i2c.i2cw(0x5b, 0x47, 0xff)
i2c.i2cw(0x5b, 0x48, 0xff)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0x28)
i2c.i2cw(0x5b, 0x4b, 0x23)
i2c.i2cw(0x5b, 0x4c, 0xc1)
i2c.i2cw(0x5b, 0x4d, 0x07)
i2c.i2cw(0x5b, 0x50, 0x1c)
i2c.i2cw(0x5b, 0x51, 0x00)
i2c.i2cw(0x5b, 0x52, 0x00)
i2c.i2cw(0x5b, 0x53, 0x00)
i2c.i2cw(0x5b, 0x54, 0x00)
i2c.i2cw(0x5b, 0x55, 0x00)
i2c.i2cw(0x5b, 0x56, 0xff)
i2c.i2cw(0x5b, 0x57, 0xff)
i2c.i2cw(0x5b, 0x58, 0xff)
i2c.i2cw(0x5b, 0x59, 0xff)
i2c.i2cw(0x5b, 0x5a, 0x28)
i2c.i2cw(0x5b, 0x5b, 0x23)
i2c.i2cw(0x5b, 0x5c, 0xc1)
i2c.i2cw(0x5b, 0x5d, 0x0e)
i2c.i2cw(0x5b, 0x60, 0x07)
i2c.i2cw(0x5b, 0x61, 0x00)
i2c.i2cw(0x5b, 0x62, 0x00)
i2c.i2cw(0x5b, 0x63, 0x00)
i2c.i2cw(0x5b, 0x64, 0x00)
i2c.i2cw(0x5b, 0x65, 0x00)
i2c.i2cw(0x5b, 0x66, 0xff)
i2c.i2cw(0x5b, 0x67, 0xff)
i2c.i2cw(0x5b, 0x68, 0xff)
i2c.i2cw(0x5b, 0x69, 0xff)
i2c.i2cw(0x5b, 0x6a, 0x28)
i2c.i2cw(0x5b, 0x6b, 0x29)
i2c.i2cw(0x5b, 0x6c, 0x0a)

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
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x46)
i2c.i2cw(0x5b, 0x15, 0x00)
i2c.i2cw(0x5b, 0x16, 0x00)
i2c.i2cw(0x5b, 0x17, 0x05)
i2c.i2cw(0x5b, 0x18, 0x00)
i2c.i2cw(0x5b, 0x19, 0x00)
i2c.i2cw(0x5b, 0x1a, 0x2e)
i2c.i2cw(0x5b, 0x1b, 0x07)
i2c.i2cw(0x5b, 0x1c, 0x02)
i2c.i2cw(0x5b, 0x1d, 0x33)
i2c.i2cw(0x5b, 0x1e, 0x02)
i2c.i2cw(0x5b, 0x1f, 0x10)
i2c.i2cw(0x5b, 0x20, 0xb1)
i2c.i2cw(0x5b, 0x21, 0x1e)
i2c.i2cw(0x5b, 0x22, 0x02)
i2c.i2cw(0x5b, 0x23, 0x00)
i2c.i2cw(0x5b, 0x24, 0x46)
i2c.i2cw(0x5b, 0x25, 0x00)
i2c.i2cw(0x5b, 0x26, 0x00)
i2c.i2cw(0x5b, 0x27, 0x05)
i2c.i2cw(0x5b, 0x28, 0x00)
i2c.i2cw(0x5b, 0x29, 0x00)
i2c.i2cw(0x5b, 0x2a, 0x2e)
i2c.i2cw(0x5b, 0x2b, 0x07)
i2c.i2cw(0x5b, 0x2c, 0x01)
i2c.i2cw(0x5b, 0x2d, 0xed)
i2c.i2cw(0x5b, 0x2e, 0x01)
i2c.i2cw(0x5b, 0x2f, 0x1a)
i2c.i2cw(0x5b, 0x30, 0xd7)
i2c.i2cw(0x5b, 0x31, 0x28)
i2c.i2cw(0x5b, 0x32, 0x02)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x46)
i2c.i2cw(0x5b, 0x35, 0x00)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x05)
i2c.i2cw(0x5b, 0x38, 0x00)
i2c.i2cw(0x5b, 0x39, 0x00)
i2c.i2cw(0x5b, 0x3a, 0x2e)
i2c.i2cw(0x5b, 0x3b, 0x07)
i2c.i2cw(0x5b, 0x3c, 0x01)
i2c.i2cw(0x5b, 0x3d, 0x3d)
i2c.i2cw(0x5b, 0x3e, 0x00)
i2c.i2cw(0x5b, 0x3f, 0x8d)
i2c.i2cw(0x5b, 0x40, 0xb2)
i2c.i2cw(0x5b, 0x41, 0x23)
i2c.i2cw(0x5b, 0x42, 0x03)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x46)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x05)
i2c.i2cw(0x5b, 0x48, 0x00)
i2c.i2cw(0x5b, 0x49, 0x00)
i2c.i2cw(0x5b, 0x4a, 0x2e)
i2c.i2cw(0x5b, 0x4b, 0x07)
i2c.i2cw(0x5b, 0x4c, 0x01)
i2c.i2cw(0x5b, 0x4d, 0x3d)
i2c.i2cw(0x5b, 0x4e, 0x00)
i2c.i2cw(0x5b, 0x4f, 0x8d)
i2c.i2cw(0x5b, 0x50, 0xc5)
i2c.i2cw(0x5b, 0x51, 0x0d)
i2c.i2cw(0x5b, 0x52, 0x06)
i2c.i2cw(0x5b, 0x53, 0x00)
i2c.i2cw(0x5b, 0x54, 0x46)
i2c.i2cw(0x5b, 0x55, 0x00)
i2c.i2cw(0x5b, 0x56, 0x00)
i2c.i2cw(0x5b, 0x57, 0x05)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x59, 0x00)
i2c.i2cw(0x5b, 0x5a, 0x2e)
i2c.i2cw(0x5b, 0x5b, 0x07)
i2c.i2cw(0x5b, 0x5c, 0x01)
i2c.i2cw(0x5b, 0x5d, 0xa7)
i2c.i2cw(0x5b, 0x5e, 0x01)
i2c.i2cw(0x5b, 0x5f, 0x83)
i2c.i2cw(0x5b, 0x60, 0x10)
i2c.i2cw(0x5b, 0x61, 0x1c)
i2c.i2cw(0x5b, 0x62, 0x05)
i2c.i2cw(0x5b, 0x63, 0x00)
i2c.i2cw(0x5b, 0x64, 0x46)
i2c.i2cw(0x5b, 0x65, 0x00)
i2c.i2cw(0x5b, 0x66, 0x00)
i2c.i2cw(0x5b, 0x67, 0x05)
i2c.i2cw(0x5b, 0x68, 0x00)
i2c.i2cw(0x5b, 0x69, 0x00)
i2c.i2cw(0x5b, 0x6a, 0x2e)
i2c.i2cw(0x5b, 0x6b, 0x07)
i2c.i2cw(0x5b, 0x6c, 0x01)
i2c.i2cw(0x5b, 0x6d, 0xca)
i2c.i2cw(0x5b, 0x6e, 0x01)
i2c.i2cw(0x5b, 0x6f, 0x1a)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x71, 0xff)
i2c.i2cw(0x5b, 0x72, 0xfc)
i2c.i2cw(0x5b, 0x73, 0xff)
i2c.i2cw(0x5b, 0x7a, 0x00)
i2c.i2cw(0x5b, 0x7b, 0x00)
i2c.i2cw(0x5b, 0x7c, 0x00)
i2c.i2cw(0x5b, 0x7d, 0x00)
i2c.i2cw(0x5b, 0x7e, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x00)
i2c.i2cw(0x5b, 0x80, 0x00)
i2c.i2cw(0x5b, 0x81, 0x00)
i2c.i2cw(0x5b, 0x82, 0x00)
i2c.i2cw(0x5b, 0x83, 0x00)
i2c.i2cw(0x5b, 0x84, 0x00)
i2c.i2cw(0x5b, 0x85, 0x00)
i2c.i2cw(0x5b, 0x86, 0x00)
i2c.i2cw(0x5b, 0x87, 0x00)
i2c.i2cw(0x5b, 0x88, 0x54)
i2c.i2cw(0x5b, 0x89, 0x66)
i2c.i2cw(0x5b, 0x8a, 0x02)
i2c.i2cw(0x5b, 0x8b, 0x30)
i2c.i2cw(0x5b, 0x8c, 0x05)
i2c.i2cw(0x5b, 0x8d, 0x36)
i2c.i2cw(0x5b, 0x8e, 0x00)
i2c.i2cw(0x5b, 0x8f, 0x06)
i2c.i2cw(0x5b, 0xa0, 0x92)
i2c.i2cw(0x5b, 0xa1, 0x47)
i2c.i2cw(0x5b, 0xa2, 0x22)
i2c.i2cw(0x5b, 0xa3, 0x00)
i2c.i2cw(0x5b, 0xa4, 0x46)
i2c.i2cw(0x5b, 0xa5, 0x00)
i2c.i2cw(0x5b, 0xa6, 0x00)
i2c.i2cw(0x5b, 0xa7, 0x25)
i2c.i2cw(0x5b, 0xa8, 0x00)
i2c.i2cw(0x5b, 0xa9, 0x00)
i2c.i2cw(0x5b, 0xaa, 0x2e)
i2c.i2cw(0x5b, 0xab, 0x07)
i2c.i2cw(0x5b, 0xac, 0x01)
i2c.i2cw(0x5b, 0xad, 0xca)
i2c.i2cw(0x5b, 0xae, 0x01)
i2c.i2cw(0x5b, 0xaf, 0x1a)
i2c.i2cw(0x5b, 0xb0, 0xb3)
i2c.i2cw(0x5b, 0xb1, 0x1e)
i2c.i2cw(0x5b, 0xbf, 0x6a)
i2c.i2cw(0x5b, 0xc0, 0xe2)
i2c.i2cw(0x5b, 0xc1, 0x41)
i2c.i2cw(0x5b, 0xc2, 0x40)
i2c.i2cw(0x5b, 0xc3, 0x00)
i2c.i2cw(0x5b, 0xc4, 0x46)
i2c.i2cw(0x5b, 0xc5, 0x00)
i2c.i2cw(0x5b, 0xc6, 0x00)
i2c.i2cw(0x5b, 0xc7, 0x25)
i2c.i2cw(0x5b, 0xc8, 0x00)
i2c.i2cw(0x5b, 0xc9, 0x00)
i2c.i2cw(0x5b, 0xca, 0x2e)
i2c.i2cw(0x5b, 0xcb, 0x07)
i2c.i2cw(0x5b, 0xcc, 0x02)
i2c.i2cw(0x5b, 0xcd, 0x10)
i2c.i2cw(0x5b, 0xce, 0x00)
i2c.i2cw(0x5b, 0xcf, 0xd4)
i2c.i2cw(0x5b, 0xd2, 0x06)
i2c.i2cw(0x5b, 0xd3, 0x00)
i2c.i2cw(0x5b, 0xd4, 0x46)
i2c.i2cw(0x5b, 0xd5, 0x00)
i2c.i2cw(0x5b, 0xd6, 0x00)
i2c.i2cw(0x5b, 0xd7, 0x25)
i2c.i2cw(0x5b, 0xd8, 0x00)
i2c.i2cw(0x5b, 0xd9, 0x00)
i2c.i2cw(0x5b, 0xda, 0x2e)
i2c.i2cw(0x5b, 0xdb, 0x07)
i2c.i2cw(0x5b, 0xdc, 0x01)
i2c.i2cw(0x5b, 0xdd, 0xed)
i2c.i2cw(0x5b, 0xde, 0x01)
i2c.i2cw(0x5b, 0xdf, 0x1a)
i2c.i2cw(0x5b, 0xe0, 0x82)
i2c.i2cw(0x5b, 0xe1, 0x23)
i2c.i2cw(0x5b, 0xe2, 0x04)
i2c.i2cw(0x5b, 0xe3, 0x00)
i2c.i2cw(0x5b, 0xe4, 0x46)
i2c.i2cw(0x5b, 0xe5, 0x00)
i2c.i2cw(0x5b, 0xe6, 0x00)
i2c.i2cw(0x5b, 0xe7, 0x25)
i2c.i2cw(0x5b, 0xe8, 0x00)
i2c.i2cw(0x5b, 0xe9, 0x00)
i2c.i2cw(0x5b, 0xea, 0x2e)
i2c.i2cw(0x5b, 0xeb, 0x07)
i2c.i2cw(0x5b, 0xec, 0x02)
i2c.i2cw(0x5b, 0xed, 0x10)
i2c.i2cw(0x5b, 0xee, 0x00)
i2c.i2cw(0x5b, 0xef, 0xf7)
i2c.i2cw(0x5b, 0xf0, 0xc3)
i2c.i2cw(0x5b, 0xf1, 0x13)
i2c.i2cw(0x5b, 0xf2, 0x06)
i2c.i2cw(0x5b, 0xf3, 0x00)
i2c.i2cw(0x5b, 0xf4, 0x46)
i2c.i2cw(0x5b, 0xf5, 0x00)
i2c.i2cw(0x5b, 0xf6, 0x00)
i2c.i2cw(0x5b, 0xf7, 0x25)
i2c.i2cw(0x5b, 0xf8, 0x00)
i2c.i2cw(0x5b, 0xf9, 0x00)
i2c.i2cw(0x5b, 0xfa, 0x2e)
i2c.i2cw(0x5b, 0xfb, 0x07)
i2c.i2cw(0x5b, 0xfc, 0x11)
i2c.i2cw(0x5b, 0xfd, 0xa0)



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
# Ecsape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)
i2c.i2cw(0x5b, 0x10, 0x00)
i2c.i2cw(0x5b, 0x11, 0x00)
i2c.i2cw(0x5b, 0x12, 0x00)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x32)
i2c.i2cw(0x5b, 0x15, 0x41)
i2c.i2cw(0x5b, 0x16, 0xbf)
i2c.i2cw(0x5b, 0x17, 0x08)
i2c.i2cw(0x5b, 0x18, 0xeb)
i2c.i2cw(0x5b, 0x19, 0x02)
i2c.i2cw(0x5b, 0x1a, 0xd7)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x30)
i2c.i2cw(0x5b, 0x1e, 0x6c)
i2c.i2cw(0x5b, 0x1f, 0x00)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x00)
i2c.i2cw(0x5b, 0x22, 0x00)
i2c.i2cw(0x5b, 0x23, 0x00)
i2c.i2cw(0x5b, 0x24, 0x0a)
i2c.i2cw(0x5b, 0x25, 0x40)
i2c.i2cw(0x5b, 0x26, 0x1d)
i2c.i2cw(0x5b, 0x27, 0xcd)
i2c.i2cw(0x5b, 0x28, 0x65)
i2c.i2cw(0x5b, 0x29, 0x02)
i2c.i2cw(0x5b, 0x2a, 0x17)
i2c.i2cw(0x5b, 0x2b, 0x00)
i2c.i2cw(0x5b, 0x2c, 0x31)
i2c.i2cw(0x5b, 0x2e, 0x60)
i2c.i2cw(0x5b, 0x2f, 0x03)
i2c.i2cw(0x5b, 0x30, 0x00)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0x00)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x1d)
i2c.i2cw(0x5b, 0x35, 0x40)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x00)
i2c.i2cw(0x5b, 0x38, 0x00)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3b, 0x00)
i2c.i2cw(0x5b, 0x3c, 0x30)
i2c.i2cw(0x5b, 0x3e, 0x6c)
i2c.i2cw(0x5b, 0x3f, 0x00)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x00)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x0b)
i2c.i2cw(0x5b, 0x45, 0x40)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x00)
i2c.i2cw(0x5b, 0x48, 0x00)
i2c.i2cw(0x5b, 0x49, 0x02)
i2c.i2cw(0x5b, 0x4a, 0x17)
i2c.i2cw(0x5b, 0x4b, 0x00)
i2c.i2cw(0x5b, 0x4c, 0x31)
i2c.i2cw(0x5b, 0x4e, 0x60)
i2c.i2cw(0x5b, 0x4f, 0x05)
i2c.i2cw(0x5b, 0x50, 0x00)
i2c.i2cw(0x5b, 0x51, 0x00)
i2c.i2cw(0x5b, 0x52, 0x00)
i2c.i2cw(0x5b, 0x53, 0x00)
i2c.i2cw(0x5b, 0x54, 0x3a)
i2c.i2cw(0x5b, 0x55, 0x40)
i2c.i2cw(0x5b, 0x56, 0x00)
i2c.i2cw(0x5b, 0x57, 0x00)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x59, 0x02)
i2c.i2cw(0x5b, 0x5a, 0x0f)
i2c.i2cw(0x5b, 0x5b, 0x00)
i2c.i2cw(0x5b, 0x5c, 0x20)
i2c.i2cw(0x5b, 0x5e, 0x6c)
i2c.i2cw(0x5b, 0x5f, 0x00)
i2c.i2cw(0x5b, 0x60, 0x00)
i2c.i2cw(0x5b, 0x61, 0x00)
i2c.i2cw(0x5b, 0x62, 0x00)
i2c.i2cw(0x5b, 0x63, 0x00)
i2c.i2cw(0x5b, 0x64, 0x0b)
i2c.i2cw(0x5b, 0x65, 0x40)
i2c.i2cw(0x5b, 0x66, 0x41)
i2c.i2cw(0x5b, 0x67, 0x90)
i2c.i2cw(0x5b, 0x68, 0xab)
i2c.i2cw(0x5b, 0x69, 0x02)
i2c.i2cw(0x5b, 0x6a, 0x17)
i2c.i2cw(0x5b, 0x6b, 0x00)
i2c.i2cw(0x5b, 0x6c, 0x2a)
i2c.i2cw(0x5b, 0x6e, 0x60)
i2c.i2cw(0x5b, 0x6f, 0x03)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0x00)
i2c.i2cw(0x5b, 0x11, 0x00)
i2c.i2cw(0x5b, 0x12, 0x00)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x4b)
i2c.i2cw(0x5b, 0x15, 0x41)
i2c.i2cw(0x5b, 0x16, 0x92)
i2c.i2cw(0x5b, 0x17, 0x54)
i2c.i2cw(0x5b, 0x18, 0xd3)
i2c.i2cw(0x5b, 0x19, 0x82)
i2c.i2cw(0x5b, 0x1a, 0x17)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x28)
i2c.i2cw(0x5b, 0x1e, 0x6c)
i2c.i2cw(0x5b, 0x1f, 0x00)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x00)
i2c.i2cw(0x5b, 0x22, 0x00)
i2c.i2cw(0x5b, 0x23, 0x00)
i2c.i2cw(0x5b, 0x24, 0x32)
i2c.i2cw(0x5b, 0x25, 0x40)
i2c.i2cw(0x5b, 0x26, 0x00)
i2c.i2cw(0x5b, 0x27, 0x00)
i2c.i2cw(0x5b, 0x28, 0x00)
i2c.i2cw(0x5b, 0x29, 0x02)
i2c.i2cw(0x5b, 0x2a, 0x17)
i2c.i2cw(0x5b, 0x2b, 0x00)
i2c.i2cw(0x5b, 0x2c, 0x33)
i2c.i2cw(0x5b, 0x2e, 0x60)
i2c.i2cw(0x5b, 0x2f, 0x02)
i2c.i2cw(0x5b, 0x30, 0x00)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0x00)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x0b)
i2c.i2cw(0x5b, 0x35, 0x60)
i2c.i2cw(0x5b, 0x36, 0xa3)
i2c.i2cw(0x5b, 0x37, 0xe9)
i2c.i2cw(0x5b, 0x38, 0xab)
i2c.i2cw(0x5b, 0x39, 0x82)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3b, 0x00)
i2c.i2cw(0x5b, 0x3c, 0x30)
i2c.i2cw(0x5b, 0x3e, 0xa0)
i2c.i2cw(0x5b, 0x3f, 0x44)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x00)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x1e)
i2c.i2cw(0x5b, 0x45, 0x41)
i2c.i2cw(0x5b, 0x46, 0x0c)
i2c.i2cw(0x5b, 0x47, 0x38)
i2c.i2cw(0x5b, 0x48, 0x8d)
i2c.i2cw(0x5b, 0x49, 0x02)
i2c.i2cw(0x5b, 0x4a, 0xd7)
i2c.i2cw(0x5b, 0x4b, 0x00)
i2c.i2cw(0x5b, 0x4c, 0x28)
i2c.i2cw(0x5b, 0x4e, 0x6c)
i2c.i2cw(0x5b, 0x4f, 0x20)
i2c.i2cw(0x5b, 0x50, 0x00)
i2c.i2cw(0x5b, 0x51, 0x00)
i2c.i2cw(0x5b, 0x52, 0x00)
i2c.i2cw(0x5b, 0x53, 0x00)
i2c.i2cw(0x5b, 0x54, 0x0a)
i2c.i2cw(0x5b, 0x55, 0x40)
i2c.i2cw(0x5b, 0x56, 0x00)
i2c.i2cw(0x5b, 0x57, 0x00)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x59, 0x02)
i2c.i2cw(0x5b, 0x5a, 0x17)
i2c.i2cw(0x5b, 0x5b, 0x00)
i2c.i2cw(0x5b, 0x5c, 0x33)
i2c.i2cw(0x5b, 0x5e, 0x60)
i2c.i2cw(0x5b, 0x5f, 0x44)
i2c.i2cw(0x5b, 0x60, 0x00)
i2c.i2cw(0x5b, 0x61, 0x00)
i2c.i2cw(0x5b, 0x62, 0x00)
i2c.i2cw(0x5b, 0x63, 0x00)
i2c.i2cw(0x5b, 0x64, 0x1d)
i2c.i2cw(0x5b, 0x65, 0x40)
i2c.i2cw(0x5b, 0x66, 0x00)
i2c.i2cw(0x5b, 0x67, 0x00)
i2c.i2cw(0x5b, 0x68, 0x00)
i2c.i2cw(0x5b, 0x69, 0x02)
i2c.i2cw(0x5b, 0x6a, 0x17)
i2c.i2cw(0x5b, 0x6b, 0x00)
i2c.i2cw(0x5b, 0x6c, 0x28)
i2c.i2cw(0x5b, 0x6e, 0x6c)
i2c.i2cw(0x5b, 0x6f, 0xc0)

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
i2c.i2cw(0x5b, 0x0d, 0x00)
i2c.i2cw(0x5b, 0x10, 0xbd)
i2c.i2cw(0x5b, 0x11, 0xed)
i2c.i2cw(0x5b, 0x12, 0x9e)
i2c.i2cw(0x5b, 0x13, 0xbd)
i2c.i2cw(0x5b, 0x14, 0xed)
i2c.i2cw(0x5b, 0x15, 0x9e)
i2c.i2cw(0x5b, 0x16, 0xb0)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0b)
i2c.i2cw(0x5b, 0x19, 0x42)
i2c.i2cw(0x5b, 0x1a, 0xd8)
i2c.i2cw(0x5b, 0x1b, 0xd6)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x30)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x02)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x0b)
i2c.i2cw(0x5b, 0x25, 0xcb)
i2c.i2cw(0x5b, 0x26, 0x02)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x28, 0x88)
i2c.i2cw(0x5b, 0x29, 0xcf)
i2c.i2cw(0x5b, 0x2a, 0x98)
i2c.i2cw(0x5b, 0x2b, 0xde)
i2c.i2cw(0x5b, 0x2c, 0xfc)
i2c.i2cw(0x5b, 0x2d, 0x00)
i2c.i2cw(0x5b, 0x2e, 0x74)
i2c.i2cw(0x5b, 0x2f, 0x0f)
i2c.i2cw(0x5b, 0x30, 0x33)
i2c.i2cw(0x5b, 0x31, 0x0e)
i2c.i2cw(0x5b, 0x32, 0x42)
i2c.i2cw(0x5b, 0x33, 0x7b)
i2c.i2cw(0x5b, 0x34, 0x09)
i2c.i2cw(0x5b, 0x35, 0xed)
i2c.i2cw(0x5b, 0x36, 0x3c)
i2c.i2cw(0x5b, 0x37, 0x0c)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x02)
i2c.i2cw(0x5b, 0x3f, 0x03)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0xa0)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x00)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x88)
i2c.i2cw(0x5b, 0x48, 0x89)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xd3)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xbc)
i2c.i2cw(0x5b, 0x57, 0xc0)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0xc0, 0x20)
i2c.i2cw(0x5b, 0xc1, 0x20)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLA : end


# PLLB : begin
i2c.i2cw(0x5b, 0xff, 0x0b)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x0d, 0x00)
i2c.i2cw(0x5b, 0x10, 0x67)
i2c.i2cw(0x5b, 0x11, 0x4e)
i2c.i2cw(0x5b, 0x12, 0x89)
i2c.i2cw(0x5b, 0x13, 0x67)
i2c.i2cw(0x5b, 0x14, 0x4e)
i2c.i2cw(0x5b, 0x15, 0x89)
i2c.i2cw(0x5b, 0x16, 0xb0)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0c)
i2c.i2cw(0x5b, 0x19, 0x42)
i2c.i2cw(0x5b, 0x1a, 0x00)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0x28)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x06)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x0b)
i2c.i2cw(0x5b, 0x25, 0xcc)
i2c.i2cw(0x5b, 0x26, 0x02)
i2c.i2cw(0x5b, 0x27, 0x04)
i2c.i2cw(0x5b, 0x28, 0x44)
i2c.i2cw(0x5b, 0x29, 0x15)
i2c.i2cw(0x5b, 0x2a, 0x82)
i2c.i2cw(0x5b, 0x2b, 0xc2)
i2c.i2cw(0x5b, 0x2c, 0xac)
i2c.i2cw(0x5b, 0x2d, 0x00)
i2c.i2cw(0x5b, 0x2e, 0x84)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x45)
i2c.i2cw(0x5b, 0x31, 0x0e)
i2c.i2cw(0x5b, 0x32, 0x72)
i2c.i2cw(0x5b, 0x33, 0x1c)
i2c.i2cw(0x5b, 0x34, 0xc7)
i2c.i2cw(0x5b, 0x35, 0x71)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x0c)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x1a)
i2c.i2cw(0x5b, 0x3f, 0x04)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0xc0)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x00)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x24)
i2c.i2cw(0x5b, 0x48, 0x44)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc7)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xb4)
i2c.i2cw(0x5b, 0x57, 0xc0)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0xc0, 0x20)
i2c.i2cw(0x5b, 0xc1, 0x20)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLB : end


# PLLC : begin
i2c.i2cw(0x5b, 0xff, 0x0c)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x0d, 0x00)
i2c.i2cw(0x5b, 0x10, 0xc7)
i2c.i2cw(0x5b, 0x11, 0x23)
i2c.i2cw(0x5b, 0x12, 0xc7)
i2c.i2cw(0x5b, 0x13, 0xc7)
i2c.i2cw(0x5b, 0x14, 0x23)
i2c.i2cw(0x5b, 0x15, 0xc7)
i2c.i2cw(0x5b, 0x16, 0xb0)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0d)
i2c.i2cw(0x5b, 0x19, 0x42)
i2c.i2cw(0x5b, 0x1a, 0x00)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0xe0)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x07)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x83)
i2c.i2cw(0x5b, 0x24, 0x0b)
i2c.i2cw(0x5b, 0x25, 0x87)
i2c.i2cw(0x5b, 0x26, 0x02)
i2c.i2cw(0x5b, 0x27, 0x04)
i2c.i2cw(0x5b, 0x28, 0x44)
i2c.i2cw(0x5b, 0x29, 0x13)
i2c.i2cw(0x5b, 0x2a, 0x80)
i2c.i2cw(0x5b, 0x2b, 0x04)
i2c.i2cw(0x5b, 0x2c, 0xf0)
i2c.i2cw(0x5b, 0x2d, 0x00)
i2c.i2cw(0x5b, 0x2e, 0x74)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2e)
i2c.i2cw(0x5b, 0x31, 0x09)
i2c.i2cw(0x5b, 0x32, 0xf7)
i2c.i2cw(0x5b, 0x33, 0x12)
i2c.i2cw(0x5b, 0x34, 0xda)
i2c.i2cw(0x5b, 0x35, 0x4b)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x0b)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xbc)
i2c.i2cw(0x5b, 0x3f, 0x02)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x00)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x00)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x14)
i2c.i2cw(0x5b, 0x48, 0x44)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc8)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xbc)
i2c.i2cw(0x5b, 0x57, 0xc0)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0xc0, 0x20)
i2c.i2cw(0x5b, 0xc1, 0x20)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLC : end


# PLLD : begin
i2c.i2cw(0x5b, 0xff, 0x0d)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x0d, 0x00)
i2c.i2cw(0x5b, 0x10, 0x85)
i2c.i2cw(0x5b, 0x11, 0x3e)
i2c.i2cw(0x5b, 0x12, 0xc6)
i2c.i2cw(0x5b, 0x13, 0x85)
i2c.i2cw(0x5b, 0x14, 0x3e)
i2c.i2cw(0x5b, 0x15, 0xc6)
i2c.i2cw(0x5b, 0x16, 0xb0)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0e)
i2c.i2cw(0x5b, 0x19, 0x42)
i2c.i2cw(0x5b, 0x1a, 0x00)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0x28)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x19)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x83)
i2c.i2cw(0x5b, 0x24, 0x0b)
i2c.i2cw(0x5b, 0x25, 0x73)
i2c.i2cw(0x5b, 0x26, 0x02)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x28, 0x88)
i2c.i2cw(0x5b, 0x29, 0x15)
i2c.i2cw(0x5b, 0x2a, 0x71)
i2c.i2cw(0x5b, 0x2b, 0x2c)
i2c.i2cw(0x5b, 0x2c, 0x60)
i2c.i2cw(0x5b, 0x2d, 0x04)
i2c.i2cw(0x5b, 0x2e, 0xad)
i2c.i2cw(0x5b, 0x2f, 0x47)
i2c.i2cw(0x5b, 0x30, 0x40)
i2c.i2cw(0x5b, 0x31, 0x0b)
i2c.i2cw(0x5b, 0x32, 0x72)
i2c.i2cw(0x5b, 0x33, 0x1c)
i2c.i2cw(0x5b, 0x34, 0xc7)
i2c.i2cw(0x5b, 0x35, 0x71)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x00)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xce)
i2c.i2cw(0x5b, 0x3f, 0x03)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x00)
i2c.i2cw(0x5b, 0x43, 0x66)
i2c.i2cw(0x5b, 0x44, 0x66)
i2c.i2cw(0x5b, 0x45, 0x66)
i2c.i2cw(0x5b, 0x46, 0x66)
i2c.i2cw(0x5b, 0x47, 0x28)
i2c.i2cw(0x5b, 0x48, 0x88)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc8)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xa5)
i2c.i2cw(0x5b, 0x57, 0xc0)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0xc0, 0x00)
i2c.i2cw(0x5b, 0xc1, 0x00)
# Restart PLL
i2c.i2cw(0x5b, 0xbe, 0x40)
time.sleep(1e-06)
i2c.i2cw(0x5b, 0xbe, 0x00)
# PLLD : end
time.sleep(0.0049513199999999995)


