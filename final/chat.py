from openai import OpenAI
from .credentials import OPENAI_API_KEY

musicTaste = "Describe what kind of person I am because all I listen to is Indie music"
botType = "A sarcastic, rude, and sassy close friend who is brief"

def get_chat_reply():

    client = OpenAI(
        api_key=OPENAI_API_KEY
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": botType},
            {"role": "user", "content": musicTaste}
        ]
    )
    chat_reply = response.choices[0].message.content
    return chat_reply
