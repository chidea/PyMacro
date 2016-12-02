from time import sleep
from getpass import getpass
import subprocess as sp
import win32api as a, win32process as p, win32gui as g, win32con as c, win32clipboard as clip

class WinFinder():
  def __init__(self,name_start):
    self.__name_start = name_start
    self.handle=None
  def _find(self,h,e):
    if g.GetWindowText(h).startswith(self.__name_start):
      self.handle = h
  def find(self):
    g.EnumWindows(self._find, None)
    return self.handle

def click(pos=None):
  if type(pos) == tuple:
    a.SetCursorPos(pos)
  a.mouse_event(c.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
  a.mouse_event(c.MOUSEEVENTF_LEFTUP,0,0,0,0)

def typing(text):
  for i in range(len(text)):
    a.keybd_event(ord(text[i].upper()),0,0,0)
    sleep(.1)

import win32com.client
shell = win32com.client.Dispatch("WScript.Shell")
SendKeys = shell.SendKeys
#if __name__ == '__main__':
#  pwd = getpass()
#  a.WinExec('c:\\Program Files (x86)\\Maxthon\\Bin\\Maxthon.exe about:config')
#  sleep(2.5)
#  w = WinFinder('Maxthon 설정')
#  g.SetForegroundWindow(w.find())
#  g.ShowWindow(w.find(), c.SW_MAXIMIZE)
#  #a.mouse_event(c.MOUSEEVENTF_MOVE or c.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))
#  #a.mouse_event(c.MOUSEEVENTF_MOVE or c.MOUSEEVENTF_ABSOLUTE,119,326,0,0)
#  click((119,350))
#  sleep(1)
#  click((1966,302))
#  sleep(1)
#  
#  from sys import argv
#  typing(argv[1])
#  #a.keybd_event(ord(argv[1][0].upper()),0,0,0)
#  #sleep(.1)
#  #for i in range(1, len(argv[1])):
#    #a.keybd_event(ord(argv[1][i].upper()),0,0,0)
#  
#  #a.keybd_event(ord('F'),0,0,0)
#  #sleep(.1)
#  #a.keybd_event(ord('F'),0,0,0)
#  #a.keybd_event(ord('1'),0,0,0)
#  #a.keybd_event(ord('4'),0,0,0)
#	
#  sleep(.1)
#  click((529,385))
#  click((453,311))
#  sleep(.5)
#  
#  typing(pwd)
#  a.keybd_event(c.VK_RETURN,0,0,0)
#  
#  sleep(.5)
#  click((515,309))
#  sleep(.1)
#  a.mouse_event(c.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
#  a.SetCursorPos((611,309))
#  sleep(.5)
#  a.mouse_event(c.MOUSEEVENTF_LEFTUP,0,0,0,0)
#  
#  #a.keybd_event(c.VK_LCONTROL,0,c.KEYEVENTF_EXTENDEDKEY,0)
#  #sleep(.1)
#  #a.keybd_event(ord('C'),0,c.KEYEVENTF_EXTENDEDKEY,0)
#  #a.keybd_event(ord('C'),0,c.KEYEVENTF_KEYUP,0)
#  #a.keybd_event(ord('W'),0,c.KEYEVENTF_EXTENDEDKEY,0)
#  #a.keybd_event(ord('W'),0,c.KEYEVENTF_KEYUP,0)
#  #sleep(.1)
#  #a.keybd_event(c.VK_LCONTROL,0,c.KEYEVENTF_KEYUP,0)
#  #sleep(10)
#  #clip.OpenClipboard()
#  #clip.EmptyClipboard()
#  #clip.SetClipboardText('',c.CF_UNICODETEXT)
