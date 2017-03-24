#! utf-8

from selenium import webdriver

from time import sleep
from tg import *

# drv.execute_script("return root.$broadcast('ui_history_focus').targetScope.selectedPeerID")

if __name__ == '__main__':
  drv = webogram()
  l=openlinkfile(getenv('USERPROFILE')+'\\desktop\\project\\civiceyes\\telegram')
  for n in l:
    #drv.execute_script("return mm.getConversations('%s', 0, 1).$$state.value.dialogs[0].peerID" % l[n])
    #print(n, drv.execute_script("""
    #  /*d.then(function(){
    #    o.pid = mm.getConversations("%s", 0, 1).$$state.value.dialogs[0].peerID;
    #    o.title = cm.getChat(pid).title;
    #  });*/
    #  """ % n))
    print("INSERT OR IGNORE INTO location VALUES ( 0 , '%s', '%s', " % (n, l[n]), end='')
    while True:
      if len(l[n]) == 22 and l[n][0] in 'AC':
        drv.execute_script(""" 
          mtp.invokeApi('messages.checkChatInvite', {hash:'%s'}).then(function(x){window.o=x.chat;}).catch(function(){window.o=false});
        """ % l[n])
      else:
        drv.execute_script("""
            var x = peer.resolveUsername('%s').then(function(peerID){window.o = cm.getChat(-peerID);});
            """ % l[n])
      sleep(1)
      rst = drv.execute_script("return window.o")
      if rst == False:
        sleep(60*5)
        drv.execute_script("$('div.modal button').click()")
        continue
      elif rst is None:
        sleep(1)
        while drv.execute_script("return window.o") is None:
          sleep(1)
      else:
        break
    rst =  drv.execute_script('return window.o')
    print("'%s', %d );" % (rst['title'], rst['id']))
    drv.execute_script('delete window.o')
    sleep(9)
