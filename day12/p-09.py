# Practice1
# 1. 데이터 준비
#  - Seaborn 내장 데이터셋인 'tips'를 불러옵니다.
import seaborn as sns
import pandas as pd
df = sns.load_dataset('tips')
df.info()

feature = ['total_bill']   # 특성: 식사 총액 ($) # 2차원으로 추출하기 위해 리스트로 감싼다
target = 'tip'             # 타깃: 팁 ($)
X = df[feature]  # 2차원 (DataFrame)
Y = df[target]   # 1차원 (Series)
#  - 독립변수(X, 문제지): 식사 총액 'total_bill' 컬럼 (2차원)
#  - 종속변수(Y, 정답지): 팁 'tip' 컬럼 (1차원)

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 )

# 3. 모델 학습 및 수학적 파라미터 확인 
#  - Scikit-learn의 LinearRegression 모델을 생성하고 훈련 데이터로 학습시킵니다.
#  - 학습 완료 후 모델이 도출한 '기울기'와 'y절편'을 출력하세요.
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit( X_train , Y_train )
print( "기울기(coef_):" , model.coef_ )         # 식사 총액이 $1 늘 때 팁이 늘어나는 양
print( "y절편(intercept_):" , model.intercept_ ) # 식사 총액이 $0일 때의 팁 (이론상 값)

# 4. 성능 평가 및 신규 데이터 예측
#  - 테스트 세트(X_test)에 대한 예측값(Y_pred)을 생성하세요.
#  - 실제값(Y_test)과 예측값(Y_pred)을 비교하여 R²(결정계수)와 RMSE(평균 제곱근 오차)를 산출하고 소수점 둘째 자리까지 출력하세요.
#  - 만약 식사 총액이 $30, $100인 새로운 손님이 방문했을 때, 예상되는 팁 금액을 각각 예측하여 출력하세요.
Y_pred = model.predict( X_test )  # 테스트용 특성으로 예측

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
r2 = r2_score( Y_test , Y_pred )
rmse = np.sqrt( mean_squared_error( Y_test , Y_pred ) )
print( f"R2: {r2:.2f}" )      # 소수점 둘째 자리
print( f"RMSE: {rmse:.2f}" )  # 단위는 타깃과 같은 $
 
# 새로운 손님 예측 ( 학습 때와 같은 컬럼명을 가진 DataFrame으로 넣으면 경고가 안 뜬다 )
new_bill = pd.DataFrame( [[30] , [100]] , columns=feature )
new_tip = model.predict( new_bill )
print( f"식사 총액 $30 -> 예상 팁: ${new_tip[0]:.2f}" )
print( f"식사 총액 $100 -> 예상 팁: ${new_tip[1]:.2f}" )

# 5. 결과 시각화 및 한계점 분석 
#  - Matplotlib을 활용하여 아래 3가지 요소를 하나의 차트에 시각화하세요:
#  1. 테스트 세트의 실제 데이터 산점도 (X_test vs Y_test)
#  2. 식사비 $5부터 $100까지 모델이 예측한 선형 회귀선
#  3. 식사비 $50일 때의 모델 예측 지점 (붉은 점으로 강조)
import matplotlib.pyplot as plt
 
# 1) 테스트 세트 실제 데이터 산점도
plt.scatter( X_test , Y_test , label="Actual (test set)" )
 
# 2) $5 ~ $100 선형 회귀선
line_x = pd.DataFrame( [[5] , [100]] , columns=feature )
plt.plot( line_x['total_bill'] , model.predict( line_x ) , label="Regression line" )
 
# 3) $50일 때 예측 지점 (붉은 점)
point_x = pd.DataFrame( [[50]] , columns=feature )
plt.scatter( [50] , model.predict( point_x ) , color="red" , s=80 , label="Prediction at $50" )
 
plt.xlabel( "total_bill ($)" )
plt.ylabel( "tip ($)" )
plt.title( "Tip prediction by total bill" )
plt.legend()
plt.show()  # 그래프 창을 닫을 때까지 대기하므로 맨 끝에 둔다
 
# 한계점 분석
# 1) 팁은 식사 총액 외에도 인원수(size), 요일(day), 시간대(time), 흡연 여부 등의 영향을 받는데
#    특성을 total_bill 하나만 써서 설명력이 제한된다. -> 다중 회귀로 특성을 추가해 볼 수 있다.
# 2) 원본 데이터의 식사 총액은 약 $3 ~ $51 범위라서 $100 예측은 학습 범위 밖의 외삽이다.
#    직선이 그대로 이어진다고 가정한 값이므로 신뢰도가 낮다.
# 3) 금액이 커질수록 팁의 편차도 커지는데(점들이 오른쪽으로 갈수록 넓게 퍼짐),
#    선형 회귀는 오차가 고르게 퍼져 있다고 가정하므로 큰 금액 구간의 예측 오차가 커진다.