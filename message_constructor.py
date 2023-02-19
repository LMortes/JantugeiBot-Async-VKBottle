import datetime


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
