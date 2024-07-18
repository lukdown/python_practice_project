# app/routes/items.py

from fastapi import APIRouter, File, UploadFile, HTTPException
from app.models.grammar_correction import grammar_corrector
from app.models.t2t import t2t

router = APIRouter()

@router.post("/correct_grammar")
async def correct_grammar(file: UploadFile = File(...)):
    try:
        corrected_text = await grammar_corrector.correct_text(file)
        return {corrected_text.body}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/t2t")
async def t2t_endpoint(file: UploadFile = File(...)):
    try:
        # 텍스트 파일 비동기적으로 읽기
        text_data = (await file.read()).decode("utf-8").strip()

        # t2t.generate_code 호출
        result = await t2t.generate_code(text_data)

        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))