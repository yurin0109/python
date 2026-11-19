# '텍스트 마이닝' 실습에 필요한 데이터셋
import pandas as pd
# 리뷰 데이터셋
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
df = pd.read_table(url, names=['rating', 'review']) # rating : 평점 , review : 리뷰
df = df[df['rating'] != 3]                         
df['label'] = (df['rating'] >= 4).astype(int)       # 평점4 이상은 긍정 , 평점 2 이하 부정
# 전체데이터셋 에서 특정 n개 샘플링
df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True)
print( df_sample.shape ) # (5000, 3)

# 1) 텍스트에서 전처리 = 정규표현식 자주 사용됨. vs 리액트/JS 입력 유효성검사
import re # 정규표현식 함수
cleaned_list = [] # 정규표현식 통과한 목록
for text in df_sample['review'] : # 리뷰 들을 반복
    # re.sub( r'[표현식]' , '치환문자' , str() )
    text = re.sub( r'[^가-힣a-zA-Z0-9\s]',' ',str(text) )
    # .join( 리스트 ) : 각 리스트 항목 사이에 특정 문자 연결
    # . split() : 하나의 문자열 내 특정 문자로 분리하여 리스트 반환
    cleaned_list = ''.join( text.split() ) # '대한 민국' -> ['대한','민국'] -> 대한 민국
    cleaned_list.append( cleaned_text )
df_sample['cleaned_review'] = cleaned_list
print( df_sample.head(3) )
df_sample['cleaned_review'] = cleaned_list
print( df_sample.head(3) )