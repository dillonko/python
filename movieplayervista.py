#qpy:http://qpython.com/s/movieplayervista.py
"""
This is an example file which tell you how to use QPython to develop android app.
If get a video link address from a remote webpage and play it with the Movie Player Vista to play. ( It needs the network )

@Author: River
@Date: 2012-10-22
"""

from jnius import cast
from jnius import autoclass
from jnius import JavaException
from android import AndroidBrowser
from urllib2 import urlopen

print "[Movie Player Vista with qpython example]"

# get and parse video link
response = urlopen('http://qpy.zuowuxuxi.com/samples/script_data.txt')
if response:
    content = response.read()
    import json
    data = json.loads(content)
    link = data['link']

    # get android object
    PythonActivity = autoclass('org.renpy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    Toast = autoclass('android.widget.Toast')


    # play the url
    intent = Intent()
    intent.setAction(Intent.ACTION_VIEW)
    intent.setClassName('com.hipipal.mn', 'com.hipipal.m.PLAPlayerAct')
    intent.setDataAndType(Uri.parse(link), 'video/*')
    currentActivity = cast('android.app.Activity', PythonActivity.mActivity)

    try:
        s = "Play Video from %s..." % link
        print s

        currentActivity.startActivity(intent)
    except JavaException:
        s = "Need install Movie Player Vista App first"
        print s

        browser = AndroidBrowser()
        browser.open("http://zuowuxuxi.com/movie-player-for-youtube.html")

    print "[Movie Player Vista with qpython END]"

else:

    print "Maybe network error, could not get the parameters for play"
