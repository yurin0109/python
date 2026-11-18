# 지도학습 : X특성(독립변수)과 Y타깃(종속변수) 모델에 학습 하여 예측 , 회귀 r2 , 분류 f1-score 평가지도
# 비지도학습 : X특성(독립) 모델 이용하여 거리/밀도 군집/클러스터/그룹 , 최적의 K 찾기( SSE , 실루엣 )

# 실습에 필요한 
import pandas as pd
url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
df = pd.read_csv(url, sep=';')

X = df[['studytime', 'absences', 'G1', 'G2', 'G3']] # 공부시간, 결석일수, 1학기 성적 ~ 3학기 성적
# 타깃/종속 없다. -> 비지도학습 이라서
from sklearn.model_selection import train_test_split # 학습 98% 검증용 2% ( 검증용 중요도 낮음 )
X_train, X_test = train_test_split(X, test_size=0.02, random_state=42)

# 1) 스케일링/단위 표준화 
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
X_train_scaled = ss.fit_transform( X_train ) # fit + transform -> fit_transform
X_test_sacled = ss.transform( X_test )
# 2) 군집 = 그룹만들기 = 클러스터 , K개의 군집을 찾는 Kmeans 모델
from sklearn.cluster import KMeans
model = KMeans( n_clusters= 3 ) # 모델 생성
model.fit( X_train_scaled ) # 군집 학습 
train_labels = model.predict( X_train_scaled ) # 군집 확인
print( ' 앞에서 10명 그룹 확인 : ' , train_labels[ :10] )
# 앞에서 10명 그룹 확인 :  [1 2 2 1 2 2 2 1 1 2] # 0 또는 1 또는 2 집합으로 클러스터링
print( ' 테스트 학생 : ' , model.predict( X_test_sacled ) )
#  테스트 학생 :  [1 2 0 1 1 2 2 1]