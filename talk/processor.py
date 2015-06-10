#!/usr/bin/env python
# -*- coding:utf-8 -*-
from listener import Listener
from comprehender import Comprehender
#from database import Database
#from drowner import Drowner

#---- enumeration ----
MODE_UNLOCK = -2
MODE_LOCKED = -1
MODE_QUIT = 0
MODE_HOME = 1
MODE_SEARCH = 2
MODE_PLAY = 3
MODE_EVAL = 4

#---- global variable ----
norecogn = 0
mode = MODE_LOCKED
listener = Listener(600)
comprehender = Comprehender()

#( get_input : unit -> (string | None) )
def get_input():
  print "* waiting input... : 入力を待っています…"
#  return listener.listen()
  return raw_input()

def deal_with_no_recognition():
  norecogn += 1
  if norecogn < 3:
    print ("!---No word recognized.")
  else:
    print ("!---No word recognized for three consecutive times.")
    norecogn = 0
    mode = MODE_HOME

  return

def mode_locked():
  print "  [locked mode]"
  #(should be written)
  # * if 人感センサからの情報が陽性
  # *   mode = MODE_UNLOCK
  # * #end if

  return

def mode_unlock():
  print "  [unlock mode]"
  #(should be written)
  # * 認識された文字列をデータベースに送信
  # * if ロックが外れた
  #     mode = MODE_HOME
  # * #end if

  return

def mode_home():
  print "  [command mode]"
  result = get_input()

  if result == None:
    print ("!---No word recognized.")
  else:
    norecogn = 0
    words_dict = comprehender.comprehend(result)
    print (" ".join(words_dict['all']).encode("utf-8"))

    #( 超絶単純な判定によるコマンド認識 )
    if u"終了" in words_dict['all']:
      mode = MODE_QUIT
    elif u"検索" in words_dict['all']:
      mode = MODE_SEARCH
    elif u"再生" in words_dict['all']:
      mode = MODE_PLAY
    elif u"評価" in words_dict['all']:
      mode = MODE_EVAL
    else:
      print "!---No command recognized."
      mode = MODE_HOME

  return

def mode_search():
  print "  [search mode]"
  result = get_input()

  if result == None:
    deal_with_no_recognition()
  else:
    #(should be written)
    #( 検索：Drawnerを呼ぶ )
    pass

  return

def mode_play():
  print "  [play mode]"
  #(should be written)
  #( 再生：Drawnerを呼ぶ )

  return

def mode_eval():
  print "  [review mode]"
  result = get_input()

  if result == None:
    deal_with_no_recognition()
  else:
    #(should be written)
    #( 評価処理：ReviewSenderを呼ぶ )
    pass

  return

def main():
  #---- 初期化 ----
  # mode = MODE_LOCKED
  mode = MODE_HOME
  norecogn = 0

  while mode != MODE_QUIT:

    if mode == MODE_LOCKED:
      mode_locked()
    elif mode == MODE_UNLOCK:
      mode_unlock()
    elif mode == MODE_HOME:
      mode_home()
    elif mode == MODE_SEARCH:
      mode_search()
    elif mode == MODE_PLAY:
      mode_play()
    else:
      print "!---[BUG] This cannot happen."
      mode = MODE_HOME

  #end while

  print "  [quit]"
  return

#---- execute ----
if __name__ == "__main__":
  main()
