import os
from openai import OpenAI
#from .config import Config

class OpenAIService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("SECRET_KEY"))

    def get_response(self, message):
        try:
            message_end = "\nтвоя відповідь має бути результатами пошуку, збери у json. схема об'єкту має бути наступною - назва (оригінал + переклад) (title), рік виходу (year), оцінки imdb (rate), режисер (director), головні актори (actors), опис (description). якщо ти нічого не знайдеш, поверни пустий масив."
            message = message + message_end

            response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ],
            response_format={
                "type": "text"
            },
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

            return response
        except Exception as e:
            return {"error": str(e)}