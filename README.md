# kernel-adaptation-halium-degas

Sailfish OS kernel package for the Xiaomi 14T (`degas`, MediaTek
Dimensity 8300-Ultra `mt6897`).

- `linux/`: [android_kernel_xiaomi_degas](https://github.com/nyxianglyph/android_kernel_xiaomi_degas),
  branch `halium-6.1.157` (Android Common Kernel 6.1.157 + UBports Halium
  patches), configured as `gki_defconfig halium.config sfos-degas.config`.
  It keeps the stock module ABI, so the stock `vendor_boot` and `vendor_dlkm`
  modules are used unchanged.
- `kernel-adaptation-simplified/`: packaging scripts, with support for a
  boot.img cmdline without a vendor_boot build and for AVB footer props.
- `ramdisk-overlay/`: appended to the Halium boot ramdisk (`init_boot`).

The package builds `boot.img` (kernel and cmdline) and `init_boot.img`
(Halium ramdisk). `vendor_boot` is not built: the one on the device (stock or
TWRP) stays. Both images carry the stock AVB footer props
(`com.android.build.*.os_version`, `security_patch`, `fingerprint`); without
them MiTEE KeyMint rejects the metadata key on this phone.

Derived from [kernel-adaptation-halium-ansuz](https://github.com/HelloVolla/kernel-adaptation-halium-ansuz)
(Volla Phone Plinius).
