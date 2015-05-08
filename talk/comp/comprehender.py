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
            "all": words[1:-1], #(omit first and last spaces)
            "nouns": nouns,
            "verbs": verbs,
            "adjs": adjs}
    
        return parsed_words_dict

