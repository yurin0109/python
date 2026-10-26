import numpy as np
# 1] 배열의 인덱싱
x = np.array( [10,20,30,40,50] )
print( x[0] )
print( x[-2] )
print( x[ [0 , 2 ]]  ) # [ [특정인덱스 , 특정인덱스] ]
print( x[ x > 20] )    # [ 논리조건 ] # [ 30 40 50 ]

# 2] 2차원 인덱싱
x = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
print( x[0,0] )
print( x[1,2] )
print( x[ -1 , -1 ] )
print( x[ x>5 ] )

# 3] 슬라이싱 . [ 시작인덱스 : 끝인덱스-1 : 단계 ]
x = np.array( [10,20,30,40,50] )
print( x[ 1 : 4] )
print( x[ :3] )
print( x[ -3: ] )
print( x[ : : 2 ] )

# 4] 
x = np.array( [ [1,2,3] , [4,5,6] , [7,8,9] ] )
# print( x[ 행슬라이싱 , 열슬라이싱 ])
print( x[ : , 1] ) # 행:전체 , 열:1 
print( x[ 1 , : ] )
print( x[ 0:2 , 1:3 ])

# 5] 슬라이싱 주의할 점 : 
x = np.array( [10,20,30,40,50] )
y = x[ 1:4 ] # [20,30,40]
y[0] = 100
print( x )
y2 = x[ 1:4 ].copy() # 슬라이싱 에서 비파괴로 하고 싶으면 .copy() 하면 됨
y2[0] = 1000
print( x ) 
# 6] 배열의 연산 
x = np.array( [1,2,3] )
y = np.array( [4,5,6] )
print( x + y ) # 같은 위치끼리 더함
print( x * y )
print( x**2 )
print( x - 2 )
print( np.sqrt( x ) ) # 제곱근
print( x > 2 )
print( (x>1) & (x<3) ) # (조건1) & (조건2) , AND
print( ( x==1 ) | ( x==3 ) ) # (조건1) | (조건2) , OR 
print( x > y ) # 같은 위치끼리 비교연산 # [False False False]

# 배열 간 비교/연산 : 같은 위치끼리 연산/비교
# 배열 와 스칼라(단일 숫자) 비교/연산 : 스칼라와 연산/비교 결과


