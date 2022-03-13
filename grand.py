import random

def get_random_id(): return random.randint(0, 500000000000000000000000000)

def reply_to_message(message_text: str, vk_api, user_id: int):
    reply_list = {"привет": 'vk_api.messages.send(user_id = user_id, message = "И тебе привет", random_id = get_random_id(), v=5.131)',
        "как дела": '''vk_api.messages.send(user_id = user_id, message = "Хорошо", random_id = get_random_id(), v=5.131)
vk_api.messages.send(user_id = user_id, message = "Как у тебя?", random_id = get_random_id(), v=5.131)'''}
    if message_text in reply_list: exec(reply_list[message_text])