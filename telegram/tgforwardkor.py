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
    room_name = input('공지할 메시지를 가져올 방 이름(ex:공지, 살림꾼, 서울특별시) (q를 입력하면 종료합니다) >')
    if room_name == 'q':
      exit()
    dbcur.execute('select peerid from location where name like "%' + room_name +'%" limit 1')
    pid, = dbcur.fetchone()
    print('debug)peerid is', pid)
    msg = input('공지할 메시지 키워드 (조사를 포함한 단어 전체) >')
    drv.execute_script("mm.getSearch(%d, '%s').then(x => window.o=x, e => window.o=false)" % (pid, msg))
    mid = waitrst(drv)
    if mid == False:
      print('해당 키워드가 들어간 메시지를 찾을 수 없습니다')
      continue
    else:
      mid = mid['history'][0]
    print('message id :', mid)
    msg = drv.execute_script('return mm.getMessage(%d)' % mid)
    if not msg:
      print('해당 키워드가 들어간 메시지를 찾을 수 없습니다')
      continue
    else:
      print('공지할 메시지 내용 >')
      text = msg['message'] if msg['message'] else msg['media']['caption']
      for t in text:
        try: print(t, end='')
        except:pass
    room_name = input('\n\n공지할 메시지가 맞나요? 아니라면 빈 칸을 입력하시고\n맞다면 공지할 지역 이름(ex:경남)이나 *을 입력해 전체지역에 보냅니다 >').strip()
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
