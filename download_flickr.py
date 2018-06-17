#!/usr/bin/env python
from flickrapi import FlickrAPI
import urllib.request
import os, shutil, re
import signal
import config
from random import randint
import time
import subprocess
from subprocess import check_output

# Settings and variables
flickr_key = config.SLIDE_CONFIG['flickr_key']
flickr_secret = config.SLIDE_CONFIG['flickr_secret']
user_id = config.SLIDE_CONFIG['user_id']
max_images = config.SLIDE_CONFIG['max_images']
folder = "slideshow/flickr"

# FlickrAPI instance
flickr = FlickrAPI(flickr_key, flickr_secret)
size_url = 'url_o'
max_nb_img = max_images

def main():
    download_images()

def delete_unwanted_images(stream_count):
    
    # Get number of images on disk to delete images not in flickr stream
    print('Counting existing images in folder')
    path, dirs, files = next(os.walk('slideshow/flickr'))
    image_count = len(files)
    print('Number of images on disk: ', image_count)
    
    if (stream_count <= image_count):
        print('Deleting extra images in folder')
        folder_path = '/home/pi/slideshow/flickr'
        while (stream_count <= image_count):
            try:
                for image in os.listdir(folder_path):
                    pattern = str(stream_count) + ".jpg"
                    os.remove(os.path.join(folder_path, pattern))
                    print('Deleted image; ', pattern)
                    stream_count += 1
                print('Done deleting leftover images!')
            except Exception as e:
                print(e)

def download_images():
    count = 0

    # Creating folder for images if not already existing
    results_folder = folder.replace(" ", "_") + "/"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    try:
        print('Fetching photo information from Flickr')
        photos = flickr.walk(user_id=user_id,
                        extras=size_url)

        urls = []
        # Iterating through photo data, using url data to download
        for photo in photos:
            t = randint(1, 3)
            time.sleep(t)
            count += 1
            if max_nb_img != -1:
                if count > max_nb_img:
                    print('Reached maximum number of images to download')
                    break
            try:
                url=photo.get(size_url)
                urls.append(url)
                
                urllib.request.urlretrieve(url,  results_folder + str(count) +".jpg")
                print('Downloading image #' + str(count) + ' from url ' + url)
            except Exception as e:
                print(e, 'Download failure')
    except:
        print('Could not get images. No internet connection again?')
            
                            
    print("Total images downloaded:", str(count - 1))
    
    # Calling the delete function to get rid of old leftover pix
    delete_unwanted_images(count)

    # Find and kill running FBI slideshow processes
    print("Restarting slideshow in 5 seconds...")


    #Restart slideshow script to add newly downloaded images to FBI slideshow.
    subprocess.call("/home/pi/slideshow/slideshow.sh", shell=True)

# Run 
main()

