dupehunter
==========

Searches facebook for profiles that might be trying to impersonate you

Requirements
============

To properly work, dupehunter needs:

- python 2.x (https://www.python.org/)
- pHash (Open Source perceptual hash library, http://phash.org/download/)
- py-pHash (Python bindings for libpHash, https://github.com/polachok/py-phash)
- Facebook python SDK (https://github.com/pythonforfacebook/facebook-sdk)
- A facebook access token with the "user_photos" permission (can be grabbed from https://developers.facebook.com/tools/explorer/)

Instructions
============

- Replace FACEBOOK_OAUTH_TOKEN with an actual token within the script
- Run the script
- Profit!

What does it do?
================

The most common way you get impersonated is by someone using a profile with your name and profile picture. However, it's very
likely there's a lot of people with your same name in Facebook, so comparing that is not an option. This script will compare
all profiles matching your name and will look for a profile picture matching ANY of the pictures you ever used as profile
picture. You will be alerted if anyone's picture closely resemble any of yours.

Donations
=========

BTC: 15USUofa6QZ6KpYRNSwiUBxGXKRqakpCYX