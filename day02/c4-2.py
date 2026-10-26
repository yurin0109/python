# p.127 딕셔너리
# 딕셔너리란? {} 중괄호 선언하고 키:값 형태로 쉼표로 연결
# { key:value , key:value , key:value }
# key 중복 x , value 중복 o
# JS/JSON , JAVA:MAP/DTO , DB:RECORD

# 1. 선언 
dic_a = { 'name' : '어벤져스 엔드게임' , 'type' : '히어로 무비' }
# 2. 속성값 호출 , 딕셔너리명['key']
print( dic_a['name'] )
print( dic_a['type'] )
# 3. 속성값 추가 , 딕셔너리명['새로운 키'] = 새로운 값
dic_a[ 'price' ] = 5000
print( dic_a )
# 4. 속성값 수정
dic_a['type'] = '호러 무비' # 이미 존재하는 키는 값 수정
print( dic_a )
# 5. 속성값 삭제 , del 딕셔너리[ 'key' ]
del dic_a[ 'price' ]
print( dic_a )
# 6. 딕셔너리 내부 확인 , 찾을키 in 딕셔너리명
print( 'price' in dic_a ) # False
print( 'name' in dic_a ) # True
# 7. 속성값 호출 , 방법1 : 딕셔너리명['key'] , 방법2 : 딕셔너리명.get(key)
# 반환 차이 : 방법1은 존재하지 않으면 예외 발생 , 방법2는 존재하지 않으면 None 반환
print( dic_a['hehe'] )
print( dic_a.get( 'hehe' ) ) # None


# 8. for 반복문 과 딕셔너리 , 딕셔너리 내 key 하나씩 for에서 순회
# for key반복변수 in 딕셔너리명 :
#    실행코드
for key in dic_a :
    print( dic_a.get(key) ) #방법1
    print( dic_a[key] ) #방법2


