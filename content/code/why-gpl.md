Title: Why I use GPL license
Date: 2017-11-18
Tags: floss, legal
Slug: why-gpl
Summary: Why I use GNU's General Public License and why I think it's a superior free or even open software license and anyone should consider it for your project.

This issue has been discussed to death and I still find people blindly advocating MIT or even WTFPL licenses.
I'm far from a lawyer but I feel that there are few very generic and simple details about software licensing people
who lead open software projects should understand.

## Protect Yourself

First thing first - the license should protect the project contributors and creators. In legal terms it's called no-warranty-provided and exlucsion of it can be dangerous.  
Technology law sucks -
it's outdated, overly complicated and widely regional where software itself has no borders.

To illustrate tis danger imagine John made a library and used a license that does not fully protect the creators
from warranty responsibilities(like WTFPL). Now some company decides to use John's work in their software stack and
unfortunately John left a bug in his library that either exposed the company to theft or caused their technology to break. In this case the company could easily start lawsuit against John and argue that it was John's open source library that cause them to go under and John would be liable.

Most linceses however have this included, GPL for example:

>For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

While some occasional ones like WTFPL don't.

To summarise, whatever license you use make sure to protect yourself - make sure you provide no warranty!

## Philosophy and Copyleft

It's important to consider license philosophy as well.

> Copyleft is a general method for making a program (or other work) free
(in the sense of freedom, not “zero price”), and requiring all modified
and extended versions of the program to be free as well.

For example GPL is a copyleft license. It's a "viral" license, 
which means any forks or modifications (that are published) have to also
carry the same license. This protects the projects ecosystem and enables 
a bunch of benefits for everyone involved.

### Benefits
On the other hand it's also worth considering the __benefits__ of viral copyleft nature of GPL type licenses:

- Patches - since the license is viral any changes or forks will be public and those changes can be applied
to the original project very easily. This huge reason why Linux kernel itself is licensed under GPL.
- Freedom - it continues the message of free software. As project lead you have the
power to propagate the message as any derivatives will have to carry your choice.


### Restrictions

> it's too restrictive and puts too many gates in education!  

This quote comes up a lot when people argue against GPL, however this argument is false as __GPL's restriction only applies to published software__  
([as per FAQ](https://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic)).
So in other words you can modify and learn from software all you want and use it (even for profit)
as long as you don't publish it and try to turn it into a product of your own.

Is it too restrictive for business? Maybe, but why would you be concerned about business?
The ecosystem should not expect anything from a business, it puts an unnecessary
centralization to an unreliable source. At the end of the day a business is out there with
one goal in mind - to make money - it's not a bad goal, but putting any expectations
for a business to go out of their way and support the ecosystem is wildly unreasonable.

## Closing Statement

I'll continue using GPL license for all of my project where possible. It aligns with my ideology of software and
I believe I can develop and maintain software where I don't need to rely on adoption.

Additional read:

[Copyleft: Pragmactic Idealism](https://www.gnu.org/philosophy/pragmatic.html)  
[GPL's FAQ](https://www.gnu.org/licenses/gpl-faq.html)  
[It's possible to sell GPL exception](https://www.fsf.org/blogs/rms/selling-exceptions)   
