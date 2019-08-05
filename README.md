# REST API 

API 목록
 - 워드 클라우드 생성
 - 감성 분석
 
<hr/>

워드클라우드 생성
--

API url : http://35.221.123.234/cloud/

INPUT (POST Only)
<pre><code>{
    "title" : "파일 제목",
    "count" : 50,
    "text" : "내용"
}
</code></pre>

OUTPUT
<pre><code>{
    "url": "http://35.221.123.234/images/파일 제목.png",
    "length": 2,
    "target": "내용"
}
</code></pre>
<hr/>

감성 분석
--

API url : http://35.221.123.234/emotion/

INPUT (POST Only)
<pre><code>{
    "text" : "내용"
}
</code></pre>

OUTPUT (sample)
<pre><code>{
    "value": -3,
    "length": 247,
    "target": "바른미래당 '김정은 위원장, 문재인 대통령에 배은망덕' 문재인 대통령, 조계종 총무원장 원행스님 등 불 교계 지도자와 오찬 간담회 문재인 대통령 - 한국 불교지도자들 초청해 오찬 가져 문재인 정부 D+805 [문재인 국정지지율] 서울서 부정이 긍정보다 높았다 문재인 직무수행, 긍정 48% 부정 42% 문재인 대통령 '국민 통합 가장 어려워…국가적 어려움에 마음 모여야' ‘정전협정 66주년’ 문재인 대통령,  한반도 안보정세-개각 과제 고심"
}
</code></pre>
