[app]
title = Pronunciation Coach
package.name = proncoach
package.domain = org.proncoach
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = RECORD_AUDIO, INTERNET

android.api = 33
android.min_api = 21
android.sdk = 33
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
