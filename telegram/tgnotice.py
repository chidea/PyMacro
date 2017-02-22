#! utf-8

from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By

from windows import *
from time import sleep
from tg import *

if __name__ == '__main__':
  input('copy a text to notice and press enter')
  clip.OpenClipboard()
  msg = clip.GetClipboardData()
  clip.CloseClipboard()
  try:
    print(msg)
  except: pass
  #for u in [
  #    #'C2CFpwlvQiwIRjk6xCtU0w',
  #    #'C2CFpwmRfEwBizBuU9OQtA',
  #    #'C2CFpwmNdSPp8X4nxNAqNA',
  #    #'C2CFpwmEEWxVBAl1eDx9ew',
  #    #'C2CFpwqzJg07QDOW9IS3dw',
  #    #'C2CFpwobTvCjgV-V8uoTGg',
  #    #'C2CFpwgGMs1pqM1YW3K2pQ',
  #    #'C2CFpwljUG7TLzsS50oarg',
  #    #'C2CFpwoAqRi5zOoq5Z6Hrg',
  #    #'C2CFpwo4UwFWBbMwZR9-Pg',
  #    #'C2CFpwcP41BST9OrNBFfiA',
  #    #'C2CFpwkmPHowmT4TlWGi0A',
  #    #'C2CFpwglTxLHW8X9MEefig',
  #    #'C2CFpwj8kJ3Ms6xo4Z37bA',
  #    #'C2CFpwkbDSLtYtsShINsdg',  # 전북 부안
  #      # 인원수 # 접주이름
  #    #'A4uFmD2i6TsKKU3S8mYBCQ', # 전라남도 #20
  #    #'C2CFpwpZrMFMcfF77Lrkyw', # 전남_목포시 #1
  #    #'C2CFpwp0Iu2pIfT8oi5fwg', # 전남_여수시 #3
  #    #'C2CFpwdr-WvhpSBYqOohJg', # 전남_순천시 #4
  #    #'C2CFpwq47jxiHqN5UoKIRw', # 전남_광양시 #2
  #    #'C2CFpwl_1m4GkQkVVm2Vow', # 전남_화순군 #0
  #    #'C2CFpwpIgdRpAAOutS_plA', # 전남_해남군 #1
  #    #'C2CFpwlvpmQsQosxN2vudw', # 전남_영암군 #1
  #    #'C2CFpwmlmKlXMPqS0AsXMw', # 전라남도_영광군 #2
  #    #'C2CFpwmL8RLaMyDRzbkD-w', # 전남_진도군 #2
  #    'C2CFpwnZJA8nYMFwSW0CAQ', # 전남_보성군 #1 # 이준재
  #    'C2CFpwo_BU5srfHCo8paGw', # 전남_나주시 #0
  #    'C2CFpwl7EcAkb1fMvj3Rvw', # 전남_담양군 #0
  #    'C2CFpwoHLs3uhouDWL3glw', # 전남_곡성군 #0
  #    'C2CFpwlv8nmsHEXCiot8ZA', # 전남_고흥군 #0
  #    'C2CFpwq4zmMMgIUx3T8urw', # 전남_장흥군 #0
  #    'C2CFpwnVPNQR1o8c-Y_rtA', # 전남_강진군 #0
  #    'C2CFpwqiBfpGIRlzTTiW-A', # 전남_무안군 #1
  #    'C2CFpwm-rf79sSIeQMkNTQ', # 전남_구례군 #0
  #    'C2CFpwolr0BmtMrIE7fKoQ', # 전라남도_함평군 #0
  #    'C2CFpwa4iF5XcecEtxaE_A', # 전라남도_장성군 #0
  #    'C2CFpwpJs6L1Rjys9uFx9Q', # 전라남도_완도군 #0
  #    'C2CFpwmSYDFW4s-LHQsNQw', # 전남_신안군 #1
  #    ]:
  #  tgopen(u, True)
  #  sleep(1)
  #  SendKeys('^v{ENTER}')
  #  sleep(1)

  # loc.openUrl('tg://join?invite=A4uFmD2i6TsKKU3S8mYBCQ')
  # mm.getConversations('전남_나주', 0, 1).$$state.value.dialogs[0].peerID
  drv = webdriver.Edge()
  drv.get('https://web.telegram.org/#/im?p=@civiceyeall')
  input('enter after loading webogram is done')
  drv.execute_script("""var s = angular.element(document.querySelector('.ng-scope'));
    cm = s.injector().get('AppChatsManager');
    peer = s.injector().get('AppPeersManager');
    prof = s.injector().get('AppProfileManager');
    loc = s.injector().get('LocationParamsService');
    um = s.injector().get('AppUsersManager');
    mm = s.injector().get('AppMessagesManager');
    up = s.injector().get('ApiUpdatesManager');
    mmid = s.injector().get('AppMessagesIDsManager');
    me = um.getSelf();
    mtp = s.injector().get('MtpApiManager');
    """)
  #drv.execute_script("log.openUrl('%s')" % tglink(u))
  drv.execute_script("""
    /* jrooms = [ 'C2CFpwmSYDFW4s-LHQsNQw', 'C2CFpwpJs6L1Rjys9uFx9Q' ];
    function jroom(i) {
      mtp.invokeApi('messages.checkChatInvite', { hash: jroom[i]}).then(function (chatInvite){
        var c = chatInvite.chat;
        console.log(c.title, c.id, c.participants_count);
      });
    }*/
    jrooms = [1034086715, 173649089, 175383277, 124516715, 179891772, 159372910, 172523988, 158312036, 161847465, 160166162, 165225487, 171902286, 159060416, 168242893, 158331513, 179883619, 164969684, 178390522, 163491326, 170241856, 112756830, 172602274, 160587825];
            // 전라남도     목포시    여수시      순천시     광양시     화순군     해남군     영암군     영광군     진도군     보성군    나주시      담양군     곡성군     고흥군     장흥군     강진군     무안군     구례군    함평군      장성군     완도군     신안군 
    notiMsg = `%s`
    mksender = function(i){
      mm.sendText(-jrooms[i], notiMsg);
    }
    sender = function(i){
      return mksender(i);
    }
    for (var i = 0; i < jrooms.length; i++){
      setTimeout(function(i){mm.sendText(-jrooms[i], notiMsg);}.bind(this, i), i*500);
    }
  """ % msg)
