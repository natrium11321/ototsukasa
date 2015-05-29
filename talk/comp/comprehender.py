#!/usr/bin/env python                                                                                                                           
# -*- coding:utf-8 -*-                                                                                                                                            

import MeCab

# ---- Constants ----
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

# ---- Functions ----
class Comprehender:
    def __init__(self):
        self.tagger = MeCab.Tagger(MECAB_MODE)
    #end def

    #( comprehend : Comprehender. -> unicode -> {"all" * "nouns" * "verbs" * "adjs"} )
    def comprehend(self, raw):
        text = raw.encode(PARSE_TEXT_ENCODING)
          #(convert into str type)
        node = self.tagger.parseToNode(text)
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
            #end if
            words.append(word)
            node = node.next
        #end while

        parsed_words_dict = {
            "all": words[1:-1], #(omit first and last spaces)
            "nouns": nouns,
            "verbs": verbs,
            "adjs": adjs}

        return parsed_words_dict
    #end def
#end class
