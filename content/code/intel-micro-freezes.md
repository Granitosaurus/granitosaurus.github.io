Title: Fixing Intel Micro-freezes
Date: 2020-01-03
Tags: linux, fix, guide
Status: draft
Slug: linux-intel-freeze
Summary: I've been having the most annoying freezes since the latest linux kernel update. It has been a bit difficult to debug but the culprit is intel's video driver.

I've been having the most annoying freezes since the latest linux kernel update. It has been a bit difficult to debug but the culprit is intel's video driver - __i915__.


The 2019 release of i915 driver has some weird bugs that are difficult to reproduce that often when engaged via chrome's webengine causes the system to freeze for few seconds or stutter, or even freeze completely. 

# Debug

I fired up `journalctl` and started digging:

```
Jan 02 04:40:40 nanosaurus kernel: i915 0000:00:02.0: Resetting rcs0 for hang on rcs0, bcs0
Jan 02 04:40:38 nanosaurus audit[1]: SERVICE_STOP pid=1 uid=0 auid=4294967295 ses=4294967295 msg='unit=systemd-coredu>
Jan 02 04:40:38 nanosaurus kernel: audit: type=1131 audit(1577940038.557:72): pid=1 uid=0 auid=4294967295 ses=4294967>
Jan 02 04:40:38 nanosaurus systemd[1]: systemd-coredump@2-25794-0.service: Succeeded.
Jan 02 04:40:38 nanosaurus systemd-coredump[25795]: Process 25210 (chromium) of user 1000 dumped core.
                                                    
                                                    Stack trace of thread 25701:
                                                    #0  0x000055b6f99c8c88 n/a (chromium + 0x5539c88)
                                                    #1  0x000055b6f87bb647 n/a (chromium + 0x432c647)
                                                    #2  0x000055b6f87cc9ac n/a (chromium + 0x433d9ac)
                                                    #3  0x000055b6f87cc754 n/a (chromium + 0x433d754)
                                                    #4  0x000055b6f8785508 n/a (chromium + 0x42f6508)
                                                    #5  0x000055b6f87cd2ff n/a (chromium + 0x433e2ff)
                                                    #6  0x000055b6f87a5b5e n/a (chromium + 0x4316b5e)
                                                    #7  0x000055b6f87e19e2 n/a (chromium + 0x43529e2)
                                                    #8  0x000055b6f881e6da n/a (chromium + 0x438f6da)
                                                    #9  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #10 0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25210:
                                                    #0  0x00007f18634499ef __poll (libc.so.6 + 0xf49ef)
                                                    #1  0x00007f1867093630 n/a (libxcb.so.1 + 0xc630)
                                                    #2  0x00007f1867094fef n/a (libxcb.so.1 + 0xdfef)
                                                    #3  0x00007f1867095162 xcb_wait_for_reply64 (libxcb.so.1 + 0xe162)
                                                    #4  0x00007f18670f7269 _XReply (libX11.so.6 + 0x41269)
                                                    #5  0x00007f18670dd7ca _XGetWindowAttributes (libX11.so.6 + 0x277>
                                                    #6  0x00007f18670dd93b XGetWindowAttributes (libX11.so.6 + 0x2793>
                                                    #7  0x000055b6f91562c4 n/a (chromium + 0x4cc72c4)
                                                    #8  0x000055b6f9154fb7 n/a (chromium + 0x4cc5fb7)
                                                    #9  0x000055b6f9154ea9 n/a (chromium + 0x4cc5ea9)
                                                    #10 0x000055b6f9162518 n/a (chromium + 0x4cd3518)
                                                    #11 0x000055b6f915d746 n/a (chromium + 0x4cce746)
                                                    #12 0x000055b6f915d852 n/a (chromium + 0x4cce852)
                                                    #13 0x000055b6f99c6545 n/a (chromium + 0x5537545)
                                                    #14 0x000055b6fcad495b n/a (chromium + 0x864595b)
                                                    #15 0x000055b6f835ebae n/a (chromium + 0x3ecfbae)
                                                    #16 0x000055b6f8381fbf n/a (chromium + 0x3ef2fbf)
                                                    #17 0x000055b6f835dde1 n/a (chromium + 0x3ecede1)
                                                    #18 0x000055b6f608af4e ChromeMain (chromium + 0x1bfbf4e)
                                                    #19 0x00007f186337c153 __libc_start_main (libc.so.6 + 0x27153)
                                                    #20 0x000055b6f5dfb02e _start (chromium + 0x196c02e)
                                                    
                                                    Stack trace of thread 25702:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25703:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25704:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25705:
                                                    
                                                    Stack trace of thread 25703:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25704:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
                                                    
                                                    Stack trace of thread 25705:
                                                    #0  0x00007f1867205c45 pthread_cond_wait@@GLIBC_2.3.2 (libpthread>
                                                    #1  0x00007f185ba0ed0c n/a (i965_dri.so + 0x4f6d0c)
                                                    #2  0x00007f185ba0e908 n/a (i965_dri.so + 0x4f6908)
                                                    #3  0x00007f18671ff4cf start_thread (libpthread.so.0 + 0x94cf)
                                                    #4  0x00007f18634542d3 __clone (libc.so.6 + 0xff2d3)
```

So chrome crashes the driver and it jumps into a pretty lengthy restart loop for almost 10 seconds:

```
Resetting rcs0 for hang on rcs0, bcs0
```

# The fix

I dug around it seems the only fix for the time being is enabling some kernel parameters for `i915` driver:

```
i915.modeset=1 
i915.enable_fbc=1 
i915.enable_psr=1 
i915.disable_power_well=0 
```

To explain these:

* modeset - prioritizes driver initiation on boot (not really necessary here)
* [enable_fbc] - enables framebuffer compensation
* [enable_psr] - power saving feature for screen refresh
* disable_power_well - disable power wells when possible, this seems to be the culprit. However the info about it really scarce and only points to issues about hangs.


To enable the fixes you need to enable these kernel options either on compile or on boot. If you're running `systemctl-boot` simply extend your boot config under options:
```shell
# my config example
$ sudo vim /boot/loader/entries/arch.conf  
title	arch
linux	/vmlinuz-linux
initrd	/initramfs-linux.img
initrd	/intel-ucode.img
options	<...> i915.modeset=1 i915.enable_fbc=1 i915.enable_psr=1 i915.disable_power_well=0
```

Otherwise refer to [Kernel Parameters] article by arch wiki.

[enable_fbc]: https://wiki.archlinux.org/index.php/Intel_graphics#Framebuffer_compression_(enable_fbc)  
[enable_psr]: https://wiki.archlinux.org/index.php/Intel_graphics#Screen_flickering

[Kernel Parameters]: https://wiki.archlinux.org/index.php/Kernel_parameters
