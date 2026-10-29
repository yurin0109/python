# 맷플롯립: 파이썬에서 시각적으로 표현 하는 라이브러리
# 설치: pip install matplotlib
# 확인
import matplotlib.pyplot as plt
import matplotlib
print( matplotlib.__version__ )
import matplotlib.pyplot as plt

# 맷플롯립 그래프는 한글폰트 지원 안한다.
# #### 한글 폰트 설정 #### #
import matplotlib.pyplot as plt
plt.rc('font' , family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

# 1] 선 차트
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
train_loss = [0.9, 0.7, 0.55, 0.45, 0.38, 0.32, 0.28, 0.25, 0.23, 0.20]
val_loss = [0.95, 0.75, 0.60, 0.52, 0.48, 0.45, 0.44, 0.43, 0.44, 0.45]
# 1) 차트의 전체크기 설정 : plt.figure( figsize=(가로inch , 세로inch) )
plt.figure( figsize=( 7 , 4 ) )
# 2) 선차트 : plt.plot( x축값 , y축값 , label = "계열명" , color="색상명" ,  여기부턴 안 보임 )
plt.plot( epochs , train_loss , label="Train Loss" , color="blue" , linestyle = '-' , marker = 'o' )
plt.plot( epochs , val_loss , label="값 손실" , color="red" , linestyle = '--' , marker = 's' )
# 3. 차트의 제목
plt.title( "학습별 모델 손실 추세" ) # 3) 차트의 제목
plt.xlabel( "학습수" ) # 4) x축 제목
plt.ylabel( "손실" ) # 5) y축 제목
plt.grid( True ) # 6) 구분선
plt.legend() # 7) 범례 표시
# plt # 맷플롯립 별칭
plt.show() # 차트실행
 