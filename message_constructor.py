import datetime

from settings import bot


async def construct_message_info_leader(leader_info):
    days_on_post = datetime.date.today() - leader_info["leader_info"][7]
    days_remove = leader_info["leader_info"][8] - datetime.date.today()
    message_info = f'🗂 Основая информация о пользователе:\n' \
                   f'👤 Ник пользователя: [id{leader_info["leader_info"][1]}|{leader_info["leader_info"][2]}]\n' \
                   f'👥 Должность: {leader_info["leader_info"][4]}\n' \
                   f'🗺 Сервер: -\n' \
                   f'📅 Дата назначения: {leader_info["leader_info"][7]}\n' \
                   f'📅 Дата снятия: {leader_info["leader_info"][8]}\n' \
                   f'📅 Дней на посту: {days_on_post.days}\n' \
                   f'📅 Дней до снятия: {days_remove.days}\n' \
                   f'🖥 Discord: {leader_info["leader_info"][13]}\n\n' \
                   f'🧾 Наказания и баллы:\n' \
                   f'⛔ Выговоры: {leader_info["leader_info"][5]}\n' \
                   f'⚠ Предупреждения: {leader_info["leader_info"][6]}\n' \
                   f'🪙 Баллы: {leader_info["leader_info"][10]}\n\n' \
                   f'⏰ Онлайн:\n' \
                   f'⏲ 🔜 В разработке'
    return message_info


async def construct_message_info_admin(admin_info):
    days_on_post = datetime.date.today() - admin_info["admin_info"][8]
    message_info = '🗂 Основная информация о администраторе:\n' \
                   f'👤 Ник администратора: [id{admin_info["admin_info"][1]}|{admin_info["admin_info"][2]}][{admin_info["admin_info"][4]}]\n' \
                   f'🔢 Уровень администратора: {admin_info["admin_info"][7]}\n' \
                   f'👥 Уровень доступа: [D:{admin_info["admin_info"][6]}]\n' \
                   f'👥 Должность: {admin_info["admin_info"][5]}\n' \
                   f'🗺 Сервер: - \n' \
                   f'📅 Дата назначения: {admin_info["admin_info"][8]}\n' \
                   f'📅 Дней на посту: {days_on_post.days}\n' \
                   f'🖥 Discord: {admin_info["admin_info"][12]}\n\n' \
                   f'🧾 Наказание и баллы:\n' \
                   f'⛔ Выговоры: {admin_info["admin_info"][13]}\n' \
                   f'⚠ Предупреждения: {admin_info["admin_info"][14]}\n' \
                   f'🪙 Баллы: {admin_info["admin_info"][10]}\n\n' \
                   f'🧾 Онлайн:\n' \
                   f'⏲ 🔜 В разработке'
    return message_info


async def construct_message_info_blacklist(player_info_black):
    message_info_black = '📝  Информация о игроке находящемся в черном списке:\n\n'\
                         f'👤 Игровой ник: {player_info_black["player_info"][2]}\n' \
                         f'📋 ЧС структуры: {player_info_black["player_info"][1]}\n' \
                         f'🔢 Степень ЧСа: {player_info_black["player_info"][3]}\n' \
                         f'📁 Причина занесения в ЧС: {player_info_black["player_info"][4]}\n' \
                         f'📅 Дата занесения в ЧС: {player_info_black["player_info"][5]}\n' \
                         f'📅 Прошло дней с момента занесения в ЧС: {(datetime.date.today() - player_info_black["player_info"][5]).days}\n' \
                         f'👤 Ник администратора, который занес игрока в ЧС: {player_info_black["player_info"][6]}\n' \
                         '🕗 Количество смен: В разработке\n' \
                         '📅 Дата последней смены: В разработке'
    return message_info_black


async def construct_message_info_formaccess(forms_info):
    message_info_formaccess = '📂 Пользователи с доступом к форме:\n'
    counter = 1
    for row in forms_info["info_formaccess"]:
        user_info = await bot.api.users.get(row[1])
        user_first_name = user_info[0].first_name
        user_last_name = user_info[0].last_name
        condition = ''
        if row[5] == 0:
            condition = '📤 На заполнении'
        elif row[5] == 1:
            condition = '📥 На одобрении'
        message_info_formaccess += f'{counter}. [id{row[1]}|{user_first_name} {user_last_name}] | Тип формы: {row[2]} | Адм. выдавший форму: [id{row[3]}|{row[4]}] | Состояние: {condition}\n'
        counter += 1
    return message_info_formaccess


async def construct_message_ip_information(response_ip):
    message_ip = 'Информация по запрошенному IP адресу:\n\n'\
                 f'IP адрес: {response_ip["response_ip"]["ip"]}\n' \
                 f'Страна: {response_ip["response_ip"]["country"]}\n' \
                 f'Город: {response_ip["response_ip"]["city"]}\n' \
                 f'Часовой пояс: {response_ip["response_ip"]["timezone"]}\n' \
                 f'Провайдер: {response_ip["response_ip"]["isp"]}'
    return message_ip


async def construct_message_dayshistory(info_dayshistory, leader_info_dayshistory):
    add_or_remove = ''
    message_dayshistory = ''
    message_info_dayshistory = ''
    if leader_info_dayshistory:
        days_on_post = leader_info_dayshistory["end_date"] - leader_info_dayshistory["start_date"]
        message_info_dayshistory = f'История изменений дней к сроку - [id{leader_info_dayshistory["vk_id"]}|{leader_info_dayshistory["name"]}]\n'\
                              f'Дата назначения: {leader_info_dayshistory["start_date"]}\n' \
                              f'Дата снятия: {leader_info_dayshistory["end_date"]}\n' \
                              f'Дней на посту: {days_on_post.days}\n\n'
    for row in reversed(info_dayshistory["info_dayshistory"]):
        if row[4] == 0:
            add_or_remove = '-'
        elif row[4] == 1:
            add_or_remove = '+'
        if row[3] == 1:
            day = 'день'
        elif (row[3] == 2) or (row[3] == 3) or (row[3] == 4):
            day = 'дня'
        else:
            day = 'дней'
        message_dayshistory += f'📜 {row[8]} [id{row[1]}|{row[2]}] было установлено {add_or_remove}{row[3]} {day} к окончанию срока от [id{row[6]}|{row[7]}]. Причина: {row[5]}\n'
    result_message_dayshistory = message_info_dayshistory + message_dayshistory
    return result_message_dayshistory
