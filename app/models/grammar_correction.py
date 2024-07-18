from happytransformer import HappyTextToText, TTSettings
from fastapi.responses import JSONResponse

# HappyTextToText 모델 초기화
happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
args = TTSettings(num_beams=10, max_length=1000, min_length=1)

class GrammarCorrector:
    @staticmethod
    async def correct_text(text_data: str):
        try:
            # 문법 교정
            input_text = f"grammar: {text_data}"
            result = happy_tt.generate_text(input_text, args=args)

            return JSONResponse(content={
                "original_text": text_data,
                "corrected_text": result.text
            })
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": str(e)})

# 단일 인스턴스를 만들어 모듈 전역에서 사용할 수 있도록 합니다.
grammar_corrector = GrammarCorrector()
