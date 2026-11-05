# 1] 항 추가 하는 함수
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures()               # 객체 생성
poly.fit( [[2]] )                         # 특성(2) 규칙
print( poly.transform( [[ 2 ]] ) )        # [[1. 2. 4.]] # 기본절편,원래값,제곱값
poly.fit( [[3]] )                         # 특성(3) 규칙
print( poly.transform( [[ 3 ]] ) )        # [[1. 3. 9.]] 
# 2] 기본 절편 제외
poly = PolynomialFeatures( include_bias = False )
poly.fit( [[2]] )
print( poly.transform( [[2]] ) )          # [[2. 4.]]
# 3] 특성 2개 인 경우
poly = PolynomialFeatures( include_bias = False )
poly.fit( [[ 2,3 ]] )                      # 특성( 2,3 ) 규칙 ( 제곱/곱셈 )
print( poly.transform( [[ 2 , 3 ]] ) )     # 2,3 / 4,9 / 6
# *] 특성 3개 인 경우
poly = PolynomialFeatures( include_bias = False )
poly.fit( [[2,3,4]] )
print( poly.transform( [[2,3,4]] ) ) # 9개
# 수동으로 특성의 제곱항을 만들지 않고 자동으로(PolynomialFeatures)으로 다항 추가

# 2] 다항 회귀 모델
import pandas as pd
df = pd.read_csv( './day13/Fish.csv' )
# 1) 특성 과 타깃 구성
X = df[ ['Length2' , 'Height' , 'Width'] ] # 특성 3개
Y = df[ 'Weight' ] # 타깃 1개
# 2) 훈련용/테스트용 분리 8:2
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 )
# 3) 과소적합 해결/방지 하고자 항 추가 == PolynomialFeatures
poly = PolynomialFeatures( include_bias=False )
poly.fit( X_train ) # 학습할 특성들을 규칙(제곱/곱셈) 찾기
X_train_poly = poly.transform( X_train )
X_test_poly = poly.transform( X_test )
print( X_train.shape )                #  (127, 3) 127, 3(특성)
print( X_train_poly.shape )           #  (127, 9) 127, 9( 특성-> 항 추가됨 확인 )
# 4) 모델 학습
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit( X_train_poly , Y_train ) # 훈련용 다항 특성으로 학습*
# 5) 결정 계수
from sklearn.metrics import r2_score
Y_pred = model.predict( X_test_poly ) # 테스트용 다항 특성으로 예측*
print( 'r2 : ' , r2_score( Y_test , Y_pred ) ) # r2_score( 정답지 , 예측값 )
# r2 :  0.9719372415762594

# 3] 다항의 차수 늘리기 , degree = 10 , (차수n) 제곱까지 항 추가하기 / 생략 시 2
poly = PolynomialFeatures( include_bias=False , degree= 10 )
poly.fit( X_train )
X_train_poly2 = poly.transform( X_train )
print( X_train_poly2.shape ) # 차수 2 -> 차수 10 증가에 따른 (127 ,9) -> (127, 285)
X_test_poly2 = poly.transform( X_test )

# 학습 후 결정계수 확인 
model = LinearRegression()
model.fit( X_train_poly2 , Y_train ) # 훈련용 다항 특성으로 학습*
from sklearn.metrics import r2_score
Y_pred = model.predict( X_test_poly2 ) # 테스트용 다항 특성으로 예측*
print( 'r2 : ' , r2_score( Y_test , Y_pred ) ) # r2_score( 정답지 , 예측값 )
# r2 :  0.07276663213888512
# *] 모델 구현 에서 다양한 속성값( degree = N ) 들을 테스트하여 설계/구현 한다.
# *] 특성이 너무 많아지면 훈련 데이터가 과하게 집착하여 과대적합 발생. -> 점수 낮아질 확률 높음

# 4] 특성이 많아짐에 따라 특성간의 단위 표준화( 0 ~ 1 )
from sklearn.preprocessing import StandardScaler
ss = StandardScaler() # 객체 생성
ss.fit( X_train_poly ) # 항이 추가된 특성으로 표준화
X_train_scaled = ss.transform( X_train_poly )
X_test_scaled = ss.transform( X_test_poly )
print( X_train_poly[0] )    # [ 16.2          4.5924 ~ ]
print( X_train_scaled[0] )  # [ -1.14878727 -1.06273398 ~ ] 
# 평균보다 작으면 음수 , 평균+1 했을 때 표준편차 보다 크면 1 이상


# 5] 규제: 기울기(가중치) 크기에 패널티를 부여 하여 특성들의 오차 확인 하여 특성 완만/제외
# 1) 릿지
from sklearn.linear_model import Ridge
# 2) alpha(규제강도) : 값이 커질수록 가중치/기울기를 0에 가깝게 규제: 완만 
# 반복하여 최적의 규제 강도 찾기
alpha_list = [ 0.001 , 0.01 , 0.1 , 1 , 10 , 100 ]
for alpha in alpha_list :
    model = Ridge( alpha = alpha ) # 강도 설정 하여 릿지 모델 생성
    model.fit( X_train_scaled , Y_train ) # 학습
    # 훈련 데이터 점수와 테스트용 점수 격차 적은 alhpa 찾기
    print( alpha, " --- 훈련용 학습 데이터 점수 vs 테스트용 학습 데이터 점수 --- " )
    print( "Train R2: " , model.score( X_train_scaled , Y_train ) )
    print( "Test R2: " , model.score( X_test_scaled , Y_test ) ) # alpha 10 : 격차 가장 적다.

# 3) 라쏘 모델
from sklearn.linear_model import Lasso
lasso = Lasso( alpha=10 ) # 임의의 강도 지정 라쏘 모델 객체 생성
lasso.fit( X_train_scaled , Y_train )
print( lasso.score( X_train_scaled , Y_train ) )
print( lasso.score( X_test_scaled , Y_test ) )
# 제거된 특성
import numpy as np
zero_features = np.sum( lasso.coef_ == 0 )
print( " 기울기 0으로 제거된 특성 수 : " , zero_features )

# 다항에서는 StandardScaler() 표준화 필수
# 특성이 적으면(과소적합: 모델이 단순해짐) -> 항 추가( PolynomialFeatures ) / degree
# 특성이 많으면(과대적합: 모델 복잡도 올라감) -> 규제( L1라쏘 , L2릿지 ) / alpha