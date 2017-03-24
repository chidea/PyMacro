from webbrowser import open as wopen

def tglink(link, direct=False):
  if len(link) == 22 and link[0] in 'AC':
    link = ('join?invite=' if direct else 'joinchat/') + link
  elif direct:
    link = 'resolve?domain=' + link
  return ('tg://' + link) if direct else ('https://telegram.me/' + link)

def tgopen(link, direct=False):
  wopen(tglink(link, direct))

from os import getenv
def openlinkfile(dirname='', fname='tglink.txt'):
  from os.path import join
  with open(join(dirname, fname)) as f:
    l = f.readlines()
    l = eval( '{' + '\n'.join(l) + '\n}' )
  return l

def webogram():
  from selenium import webdriver
  drv = webdriver.Edge()
  drv.get('https://web.telegram.org/')
  input('enter after loading webogram is done')
  drv.execute_script("""
    var s = angular.element(document.querySelector('body'));
    root = s.injector().get('$rootScope');
    cm = s.injector().get('AppChatsManager');
    peer = s.injector().get('AppPeersManager');
    peers = s.injector().get('PeersSelectService');
    prof = s.injector().get('AppProfileManager');
    loc = s.injector().get('LocationParamsService');
    um = s.injector().get('AppUsersManager');
    mm = s.injector().get('AppMessagesManager');
    up = s.injector().get('ApiUpdatesManager');
    mmid = s.injector().get('AppMessagesIDsManager');
    me = um.getSelf();
    photos = s.injector().get('AppPhotosManager');
    docs = s.injector().get('AppDocsManager');
    mtp = s.injector().get('MtpApiManager');
    mtpf = s.injector().get('MtpApiFileManager');
    fm = s.injector().get('FileManager');
    
    (function loadMoreConv(lastDI=0){
      return mm.getConversations('', lastDI, 100).then(o =>
        o.dialogs.length===100 ?
          loadMoreConv(o.dialogs[99].index) : (window.o=true));
    })();
    """)
  rst = waitrst(drv)
  drv.execute_script('delete window.o')
  return drv

def waitrst(drv, interval=0.1):
  from time import sleep
  while True:
    sleep(interval)
    rst = drv.execute_script('return window.o')
    if not rst is None: break
  drv.execute_script('delete window.o')
  return rst
