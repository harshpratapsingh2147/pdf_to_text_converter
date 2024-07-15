import requests
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')
MODEL = config('MODEL')


class GPTManager:
    """GPT call manager"""

    def __init__(self, system_prompt):
        self.model = MODEL
        self.system_prompt = system_prompt
        self.api_key = OPENAI_API_KEY

    def image_to_text(self, image):
        try:
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }

            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": self.system_prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image}"
                                }
                            }
                        ]
                    }
                ],
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
            return response.json()
        except Exception as err:
            print(err)