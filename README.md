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

```
 - Add cronjob
```
*/30/ * * * * /usr/bin/python3 /home/pi/slideshow/download_flickr.py
```

 - Add a cronjob to start slideshow at reboot

```
@reboot/home/pi/slideshow/slideshow.sh
```
 - Customize your paths to work with your own setup if it's different.


## Misc
 
This is in it's simplest form and far from perfect. The script will only overwrite existing files and if images in the Flickr stream gets deleted, it could mean that local files will be picked up by FBI.
Also, the flickr download script will break at the moment if there is no internet connection.



