Title: Fuck reCaptcha and everyone who uses it blindly
Date: 2017-10-28
Tags: security, captcha, web-crawling, api
Slug: fuck-recaptcha
Summary: and fuck you bandcamp


reCaptcha is a joke, it doesn't work and it only fucks with your userbase - stop using this cancer.

Recently I bought a collection of 160 albums on Bandcamp. Turns out I need to download all of them individually,
so I thought I'll write up short script to pull it via api or something. Well api is not a thing on bandcamp,
which is hardly a surprise really for today's standards.

Being a web crawler junkie that I am I thought I can put up a simple web-crawler to get my music that is being kept
hostage by technological illiteracy.
I open up web inspector and everything seems to be pretty easy. There's an api under the hood that uses log in
cookies to serve your data with album download links - easy!

Well login page is under reCaptcha protection, from what?
Brute force password cracking? That's not how the shit works. Web Crawling? That's not how any of this works.
You think by putting reCaptcha (which is an abomination on it's own right) will protect your users or you from real bots?
People who do web-crawling in scale you want to protect from have all the necessary tools to get around the captcha,
I know, because I've been working in this field for half-a-decade now - captcha doesn't do shit.

What suffers from this blanket policies is __your userbase__. I could put up simple cli app and github so people
and pull their songs easily. Everyone would be happy with extra features that you don't need to implement
but your userbase can take care of. Everyone wins right?

Will I be able to save my songs from retardedCaptcha captors? Yes, I'll just use the resources from my work.
Can I publish it as an app on github? Kinda, but it will suck. I'd need to prompt the user to solve the captcha
or input cookies from browser - all of which makes the whole ordeal inconvenient and hell to maintain and implement.
Something that would be an evening project ends up being a week-long one.
How does one motivate itself to produce free code and build a community around your project at this point?

Captcha is DRM and just like any sort of DRM it hurts the userbase more than anything else.

I'll make the fucking app, I'll jump through hoops, I'll find something because
__Fuck DRM, fuck Google and fuck Bandcamp.__
