from sqlalchemy import text
from sqlalchemy.ext.asyncio.session import AsyncSession

async def get_response(session: AsyncSession, req: str):
    sql_text = text(f"""
        SELECT answer FROM phrases WHERE phrase = '{req}'
    """)
    result = await session.execute(sql_text)
    await session.commit()
    return result.all()
async def add_phrase(session: AsyncSession, phrase, answer):
    sql_text = text(f"""
        SELECT id FROM phrases ORDER BY id DESC
    """)
    result = await session.execute(sql_text)
    result = result.all()
    for item in await session.execute("SELECT phrase FROM phrases").all():
        if item.phrase.lower() == phrase.lower(): return
    last_id = result[0].id
    sql_text = text(f"""
        INSERT INTO phrases VALUES({last_id+1}, '{phrase.lower()}', '{answer.lower()}')
    """)
    result = await session.execute(sql_text)
    await session.commit()
async def create_table(session: AsyncSession):
    sql_text = text("""
        CREATE TABLE groups (
            id INTEGER PRIMARY KEY, 
            name TEXT
    )
    """)
    await session.execute(sql_text)
    await session.commit()
async def create_group(session: AsyncSession, chat_id: int, group_name: str):
    sql_text = text(f"""
        SELECT id FROM users ORDER BY id DESC
    """)
    result = await session.execute(sql_text)
    result = result.all()
    result2 = await session.execute(text("SELECT chat_id FROM users"))
    result2 = result2.all()
    for item in result2:
        if item.chat_id == chat_id: return "Already exists"
    last_id = result[0].id
    group_ids = {"friends": 1, "classmates": 2, "programmers": 3}
    sql_text = text(f"""
        INSERT INTO users VALUES({last_id+1}, {chat_id}, '{group_ids.get(group_name)}')
    """)
    result = await session.execute(sql_text)
    await session.commit()