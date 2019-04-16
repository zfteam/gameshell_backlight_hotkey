# gameshell_backlight_hotkey

Control backlight brightness everywhere!

How install:

1.command line:

sudo pip install evdev

sudo pip install select

cd gameshell_backlight_hotkey

cp backlight_hotkey.py ~/launcher/sys.py/

cp -r tools ~/launcher/sys.py/


2.add reboot command shell

"sudo nano /etc/rc.local" open rc.local file and input this to the last line

nohup python /home/cpi/launcher/sys.py/backlight_hotkey.py &
