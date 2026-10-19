# 파이썬 파일 만들기
## 파일명 뒤에 확장자(.py) 만든다.
# 파이썬 한줄 주석
# 56p.
print("Hello World")
# shift + enter 한줄씩/문장 실행
# 파일내 오른쪽 클릭 -> run python -> 전체 실행

# 70p.
import keyword
print( keyword.kwlist )

# 77p. 출력하기
# 하나만 출력
print( "하나만 출력합니다." )
# 여러 개 출력 , 주의할 점 : 쉼표 기준으로 공백 자동 포함
print( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
print( 1,2,3 )
print( "안녕", "하세용" )
print() # 한줄 공백, 제어문자 \n


# 85p. 타입 확인하기 , type( 자료 )
print( type("안녕하세요") ) # <class 'str'>
print( type(123) )
print( type(1.23) )
print( type(True) )
print( type(None) )
print( type([]) )
print( type( {} ) )
print( type( () ) )

# 86p. 문자열 만들기
print( "ABC" ) # 큰 따옴표
print( 'abc' ) # 작은 따옴표
print( """abc """ ) # 줄 바꿈
print( " 'a', 'b', 'c' " ) # 작은 따옴표 출력
print( ' "a", "b", "c" ' ) # 큰 따옴표 출력 
# 큰 따옴표 안 큰 따옴표 출력은 안 됨, 작은 따옴표 안 작은 따옴표 출력도 x
# 이스케이프 문자를 사용하면 가능
# \""
print( )