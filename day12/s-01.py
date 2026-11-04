# 사이킷런 ? 방대한 머신러닝 알고리즘 모델 제공 라이브러리
# pip install scikit-learn

# 머신러닝 목표: 추론/예측 과정
# 특성: 모델이 학습하는 자료 정보 , 타깃 : 모델이 맞혀야 하는 정답 정보

# 지도학습: 특성 , 타깃을 모두 제공하여 학습 ( 회귀 / 분류 )
# 비지도학습: 타깃 없이 특성 만으로 제공하여 학습 ( 군집 / 토픽 / 주성분 )

# 회귀모델
# 1] 단순 선형 회귀
# https://www.kaggle.com/datasets/vipullrathod/fish-market
# 1) 판다스로 자료 불러오기
import pandas as pd
df = pd.read_csv( './day12/Fish.csv' )
df.info()
# 2) 모델 학습에 사용할 데이터 추출
feature = ['Length2']           # 특성: Lenght2 ( 물고기의 대각선 cm ) # 사이킷런 모델 구조상 학습할 특성은 2차원
target = 'Weight'                 # 타깃: Weight ( 물고기의 무게 g )
# 3) 독립변수/입력변수/특성/X    ,     종속변수/목표변수/타깃/Y
X = df[feature] # 2차원
Y = df[target]  # 1차원
# 4) 