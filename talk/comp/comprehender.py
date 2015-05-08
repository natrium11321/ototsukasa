#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

import MeCab

# ---- Constants ----
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

# ---- Functions ----
class Comprehender:

    # type comprehender = Content of unicode
    def __init__(self, raw):
        self.raw = raw

    # comprehend : unicode -> unit
    def comprehend(self):
        tagger = MeCab.Tagger(MECAB_MODE)
        text = self.raw.encode(PARSE_TEXT_ENCODING)
          #(convert into str type)
        node = tagger.parseToNode(text)

        words = []
        nouns = []
        verbs = []
        adjs = []
    
        while node:
            pos = node.feature.split(",")[0]
              #(decode to unicode)
            word = node.surface.decode("utf-8")
            if pos == "名詞":
                nouns.append(word)
            elif pos == "動詞":
                verbs.append(word)
            elif pos == "形容詞":
                adjs.append(word)
            words.append(word)
            node = node.next
    
        parsed_words_dict = {
            "all": words[1:-1], # 最初と最後には空文字列が入るので除去
            "nouns": nouns,
            "verbs": verbs,
            "adjs": adjs}
    
        return parsed_words_dict

def main():
    # sample_c = Comprehender(u"ライ麦畑のつかまえ役、そういったものに僕はなりたいんだよ。馬鹿げてることは知ってるよ。でも、ほんとうになりたいものといったらそれしかないね。")
    sample_c = Comprehender(u"暗証番号")
    words_dict = sample_c.comprehend()
    f = open("test/testout3.txt", "w")
    f.write("All: " + ", ".join(words_dict['all']).encode("utf-8") + "\n")
    f.write("Nouns: " + ", ".join(words_dict['nouns']).encode("utf-8") + "\n")
    f.write("Verbs: " + ", ".join(words_dict['verbs']).encode("utf-8") + "\n")
    f.write("Adjs: " + ", ".join(words_dict['adjs']).encode("utf-8") + "\n")
    f.close()
    return

# ---- Execute ----
if __name__ == "__main__":
    main()
