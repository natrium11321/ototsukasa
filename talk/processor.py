#!/usr/bin/env python
# -*- coding:utf-8 -*-
import listener
import comprehender

# ---- enumeration ----
MODE_UNLOCK = -2
MODE_LOCKED = -1
MODE_QUIT = 0
MODE_HOME = 1
MODE_SEARCH = 2
MODE_PLAY = 3
MODE_EVAL = 4

#( main : unit -> unit )
def main():
    # mode = MODE_LOCKED
    mode = MODE_HOME
    norecogn = 0

    while mode != MODE_QUIT:

        if mode == MODE_LOCKED:
            #(should be written)
            # * if 人感センサからの情報が陽性
            # *    mode = MODE_UNLOCK
            # * #end if
            pass
        else:
            if mode == MODE_UNLOCK:
                print "  [unlock mode]"
            elif mode == MODE_HOME:
                print "  [command mode]"
            elif mode == MODE_SEARCH:
                print "  [search mode]"
            elif mode == MODE_PLAY:
                print "  [play mode]"
            else:
                print "!---[BUG 01] This cannot happen."
                print "  [command mode]"
                mode = MODE_HOME
            #end if

            print "* waiting input..."
            lsnr = listener.Listener(600)
            result = lsnr.listen()

            if result == None:

                norecogn += 1
                if norecogn < 3:
                    print ("!---No word recognized.")
                else:
                    print ("!---No word recognized for three consecutive times.")
                    norecogn = 0
                    if mode == MODE_HOME:
                        mode = MODE_QUIT
                    else:
                        mode = MODE_HOME
                    #end if
                #end if

            else:
                norecogn = 0
                cmprhdr = comprehender.Comprehender()
                words_dict = cmprhdr.comprehend(result)
                print (", ".join(words_dict['all']).encode("utf-8"))

                if mode == MODE_UNLOCK:
                    #(should be written)
                    # * 認識された文字列をデータベースに送信
                    # * if ロックが外れた
                    #       mode = MODE_HOME
                    # * #end if
                    pass

                elif mode == MODE_HOME:

                    #( 超絶単純な判定によるコマンド認識 )
                    if "終了" in words_dict['noun']:
                        mode = MODE_QUIT
                    elif "検索" in words_dict['noun']:
                        mode = MODE_SEARCH
                    elif "再生" in words_dict['noun']:
                        mode = MODE_PLAY
                    elif "評価" in words_dict['noun']:
                        mode = MODE_EVAL
                    else:
                        print "!---No command recognized."
                        mode = MODE_HOME
                    #end if

                elif mode == MODE_SEARCH:

                    #(should be written)
                    #( 検索機能を追加する )

                    mode = MODE_HOME

                elif mode == MODE_PLAY:

                    #(should be written)
                    #( 再生機能を追加する )

                    mode = MODE_HOME

                elif mode == MODE_EVAL:

                    #(should be written)
                    #( 評価を処理する )

                    mode = MODE_HOME

                else:
                    print "!---[BUG 02] This cannot happen."
                    mode = MODE_HOME
                #end if
            #end if
        #end if
    #end while

    print "  [quit]"
    return

# ---- execute ----
if __name__ == "__main__":
    main()
