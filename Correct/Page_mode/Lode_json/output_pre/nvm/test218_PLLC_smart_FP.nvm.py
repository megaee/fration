# Generated by Sandhiya
# Generated on 20210401 at 11:00:20
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
i2c.i2cw(0x5b, 0x32, 0x1f)
i2c.i2cw(0x5b, 0x34, 0x6c)
i2c.i2cw(0x5b, 0x35, 0xff)
i2c.i2cw(0x5b, 0x3c, 0x80)
i2c.i2cw(0x5b, 0x3f, 0x2b)
i2c.i2cw(0x5b, 0x40, 0x78)
i2c.i2cw(0x5b, 0x50, 0x08)


i2c.i2cw(0x5b, 0xff, 0x01)
i2c.i2cw(0x5b, 0xbd, 0xc3)

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
i2c.i2cw(0x5b, 0x1b, 0x21)
i2c.i2cw(0x5b, 0x20, 0x01)
i2c.i2cw(0x5b, 0x26, 0xff)
i2c.i2cw(0x5b, 0x27, 0xff)
i2c.i2cw(0x5b, 0x28, 0xff)
i2c.i2cw(0x5b, 0x29, 0xff)
i2c.i2cw(0x5b, 0x2a, 0x38)
i2c.i2cw(0x5b, 0x2b, 0x21)
i2c.i2cw(0x5b, 0x30, 0x01)
i2c.i2cw(0x5b, 0x36, 0xff)
i2c.i2cw(0x5b, 0x37, 0xff)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0x38)
i2c.i2cw(0x5b, 0x3b, 0x21)
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
i2c.i2cw(0x5b, 0x14, 0x64)
i2c.i2cw(0x5b, 0x17, 0xc5)
i2c.i2cw(0x5b, 0x1a, 0x30)
i2c.i2cw(0x5b, 0x1b, 0x0a)
i2c.i2cw(0x5b, 0x1c, 0x01)
i2c.i2cw(0x5b, 0x1d, 0x07)
i2c.i2cw(0x5b, 0x1f, 0xd2)
i2c.i2cw(0x5b, 0x20, 0x43)
i2c.i2cw(0x5b, 0x21, 0x05)
i2c.i2cw(0x5b, 0x22, 0x04)
i2c.i2cw(0x5b, 0x24, 0x5b)
i2c.i2cw(0x5b, 0x25, 0x8d)
i2c.i2cw(0x5b, 0x26, 0x80)
i2c.i2cw(0x5b, 0x27, 0xd5)
i2c.i2cw(0x5b, 0x29, 0x60)
i2c.i2cw(0x5b, 0x2a, 0x2d)
i2c.i2cw(0x5b, 0x2b, 0x08)
i2c.i2cw(0x5b, 0x2d, 0x4f)
i2c.i2cw(0x5b, 0x2f, 0x3f)
i2c.i2cw(0x5b, 0x30, 0x43)
i2c.i2cw(0x5b, 0x31, 0x05)
i2c.i2cw(0x5b, 0x32, 0x04)
i2c.i2cw(0x5b, 0x34, 0x5b)
i2c.i2cw(0x5b, 0x35, 0x8d)
i2c.i2cw(0x5b, 0x36, 0x80)
i2c.i2cw(0x5b, 0x37, 0xd5)
i2c.i2cw(0x5b, 0x39, 0x60)
i2c.i2cw(0x5b, 0x3a, 0x2d)
i2c.i2cw(0x5b, 0x3b, 0x08)
i2c.i2cw(0x5b, 0x3d, 0x4f)
i2c.i2cw(0x5b, 0x3f, 0x3f)
i2c.i2cw(0x5b, 0x70, 0x0c)
i2c.i2cw(0x5b, 0x8b, 0x11)
i2c.i2cw(0x5b, 0x8c, 0x10)
i2c.i2cw(0x5b, 0x8f, 0x06)


i2c.i2cw(0x5b, 0xff, 0x07)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x27, 0x33)
i2c.i2cw(0x5b, 0x28, 0x07)
i2c.i2cw(0x5b, 0x29, 0x15)
i2c.i2cw(0x5b, 0x2a, 0xd5)
i2c.i2cw(0x5b, 0x2b, 0x55)
i2c.i2cw(0x5b, 0x2c, 0x55)
i2c.i2cw(0x5b, 0x2d, 0x55)
i2c.i2cw(0x5b, 0x2e, 0x18)
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
i2c.i2cw(0x5b, 0x34, 0x1f)
i2c.i2cw(0x5b, 0x35, 0x60)
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


