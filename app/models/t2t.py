import os
from transformers import T5Tokenizer, T5ForConditionalGeneration

# 환경 변수 설정
os.environ["TOKENIZERS_PARALLELISM"] = "false"

class T2T:
    @staticmethod
    async def generate_code(text_data):

        # Hugging Face 모델과 토큰 불러오기
        tokenizer = T5Tokenizer.from_pretrained("t5-base")
        model = T5ForConditionalGeneration.from_pretrained("t5-base")

        questions = [line.strip() for line in text_data.split("\n")]

        results = []
        for question in questions:
            inputs = tokenizer(question, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
            summary_ids = model.generate(**inputs)
            summary = tokenizer.decode(summary_ids.squeeze(), skip_special_tokens=True)
            results.append(summary)

        python_code = "".join(results)
        return {"result": python_code}
    

t2t = T2T()