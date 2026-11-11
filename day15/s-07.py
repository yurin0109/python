import pandas as pd
fish = pd.read_csv( "./day15/Fish.csv" ) 
# 1) 다중 분류 실습 하기 위한 특성 / 타깃(여러 개 어종) 구분
X = fish.drop( columns=['Species'] )     # 어종 제외한 모든 열
Y = fish['Species']                      # 어종 열
# 2) 분리 , stratify=Y 정답지에 학습용과 테스트용 비율 유지( 분류 모델 권장 )
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42, stratify=Y
)
# 3) 다항 특성들의 스케일링
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform( X_train ) # fit + transform
X_test_scaled = ss.transform( X_test )
# 4) 로지스틱 회귀 = 이진(시그모이드) 또는 다중(소프트맥스)에서 자동 선택 된다.
# L2규제(릿지) 자동 포함. 손실(오차)함수 계산 한다. C = 1.0 기본값 / 하이퍼파라미터
# 계산반복수(경사하강법) : 최적의 가중치/기울기 찾기 위한 계산 반복수 , 기본값 100 / 권장 1000 ~ 3000 
# 경사하강법 : 기울기(가중치) 변경하면서 최적의 기울기(가중치) 찾는 과정
from sklearn.linear_model import LogisticRegression
model = LogisticRegression( C=1.0 , max_iter=1000 , random_state=42 )
model.fit( X_train_scaled , Y_train )
Y_pred = model.predict( X_test_scaled )
print( Y_pred )
print( Y_pred[ :3] ) # ['Bream' 'Perch' 'Smelt']
Y_pred_proba = model.predict_proba( X_test_scaled )
import numpy as np
print( np.round( Y_pred_proba[:3] , 3 ) ) # np.round( 리스트 , 자릿수 )
print( model.classes_ ) # 정답지 경우의 수 , 타깃의 클래스/값
# ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']

