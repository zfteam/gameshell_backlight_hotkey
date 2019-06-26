# gameshell_backlight_hotkey

Control backlight brightness and sound volume everywhere!
hotkey:

select+left sound volume down

select+right sound volume up

select+up sound light up

select+down sound light down



How install:

1.command line:

sudo pip install evdev

git clone https://github.com/zfteam/gameshell_backlight_hotkey.git

cd gameshell_backlight_hotkey

cp backlight_hotkey.py ~/launcher/sys.py/

cp -r tools ~/launcher/sys.py/


2.add reboot command shell

"sudo nano /etc/rc.local" open rc.local file and input this to the last line

nohup python /home/cpi/launcher/sys.py/backlight_hotkey.py &


3.reboot system
