# -*- coding: utf-8 -*-

from konlpy.tag import Okt
from collections import Counter
from .knu.knusl import KnuSL


class Emo:

    def __init__(self):
        self.okt = Okt()
        self.data = list()
        self.ksl = KnuSL()
    

    def add_data(self, string):
        input_data = self.okt.pos(string, norm=True, stem=True)
        self.data += input_data
    

    def get_emo(self):
        pos = 0
        for word in map(lambda x:x[0], self.data):
            _ , tmp = self.ksl.data_list(word)
            try:
                pos += int(tmp)
            except:
                pass
        return pos
    
    
    def clear(self):
        self.data = list()


if __name__ == "__main__":
    data_set = [
        '바른미래당 “김정은 위원장, 문재인 대통령에 배은망덕”',
        '문재인 대통령, 조계종 총무원장 원행스님 등 불교계 지도자와 오찬 간담회', 
        '문재인 대통령 - 한국 불교지도자들 초청해 오찬 가져',
        '문재인 정부 D+805', 
        '[문재인 국정지지율] 서울서 부정이 긍정보다 높았다', 
        '문재인 직무수행, 긍정 48% 부정 42%', 
        '문재인 대통령 "국민통합 가장 어려워…국가적 어려움에 마음 모여야"', 
        '‘정전협정 66주년’ 문재인 대통령,  한반도 안보정세-개각 과제 고심',
        ]
    TEST = Emo()
    for data in data_set:
        TEST.add_data(data)
    print(TEST.data)
    print(TEST.get_emo())