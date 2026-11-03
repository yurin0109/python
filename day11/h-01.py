# httpx 란? 외부 api 통신하는 라이브러리 , API연동 / SPRING API 
# 설치1 : pip install httpx
# httpx 라이브러리 에는 .json() 타입변환 하지만 xml 변환 지원하지 않는다.
# xmltodict 란? xml 파싱 라이브러리
# 설치2 : pip install xmltodict 

import httpx
import pandas as pd
# 0] 공공데이터포털 본인 인증키
service_key = "98a696256251088d83e53fb49fd23cb19d1a271aced6b6d99238801b125fe2fe"

# 1] 공공데이터포털 json 형식의 자료 요청
def test1() :
    # 2] 신청한 API 의 주소 및 파라미터 분석 , page 현재페이지 , perPage 페이지당자료수 , serviceKey
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url += "?page=1"
    url += "&perPage=147"
    url += f"&serviceKey={service_key}"
    # 3] httpx 이용하여 통신하기 , import httpx
    # httpx.HTTP메소드명( 통신할주소 ) , 통신 결과 반환 
    response = httpx.get( url )
    print( response ) # <Response [200 OK]> 성공 했다는 뜻
    # 4] 응답 결과 JSON 파싱
    response_json = response.json() # print( response_json )
    # 5] 판다스에 저장하기
    df = pd.DataFrame( response_json['data'] ) 
    df.info() # 확인 

test1()

