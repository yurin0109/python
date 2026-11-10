import joblib
# 1. 모델 불러오기 , joblib.load( '모델경로.pkl' )
model = joblib.load( './day14/fish_model.pkl' )
# 2. 불러온 모델로 예측 테스트
import pandas as pd # 임의의 특성 넣어서 예측 무게 찾기
sample = pd.DataFrame( { "Length2":[32] , 'Height':[10] , 'Width':[4] } )
predict = model.predict( sample )
print( '예측값/무게: ' , predict )
# 예측값/무게: [346.91669994]

