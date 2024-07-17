# app/routes/items.py

from fastapi import APIRouter, HTTPException, File, UploadFile
from app.models.item import Item
from app.models.grammar_correction import grammar_corrector

router = APIRouter()

# 예시 데이터
fake_items_db = [
    {"name": "Item1", "price": 100.0},
    {"name": "Item2", "price": 50.0},
]

@router.get("/items/")
async def read_items():
    return fake_items_db

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id >= len(fake_items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_items_db[item_id]

@router.post("/items/")
async def create_item(item: Item):
    fake_items_db.append(item.dict())
    return {"message": "Item created successfully"}

@router.post("/correct_grammar")
async def correct_grammar(file: UploadFile = File(...)):
    try:
        corrected_text = await grammar_corrector.correct_text(file)
        return {corrected_text.body}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))