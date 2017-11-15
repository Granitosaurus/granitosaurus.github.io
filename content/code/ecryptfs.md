Title: Securing Data With eCryptfs
Date: 2017-10-22
Tags: linux, guide, crypto, security
Slug: ecrypt-yourself 
Summary: protect your sensitive data like crypto wallets with eCrypt overlay filesystem!

Since I started dabbling in Cryptocurrency I've been feeling a bit paranoid about protecting my wallet information and keys. Fortunately there are already tools that are dead easy to use.   
The standard tool for linux is called eCryptfs and let me tell you how awesome and convenient it is!


# eCryptfs

eCryptfs is a cryptographic overlay filesystem for Linux. It's a great tool to encrypt some private data like cryptocurrency wallet keys, private pictures — anything really.  
It allows you to mount a password protected, encrypted filesystem on your usual unencrypted filesystem:

    dex@~/.private $ ls
    Access-Your-Private-Data.desktop  README.txt
    $ ecryptfs-mount-private 
        Enter your login passphrase:
        Inserted auth tok with sig [xxxxxx] into the user session keyring
        INFO: Your private directory has been mounted.
        INFO: To see this change in your current shell:
          cd /home/dex/.private
    dex@~/.private $ cd .
    dex@~/.private $ ls 
    myetherwallet  btc

Pretty damn cool - simple and secure!  

## Setup

eCryptfs setup is dead easy!  
Since linux version 3.18 eCrypt overlay filesystem is included with core kernel. 
Simply enable it with:

    modprobe ecryptfs

Then we need some tools to easily mount, unmount and generate our filesystem: `ecryptfs-utils` has everything we would need and is available on every linux package manager:  

    sudo apt install ecryptfs-utils  # Ubuntu
    sudo pacman -S ecryptfs-utils  # Arch
    etc. etc.

Once you have it installed you'll find your user-space path populated with a bunch of ecryptfs utils, just type in your terminal `ecryptfs-` and press tab to see the goodies:

    [dex@nanosaurus ~]$ ecryptfs-<tab>
    ecryptfs-add-passphrase
    ecryptfs-find
    ecryptfs-insert-wrapped-passphrase-into-keyring
    ecryptfs-manager
    ...

Finally to initiate an ecryptfs system we need to run:

    $ ecryptfs-setup-private --nopwcheck --noautomount 

We use `--nopwcheck` and `--noautomount` flags here for extra security.   

* `nopwcheck` allows us to use different password from our user's password   
* `noautomount` disables automatic encrypted system mounting, since it's also not a very great idea and wouldn't work if our encryption password is different from our user's one.

This command will ask you for `login` and `mount` passwords. For login password use your own password and for mount password leave it empty as ecryptfs will create it for you using your login password as a seed.

Afterwards the system will be initiated and  `~/Private` and `~/.ecryptfs` directories will be created.  

_Note: you want to backup your encrypted mount password which is located in `~/.ecryptfs/wrapped-passphrase`. Remember that mount password is generated from your login password, so the passphrase is completely useless without your login password - put a copy of this file somewhere where you will never lose it!_

## Usage

`~/Private` is your ecryptfs encrypted directory from now on. To use it you must mount it with `ecryptfs-mount-private` command and once you're done using it use `ecryptfs-umount-private` command to make it inaccessible once again:  

    dex@~/Private $ ls
    Access-Your-Private-Data.desktop  README.txt
    $ ecryptfs-mount-private 
    dex@~/Private $ cd .
    dex@~/Private $ ls 
    myetherwallet  btc diary emberassing_hobbies

That's it! Now you have a safe directory on your computer where you can store sensitive data! Even if someone gets access to your user's homespace they'll still need your ecryptfs password to get anything out of it.  

## Customizing

`~/Private` is a pretty terrible name. It's Camelcase and I'd very much prefer it to be hidden.  
We can change it to `~/.private` very easily though:

    mv ~/Private ~/.private
    echo /home/dex/.private > ~/.ecryptfs/Private.mnt

# General Security tips

## The Three Rule

_If it doesn't exist in __three__ places it doesn't exist at all._

Fortunately ecryptfs directory acts like a normal directory so you can easily back it up to usb-stick, cloud storage or even email. Really just put that shit everywhere as longs as you have your login and mount passwords safe no one will be able to access your stuff.

We've all heard magical stories about people losing usb sticks with their bitcoin wallets. Well if you had your wallet encrypted and in three different places that would have never happened!

## Long Passwords Triumph 

I don't think I can top the explanation by this [xkcd comic](https://xkcd.com/936/) so I'll just leave you with it and say that just have a simple a-z password which is at least 13 characters long.  


# Further Reading

If you want to dig deeper I suggest arch-wiki [article](https://wiki.archlinux.org/index.php/ECryptfs) or symply `man ecryptfs`!
Additionally [top questions on stackoverflow](https://stackoverflow.com/questions/tagged/ecryptfs?sort=votes&pageSize=15) also offer some interesting read.
