import uvicorn, random, vk

from fastapi import FastAPI, Request, Response
from pydantic import BaseSettings

class Settings(BaseSettings):
    confirmation_string: str
    vk_token: str
    group_id: int
    class Config:
        env_file = ".env"

settings = Settings()

vk_session = vk.Session(access_token=settings.vk_token)
vk_api = vk.API(vk_session)

app = FastAPI()

def get_random_id(): return random.randint(0, 500000000000000000000000000)

def reply_to_message(message_text: str, vk_api, user_id: int):
    reply_list = {"привет": 'vk_api.messages.send(user_id = user_id, message = "И тебе привет", random_id = get_random_id(), v=5.131)',
        "как дела": '''vk_api.messages.send(user_id = user_id, message = "Хорошо", random_id = get_random_id(), v=5.131)
vk_api.messages.send(user_id = user_id, message = "Как у тебя?", random_id = get_random_id(), v=5.131)'''}
    if message_text in reply_list: exec(reply_list[message_text])

@app.post("/main")
async def authorize(req: Request):
    req_body = await req.json()
    if req_body['type'] == 'confirmation' and req_body['group_id'] == settings.group_id:
        return Response(content=settings.confirmation_string, media_type="application/json")
    elif req_body['type'] == 'message_new':
        reply_to_message(
            req_body['object']['message']['text'].lower(),
            vk_api, 
            req_body['object']['message']['from_id'])
        return Response('ok', media_type="application/json")
    else:
        return False

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True)