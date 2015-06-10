#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

import comprehender

def main():
    # sample_c = Comprehender(u"ライ麦畑のつかまえ役、そういったものに僕はなりたいんだよ。馬鹿げてることは知ってるよ。でも、ほんとうになりたいものといったらそれしかないね。")
    sample_c = comprehender.Comprehender(u"暗証番号")
    words_dict = sample_c.comprehend()
    f = open("test/testout4.txt", "w")
    f.write("All: " + ", ".join(words_dict['all']).encode("utf-8") + "\n")
    f.write("Nouns: " + ", ".join(words_dict['nouns']).encode("utf-8") + "\n")
    f.write("Verbs: " + ", ".join(words_dict['verbs']).encode("utf-8") + "\n")
    f.write("Adjs: " + ", ".join(words_dict['adjs']).encode("utf-8") + "\n")
    f.close()
    return

# ---- Execute ----
if __name__ == "__main__":
    main()
