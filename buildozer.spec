[app]

title = Love App
package.name = loveapp
package.domain = org.bluemen2007

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0


# Android

android.api = 35
android.minapi = 24
android.ndk_api = 24

android.accept_sdk_license = True

android.archs = arm64-v8a

android.permissions = INTERNET


[buildozer]

log_level = 2
warn_on_root = 1
[android]
android.api = 35
android.minapi = 24
android.ndk = 27c
android.accept_sdk_license = True
