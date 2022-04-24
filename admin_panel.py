from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy import text
import random

def get_random_id(): return random.randint(0, 500000000000000000000000000)

async def send_msgs(vk_api, group, msg, session: AsyncSession):
    groups = {"friends": 1, "classmates": 2, "programmers": 3}
    sql_text = text(f"""
        SELECT chat_id FROM users WHERE group_id = {groups.get(group)}
    """)
    result = await session.execute(sql_text)
    result = result.all()
    for user_id in result:
        vk_api.messages.send(
            user_id=user_id,
            message=msg,
            random_id=get_random_id(),
            v=5.131
        )