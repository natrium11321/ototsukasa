#!/usr/bin/env python                                                                                                                                             
# -*- coding:utf-8 -*-                                                                                                                                            

import MeCab

# ---- constants ----
MECAB_MODE = 'mecabrc'
PARSE_TEXT_ENCODING = 'utf-8'

class Comprehender:

    # type comprehender = Content of unicode
    def __init__(self, init_content):
        self.content = init_content

    # unicode -> unit
    def comprehend(self):
        words_dict = self.parse
        print "All:", ",".join(words_dict['all'])
        print "Nouns:", ",".join(words_dict['nouns'])
        print "Verbs:", ",".join(words_dict['verbs'])
        print "Adjs:", ",".join(words_dict['adjs'])
        return
    
    # unicode -> {all:string, nouns:string, verbs:string, adjs:string}
    def parse(self):
        tagger = MeCab.Tagger(MECAB_MODE)
        # convert into string type
        text = self.content.encode(PARSE_TEXT_ENCODING)
        node = tagger.parseToNode(text)
    
        words = []
        nouns = []
        verbs = []
        adjs = []
        while node:
            pos = node.feature.split(",")[0]
            # unicode 型に戻す
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
            "adjs": adjs
            }
        return parsed_words_dict

### Execute                                                                                                                                                       
if __name__ == "__main__":
    c = Comprehender(u"今日も1日頑張るぞい！")
    c.comprehend()