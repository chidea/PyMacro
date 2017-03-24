#! utf-8

from time import sleep
from windows import click, g

if __name__ == '__main__':
  from tg import webogram, waitrst
  drv = webogram()
  from sqlite3 import connect
  db=connect('test.db')
  c=db.cursor()
  c.execute('select peerid from location where name like "%' + input('target name>') + '%" and lid>=1000')
  pid, = c.fetchone()
  print('peerid is', pid)
  drv.execute_script("mm.getSearch(%d, 0, {_:'inputMessagesFilterPhotoVideo'}, 0, 999).then(x=>window.o=x)" % pid)
  rst = waitrst(drv, 1)
  downbutpos = None
  for mid in rst['history']:
    #print(drv.execute_script("return mm.getMessage(%d)" % mid))
    print(drv.execute_script("""
        delete window.o;
        var m = mm.getMessage(%d).media;
        switch(m._){
        case 'messageMediaPhoto':
          //photos.downloadPhoto(m.photo.id);
          var fname = 'photo'+m.photo.id+'.jpg';
          var size = m.photo.sizes[m.photo.sizes.length-1]; //best
          //var size = m.photo.sizes[0]; //worst
          var floc = size.location;
          var inputFileLocation = {
            _: 'inputFileLocation',
            volume_id: floc.volume_id,
            local_id: floc.local_id,
            secret: floc.secret
          }
          var mimeType='image/jpeg';
          window.o = false;
          mtpf.downloadFile(floc.dc_id, inputFileLocation, size.size, {mime:mimeType}).then( function (blob) {
              window.o = true;
              fm.download(blob, mimeType, fname);});
          return fname;
        case 'messageMediaDocument':
          var p = {};
          if(!docs.getDoc(m.document.id).downloaded)
            p = docs.downloadDoc(m.document.id);
          else
            p = $.Deferred(o=>o.resolve()).promise();
          p.then(o => docs.saveDocFile(window.o = m.document.id));
          return m.document.id;
        }
        """ % mid))
    rst = waitrst(drv, .5)
    if not downbutpos:
      input('press enter while pointing download button')
      downbutpos = g.GetCursorPos()
      input('press enter while pointing close button')
      closebutpos = g.GetCursorPos()
    else:
      input('press enter when download is ready')
    click(downbutpos)
    sleep(1)
    click(closebutpos)
    sleep(.1)
