# -*- coding: utf-8 -*-

from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Cloud:

    def __init__(self, cnt = 100):
        self.okt = Okt()
        self.data = list()
        self.word_count = cnt

    
    def add_data(self, string):
        input_data = self.okt.nouns(string)
        self.data += input_data

    
    def count(self):
        cnt = Counter(self.data)
        return dict(cnt.most_common(self.word_count))
    

    def make_cloud(self, title = "results/result"):
        wc = WordCloud(font_path='cloud/WordCloud/BMHANNA_11yrs_ttf.ttf', \
            background_color='white', width=800, height=600)
        cloud = wc.generate_from_frequencies(self.count())
        plt.figure(figsize=(10, 8))
        plt.axis('off')
        plt.imshow(cloud)
        plt.savefig("%s.png" %title)


# for TEST
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
    TEST = Cloud(cnt = 30)
    for data in data_set:
        TEST.add_data(data)
    print(TEST.data)
    print(TEST.count())
    TEST.make_cloud()