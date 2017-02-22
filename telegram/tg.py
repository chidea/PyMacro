from webbrowser import open as wopen

def tglink(link, direct=False):
  if len(link) == 22 and link[0] in 'AC':
    link = ('join?invite=' if direct else 'joinchat/') + link
  elif direct:
    link = 'resolve?domain=' + link
  return ('tg://' + link) if direct else ('https://telegram.me/' + link)

def tgopen(link, direct=False):
  wopen(tglink(link, direct))

def openlinkfile(fname='tglink.txt'):
  with open(fname) as f:
    l = f.readlines()
    l = eval( '{' + '\n'.join(l) + '\n}' )
  return l
