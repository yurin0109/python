# if ~ else
# if 조건식 :
#   (tap 들여쓰기) 참이면
# else :
#   (tap 들여쓰기) 거짓이면
num = 13
if 11 < num < 15 :
    print ( "정답" )
else :
    print( "오답" )

# if ~ elif ~ elif ~ else :
point = 85
if point >= 90 :
    print( "A" )
elif point >= 80 :
    print( "B" )
elif point >= 70 :
    print( "C" )
else :
    print( "재시험" )

# 주의할 점 : if ~ if ~ else [vs] if ~ elif ~ elif ~ else
# 다수 조건에 다수 결과 vs 다수 조건에 따른 1개의 결과 (하나의 세트)
# 자바와 다르게 (조건식){} 없이 :콜론과 들여쓰기로 구분

# if중첩 가능
x = 10
if x > 5 :
    if x > 10 :
        print( "10보다 크다" )
    else :
        print( "5보다 크고 10보다 작거나 같다" )
else :
    print( "5보다 작거나 같다" )

# p.182 False 되는 경우
# None , 0 , 0.0 , 빈 문자열 , 빈 리스트 , 빈 객체 등
# 그 외 True