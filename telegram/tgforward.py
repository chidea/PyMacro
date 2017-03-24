#! utf-8

from selenium import webdriver
#import selenium
#from selenium.webdriver.common.by import By

#from windows import *
from time import sleep
#from tg import *
from sqlite3 import connect
if __name__ == '__main__':
  from tg import webogram, waitrst
  drv = webogram()
  dbcon = connect('test.db')
  dbcur = dbcon.cursor()
  while True:
    room_name = input('name of room where the message is (enter q to exit) >')
    if room_name == 'q':
      exit()
    dbcur.execute('select peerid from location where name like "%' + room_name +'%" limit 1')
    pid, = dbcur.fetchone()
    print('debug)peerid is', pid)
    msg = input('keyword of message to forward >')
    drv.execute_script("mm.getSearch(%d, '%s').then(x => window.o=x, e => window.o=false)" % (pid, msg))
    mid = waitrst(drv)
    if mid == False:
      print('cannot find message containing such keyword')
      continue
    else:
      mid = mid['history'][0]
    print('message id :', mid)
    msg = drv.execute_script('return mm.getMessage(%d)' % mid)
    if not msg:
      print('cannot find message containing such keyword')
      continue
    else:
      print('content of message to forward >')
      text = msg['message'] if msg['message'] else msg['media']['caption']
      for t in text:
        try: print(t, end='')
        except:pass
    room_name = input('\n\nis this right message to forward? if not, enter blank\nif it is, enter chat name to send or * to send to every rooms >').strip()
    if room_name == '': continue
    elif room_name == '*':
      room_name = ' where lid > 0 and lid < 1000 and lid != 20'
    else:
      room_name = ' where name like "%' + room_name + '%"'
    dbcur.execute('select peerid from location' + room_name)
    for pid, in dbcur.fetchall():
      drv.execute_script("""
      delete window.o;
      var pid = %d;
      var doit = function(){mm.forwardMessages(pid, [%d]).then(o=>window.o=true, o=>window.o=false);}
      var p = false;
      if(peer.isChannel(pid))
        mm.getHistory(pid,0, 1).then(doit);
      else
        doit();
      """ % (pid, mid))
      rst = waitrst(drv)
      if rst == False:
        print('fail with', pid)
        sleep(60)
