# Generated by megan
# Generated on 20210108 at 17:41:26
# Version v2.3.3rc1


# Step1: HARD Reset
# Step2: Wait for CPU to reach Active State
time.sleep(0.02)
# GENERIC : begin
time.sleep(1e-06)
spi.spiw(0xff, 0x00)
spi.spiw(0xbd, 0xc3)
spi.spiw(0x10, 0x01)
spi.spiw(0x11, 0x00)
spi.spiw(0x12, 0x00)
spi.spiw(0x13, 0x00)
spi.spiw(0x14, 0x00)
spi.spiw(0x15, 0x00)
spi.spiw(0x16, 0x00)
spi.spiw(0x17, 0x00)
spi.spiw(0x18, 0x00)
spi.spiw(0x19, 0x00)
spi.spiw(0x1a, 0x1f)
spi.spiw(0x1b, 0x1f)
spi.spiw(0x1c, 0x1f)
spi.spiw(0x1d, 0xff)
spi.spiw(0x1e, 0xff)
spi.spiw(0x1f, 0xff)
spi.spiw(0x20, 0xff)
spi.spiw(0x21, 0xff)
spi.spiw(0x22, 0xdf)
spi.spiw(0x23, 0x03)
spi.spiw(0x24, 0x00)
spi.spiw(0x25, 0x00)
spi.spiw(0x26, 0x00)
spi.spiw(0x27, 0x00)
spi.spiw(0x28, 0x40)
spi.spiw(0x29, 0x00)
spi.spiw(0x2a, 0x60)
spi.spiw(0x2b, 0x00)
spi.spiw(0x2c, 0xa2)
spi.spiw(0x2d, 0x3f)
spi.spiw(0x2e, 0x00)
spi.spiw(0x2f, 0x00)
spi.spiw(0x30, 0x00)
spi.spiw(0x31, 0x00)
spi.spiw(0x32, 0x00)
spi.spiw(0x33, 0x00)
spi.spiw(0x34, 0x6c)
spi.spiw(0x35, 0xff)
spi.spiw(0x3c, 0x80)
spi.spiw(0x3d, 0x00)
spi.spiw(0x3f, 0x76)
spi.spiw(0x40, 0x00)
spi.spiw(0x50, 0x08)
spi.spiw(0x64, 0x00)
spi.spiw(0xbf, 0x00)
spi.spiw(0xff, 0x01)
spi.spiw(0xbd, 0xc3)
spi.spiw(0x10, 0x00)
spi.spiw(0x11, 0x00)
spi.spiw(0x12, 0x00)
spi.spiw(0x13, 0x00)
spi.spiw(0x14, 0x00)
spi.spiw(0x15, 0x00)
spi.spiw(0x16, 0x00)
spi.spiw(0x17, 0x00)
spi.spiw(0x18, 0x00)
spi.spiw(0x19, 0x00)
spi.spiw(0x1a, 0x00)
spi.spiw(0x1b, 0x00)
spi.spiw(0x1c, 0x00)
spi.spiw(0x1d, 0x00)
spi.spiw(0x1e, 0x00)
spi.spiw(0x1f, 0x00)
spi.spiw(0x20, 0x00)
spi.spiw(0x21, 0x00)
spi.spiw(0x22, 0x00)
spi.spiw(0x23, 0x00)
spi.spiw(0x24, 0x00)
spi.spiw(0x25, 0x00)
spi.spiw(0x26, 0x00)
spi.spiw(0x27, 0x00)
spi.spiw(0x28, 0x00)
spi.spiw(0x29, 0x00)
spi.spiw(0x2a, 0x00)
spi.spiw(0x2b, 0x00)
spi.spiw(0x2c, 0x00)
spi.spiw(0x2d, 0x00)
spi.spiw(0x2e, 0x00)
spi.spiw(0x2f, 0x00)
# Update NVM Bank
spi.spiw(0xff, 0x00)
spi.spiw(0x29, 0x00)
spi.spiw(0xc5, 0x01)
spi.spiw(0xc4, 0x01)
time.sleep(0.015)
spi.spiw(0xc5, 0x00)
spi.spiw(0xc4, 0x00)
# Disabling CPU PLL
spi.spiw(0xec, 0x10)
# GENERIC : end


