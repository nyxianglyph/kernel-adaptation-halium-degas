# Device details
%define device halium-degas

# Kernel target architecture
%define kernel_arch arm64

%define kcflags "KCFLAGS="

#Compiler to use
%define makeopts LLVM=1 LLVM_IAS=1
%define clangtriple aarch64-linux-gnu-
%define crosscompile aarch64-linux-gnu-
%define crosscompile32 arm-linux-androideabi-
%define hostldflags "-fuse-ld=lld --rtlib=compiler-rt"

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu aarch64

# Defconfig to pick-up. sfos-degas.config is part of the kernel tree
# (android_kernel_xiaomi_degas, halium-6.1.157). The result keeps the
# stock module ABI: all 2709 kernel symbols used by the 456 stock
# vendor_boot/vendor_dlkm modules keep their CRCs.
%define defconfig gki_defconfig halium.config
%define kernel_config %{defconfig} sfos-degas.config

# Linux kernel source directory
%define source_directory linux

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# vendor_boot stays as it is on the device (stock or TWRP): it carries the
# stock vendor ramdisk, the 215 first stage modules and the dtb. The Halium
# ramdisk goes into init_boot, the kernel into boot.

#Device Info
# v4 boot: the cmdline goes into boot.img, the bootloader appends the
# vendor_boot cmdline (bootopt=...) to it
%define deviceinfo_kernel_cmdline systempart=/dev/mapper/system
%define deviceinfo_ramdisk_compression lz4
%define deviceinfo_flash_pagesize 4096
%define deviceinfo_flash_offset_base 0x0
%define deviceinfo_flash_offset_kernel 0x40000000
%define deviceinfo_flash_offset_ramdisk 0x66f00000
%define deviceinfo_flash_offset_tags 0x47c80000
%define deviceinfo_flash_offset_dtb 0x47c80000
%define deviceinfo_bootimg_qcdt false
%define deviceinfo_bootimg_header_version 4
%define deviceinfo_bootimg_has_init_boot_partition true
%define deviceinfo_bootimg_partition_size 67108864
%define deviceinfo_init_boot_partition_size 8388608
%define deviceinfo_bootimg_os_version 14
%define deviceinfo_bootimg_os_patch_level 2026-08
# The bootloader hands these AVB footer props to MiTEE. Without them
# KeyMint rejects the metadata key (-33 INVALID_KEY_BLOB) on this phone.
%define deviceinfo_bootimg_avb_props com.android.build.%%PART%%.os_version:14 com.android.build.%%PART%%.security_patch:2026-08-01 com.android.build.%%PART%%.fingerprint:Xiaomi/hal_mgvi_64_armv82_mt6897_global/mgvi_64_armv82:14/UP1A.231005.007/OS3.0.305.0.WNEIDXM:user/release-keys
%define deviceinfo_rootfs_image_sector_size 4096
%define deviceinfo_halium_version 14
%define deviceinfo_kernel_disable_modules false

Version:        6.1.157
Release:        1

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
