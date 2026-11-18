



# 7) 이상치 제외한 G3 평균 계산 
normal_clusters = X_train[ X_train['PCA_cluster'] != -1 ] # 이상치 제외 
# pd.groupby('성별')['국어점수'].mean() : 성별/열 그룹/끼리 국어점수/특정 열에 평균
cluster_means = normal_clusters.groupby

print( sorted _ )

# 8) 라벨링
# enumerate() # range()
lebels = {}
for idx , cluter_id in enumerate( sorted_cluster.index , start=1 ) :
    labels[ cluter_id ] = f'Level{idx}'
labels[-1] = 'Outlier' # 이상치는 리스트 가장 뒤에 
print( labels )
X_train['pca_cluster_label'] = X_train['PCA_cluster'].replace( labels )
print( X_train ) # 군집화한 결과 가지고 추후에 지도학습
# 지도학습에서 성능 향상 하기 위한 방법 : 0) 전처리 1) 하이퍼파라미터 2) 파생변수


# 9) 시각화
for lbl in list( labels.values() ) :
    sub = X_train[ X_train['pca_cluster_label'] == lbl ]
    if lbl == 'Outlier' :
        plt.scatter( sub['PC1'] , sub['PC2'] , c='red' , marker='*' , label=lbl )
    else :
        plt.scatter( sub['PC1'] , sub['PC2'] , marker='o' )

plt.legend()
plt.show()
# PCA 시각화 하게 되면 특성들을 2가지(CD) 형태 표현 가능하다.
# 현재 주성분 PC1( G1 G2 G3 ) , PC2( 공부시간 , 결석일수 )