# INPUT_SYS: begin
spi.spiw(0xff, 0x02)
spi.spiw(0xbd, 0xc3)
# Ecsape to PRG_CMD
spi.spiw(0x0f, 0x01)
time.sleep(5e-06)
spi.spiw(0x10, 0x02)
spi.spiw(0x11, 0x00)
spi.spiw(0x12, 0x00)
spi.spiw(0x13, 0x00)
spi.spiw(0x14, 0x00)
spi.spiw(0x15, 0x00)
spi.spiw(0x16, 0xff)
spi.spiw(0x17, 0xff)
spi.spiw(0x18, 0xff)
spi.spiw(0x19, 0xff)
spi.spiw(0x1a, 0x28)
spi.spiw(0x1b, 0x21)
spi.spiw(0x1c, 0x00)
spi.spiw(0x6c, 0x0a)

# Update NVM Bank
spi.spiw(0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
spi.spiw(0x0f, 0x40)
time.sleep(0.005)
# INPUT_SYS : end


# CLOCK_MON : begin
spi.spiw(0xff, 0x06)
spi.spiw(0xbd, 0xc3)
# Ecsape to PRG_CMD
spi.spiw(0x0f, 0x01)
time.sleep(5e-06)
spi.spiw(0x10, 0x43)
spi.spiw(0x11, 0x05)
spi.spiw(0x12, 0x04)
spi.spiw(0x13, 0x00)
spi.spiw(0x14, 0x50)
spi.spiw(0x15, 0x00)
spi.spiw(0x16, 0x00)
spi.spiw(0x17, 0xc3)
spi.spiw(0x18, 0x00)
spi.spiw(0x19, 0x00)
spi.spiw(0x1a, 0x2a)
spi.spiw(0x1b, 0x06)
spi.spiw(0x1c, 0x00)
spi.spiw(0x1d, 0x1f)
spi.spiw(0x1e, 0x00)
spi.spiw(0x1f, 0x15)
spi.spiw(0x70, 0x0c)
spi.spiw(0x71, 0x00)
spi.spiw(0x72, 0x00)
spi.spiw(0x73, 0x00)
spi.spiw(0x7a, 0x00)
spi.spiw(0x7b, 0x00)
spi.spiw(0x7c, 0x00)
spi.spiw(0x7d, 0x00)
spi.spiw(0x7e, 0x00)
spi.spiw(0x7f, 0x00)
spi.spiw(0x80, 0x00)
spi.spiw(0x81, 0x00)
spi.spiw(0x82, 0x00)
spi.spiw(0x83, 0x00)
spi.spiw(0x84, 0x00)
spi.spiw(0x85, 0x00)
spi.spiw(0x86, 0x00)
spi.spiw(0x87, 0x00)
spi.spiw(0x88, 0x00)
spi.spiw(0x89, 0x00)
spi.spiw(0x8a, 0x00)
spi.spiw(0x8b, 0x10)
spi.spiw(0x8c, 0x00)
spi.spiw(0x8d, 0x00)
spi.spiw(0x8e, 0x00)
spi.spiw(0x8f, 0x06)



spi.spiw(0xff, 0x07)
spi.spiw(0xbd, 0xc3)
spi.spiw(0x27, 0x33)
spi.spiw(0x28, 0x07)
spi.spiw(0x29, 0x13)
spi.spiw(0x2a, 0x84)
spi.spiw(0x2b, 0xbd)
spi.spiw(0x2c, 0xa1)
spi.spiw(0x2d, 0x2f)
spi.spiw(0x2e, 0x17)
spi.spiw(0x2f, 0x01)

# Update NVM Bank
spi.spiw(0xff, 0x06)
spi.spiw(0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
spi.spiw(0x0f, 0x40)
# CLOCK_MON : end


# OUTSYS : begin
spi.spiw(0xff, 0x03)
spi.spiw(0xbd, 0xc3)
# Ecsape to PRG_CMD
spi.spiw(0x0f, 0x01)
time.sleep(5e-06)


spi.spiw(0xff, 0x04)
spi.spiw(0xbd, 0xc3)
spi.spiw(0x30, 0x00)
spi.spiw(0x31, 0x00)
spi.spiw(0x32, 0x00)
spi.spiw(0x33, 0x00)
spi.spiw(0x34, 0x19)
spi.spiw(0x35, 0x60)
spi.spiw(0x36, 0x00)
spi.spiw(0x37, 0x00)
spi.spiw(0x38, 0x00)
spi.spiw(0x39, 0x02)
spi.spiw(0x3a, 0x17)
spi.spiw(0x3b, 0x00)
spi.spiw(0x3c, 0x30)
spi.spiw(0x3e, 0xa0)
spi.spiw(0x3f, 0x40)

# Update NVM Bank
spi.spiw(0xff, 0x03)
spi.spiw(0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
spi.spiw(0x0f, 0x40)
# OUTSYS : end


# PLLA : begin
spi.spiw(0xff, 0x0a)
spi.spiw(0xbd, 0xc3)
spi.spiw(0x0d, 0x00)
spi.spiw(0x10, 0xae)
spi.spiw(0x11, 0x4e)
spi.spiw(0x12, 0xd2)
spi.spiw(0x13, 0xae)
spi.spiw(0x14, 0x4e)
spi.spiw(0x15, 0x6e)
spi.spiw(0x16, 0x3f)
spi.spiw(0x17, 0x02)
spi.spiw(0x18, 0x0d)
spi.spiw(0x19, 0x56)
spi.spiw(0x1a, 0x00)
spi.spiw(0x1b, 0x00)
spi.spiw(0x1c, 0x00)
spi.spiw(0x1d, 0x00)
spi.spiw(0x1e, 0x00)
spi.spiw(0x1f, 0xa0)
spi.spiw(0x20, 0x00)
spi.spiw(0x21, 0x00)
spi.spiw(0x22, 0x32)
spi.spiw(0x23, 0x80)
spi.spiw(0x24, 0x03)
spi.spiw(0x25, 0xa5)
spi.spiw(0x26, 0xa2)
spi.spiw(0x27, 0x08)
spi.spiw(0x28, 0x00)
spi.spiw(0x29, 0x1d)
spi.spiw(0x2a, 0x32)
spi.spiw(0x2b, 0x66)
spi.spiw(0x2c, 0x70)
spi.spiw(0x2d, 0x18)
spi.spiw(0x2e, 0x36)
spi.spiw(0x2f, 0x07)
spi.spiw(0x30, 0x2e)
spi.spiw(0x31, 0x00)
spi.spiw(0x32, 0xf7)
spi.spiw(0x33, 0x12)
spi.spiw(0x34, 0xda)
spi.spiw(0x35, 0x4b)
spi.spiw(0x36, 0x00)
spi.spiw(0x37, 0x00)
spi.spiw(0x38, 0xff)
spi.spiw(0x39, 0xff)
spi.spiw(0x3a, 0xff)
spi.spiw(0x3b, 0xff)
spi.spiw(0x3c, 0xf8)
spi.spiw(0x3d, 0x15)
spi.spiw(0x3e, 0xc8)
spi.spiw(0x3f, 0x00)
spi.spiw(0x40, 0x00)
spi.spiw(0x41, 0x00)
spi.spiw(0x42, 0x08)
spi.spiw(0x43, 0x00)
spi.spiw(0x44, 0x00)
spi.spiw(0x45, 0x00)
spi.spiw(0x46, 0x00)
spi.spiw(0x47, 0x00)
spi.spiw(0x48, 0x00)
spi.spiw(0x49, 0xff)
spi.spiw(0x4a, 0xff)
spi.spiw(0x4b, 0xff)
spi.spiw(0x4c, 0xff)
spi.spiw(0x4d, 0xc0)
spi.spiw(0x4e, 0x20)
spi.spiw(0x4f, 0xe7)
spi.spiw(0x57, 0x40)
spi.spiw(0x58, 0x00)
spi.spiw(0x72, 0x00)
spi.spiw(0x7f, 0x40)
spi.spiw(0xc0, 0x00)
spi.spiw(0xc1, 0x00)

# Update NVM Bank
spi.spiw(0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
spi.spiw(0x0f, 0x40)
# PLLA : end


# Disable the Outputs from CPU PLL
spi.spiw(0xff, 0x0d)
spi.spiw(0x27, 0x00)
spi.spiw(0x28, 0x00)
spi.spiw(0x0f, 0x02)
