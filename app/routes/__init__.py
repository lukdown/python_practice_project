# /app/routes/__init__.py

# 예시: items 라우터를 현재 패키지에 포함시킵니다.
# from . import items
from .items import router as items_router
# 이곳에 필요한 초기화 코드를 추가할 수 있습니다.
