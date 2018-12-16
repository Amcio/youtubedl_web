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
        print("Status: 302 Found")

#    if d['status'] == 'downloading':
#        print("Content-type: text/html\n")
#        print("<h1 style: text-align: center; font-family: monospace;>Downloading...</h1>")


# Set optionS
ytdl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/var/www/html/out/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': Logger(),
    'progress_hooks': [progress],
}


def download(link):
    with youtube_dl.YoutubeDL(ytdl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title', None)
        filename = ydl.prepare_filename(info_dict)[13:-5]
        ydl.download([link])
#        print("Status: 303 See other")
        print("Location: http://107.175.36.50{}.mp3\n".format(filename))


form = cgi.FieldStorage()
link = form.getvalue('link')
download(link)
