#! utf-8

from time import sleep
from tg import *

if __name__ == '__main__':
  from tg import webogram, waitrst
  drv = webogram()
  from sqlite3 import connect
  db=connect('test.db')
  c=db.cursor()
  c.execute('select name, peerid from location where (lid > 1 and lid < 20) or name="¼¼Á¾"')
  for name, pid in c.fetchall():
    drv.execute_script("prof.getChatFull(%d).then(o=>window.o=o)" % (-pid,))
    cnt = waitrst(drv)
    if cnt : cnt = cnt['participants_count']
    print(name, cnt)
