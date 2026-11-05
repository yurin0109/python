# PythonML Practice 2: 다항 규제 회귀 기반 성적 예측
# 데이터 출처: https://www.kaggle.com/datasets/shambhurajejagadale/student-performance-prediction-dataset
# 1. 데이터 준비 및 전처리
#  - Kaggle 데이터셋을 불러옵니다.
#    import pandas as pd
#    df = pd.read_csv('./student_dataset_10000_rows.csv')
#  - 범주형 변수를 제외한 6개 수치형 컬럼을 독립변수(X, 문제지)로 추출하세요:
#    ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']
#  - 시험 성적인 'exam_score' 컬럼을 종속변수(Y, 정답지)로 설정하세요.
import pandas as pd
df = pd.read_csv('./day13/student_dataset_10000_rows.csv')
df.info()
 
feature = ['study_hours', 'attendance', 'sleep_hours', 'internet_usage', 'assignments_completed', 'previous_score']
target = 'exam_score'
X = df[feature]  # 2차원 (범주형 placement_status 제외한 수치형 6개)
Y = df[target]   # 1차원

# 2. 데이터 분할
#  - train_test_split을 사용하여 훈련 세트(80%)와 테스트 세트(20%)로 분할하세요.
#  - 재현성을 위해 random_state=42로 고정합니다.
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size=0.2 , random_state=42 )
 
# 3. 다항 특성 확장 및 표준화 (고정 차수: degree=2)
#  - PolynomialFeatures(degree=2, include_bias=False)를 사용하여 2차 다항 특성을 생성하세요.
#    * 훈련 세트(X_train)로만 .fit()을 수행하고, X_train과 X_test를 각각 .transform() 하세요.
#  - StandardScaler를 생성하고, 다항 확장된 훈련 세트(X_train_poly) 기준으로 .fit()한 뒤 표준 점수로 변환하세요.
#    * 특성 간 스케일 차이를 맞추기 위해 훈련 세트와 테스트 세트 모두 .transform() 하세요.
# 3-1) 다항 특성: 훈련 세트로만 fit, 훈련/테스트 모두 transform
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
poly = PolynomialFeatures( degree=2 , include_bias=False )
poly.fit( X_train )
X_train_poly = poly.transform( X_train )
X_test_poly = poly.transform( X_test )
print( "다항 확장 후 특성 개수:" , X_train_poly.shape[1] )  # 6개 -> 27개 ( 원본 6 + 제곱 6 + 교차곱 15 )
 
# 3-2) 표준화: 다항 확장된 훈련 세트로만 fit, 훈련/테스트 모두 transform
scaler = StandardScaler()
scaler.fit( X_train_poly )
X_train_scaled = scaler.transform( X_train_poly )
X_test_scaled = scaler.transform( X_test_poly )
# 왜 훈련 세트로만 fit? 테스트 세트의 정보(평균/표준편차)가 학습에 섞이지 않게 하기 위해서 ( 데이터 누수 방지 )
 
# 4. 3가지 모델 학습 및 결정계수(R²) 비교 (고정 규제: alpha=1.0)
#  - 3가지 회귀 모델을 각각 생성하고 스케일링된 훈련 데이터로 학습시키세요:
#    1) LinearRegression()
#    2) Ridge(alpha=1.0, random_state=42)
#    3) Lasso(alpha=1.0, random_state=42)
#  - 각 모델별 훈련 세트 R² 점수(Train R²)와 테스트 세트 R² 점수(Test R²)를 각각 산출하여 비교 출력하세요.
from sklearn.linear_model import LinearRegression, Ridge, Lasso
models = {
    'LinearRegression' : LinearRegression(),
    'Ridge' : Ridge( alpha=1.0 , random_state=42 ),
    'Lasso' : Lasso( alpha=1.0 , random_state=42 ),
}
 
print( "\n[ 모델별 R² 비교 ]" )
for name, model in models.items():
    model.fit( X_train_scaled , Y_train )
    train_r2 = model.score( X_train_scaled , Y_train )  # score() = r2_score
    test_r2 = model.score( X_test_scaled , Y_test )
    print( f"{name:<17} Train R²: {train_r2:.4f} | Test R²: {test_r2:.4f}" )
 
# 5. 임의 대조군 데이터에 대한 3가지 모델 예측 비교
#  - 아래 대조군 샘플 2개를 준비하세요:
#    * 샘플 1 (상위권): study_hours=9, attendance=95, sleep_hours=7, internet_usage=2, assignments_completed=18, previous_score=85
#    * 샘플 2 (하위권): study_hours=2, attendance=60, sleep_hours=5, internet_usage=9, assignments_completed=4, previous_score=50
#  - 각 샘플 데이터를 앞서 학습시킨 동일한 변환기(PolynomialFeatures, StandardScaler)로 변환하세요.
#  - 3가지 모델(LinearRegression, Ridge, Lasso)에 변환된 데이터를 각각 대입하여 예상 시험 성적을 산출하고 비교 출력하세요.
sample = pd.DataFrame( [
    [ 9 , 95 , 7 , 2 , 18 , 85 ],  # 샘플 1 (상위권)
    [ 2 , 60 , 5 , 9 , 4 , 50 ],   # 샘플 2 (하위권)
] , columns=feature )
 
# 학습에 쓴 것과 동일한 변환기로 transform만 한다 ( 다시 fit 하면 안 됨 )
sample_poly = poly.transform( sample )
sample_scaled = scaler.transform( sample_poly )
 
print( "\n[ 대조군 예상 시험 성적 ]" )
for name, model in models.items():
    pred = model.predict( sample_scaled )
    print( f"{name:<17} 샘플1(상위권): {pred[0]:.2f} | 샘플2(하위권): {pred[1]:.2f}" )
 
# 해석 포인트
# - Train R²와 Test R²의 차이가 크면 과대적합, 둘 다 낮으면 과소적합
# - Ridge: 가중치를 작게 만들어 과대적합을 줄인다 ( 가중치가 0이 되지는 않음 )
# - Lasso: 불필요한 특성의 가중치를 0으로 만든다 ( 특성 선택 효과 )
# - Lasso가 0으로 만든 특성 개수 확인: ( models['Lasso'].coef_ == 0 ).sum()