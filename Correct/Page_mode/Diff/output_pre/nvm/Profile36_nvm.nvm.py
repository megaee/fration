# Generated by megan
# Generated on 20201229 at 16:08:36
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
i2c.i2cw(0x5b, 0x3f, 0x76)
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
i2c.i2cw(0x5b, 0x16, 0x00)
i2c.i2cw(0x5b, 0x17, 0x00)
i2c.i2cw(0x5b, 0x18, 0x00)
i2c.i2cw(0x5b, 0x19, 0x00)
i2c.i2cw(0x5b, 0x1a, 0x00)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0x00)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x00)
i2c.i2cw(0x5b, 0x22, 0x00)
i2c.i2cw(0x5b, 0x23, 0x00)
i2c.i2cw(0x5b, 0x24, 0x00)
i2c.i2cw(0x5b, 0x25, 0x00)
i2c.i2cw(0x5b, 0x26, 0x00)
i2c.i2cw(0x5b, 0x27, 0x00)
i2c.i2cw(0x5b, 0x28, 0x00)
i2c.i2cw(0x5b, 0x29, 0x00)
i2c.i2cw(0x5b, 0x2a, 0x00)
i2c.i2cw(0x5b, 0x2b, 0x00)
i2c.i2cw(0x5b, 0x2c, 0x00)
i2c.i2cw(0x5b, 0x2d, 0x00)
i2c.i2cw(0x5b, 0x2e, 0x00)
i2c.i2cw(0x5b, 0x2f, 0x00)
# Update Small Change
i2c.i2cw(0x5b, 0xff, 0x00)
i2c.i2cw(0x5b, 0x0f, 0x02)
# Disabling CPU PLL
i2c.i2cw(0x5b, 0xec, 0x10)
# GENERIC : end


# INPUT_SYS: begin
i2c.i2cw(0x5b, 0xff, 0x02)
i2c.i2cw(0x5b, 0xbd, 0xc3)
# Ecsape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)
i2c.i2cw(0x5b, 0x10, 0x0a)
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
i2c.i2cw(0x5b, 0x1b, 0x21)
i2c.i2cw(0x5b, 0x1c, 0x41)
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
i2c.i2cw(0x5b, 0x10, 0x43)
i2c.i2cw(0x5b, 0x11, 0x05)
i2c.i2cw(0x5b, 0x12, 0x04)
i2c.i2cw(0x5b, 0x13, 0x00)
i2c.i2cw(0x5b, 0x14, 0x50)
i2c.i2cw(0x5b, 0x15, 0x00)
i2c.i2cw(0x5b, 0x16, 0x00)
i2c.i2cw(0x5b, 0x17, 0xc3)
i2c.i2cw(0x5b, 0x18, 0x00)
i2c.i2cw(0x5b, 0x19, 0x00)
i2c.i2cw(0x5b, 0x1a, 0x2a)
i2c.i2cw(0x5b, 0x1b, 0x06)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0xa1)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0x97)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x71, 0xc0)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x73, 0x00)
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
i2c.i2cw(0x5b, 0x88, 0x00)
i2c.i2cw(0x5b, 0x89, 0x00)
i2c.i2cw(0x5b, 0x8a, 0x00)
i2c.i2cw(0x5b, 0x8b, 0x30)
i2c.i2cw(0x5b, 0x8c, 0x00)
i2c.i2cw(0x5b, 0x8d, 0x00)
i2c.i2cw(0x5b, 0x8e, 0x00)
i2c.i2cw(0x5b, 0x8f, 0x06)



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


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x30, 0x00)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0x00)
i2c.i2cw(0x5b, 0x33, 0x00)
i2c.i2cw(0x5b, 0x34, 0x19)
i2c.i2cw(0x5b, 0x35, 0x60)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x00)
i2c.i2cw(0x5b, 0x38, 0x00)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
i2c.i2cw(0x5b, 0x3b, 0x00)
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
i2c.i2cw(0x5b, 0x0d, 0x00)
i2c.i2cw(0x5b, 0x10, 0xae)
i2c.i2cw(0x5b, 0x11, 0x4e)
i2c.i2cw(0x5b, 0x12, 0xd2)
i2c.i2cw(0x5b, 0x13, 0xae)
i2c.i2cw(0x5b, 0x14, 0x4e)
i2c.i2cw(0x5b, 0x15, 0x6e)
i2c.i2cw(0x5b, 0x16, 0x3f)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x0d)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1a, 0x00)
i2c.i2cw(0x5b, 0x1b, 0x00)
i2c.i2cw(0x5b, 0x1c, 0x00)
i2c.i2cw(0x5b, 0x1d, 0x00)
i2c.i2cw(0x5b, 0x1e, 0x00)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x20, 0x00)
i2c.i2cw(0x5b, 0x21, 0x00)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x80)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0xa5)
i2c.i2cw(0x5b, 0x26, 0xa2)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x28, 0x00)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x7c)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x36)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x2e)
i2c.i2cw(0x5b, 0x31, 0x00)
i2c.i2cw(0x5b, 0x32, 0xf7)
i2c.i2cw(0x5b, 0x33, 0x12)
i2c.i2cw(0x5b, 0x34, 0xda)
i2c.i2cw(0x5b, 0x35, 0x4b)
i2c.i2cw(0x5b, 0x36, 0x00)
i2c.i2cw(0x5b, 0x37, 0x00)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0xc8)
i2c.i2cw(0x5b, 0x3f, 0x00)
i2c.i2cw(0x5b, 0x40, 0x00)
i2c.i2cw(0x5b, 0x41, 0x00)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x43, 0x00)
i2c.i2cw(0x5b, 0x44, 0x00)
i2c.i2cw(0x5b, 0x45, 0x00)
i2c.i2cw(0x5b, 0x46, 0x00)
i2c.i2cw(0x5b, 0x47, 0x00)
i2c.i2cw(0x5b, 0x48, 0x00)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xe7)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x58, 0x00)
i2c.i2cw(0x5b, 0x72, 0x00)
i2c.i2cw(0x5b, 0x7f, 0x40)
i2c.i2cw(0x5b, 0xc0, 0x00)
i2c.i2cw(0x5b, 0xc1, 0x00)

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
