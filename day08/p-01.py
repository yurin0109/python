# 판다스 : 데이터 조작 및 분석( 표 형태 ) 라이브러리
# 설치 : pip install pandas
# 호출/버전 확인

import pandas as pd
print(pd.__version__)


# 1] 데이터프레임: 2차원( 표 ) , pd.DataFrame( 리스트 , colums=[ '열이름' , '열이름' ] )
data_list = [ [ 'ant' , 25 , 'seoul'] ,
              ['bee' , 30 , 'busan'] ,
              ['cat' , 35 , 'incheon'] ] # 2차원 리스트 
x = pd.DataFrame( data_list )
print( x ) # 행 과 열 => 표 형식
x = pd.DataFrame( data_list , columns=[ 'name' , 'age' , 'city' ] )
print( x )
# 2] 데이터프레임2 , pd.DataFrame( 딕셔너리 ) , 키(열이름) 
data_dict = { 
                'name' : ['ant','bee','cat'] , 
                'age' : [25,30,35] , 
                'city' : ['seoul','busan','incheon'] } # 딕셔너리
df = pd.DataFrame( data_dict )
print( x )

# 3] 특정 컬럼 의 값들을 추출 , df['열 이름]
ages = df['age']
print( type(ages) ) # Series(1차원)
print( type(ages.values) )

# 4] 데이터프레임 : pd.DataFrame( 자료 , colums = [] , index = [] )
import numpy as np
data_np = np.array( data_list ) # 넘파이 자료
df = pd.DataFrame( data_np , columns= [ 'name' , 'age' , 'city' ] , index=[ 'A' , 'B' , 'C' ] )
print( df )

# RPA 업무자동화 교재
# RPA = 사무업무 자동화

# 5] 주요 속성
print( df.shape ) # 행/열 크기
print( df.colums ) # 컬럼 목록 Index([ 'name' , 'age' , 'city' ]), dtype='str'
print( df.index ) # 인덱스 목록 Index( ['A' , 'B' , 'C'], dtype='str' )
print( df.values ) # 값만 2차원 리스트로 추출
print( df.head( 2 ) ) # 상위 n개 만 반환
print( df.tail( 2 ) ) # 하위 n개 만 반환
df.info() # 컬럼 이름 , 결측치 , 타입 확인

# 6] 인덱싱 , df.iloc(인덱스) / df.loc[ 행라벨 , 열라벨 ]
print( df.iloc[ 1 ] ) # 1행
print( df.ilo[ 1 , 2 ] ) # busan 
print( df.loc[ 'B' ] )   # 1행 = B행
print( df.loc['B' , 'city'] ) # B행 city열 # busan

# 7] 슬라이싱, [시작인덱스:끝인덱스] , [ 행슬라이싱 , 열슬라이싱 ]
print( df.iloc[ 0:2 , 0:1 ] )
print( df.loc[ 'A' : 'C' , 'name' : 'age' ] )

# 8] 열 추가 , df[새로운열] = 새로운값
df['score'] = [ 100 , 80 , 95 ]
print( df )

# 9] 값 수정 , df[수정할열] = 새로운값
df[ 'age' ] =  [ 31 , 52 , 40 ]
print( df )
df.loc['B' , 'age'] = 70 # B행 age열
print( df )
df.iloc[ 0,0 ] + 'apple'
print( df )

# 10] 여러 개 수정 , [ [ 특정인덱스 , 특정인덱스 ] ]
df.loc[ ['A' ,'B'] , 'score' ] = [ 50 , 60 ]
print( df )

# 11] 필터링(조건)
print( df['score'] > 70 )
#A     False
#B     False
#C     True
print( df[ df['score'] > 70 ] )
#  name   age   city    scre
#C cat    40   incheon   95
cont = df['age'] >= 40
print( df[ (df['score'] > 70) & cont ] )
print( df[ (df['score'] > 70) | cont ] )
# 필터링 이용하여 새로운 열**
df['passed'] = False
df.loc[ df['score'] > 70 , 'passed' ] = True
print( df )
      












 