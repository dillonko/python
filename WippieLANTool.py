#!/usr/bin/python
##############################################################################
# This is a very quick and dirty Wippies LAN utility
##############################################################################
# This script will get the lan and wan ip from Wippies network
##############################################################################
#    WippieLANTool is a small quick and dirty script which will provide some 
#    Wippies network utilities
#
#    Copyright (C) 2008  Juhapekka Piiroinen
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#############################################################################
# Contact: juhapekka.piiroinen@gmail.com
# Version: 0.1
#############################################################################

print "WippieLanTool v0.1\nGNU/GPL - http://code.google.com/p/quickanddirty\n(c) 2008 Juhapekka Piiroinen\n"
print "Ohjelma tarvitsee seuraavat kirjastot:"
print "pyWin32: http://sourceforge.net/project/platformdownload.php?group_id=78018"
print "wxpython: http://www.wxpython.org/download.php#binaries"
print
print "Odota hetkinen.."
import wx,sys
import socket
import win32clipboard, win32con, random
dns = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
server = "http://192.168.0.1"

import cookielib,urllib2
c = cookielib.CookieJar()
o = urllib2.build_opener(urllib2.HTTPCookieProcessor(c))
s= o.open(server)
p = s.read()
s.close()

import re
dat = ""
for line in p:
 line = line.strip()
 dat += line
d = re.compile("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+")
addr = d.findall(dat)

text = "WAN: " + addr[0] + "\n"
text += "LAN: " + ip + "\n\n"


win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(text)

print "Tiedot kopioitu leikepoydalle:"
print win32clipboard.GetClipboardData(win32con.CF_TEXT) 
text += "Tiedot on kopioitu leikepoydalle."
win32clipboard.CloseClipboard()

app = wx.PySimpleApp(0)
wx.InitAllImageHandlers()
dlg = wx.MessageDialog ( None, text, 'WippieLanTool v0.1 - Kotiverkon tiedot',style=wx.OK)
dlg.ShowModal()
print "Valmis suljetaan ohjelmaa.."
sys.exit(1)
