# p.251
numbers = [ 103, 52, 273, 32, 77 ]
print( min( numbers ) ) # min( 리스트 ) 최솟값
print( max( numbers ) ) # max( 리스트 ) 최댓값
print( sum( numbers ) ) # sum( 리스트 ) 합계
# p.252 revered
numbers_reveved = reversed( numbers ) # 리스트 뒤집기
print( next( numbers_reveved ) )
print( list( numbers_reveved ) ) 
# int() float() str() list() : 특정 타입으로 변환 함수

# 이터러블 : 요소들을 하나씩 차례로 꺼내기 가능한 객체 의미
# 이터레이터 : 이터러블 중에서 하나씩 차례로 빼낼 수 있는 요소
# 이터레이터 가능한 타입 : 리스트 / 딕셔너리 / 문자열 / 튜플 등
# 이터레이터 하나씩 꺼내는 함수 = next() 함수 ----> 이터러블
# 즉] 이터레이터가 존재하는 자료만 for문 사용 가능!

# p.254 enumerate [ (인덱스,값) , (인덱스,값) ]
numbers = [ 103, 52, 273, 32, 77 ]
print( enumerate( numbers ) )
print( list ( enumerate( numbers ) ) )
for index , value in enumerate( numbers ) :
    print( index , value )

# p.256 itmes( 딕셔너리 ) , [ (key , value) , (key , value) ]
dict_a = { "name" : "유린" , "age" : "24" }
for key , value in dict_a.items() :
    print( key , value )


# p. 258 리스트 내포 , 인덱스 자리에 반복문 사용 가능
# 0부터 20까지 2씩 증가한 자료들을 리스트에 저장
# 방법1]
array = []
for i in range( 0 , 21 , 2 ) :
    array.append( i )
# 방법2] 리스트변수 = [ 값 for 반복변수 in range() ]
array = [ i for i in range( 0 , 21 , 2 ) ]
# 활용 : 10 제외한  리스트변수 = [ 값 for 반복변수 in range() if 조건식 ]
array = [
    i
    for i in range( 0 , 21 , 2 )
    if i != 10
    ]

# p.263 , .join( )
# 방법1]
print( """ 안녕하세요
 안녕하세요 """ )
# 방법2] \n 제어문자
print( "안녕하세요1\n안녕하세요2" )
# 방법3] ( "문자열" "문자열" "문자열" ) # 튜플 차이
print( ("안녕하세요1\n" "안녕하세요2") )
# 방법4] 특정문자열.join( 리스트 ) , 리스트 요소 사이마다 특정 문자열 삽입
print( "\n".join( ["안녕하세요1" , "안녕하세요2"] ) )
print( "-".join( "대한민국" ) ) # 대-한-민-국