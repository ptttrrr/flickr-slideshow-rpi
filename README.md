# flickr-slideshow-rpi
Simple Flickr slideshow for Raspbian using Python- and shell scripts together with crontab and Frame Buffer Image Viewer (FBI).

## Prerequisites
 - Raspbian
 - FBI (which is the actual slideshow functionality)
 - A [Flickr account and API key](https://www.flickr.com/services/api/keys/apply/)
 - An internet connection for the RPI


## Setup
 - Install FBI

```
sudo apt-get update
sudo apt-get -y install fbi
```

 - Use Crontab to run the Flickr download script in an interval to your liking

 - Open Crontab

```
crontab -e
```
 - Add cronjob
```
*/30/ * * * * /usr/bin/python3 /home/pi/slideshow/download_flickr.py
```

 - Add a cronjob to start slideshow at reboot

```
@reboot sudo /home/pi/slideshow/slideshow.sh &
```
 - Customize your paths to work with your own setup if it's different.


## Misc
 
You might need to install several modules via Pip for this to work (like Pytz for example).



