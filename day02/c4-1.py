# p.192
# 파이썬 특징 : 정형화된 데이터들의 연산이 가능함
# 리스트란? 대괄호[]에 자료를 쉼표로 구분하여 여러 자료들을 저장
# [ 요소, 요소, 요소 ] , 요소 = element
# 인덱스란? 리스트 내 요소들이 저장된 순서 번호 , 0번 시작~

# 리스트 
yuring = [ 3 , 4 , 333434 , 200 , True , "ㅎㅎ" ] # 리스트 선언
yuring[-1] = "집 가고 싶다"
print( yuring[:3] )
# 파이썬에서는 인덱싱 음수로 가능
# 인덱싱/슬라이싱은 파이썬만 가진 특징
print( yuring[0][0] ) # 문자열도 리스트/배열
print( [2][0] ) # 오류 # 문자만 가능
list_1 = [ 1 , 2 , 3 ] # 1차원
list_2 = [ [ 1 , 2] , [ 3 , 4 ] , [ 5 , 6 ] ] # 2차원
list_3 = [ [ [ 1 , 2] , [ 3 , 4 ] ] , [ 5 , 6 ] ] # 3차원
print( list_2[1][0] ) #[행][열] => 판다스/데이터프레임

# p.196 +연결 , *반복 , len()길이
list_a = [ 1 , 2 , 3 ]
list_b = [ 4 , 5 , 6 ]
print( list_a + list_b ) # 1차원 배열로 나열 # 리스트 + 리스트 => 연결
print( list_a * 3 )
print( len(list_a) )
list_aa = [ [1] , [2] , [3] ]
print( list_a + list_aa ) # 차원이 다른 리스트를 합칠 때 리스트 안 내용물들 나열한다고 생각하면 됨
list_a.append( 4 ) # 요소 추가
print(list_a) # [ 1 , 2 , 3 , 4 ]
list_a.insert( 0 , 5 ) # ( 위치 , 값 ) # 특정 인덱스 요소 삽입
print( list_a ) # [ 5 , 1 , 2 , 3 , 4 ]
# 주의할 점
list_c = [ 1 , 2 ]
list_c + [3] # 새로운 리스트 생성 ,  ( list_c 변화 없다 ) , 비파괴적 
list_c.append(3) # 기존 리스트 추가 , ( list_c 변화 있다 ) , 파괴적 : 원본을 바꾸면


# p.202 요소 삭제하기 , del 리스트명[인덱스] , 리스트명.pop( 인덱스 )
list_a = [ 1 , 2 , 3 , 4 , 5 ]
del list_a[1] # 1번 인덱스 삭제
print( list_a ) # [ 1 , 3 , 4 , 5 ]
list_a.pop( 2 ) # 2번 인덱스 삭제
del list_a[ 0:2 ] # del 키워드 이용한 슬라이싱 삭제
print( list_a ) # [5]
# 리스트명.remove( 값 )
list_a.remove( 5 ) # 값 삭제
print( list_a ) # []
# 리스트명.clear() : 전체 삭제
list_a.clear()
# p.204 슬라이싱 , [ 시작인덱스 : 끝인덱스 : 단계 ]
list_u = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]
print( list_u[ 0 : 6 : 2  ] ) # 0번부터 5번까지 2씩 증가
print( list_u[ : : -1 ] ) # 시작인덱스 생략 시 0 , 끝 인덱스 생략 시 마지막 인덱스 

# p.205 정렬 , 리스트명.sort() , 리스트명.sort( reverse = True )
list_u = [ 52, 333 , 12 , 4 , 0 , 434 ]
list_u.sort()
print(list_u)
list_u.sort( reverse=True )
print(list_u)

# p.206 내부 확인 , 찾을값 in 리스트
print( 4 in list_u )
print( -1 in list_u )
print( 4 not in list_u )
print( -1 not in list_u )

# p.208 리스트와 반복문 , 리스트 내 요소들이 순차적인 인덱스 구조
# for 반복변수 in 반복 가능한 자료 :    
#   실행 코드
for element in list_u :
    print( element )
for char in "안녕하세요" : # 문자열도 리스트/배열이다.
    print( char )


list = [ 2,34,6,1 ]
for i in list :
    print( i )


# 전개 연산자 , 리스트명 앞에 * 붙인다
print( *list_u )

