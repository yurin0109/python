'''
for i in numbers :
    if i % 2 == 0 :
        print( i,"는 짝수입니다" )
    elif  i % 2 == 1 :  
        print( i,"는 홀수입니다" )
'''

list_a = [ 273, 103, 5, 32, 65, 9, 72, 800, 99 ]
str( i )
len( str(i) )
for i in list_a :
    if len( str(i) ) > 0 :
        print( i,"는",len( str(i) ),"자릿수입니다.")

'''
# p.214 3번
list_a = [ 273, 103, 5, 32, 65, 9, 72, 800, 99 ]
str( i )
str( len(i) )
for i in list_a :
    if len(i) > 0 :
print( "{}는 {}자릿수입니다.".format(i, len(i) ) )
'''

# p.215
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(a) // 2):
    j = i**2
