# Generated by Auraauro
# Generated on 20210215 at 21:25:48
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
i2c.i2cw(0x5b, 0x2c, 0xa1)
i2c.i2cw(0x5b, 0x2d, 0xbf)
i2c.i2cw(0x5b, 0x32, 0x1f)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x76)
i2c.i2cw(0x5b, 0x40, 0x7e)
i2c.i2cw(0x5b, 0x50, 0x08)
i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)

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
i2c.i2cw(0x5b, 0x10, 0x03)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0xff)
i2c.i2cw(0x5b, 0x18, 0xff)
i2c.i2cw(0x5b, 0x19, 0xff)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x21)
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
i2c.i2cw(0x5b, 0x10, 0x43)
i2c.i2cw(0x5b, 0x11, 0x05)
i2c.i2cw(0x5b, 0x12, 0x04)
i2c.i2cw(0x5b, 0x14, 0x78)
i2c.i2cw(0x5b, 0x17, 0xc3)
i2c.i2cw(0x5b, 0x1a, 0x28)
i2c.i2cw(0x5b, 0x1b, 0x06)
i2c.i2cw(0x5b, 0x1d, 0x10)
i2c.i2cw(0x5b, 0x1f, 0x0b)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x8b, 0x10)
i2c.i2cw(0x5b, 0x8f, 0x02)



i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x19)
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
# Escape to PRG_CMD
i2c.i2cw(0x5b, 0x0f, 0x01)
time.sleep(5e-06)


i2c.i2cw(0x5b, 0xff, 0x04)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x34, 0x19)
i2c.i2cw(0x5b, 0x35, 0x60)
i2c.i2cw(0x5b, 0x39, 0x02)
i2c.i2cw(0x5b, 0x3a, 0x17)
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
i2c.i2cw(0x5b, 0x10, 0x72)
i2c.i2cw(0x5b, 0x11, 0x4f)
i2c.i2cw(0x5b, 0x12, 0xf2)
i2c.i2cw(0x5b, 0x13, 0x72)
i2c.i2cw(0x5b, 0x14, 0x4f)
i2c.i2cw(0x5b, 0x15, 0x8e)
i2c.i2cw(0x5b, 0x16, 0xff)
i2c.i2cw(0x5b, 0x17, 0x02)
i2c.i2cw(0x5b, 0x18, 0x4d)
i2c.i2cw(0x5b, 0x19, 0x56)
i2c.i2cw(0x5b, 0x1f, 0xa0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x24, 0x03)
i2c.i2cw(0x5b, 0x25, 0xe1)
i2c.i2cw(0x5b, 0x26, 0xa1)
i2c.i2cw(0x5b, 0x27, 0x08)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2e, 0x2c)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x3f)
i2c.i2cw(0x5b, 0x35, 0x80)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x2c)
i2c.i2cw(0x5b, 0x3f, 0x01)
i2c.i2cw(0x5b, 0x42, 0x08)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0xc0)
i2c.i2cw(0x5b, 0x4e, 0x20)
i2c.i2cw(0x5b, 0x4f, 0xe7)
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
