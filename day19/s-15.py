

# 6. 특성과 타깃 분리
### 전처리 : 학습 하기 전에 문장들을 단어로 분리 ###
from sklearn.model_selection import train_test_split
X_train, X_test, Y_test = train_test_split(
    # X = 리뷰 , Y = 평점라벨링( 0:부정 1:긍정 )
    df_sample['cleaned_review'] , df_sample['label'] ,
    test_size=0.2 , random_state=42 , stratify=df_sample['label'] )
# 7. 리뷰 --> 행렬(벡터) 변환
from sklearn.feature_extraction.text import TfidfVectorizer
# TfidfVectorizer( tokenizer = 토큰나이즈함수 )
tfidf = TfidfVectorizer(
    tokenizer = tokenize_kiwi , # 생략시 공백/띄어쓰기 기준으로 분리 # 직접 만든 함수
    token_pattern = None , # 실행 중 발생하는 로그 비활성화
     
 )
X_train_tfidf = tfidf.fit_transform( X_train ) # 학습 -> 변환
X_test_tfidf = tfidf.transform( X_test ) # 테스트용
print( X_train_tfidf.shape )
print( X_test_tfidf.shape )


# 8. 긍정/부정 : 감성분석
from sklearn.linear_model import LogisticRegression # 실무적으로 lightGBM
model = LogisticRegression( C=1.0 , max_iter=)


# 9. 


# 정규표현식
cleaned_new = []
for text in new_reviews :
    text = re.sub( r'[^가-힣a-zA-Z0-9\s]', '', str(text) )
    cleaned_new.append( ''.join(text.split() ) )
# 정규표현식 이후 토큰나이즈
new_tfidf = tfidf.transform( cleaned_new )
# 토큰나이즈 이후 모델추론
probs = model.predict_proba( new_tfidf ) # predict 추론 # predict_proba 추론확률
# 0.6 이상이면 긍정 , 0.4 이하이면 부정 그외 중립
for i in range( len(new_reviews) ) : # 리뷰 수 만큼 반복
    pos = probs[i][1] # i번째 추론 결과 확률( 0인덱스 부정확률 1인덱스 긍정확률 )
    if pos >= 0.6 :
        contents = '긍정'
    elif pos <= 0.4 : 
        contents = '부정'
    else : 
        contents = '중립'
    print( f'리뷰 : ' , {new_reviews[i] } )
    print( f'감정분석 : ' , {contents} )

