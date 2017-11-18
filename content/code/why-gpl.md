Title: Why I use GPL license
Date: 2017-11-16
Tags: floss, legal
Slug: why-gpl
Summary: Why I use GNU's General Public License and why I think it's a superior free or even open software license and anyone should consider it for your project.

This issue has been discussed to death and I still find people blindly advocating MIT or even WTFPL licenses.
I'm far from a lawyer but I feel that there are few very generic and simple details about software licensing people
who lead open software projects should understand.

## Protect Yourself

For start the license should protect the project contributors and creators.
This called a warranty provided and it's dangerous. Technology law sucks -
it's outdated, overly complicated and widely regional where software itself has no borders.

Imagine John made a library and used a license that does not fully protect the creators
from warranty responsibilities like WTFPL. Now some company decides to use it in their software stack,
unfortunately John left a bug in his library that either exposed the company to theft or caused
their technology to break. The company could easily start lawsuit against John and argue
that it was John's open source library that cause them issues.

GPL example:

>For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

While WTFPL doesn't even mention warranty.

To summarise, whatever license you use make sure to protect yourself - make sure you provide no warranty!

## Follow the Philosophy and Copyleft

It's important to consider license philosophy as well.

> Copyleft is a general method for making a program (or other work) free
(in the sense of freedom, not “zero price”), and requiring all modified
and extended versions of the program to be free as well.

For example GPL is a copyleft license. It's a "viral" license
which means any forks or modifications (that are published) have to also
carry the same license.

This is a heavily criticised point of GPL - it's _too restrictive_ and puts too many gates in education!
However this is __not true__. The thing about __GPL is that the restriction only applies to published__ software
([as per FAQ](https://www.gnu.org/licenses/gpl-faq.html#GPLRequireSourcePostedPublic)),
so in other words you can modify and learn from software all you want and use it (even for profit)
as long as you don't publish it and try to __turn it into a product of your own__.

Is it too restrictive for business? Maybe, but why would you be concerned about business?
The ecosystem should not expect anything from a business, it put's an unnecessary
centralization to an unreliable source. At the end of the day a business is out there with
one goal in mind - to make money - it's not a bad goal, but putting any expectations
to support the ecosystem is wildly unreasonable.

On the other hand it's also worth considering the __benefits__ of viral copyleft nature of GPL type licenses:

- Patches - since the license is viral any changes or forks will be public and those changes can be applied
to the original project very easily. This huge reason why Linux kernel itself is licensed under GPL.
- Freedom - it continues the message of free software. As project lead you have the
power to propagate the message as any derivatives will have to carry your choice.

## Closing Statement

I'll continue using GPL license for all of my project where possible. It aligns with my ideology of software and
I believe I can develop and maintain software where I don't need to rely on adoption.

Additional read:

[Copyleft: Pragmactic Idealism](https://www.gnu.org/philosophy/pragmatic.html)
[GPL's FAQ](https://www.gnu.org/licenses/gpl-faq.html)
[It's possible to sell GPL exception](https://www.fsf.org/blogs/rms/selling-exceptions)

