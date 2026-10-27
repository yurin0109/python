import numpy as np
# [기본 제공 코드] CSV 파일 로드 (헤더 제외, 콤마 구분)
data = np.genfromtxt('./day07/report.csv', delimiter=',', skip_header=1)
# 데이터 구조 확인: [ID, Visits, Stay_Time, Cart_Items, Purchase_Amount]
print(f"데이터 형태: {data.shape}")

print( data.shape )

type( data )

print( ~np.isnan(data) )

data16 = ~np.isnan(data)[:,4]
print(data16)

data_without_nan16 = data[data16]
print(data_without_nan16)
print(data_without_nan16[:,4])

data_16 = data_without_nan16[6:,4]
print(len(data_16))

avg_16 = np.mean(data_16)
print(avg_16)
max_16 = np.max(data_16)
print(max_16)



dan = data_without_nan16[ ( data_without_nan16[:,4] < 65 ) | ( data_without_nan16[:,4] > 95 ) ]
print(dan)
print( len(dan) )



data16 = ~np.isnan(data)[:,4]
data17 = ~np.isnan(data)[:,5]
data1617 = ( data16 == True ) & ( data17 == True )
print(data1617)

data_without_nan1617 = data[data1617]
print(data_without_nan1617)

dangerous = data_without_nan1617[:,5] - data_without_nan1617[:,4]
print(dangerous)
print( np.min(dangerous))
print( np.argmin(dangerous) )
print( data_without_nan1617[np.argmin(dangerous)] )
print( data_without_nan1617[np.argmin(dangerous)][0] )

# abs_dangerous = np.abs(dangerous)
# print(abs_dangerous)
# print( np.argmax(abs_dangerous) )
# print( data_without_nan1617[np.argmax(abs_dangerous)] )
# print( data_without_nan1617[np.argmax(abs_dangerous)][0] )

high_risk = ( data_without_nan1617[:,4] < np.mean(data_without_nan1617[:,4]) - 15 ) & ( data_without_nan1617[:,5] < np.mean(data_without_nan1617[:,5]) - 15 )
print( high_risk )
print( data_without_nan1617[high_risk] )
print( len(data_without_nan1617[high_risk])/len(data_without_nan1617)*100 , "%" )



# 공식 : ( x - 최솟값 ) / ( 최댓값 - 최솟값 )

정규화 = ( dangerous - np.min( dangerous ) ) / ( np.max( dangerous ) - np.min(dangerous) )
print(정규화)
print(정규화 < 0.1)
print(data_without_nan1617[정규화 < 0.1])
print(len(data_without_nan1617[정규화 < 0.1]))