# PLLE : begin
i2c.i2cw(0x5b, 0xff, 0x0e)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xb7)
i2c.i2cw(0x5b, 0x11, 0xb7)
i2c.i2cw(0x5b, 0x12, 0x96)
i2c.i2cw(0x5b, 0x13, 0xb7)
i2c.i2cw(0x5b, 0x14, 0xb7)
i2c.i2cw(0x5b, 0x15, 0xb3)
i2c.i2cw(0x5b, 0x16, 0x01)
i2c.i2cw(0x5b, 0x17, 0x18)
i2c.i2cw(0x5b, 0x18, 0x08)
i2c.i2cw(0x5b, 0x19, 0x60)
i2c.i2cw(0x5b, 0x1f, 0xb2)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0x3c)
i2c.i2cw(0x5b, 0x25, 0x87)
i2c.i2cw(0x5b, 0x26, 0xe2)
i2c.i2cw(0x5b, 0x29, 0x1d)
i2c.i2cw(0x5b, 0x2a, 0x32)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x32)
i2c.i2cw(0x5b, 0x2d, 0x1c)
i2c.i2cw(0x5b, 0x2e, 0x46)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x55)
i2c.i2cw(0x5b, 0x31, 0x40)
i2c.i2cw(0x5b, 0x32, 0xab)
i2c.i2cw(0x5b, 0x33, 0xaa)
i2c.i2cw(0x5b, 0x34, 0xaa)
i2c.i2cw(0x5b, 0x35, 0x6a)
i2c.i2cw(0x5b, 0x38, 0xfe)
i2c.i2cw(0x5b, 0x39, 0xff)
i2c.i2cw(0x5b, 0x3a, 0xff)
i2c.i2cw(0x5b, 0x3b, 0xff)
i2c.i2cw(0x5b, 0x3c, 0xf8)
i2c.i2cw(0x5b, 0x3d, 0x15)
i2c.i2cw(0x5b, 0x3e, 0x9b)
i2c.i2cw(0x5b, 0x3f, 0x01)
i2c.i2cw(0x5b, 0x42, 0x40)
i2c.i2cw(0x5b, 0x43, 0x33)
i2c.i2cw(0x5b, 0x44, 0x33)
i2c.i2cw(0x5b, 0x45, 0x33)
i2c.i2cw(0x5b, 0x46, 0x33)
i2c.i2cw(0x5b, 0x48, 0x03)
i2c.i2cw(0x5b, 0x49, 0xff)
i2c.i2cw(0x5b, 0x4a, 0xff)
i2c.i2cw(0x5b, 0x4b, 0xff)
i2c.i2cw(0x5b, 0x4c, 0xff)
i2c.i2cw(0x5b, 0x4d, 0x80)
i2c.i2cw(0x5b, 0x4e, 0x1a)
i2c.i2cw(0x5b, 0x4f, 0xdf)
i2c.i2cw(0x5b, 0x57, 0x40)
i2c.i2cw(0x5b, 0x7f, 0x40)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# PLLE : end
time.sleep(9.22262693)


# PLLC : begin
i2c.i2cw(0x5b, 0xff, 0x0c)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x16, 0x31)
i2c.i2cw(0x5b, 0x17, 0x18)
i2c.i2cw(0x5b, 0x18, 0x0f)
i2c.i2cw(0x5b, 0x1f, 0xb0)
i2c.i2cw(0x5b, 0x22, 0x32)
i2c.i2cw(0x5b, 0x23, 0xbc)
i2c.i2cw(0x5b, 0x26, 0x02)
i2c.i2cw(0x5b, 0x28, 0x01)
i2c.i2cw(0x5b, 0x29, 0x10)
i2c.i2cw(0x5b, 0x2b, 0x66)
i2c.i2cw(0x5b, 0x2c, 0x70)
i2c.i2cw(0x5b, 0x2d, 0x18)
i2c.i2cw(0x5b, 0x2f, 0x07)
i2c.i2cw(0x5b, 0x30, 0x32)
i2c.i2cw(0x5b, 0x31, 0x20)
i2c.i2cw(0x5b, 0x32, 0xab)
i2c.i2cw(0x5b, 0x33, 0xaa)
i2c.i2cw(0x5b, 0x34, 0xaa)
i2c.i2cw(0x5b, 0x35, 0x74)
i2c.i2cw(0x5b, 0x38, 0xff)
i2c.i2cw(0x5b, 0x39, 0xff)
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
# PLLC : end
time.sleep(0.00286055)


# INPUT_TDC : begin
i2c.i2cw(0x5b, 0xff, 0x05)
i2c.i2cw(0x5b, 0xbd, 0xc3)
i2c.i2cw(0x5b, 0x10, 0xeb)
i2c.i2cw(0x5b, 0x11, 0x03)
i2c.i2cw(0x5b, 0x13, 0x01)
i2c.i2cw(0x5b, 0x14, 0x42)
i2c.i2cw(0x5b, 0x1e, 0xb0)

# Update NVM Bank
i2c.i2cw(0x5b, 0x0f, 0x10)
time.sleep(1e-05)
# Proceed to Loop Lock
i2c.i2cw(0x5b, 0x0f, 0x40)
# INPUT_TDC : end


# NVM END HERE
