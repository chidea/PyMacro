#! utf-8

from selenium import webdriver
#import selenium
#from selenium.webdriver.common.by import By

#from windows import *
from time import sleep
#from tg import *
if __name__ == '__main__':
  from tg import webogram, waitrst
  drv = webogram('chrome')
  from sqlite3 import connect
  dbcon = connect('test.db')
  dbcur = dbcon.cursor()
  while True:
    mids = []
    while True:
      while True:
        room_name = input('공지할 메시지를 가져올 방 이름(ex:공지, 살림꾼, 서울특별시) (q를 입력하면 종료합니다) >').strip()
        if room_name == 'q':
          drv.close()
          exit()
        dbcur.execute('select peerid from location where name like "%' + room_name +'%" limit 1')
        try:
          pid, = dbcur.fetchone()
        except:
          continue
        break
      #print('debug)peerid is', pid)
      msg = input('공지할 메시지 키워드 (조사를 포함한 단어 전체) >')
      drv.execute_script("mm.getSearch(%d, '%s').then(x => window.o=x, e => window.o=false)" % (pid, msg))
      mid = waitrst(drv)
      if mid == False or mid['count'] == 0:
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
      room_name = input('\n\nsystem> 공지할 메시지가 맞나요?\n아니라면 빈 칸을, 다른 메시지를 추가하시려면 +를 입력하시고\n보낼 메시지 선택이 완료됐다면 공지할 지역 이름(ex:경남)이나 *을 입력해 전체지역에 보냅니다 >').strip()
      if room_name == '': continue
      elif room_name == '+':
        mids.append(mid)
        print('보낼 메시지 목록에 추가되어 현재 %d 개의 메시지가 선택되었습니다.' % len(mids))
        continue
      else:
        mids.append(mid)
        print('%d 개를 보냅니다.' % len(mids))
        if room_name == '*':
          room_name = ' where (lid > 0 and lid < 20) or (lid > 99 and lid < 1000)'
        else:
          room_name = ' where name like "%' + room_name + '%"'
        break
    dbcur.execute('select peerid from location' + room_name)
    for pid, in dbcur.fetchall():
      drv.execute_script("""
      delete window.o;
      var pid = %d;
      var doit = function(){mm.forwardMessages(pid, %s).then(o=>window.o=true, o=>window.o=false);}
      var p = false;
      if(peer.isChannel(pid))
        mm.getHistory(pid,0, 1).then(doit);
      else
        doit();
      """ % (pid, str(mids)))
      rst = waitrst(drv)
      if rst == False:
        print('fail with', pid)
        sleep(60)
