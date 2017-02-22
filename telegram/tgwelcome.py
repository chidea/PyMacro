#! utf-8
from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from time import sleep

if __name__ == '__main__':
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
    peerID = -1038552215;
    lastInID = 0;
    lastMid = 0;
    msg = "님 반갑습니다~ 위 글에 있는 링크 통하셔서 사시는 지역 권역방, 지역방으로도 입장해주세요~ 투개표감시때 지역분들과 업무분장 및 소통 위한 방이므로 꼭 입장해주시길 부탁드립니다~";
    longmsg = `전체소통방에 함께하여 주셔서 고맙습니다^^

자신의 "거주지 지역구" 링크를 타고 들어가시고 "주민등록상 주소"와 달라도 괜찮습니다.
참관인 제도는 주민등록상의 주소와 무관합니다.

"투/개표 참관인"과 "사전투표함 지킴이" 정보와 지역정보를 공유하기 위해서 광역구방에 들어가 주시고 광역방안에서 지역구방 안내가 있을텐데 지역구방에 들어가셔야 "투/개표 참관인" 신청을 하실수 있습니다.
꼭! 광역방과 지역구방에 들어가 주시면 고맙겠습니다.

시민의눈 에 함께 하여 주시는 시눈님들은 전체소통방, 채널(공지), 광역방, 지역구방에 함께하여 주시면 다시한번 고맙겠습니다^^

혹시 시눈님중에 시민의힘에 가입을 아직 안하신분은 시민의눈 홈페이지에서 "투표소 수개표" 와 "공직선거법 개정"을 위한 100만인 서명과 부정선거 감시의 "시민의눈 가입"을 하여 주시면 고맙겠습니다^^

[필수 사항 : 시민의눈 가입과 서명하기] http://eye.vving.org/sign/

시민의눈_전체 소통방https://telegram.me/civiceyeall

시민의눈_채널(공지)
https://t.me/civiceyes/403



시민의눈_서울특별시 https://telegram.me/joinchat/A4uFmD2nY0NOdf1587MB6g

시민의눈_경기도 https://telegram.me/Gyeonggido

시민의눈_부산광역시 https://telegram.me/joinchat/A4uFmECnbPY5D6isaf9rkw

시민의눈_인천광역시 https://telegram.me/joinchat/A4uFmD5gy7YolsV0bGyFwg

시민의눈_대구광역시 https://telegram.me/joinchat/A4uFmD2CKtVqAoB0A0LkvQ

시민의눈_울산광역시 https://telegram.me/ulsan

시민의눈_광주광역시 https://telegram.me/joinchat/A4uFmD5YYEfALblD5QeBAA

시민의눈_대전광역시 https://telegram.me/joinchat/A4uFmD3XX7Ek9CCJY82BqQ

시민의눈_제주특별자치도 https://telegram.me/joinchat/A4uFmECPXvrhVRxehCXhrQ

시민의눈_세종특별시 https://telegram.me/joinchat/A4uFmD4aGl2zmFMbGgFO4Q

시민의눈_해외 https://telegram.me/joinchat/A4uFmEA5tqKmB-OYV6XsOw

시민의눈_강원도 https://telegram.me/joinchat/A4uFmD2QgkVsi1dvCjeaXg

시민의눈_충청북도 https://telegram.me/joinchat/A4uFmD32QopaSUUSJQSY1g

시민의눈_충청남도 https://telegram.me/joinchat/A4uFmD4CH-oRgTLnC2G-1g

시민의눈_전라북도 https://telegram.me/joinchat/A4uFmD5bprlgIO23mjkuCQ

시민의눈_전라남도 https://telegram.me/joinchat/A4uFmD2i6TsKKU3S8mYBCQ

시민의눈_경상북도 https://telegram.me/joinchat/A4uFmD4xaGn6qb38-SzMww

시민의눈_경상남도 https://telegram.me/Gyeongsangnam

            ㅡ살림꾼 일동ㅡ`;
    tmid = 17179911828;
    lastUpTime = 0;

    replyTimer=setInterval(function(){
      var mid = mm.getHistory(peerID, 0, 1).$$state.value.history[0];
      if (lastMid == mid) return;
      lastMid = mid;
      var m = mm.getMessage(mid);
      if (m.flags === 256 && m.action && m.action._.startsWith('messageActionChatJoined') && m.fromID != lastInID){
        var now = new Date();
        if ((now - lastUpTime)/1000/60/60 >= 1) {
          lastUpTime = now;
          var text = longmsg;//RichTextProcessor.parseEmojis(longmsg);
          do {
            mm.sendText(peerID, text.substr(0, 4096));
            text = text.substr(4096);
          } while (text.length);
          checker = function (){
            for (var i = 0, ms = mm.getHistory(peerID).$$state.value.history; i < ms.length; i++){
              var m = mm.getMessage(ms[i]);
              if (m.mid > 0 && m.fromID === me.id && longmsg.startsWith(m.message)){
                tmid = m.mid;
                return;
              }
            }
            setTimeout(checker, 1000);
          }
          setTimeout(checker, 1000);
        }else {
          var name = peer.getPeer(lastInID = m.fromID).first_name;
          mm.sendText(peerID, name+msg, {replyToMsgID: tmid});
          /*var text = name+msg;//RichTextProcessor.parseEmojis(name+msg);
          var options = {replyToMsgID: tmid};
          do {
            mm.sendText(peerID, text.substr(0, 4096), options);
            text = text.substr(4096);
            options = angular.copy(options);
          } while (text.length);*/
        }
      }
    }, 2000);
    """)
  #
  #  //mtp = s.injector().get('MtpApiManager');
  #  //dm = s.injector().get('DraftsManager');
  #  //ps = s.injector().get('PeersSelectService');
  #### how to get peerID of any chat
  #drv.execute_script("""
  #  dialog = mm.getConversations('전체소통방', 0, 1).$$state.value.dialogs[0];
  #  peerID = dialog.peerID;
  # """)
  #### how to get tmid
  #drv.execute_script("""
  #  var hiss = mm.getHistory(peerID, 0, 30).$$state.value.history;
  #  for (var i = 0; i < hiss.length; i++){
  #    var his = hiss[i];
  #    his.
  #""")

  #while True:
    #drv.execute_script("mid = mmid.getFullMessageID(dialog.top_message, -dialog.peerID)")
    #sleep(5)
    #drv.execute_script("ps.selectPeer({confirm_type: 'EXT_SHARE_PEER', canSend: true})")
    #drv.execute_script("scope = angular.element('[ng-controller=AppImSendController]').scope()")
    #drv.execute_script("scope.$apply()")
