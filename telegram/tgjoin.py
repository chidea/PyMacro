from windows import *
from webbrowser import open

for u in [
    'C2CFpwlvQiwIRjk6xCtU0w',
    'C2CFpwmRfEwBizBuU9OQtA',
    'C2CFpwmNdSPp8X4nxNAqNA',
    'C2CFpwmEEWxVBAl1eDx9ew',
    'C2CFpwqzJg07QDOW9IS3dw',
    'C2CFpwobTvCjgV-V8uoTGg',
    'C2CFpwgGMs1pqM1YW3K2pQ',
    'C2CFpwljUG7TLzsS50oarg',
    'C2CFpwoAqRi5zOoq5Z6Hrg',
    'C2CFpwo4UwFWBbMwZR9-Pg',
    'C2CFpwcP41BST9OrNBFfiA',
    'C2CFpwkmPHowmT4TlWGi0A',
    'C2CFpwglTxLHW8X9MEefig',
    'C2CFpwj8kJ3Ms6xo4Z37bA',
    'C2CFpwkbDSLtYtsShINsdg',
    'C2CFpwpZrMFMcfF77Lrkyw',
    'C2CFpwp0Iu2pIfT8oi5fwg',
    'C2CFpwdr-WvhpSBYqOohJg',
    'C2CFpwo_BU5srfHCo8paGw',
    'C2CFpwq47jxiHqN5UoKIRw',
    'C2CFpwl7EcAkb1fMvj3Rvw',
    'C2CFpwoHLs3uhouDWL3glw',
    'C2CFpwm-rf79sSIeQMkNTQ',
    'C2CFpwlv8nmsHEXCiot8ZA',
    'C2CFpwnZJA8nYMFwSW0CAQ',
    'C2CFpwl_1m4GkQkVVm2Vow',
    'C2CFpwq4zmMMgIUx3T8urw',
    'C2CFpwnVPNQR1o8c-Y_rtA',
    'C2CFpwpIgdRpAAOutS_plA',
    'C2CFpwlvpmQsQosxN2vudw',
    'C2CFpwqiBfpGIRlzTTiW-A',
    'C2CFpwolr0BmtMrIE7fKoQ',
    'C2CFpwmlmKlXMPqS0AsXMw',
    'C2CFpwa4iF5XcecEtxaE_A',
    'C2CFpwpJs6L1Rjys9uFx9Q',
    'C2CFpwmL8RLaMyDRzbkD-w',
    'C2CFpwmSYDFW4s-LHQsNQw'
    ][10:]:
  input()
  if len(u) == 22:
    open('tg://join/?invite=' + u)
  else:
    open('tg://resolve?domain=' + u)
  sleep(2)
  click((1749,825))
  sleep(1)
  #click((1849,825))
  #sleep(1)
  a.keybd_event(c.VK_LMENU,0,c.KEYEVENTF_EXTENDEDKEY,0)
  a.keybd_event(c.VK_TAB,0,c.KEYEVENTF_EXTENDEDKEY,0)
  a.keybd_event(c.VK_TAB,0,c.KEYEVENTF_KEYUP,0)
  sleep(.1)
  a.keybd_event(c.VK_LMENU,0,c.KEYEVENTF_KEYUP,0)
