

# 예제] 동적 크롤링
# 1) 중고나라 홈페이지 제품 크롤링 , url = "https://web.joongna.com/search/"
async def run() : # 함수 정의
    ###########
    keyword = input( "중고 제품명 : " )
    min_price = input( "최소 가격: " )
    max_price = input( "최대 가격: " )

    # 2) async_playwright() 실행 하고 끝날 때까지 대기상태
    async with async_playwright() as p :
        # 3) 크로미움 실행
        brower = await p.chromium.launch( headless = False )
        # 4) 빈 페이지 열기
        page = await brower.new_page()
        # 5) 특정 페이지 이동
        await page.goto( f'https://web.joongna.com/search/{ keyword }' )
        # 6) 3초 대기상태
        await page.wait_for_timeout( 3000 )
        # 7) 입력받은 값으로 웹페이지 채우기
        # page.get_by_속성명( "속성값" )         # DOM.fill( 값 ) 
        # page.get_by_placeholder( "최소가격" ).fill() : placeholder에 '최소가격'이면 
        # 입력받은 값
        await page.get_by_placeholder( "최대가격" ).fill( max_price ) # html placeholder 이용하여
        await page.wait_for_timeout( 1000 ) # 1초간 일시정지

        # 8) 특정한 마크업 클릭 이벤트 실행 , Dom.colick()
        await page.get_by_text("적용").click() # 텍스트 '적용'갖고 있는 마크업 선택
        await page.wait_for_timeout( 3000 )
        # 9) 제품사진, 제품명, 제품가격 추출                                 


                                            
asyncio.run( run() ) # 함수 실행
