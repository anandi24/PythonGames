#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def removeDuplicates(urls):
  result = []
  for url in urls:
    if url not in result:
      result.append(url)
  return result

def sortLastWord(word):
   try:
     filelist = word[word.rindex('-')+1:]
   except ValueError:
     filelist = word
   return filelist

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  file = open(filename, 'r')
  print(filename)
  fileContent = file.read()
  imgList = []

  match = re.search(r'GET\s(/.+/.+\.jpg)', fileContent)
  urlName = match.group(0)
  imgfilename = urlName[urlName.rindex('/')+1:]
  print(imgfilename)
  if(imgfilename.count('-')>1):
    match_second = True
  else:
    match_second = False
  matches = re.findall(r'GET\s(/.+\.jpg)', fileContent)
  unique_imgs = removeDuplicates(matches)
  print unique_imgs
  if match_second:
    print 3
    unique_imgs = sorted(unique_imgs, key=sortLastWord)
  else:
    print 4
    unique_imgs = sorted(unique_imgs)

  for i in unique_imgs:
    print i
  host = re.search(r'\w+_(.+)', filename)
  for uniqueImg in unique_imgs:
    urlName = 'http://'+host.group(1)+uniqueImg
    imgList.append(urlName)
  return imgList
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  index_content_start = "<verbatim><html><body>"
  index_content_end = "</body></html>"
  index_img_content = ''
  if not (os.path.exists(dest_dir)):
    os.mkdir(dest_dir)
  else:
    print 'dir exists already'
  i = 0
  for url in img_urls:
    print url
    filename = 'img' + str(i)
    index_img_content = index_img_content + "<img src=\""+filename+"\">"
    print("Retrieveing " + filename +" in " + dest_dir)
    try:
      urllib.urlretrieve(url, dest_dir+'\\'+filename)
      i+=1
    except IOError:
      print 'problem reading url:', url

  f = open(dest_dir+'\index.html', 'w')
  f.write(index_content_start+index_img_content+index_content_end)
  f.close()

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
