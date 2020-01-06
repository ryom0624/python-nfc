import os
import struct
import sys
import inspect

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/nfcpy')

import nfc

service_code = 0x090f
num_blocks = 20

def connected(tag):
  # tag のメソッド一覧を出す
  print ('TAG-TYPE  : ' , type(tag))
  print ('TAG-METHOD: ' , inspect.getmembers(tag, inspect.ismethod))

# 接続開始
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})