Title: How to disable thinkpad trackpoint acceleration
Date: 2017-11-17
Tags: linux, guide
Slug: disable-thinkpad-acceleration
Summary: A short note on how to properly disable thinkpoint trackpad acceleration

_I've got a new thinkpad laptop and I've been struggling with mouse acceleration on trackpoint,
turns out disabling it isn't as straight-forward as you'd expect_

To get rid of this abomination of a feature that is enabled by default we need `xinput`

# The Fix

First you need to find the code or name of your trackpoint:


    $ xinput list
    ⎡ Virtual core pointer                          id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ SynPS/2 Synaptics TouchPad                id=12   [slave  pointer  (2)]
    ⎜   ↳ TPPS/2 IBM TrackPoint                     id=13   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                         id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Video Bus                                 id=7    [slave  keyboard (3)]
        ↳ Sleep Button                              id=8    [slave  keyboard (3)]
        ↳ Integrated Camera: Integrated C           id=10   [slave  keyboard (3)]
        ↳ AT Translated Set 2 keyboard              id=11   [slave  keyboard (3)]
        ↳ ThinkPad Extra Buttons                    id=14   [slave  keyboard (3)]
        ↳ SteelSeries  SteelSeries Arctis 7         id=9    [slave  keyboard (3)]

Our guy is `TPPS/2 IBM Trackpoint` aka id `13`.
Next we can see the properties of this prop:


    $ xinput list-props 13
    Device 'TPPS/2 IBM TrackPoint':
            Device Enabled (140):   1
            Coordinate Transformation Matrix (142): 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000
            libinput Natural Scrolling Enabled (310):       0
            libinput Natural Scrolling Enabled Default (311):       0
            libinput Left Handed Enabled (312):     0
            libinput Left Handed Enabled Default (313):     0
            libinput Accel Speed (314):     0
            libinput Accel Speed Default (315):     0.000000
            libinput Accel Profiles Available (316):        1, 1
            libinput Accel Profile Enabled (317):   1, 0
            libinput Accel Profile Enabled Default (318):   1, 0
            libinput Scroll Methods Available (319):        0, 0, 1
            libinput Scroll Method Enabled (320):   0, 0, 1
            libinput Scroll Method Enabled Default (321):   0, 0, 1
            libinput Button Scrolling Button (322): 2
            libinput Button Scrolling Button Default (323): 2
            libinput Middle Emulation Enabled (324):        0
            libinput Middle Emulation Enabled Default (325):        0
            libinput Send Events Modes Available (260):     1, 0
            libinput Send Events Mode Enabled (261):        0, 0
            libinput Send Events Mode Enabled Default (262):        0, 0
            Device Node (263):      "/dev/input/event18"
            Device Product ID (264):        2, 10
            libinput Drag Lock Buttons (326):       <no items>
            libinput Horizontal Scroll Enabled (327):       1

To disable acceleration we are interested in one of these two settings:

            libinput Accel Speed (314):     0
            libinput Accel Profile Enabled (317):   1, 0

We can either diminish/change the acceleration speed by:

    # to disable we can use negative acceleration
    $ xinput set-prop 13 314 -1
    # or we can disable acceleration profile entirely
    $ xinput set-prop 13 317 0 1

Note, don't use both, -1 with disabled acceleration pretty much disables the devices.

# Make It Persisntant

To make the change persist after restart simply add the config line it to your `~/.xsessionrc` file, e.g.:

    echo "xinput set-prop 13 317 0 1" >> ~/.xsessionrc


