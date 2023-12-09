from openai import OpenAI
from credentials import OPENAI_API_KEY


def get_chat_reply(genre):
    musicTaste = f"Describe what kind of person I am because all I listen to is {genre} music"
    botType = "A sarcastic, rude, and sassy close friend who is brief"
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
