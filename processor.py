#!/usr/bin/env python
# -*- coding:utf-8 -*-
from talk.listener import Listener
from talk.comprehender import Comprehender
from talk.database import Database
from talk.drowner import Drowner
from talk.unlocker import Unlocker
from talk.speaker import Speaker
from hardware.getHuman import getHuman
from hardware import LED
from hardware.diffuser import Diffuser
import time
import sys
import argparse

#---- enumeration ----
MODE_UNLOCK = -2
MODE_LOCKED = -1
MODE_QUIT = 0
MODE_HOME = 1
MODE_SEARCH = 2
MODE_PLAY = 3
MODE_REVIEW = 4
MODE_DIFFUSE = 5

MAX_RETRY = 3

#---- initialize ----
listener = Listener(600)
comprehender = Comprehender()
speaker = Speaker()
diffuser = Diffuser(speaker)

#( get_input : unit -> (string | None) )
def get_input():
  LED.LEDon('y')
  print "* waiting input..."
  result = listener.listen()

  if result is None:
    pass # print "(None)"
  else:
    print ("> " + result)

  LED.LEDoff('y')
  return result
#  return raw_input().decode('utf-8')

  LED.LEDoff('y')
  return result
# use below instead if you'd like to input string from standard input
#   return raw_input().decode('utf-8')


#( deal_with_no_recognition : int ref -> unit )
def deal_with_no_recognition(refnorecogn):

  refnorecogn += 1
  if refnorecogn < MAX_RETRY:
    print ("!---No word recognized.")
    speaker.speak("もう一度言ってください")
    return
  else:
    print ("!---No word recognized for three consecutive times.")
    return


#( mode_locked : unit -> mode )
def mode_locked():
  print "  [locked mode]"
  time.sleep(1)
  if getHuman():
    return MODE_UNLOCK
  else:
    return MODE_LOCKED

#( mode_unlock : unit -> mode )
def mode_unlock():

  if not unlocker.is_locked():
    return MODE_HOME
  else:
    #予約中
    LED.LEDon('r')
    norecogn = 0
    while norecogn < MAX_RETRY:

      print "  [unlock mode]"
      speaker.speak("パスワードを言ってください")
      result = get_input()

      if result is None:
        norecogn += 1
        deal_with_no_recognition(norecogn)
      else:
        if unlocker.try_to_unlock(result):
          print "unlock successfully"
          LED.LEDoff('r')
          return MODE_HOME
        else:
          norecogn += 1
          if norecogn < MAX_RETRY:
            print "unlock failed, please try again."
          else:
            print "unlock failed for consecutive three times."

    #end while
    return MODE_LOCKED

#( mode_search : recogn ref -> mode )
def mode_search():

  LED.LEDon('g')
  norecogn = 0
  while norecogn < MAX_RETRY:

    print "  [search mode]"
    speaker.speak("検索ワードを言ってください")
    result = get_input()

    # print result #検索キーワードを出力
    if result is None:
      deal_with_no_recognition(norecogn)
    else:
      drowner.drown(result)
      return MODE_HOME

  #end while
  return MODE_HOME


#( mode_play : unit -> mode )
def mode_play():

  LED.LEDon('g')
  print "  [play mode]"
  drowner.drown()
  return MODE_HOME


def mode_review():

  norecogn = 0
  while norecogn < MAX_RETRY:
    print "  [review mode]"
    speaker.speak("評価を教えてください")
    result = get_input()

    if result is None:
      deal_with_no_recognition(norecogn)
    else:
      #review登録
      db.register_review(result)
      speaker.speak("レビューを登録しました。")
      return MODE_HOME


def mode_diffuse():

  diffuser.diffuse()
  return MODE_HOME


#( mode_home : unit -> mode )
def mode_home():

  LED.LEDoff('g')
  norecogn = 0
  print "  [command mode]"
  speaker.speak("何をしますか？")
  result = get_input()

  if result is None:
    print ("!---No word recognized.")
    speaker.speak("もう一度言ってください")
    return MODE_HOME
  else:
    words_dict = comprehender.comprehend(result)
    print ("[" + (" ".join(words_dict['all']).encode("utf-8")) + "]")

    #( 超絶単純な判定によるコマンド認識 )
    if u"終了" in words_dict['all']:
      return MODE_QUIT
    elif u"検索" in words_dict['all']:
      return MODE_SEARCH
    elif u"再生" in words_dict['all']:
      return MODE_PLAY
    elif u"評価" in words_dict['all']:
      return MODE_REVIEW
    elif u"臭" in words_dict['all'] or u"消臭" in words_dict['all']:
      return MODE_DIFFUSE
    else:
      print "!---No command recognized."
      return MODE_HOME


def main():
  #---- 初期化 ----
  mode = MODE_LOCKED
  for c in ['r','g','y']:
      LED.LEDoff(c)

  speaker.speak("こんにちは！")

  counter = 0

  while mode != MODE_QUIT:

    if mode == MODE_LOCKED:
      mode = mode_locked()
    else:
      if mode == MODE_UNLOCK:
        mode = mode_unlock()
      elif mode == MODE_HOME:
        mode = mode_home()
      elif mode == MODE_SEARCH:
        mode = mode_search()
      elif mode == MODE_PLAY:
        mode = mode_play()
      elif mode == MODE_REVIEW:
        mode = mode_review()
      elif mode == MODE_DIFFUSE:
        mode = mode_diffuse()
      else:
        print "!---[BUG] This cannot happen."
        mode = MODE_HOME
      if not getHuman():
        if counter < 5:
          counter += 1
        else:
          #5ループ連続で人がいないときはトイレを解放
          mode = MODE_LOCKED
          db.update_status(False)
      else:
        counter = 0

  #end while

  print "  [quit]"
  speaker.speak("さよなら")
  return


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--serverip', required=True)

    args = parser.parse_args()

    # load db, unlocker and drowner
    global db, unlocker, drowner
    db = Database(args.serverip)
    unlocker = Unlocker(db)
    drowner = Drowner(db)


#---- execute ----
if __name__ == "__main__":
  parse_arguments()
  main()
