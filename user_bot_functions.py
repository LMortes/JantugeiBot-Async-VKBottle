from settings import api
from vkbottle import VKAPIError
from dialog_ids import *


async def check_friends_and_add(user_id):
    try:
        is_add = await api.friends.add(user_id)
    except VKAPIError[174]:
        return 174
    except VKAPIError[175]:
        return 175
    if is_add == 1:
        return 200
    elif is_add == 2 or is_add == 4:
        friends = await api.friends.get()
        for friend in friends.items:
            if int(user_id) == int(friend):
                return True
    return False

async def get_user_fullname_user_bot(user_id):
    user_info = await api.users.get(user_id)
    user_first_name = user_info[0].first_name
    user_last_name = user_info[0].last_name
    result_user_name = user_first_name + ' ' + user_last_name
    return result_user_name


async def send_form_message(user_id, message):
    try:
        send_message = await api.messages.send(peer_id=user_id, message=message, random_id=0)
    except:
        return False
    return True


async def send_user_message_formdecline(user_id, user_name, adm_id, adm_name):
    message = f'👋🏻 Приветствую {user_name}\n\n'\
                '😢 У вашего VK был изъят доступ к заполнению формы\n'\
                f'администратором [id{adm_id}|{adm_name}], по всем вопросам писать ему!\n\n'\
                '© By Jantugei Inc.'
    try:
        send_message = await api.messages.send(peer_id=user_id, message=message, random_id=0)
    except:
        return False
    return True


async def testqwe():
    pass
