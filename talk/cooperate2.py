#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            
import listen.listen as listener
import comp.comprehender as comprehender

# ---- enumeration ----
MODE_QUIT = 0
MODE_HOME = 1
MODE_SEARCH = 2
MODE_PLAY = 3

def main():
    mode = MODE_HOME
    norecogn = 0

    while mode != MODE_QUIT:

        if mode == MODE_HOME:
            print "  [command mode]"
        elif mode == MODE_SEARCH:
            print "  [search mode]"
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
            if mode == MODE_HOME:

                cmprhdr = comprehender.Comprehender()
                words_dict = cmprhdr.comprehend(result)
                print (", ".join(words_dict['all']).encode("utf-8"))

                #( 超絶単純な判定によるコマンド認識 )
                if "終了" in words_dict['noun']:
                    mode = MODE_QUIT
                elif "検索" in words_dict['noun']:
                    mode = MODE_SEARCH
                elif "再生" in words_dict['noun']:
                    mode = MODE_PLAY
                else:
                    print "!---No command recognized."
                    mode = MODE_HOME
                #end if

            elif mode == MODE_SEARCH:

                cmprhdr = comprehender.Comprehender(result)
                words_dict = cmprhdr.comprehend()
                print (", ".join(words_dict['all']).encode("utf-8"))

                #( 検索機能を追加する )

                mode = MODE_HOME

            else:
                print "!---[BUG 02] This cannot happen."
                mode = MODE_HOME
            #end if
        #end if
    #end while

    print "  [quit]"
    return 0

# ---- Execute ----
if __name__ == "__main__":
    main()
