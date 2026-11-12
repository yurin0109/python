
#[1] 라우터: 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter
# router = APIRouter( prefix="공통URL" )
router = APIRouter( prefix="/api" )

# [3] 다양한 REST API CRUD 
# 서비스 객체 불러오기 # from 파일명 import 변수명/함수명
from Service import item_service
# 1) 전체 조회
# http://127.0.0.1:8000/api/items
@router.get("/items")
async def items():
    # 서비스 내 함수 호출
    return item_service.items()
# 2) 저장
# http://127.0.0.1:8000/api/save
# { "id":3 , "name":"레몬에이드" , "price":6000 }
@router.post("/save")
async def save( item:dict ):
    return item_service.save( item )
# 3) 수정
# http://127.0.0.1:8000/api/update
# { "id":3 , "name":"레몬에이드" , "price":10000 }
@router.put( "/update")
async def update( item:dict ):
    return item_service.update( item )
# 4) 삭제
@router.delete("/delete")
async def delete( id:int ):
    return item_service.delete( id )