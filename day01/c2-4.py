# p.135 , "문자열".format( 값 )        
string_a = "age:{}".format(10)
print( string_a ) # age:10
string_b = "{} {} {}".format( 1, "안녕" , True )
print( string_b )
# 주의할 점 : {} 개수와 값의 개수는 일치해야 함.
# p.137~ p.140 생략
a = "Hello"
print( a.upper() ) # 대문자 변환
print( a.lower() ) # 소문자 변환
# p.142 양쪽 여백/공백 제거
a = "                      Hello, World              "
print( a.strip() )
# p.143 , is000 구성 확인 , 반환타입 : True/False
print( "Hello".isalpha() )
print( "Hello".isdigit() )

# p.144 find() vs indexOf() ( 자바에서는 인덱스오브 ) , 없으면 -1 있으면 인덱스 반환
output_a = "안녕안녕하세요".find("안녕")
print(output_a)
output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
output_c = "안녕안녕안녕".find("안뇽")
print(output_c)

# p.145 , 찾을값 in "문자열" , 없으면 False 있으면 True
print( "Hi" in "안뇽" )
print( "안뇽" in "안뇽하세요" )  

# p.145 , "문자열".split( 기준문자 ) , 반환타입 : 리스트
a = "1 2 3 4 5".split(" ") # 공백/띄어쓰기 기준으로 자르기
print( a )
print( a[2] )

# p.146 , f-문자열 vs format 사용하는 이유
num = 10
a1 = "age:{}".format( num+1 )    # 숫자 10 , 변수 호출 o 
a2 = f"age:{ num+1 }"            # 숫자 10 , 변수 호출 o
a3 = "age:num+1"                 # 문자열 10 , 변수호출 x
print(a1, a2, a3)