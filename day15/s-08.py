# 범주형(문자) 특성 갖는 학습 방법
# 1) 실습에 필요한 펭귄 계측 데이터
import seaborn as sns
df = sns.load_dataset('penguins')
# 2) 전처리 : 결측 행 제외
df = df.dropna().reset_index( drop=True )
df.info()
# 3) 다중분류 실습 위한 특성/(다중)타깃 구성
X = df.drop( columns=['species'] ) # 펭귄 종 제외한 나머지 특성
Y = df['species']
# 4) 분리
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size=0.2, random_state=42, stratify=Y )
# 5) 복합형 파이프라인 위한 수치형 과 범주형 특성 분리
num_features = ['bill_length_mm' , 'bill_depth_mm' , 'flipper_length_mm' , 'body_mass_g']
cat_features = ['island' , 'sex']
# 6) 복합 특성
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler , OneHotEncoder
# ColumnTransformer( transformers=[ ( '식별자' , 변환기() , 컬럼명목록 ) ] )
# OneHotEncoder: 범주형 자료들을 0 과 1 표현
#   drop='first' : 첫번째 범주에 대한 카테고리는 제외,
# 0 1 0
# 0 0 1
# 0 0 0 # 모두 0으로 채워진 행이면 첫번째 범주 로 의미 가짐.
# sparse_output=False : 변환된 자료들을 numpy 배열로 반환
pp = ColumnTransformer( transformers=[ 
    ('num' , StandardScaler(), num_features), # 수치형 특성
    ('cat' , OneHotEncoder( drop='first' , sparse_output=False), cat_features ) # 범주형 특성
] )
# 파이프라인 만들기
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
# pipe = Pipeline( [ ( '식별자' , 변환기/추정기 ) ] ) 
pipe = Pipeline( [ ('pp' , pp) , ('model' , LogisticRegression() ) ] )
pipe.fit( X_train , Y_train ) # 학습하기
Y_pred = pipe.predict( X_test ) # 테스트 예측
print( Y_pred[:3] ) # ['Gentoo' 'Chinstrap' 'Adelie'] 
# 리포트( 모델 평가지표 )
from sklearn.metrics import f1_score
print( f1_score( Y_test , Y_pred , average='macro' ) )