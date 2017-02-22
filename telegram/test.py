from webbrowser import open as wopen
from sys import argv
from qrcode import make

from tg import *

def showqr(l, name):
  for o in l:
    if name in o:
      print(name)
      make( tglink(l[o]) ).show()

if __name__ == '__main__':
  l = openlinkfile()
  while True:
    lname = input('지역명>')
    showqr(l, lname)
