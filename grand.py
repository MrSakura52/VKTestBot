import random, json, main, db.database
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.database import get_response

def get_random_id(): return random.randint(0, 500000000000000000000000000)

async def reply_to_message(message_text: str, vk_api, user_id: int, session: AsyncSession):
    replies = await get_response(session, message_text.lower().capitalize())

    if len(replies) == 0: vk_api.messages.send(user_id = user_id, message = "Не понимаю вас", random_id = get_random_id(), v = 5.131)
    else:
        for reply in replies:
            reply_text = reply.answer
            vk_api.messages.send(
                user_id = user_id,
                message = reply_text,
                random_id = get_random_id(),
                v = 5.131
            )
async def add_phrase_command(message_text: str, vk_api, user_id: int, session: AsyncSession):
    phrase = message_text.split("/")[0]
    answer = message_text.split("/")[1]
    await db.database.add_phrase(session, phrase, answer)
    vk_api.messages.send(user_id = user_id, message = "Я вас запомнил!", random_id = get_random_id(), v = 5.131)
async def start(vk_api, user_id):
    message = "Привет, чтобы получать от меня уведомления выбери свою группу"
    keyboard = {
        "inline": True,
        "buttons": [
            [
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"friends"}',
                        "label": "Друзья"
                    },
                    "color": "primary"
                },
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"classmates"}',
                        "label": "Одноклассники"
                    },
                    "color": "secondary"
                },
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"programmers"}',
                        "label": "Программисты"
                    },
                    "color": "primary"
                }
            ]
        ]
    }
    vk_api.messages.send(
        user_id=user_id,
        message=message,
        keyboard=json.dumps(keyboard),
        random_id=get_random_id(),
        v=5.131
    )
async def add_to_group(vk_api, user_id: int, group_name: str, session: AsyncSession):
    if await db.database.create_group(session, int(user_id), group_name) == "Already exists":
        vk_api.messages.send(
        user_id=user_id,
        message=f"Теперь ты в группе {group_name}",
        random_id=get_random_id(),
        v=5.131
    )
    else:
        vk_api.messages.send(
            user_id=user_id,
            message=f"Теперь ты в группе {group_name}",
            random_id=get_random_id(),
            v=5.131
        )