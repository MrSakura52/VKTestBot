import uvicorn, vk, grand

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

@app.post("/main")
async def authorize(req: Request):
    req_body = await req.json()
    if req_body['type'] == 'confirmation' and req_body['group_id'] == settings.group_id:
        return Response(content=settings.confirmation_string, media_type="application/json")
    elif req_body['type'] == 'message_new':
        grand.reply_to_message(
            req_body['object']['message']['text'].lower(),
            vk_api, 
            req_body['object']['message']['from_id'])
        return Response('ok', media_type="application/json")
    else:
        return False

if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True)