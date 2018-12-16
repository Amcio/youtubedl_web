# youtubedl_web
This is a simple cgi script that allows to download .mp3 and .mp4 files from youtube with a html GUI and serve them to the user.
I made the first version in 3 days with no knowledge on how to use a python script in a website.

## Requirements
To use this you will need:
```
 - A web-server with cgi capability (apache2)
 - Python 3
 - youtube-dl
```
## Install

First install youtube-dl module
```
pip install youtube-dl
```
Download the script and put it into the cgi-bin folder
```
Default (linux): /usr/lib/cgi-bin
```
Enabling cgi can differ based on what server you're using. So google is your best friend here.
If you're using apache I recommend you add this to your apache2.conf (default output is `/var/www/html/out`):
```
<Directory /path/to/output/dir>
        AddType application/octet-stream .mp3
        AddType application/octet-stream .mp4
</Directory>
```
This will download the files instead of opening them in the browser. Alternatively you can add the same rules to a .htaccess file.

## Usage
Now that the script is in-place how do we use it?
The script looks for two things in your html form.
First it needs a input with the `name="link"` parameter. This is the link of the video you want to download
Then a whatever with the `name="format"` which specifies whether we are downloading an .mp3 or a .mp4. Values: either `mp3` or `mp4`.
And that's it.

In the current version the Location of the output file is located in the `ytdl_opts` of each function and the last `print` statement. I'll change this in a update soon. If you need any more help open an issue or look into the code (it really helps).

### Credits
youtube-dl developers for [youtube-dl](https://youtube-dl.org)

#### To-do
I want to rewrite the thing using flask and change a few things for easier usage by others.
