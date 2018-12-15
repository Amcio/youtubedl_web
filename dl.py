#!/usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import cgi
import cgitb

cgitb.enable()


class Logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def progress(d):
    if d['status'] == 'finished':
        print("Status: 302 Found") # This is bad. (Prepare for redirect).

#    if d['status'] == 'downloading':
#        print("Content-type: text/html\n")
#        print("<h1 style: text-align: center; font-family: monospace;>Downloading...</h1>")


def mp4(link):
    # Set options
    # This method does not always download the highest quality.
    # Information in mp3 function.
    ytdl_opts = {
        'format': 'best',
        'outtmpl': '/var/www/html/out/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'logger': Logger(),
        'progress_hooks': [progress],
    }
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        filename = ydl.prepare_filename(info_dict)
        path = filename[13:]
        ydl.download([link])
        print("Location: http://107.175.36.50{}\n".format(path))


def mp3(link):
    # Set options
    ytdl_opts = {
        'format': 'bestaudio/mp3/best',
        'outtmpl': '/var/www/html/out/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'logger': Logger(),
        'progress_hooks': [progress],
    }

    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)  # Get info from ydl
        video_title = info_dict.get('title', None)  # Get title
        filename = ydl.prepare_filename(info_dict).replace('.webm', '.mp3')  # The filename is before conversion.
        path = filename[13:]  # remove /var/www/html from the path
        ydl.download([link]) # Download
        print("Location: http://107.175.36.50{}\n".format(path)) # Redirect to download. This solution is bad.

# Get data from website.
form = cgi.FieldStorage()
link = form.getvalue('link')
ext = form.getvalue('format')

if ext == "mp4":
    mp4(link)
else:
    mp3(link)

