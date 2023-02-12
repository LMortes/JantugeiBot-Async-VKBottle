import datetime
import re
import asyncio
import textwrap

from vkbottle import GroupTypes, GroupEventType, Keyboard, Callback, KeyboardButtonColor
from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler
from check_dostup_rule import CheckUserDostup
from db_connect import *
from settings import bot, USER_BOT_ID
from user_bot_functions import *
import time
import pprint

bl = BotLabeler()


# Команда для всех


@bl.message(text='/status')
async def cmd_status(message: Message):
    status = '⚙ Все системы работают в штатном режиме.\n' \
             '♻ Текущая версия бота - 0.1'
    await message.answer(status)


# Команды для 0 уровня доступа(лидер/зам) и выше


@bl.message(CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), text='/help')
async def hi_handler(message: Message):
    dostup = await get_user_dostup(message.from_id)
    info = ''
    info2 = ''
    info = 'Привет👋 \n\
                Функционал Jantugei Inc: ♻ \n'
    if dostup >= 0:
        info += '0️⃣/status - проверка статуса бота. \n' \
                '0️⃣/peer_id - посмотреть ID беседы у паблика. \n' \
                '0️⃣/dostup - посмотреть свой уровень доступа в боте. \n' \
                '0️⃣/ao - посмотреть уникальный айди вк по упоминанию. \n' \
                '0️⃣/info - посмотреть статистику пользователя. \n' \
                '0️⃣/members - вывести актуальный список пользователей. \n' \
                '0️⃣/warnhistory - вывести историю выдачи или снятия наказаний у пользователя. \n' \
                '0️⃣/scorehistory - вывести историю выдачи или снятия баллов у пользователя. \n' \
                '0️⃣/dayshistory - вывести историю выдачи или снятия дней к сроку у пользователя. \n' \
                '0️⃣/getip - вывести информацию о айпи адресе(ах). \n' \
                '0️⃣/fonline - вывести информацию о онлайне фракции.\n'
    if dostup >= 1:
        info += '1️⃣/online - посмотреть свой онлайн прямиком из логов. \n' \
                '1️⃣/checkblacklist - проверить находится ли пользователь в чс организаций по нику или иду аккаунта. \n'
    if dostup >= 3:
        info += '3️⃣/clrbuttons - убрать кнопки из беседы. \n' \
                '3️⃣/checknick - проверить меняли ли пользователь ник по нику или по иду аккаунта. \n' \
                '3️⃣/formslist - вывести список пользователей с доступом к форме. \n' \
                '3️⃣/getdsid - выводит дискорд ID по нику дискорда. \n'
    if dostup >= 4:
        info += '4️⃣/formaccess - выдать доступ пользователю к заполнению формы. \n' \
                '4️⃣/formremove - снять доступ у пользователя к заполнению формы. \n' \
                '4️⃣/rwarn - выдать или снять выговор пользователю. \n' \
                '4️⃣/ywarn - выдать или снять предупреждение пользователю. \n' \
                '4️⃣/setscore - выдать или снять баллы пользователю. \n' \
                '4️⃣/setdays - выдать или снять дни к сроку пользователю. \n' \
                '4️⃣/kickfrom - исключить пользователя без или с доступом из бесед без занесения его в архив. \n' \
                '4️⃣/addto - добавить пользователя без или с доступом в любую конференцию. \n' \
                '4️⃣/kick - исключить пользователя из всех бесед и занести его в архив. \n' \
                '4️⃣/forcearchive - досрочно занести пользователя в архив, без исключения из бесед. \n' \
                '4️⃣/msg - отправить уведомление в нужную вам беседу с упоминанием нужных участников. \n' \
                '4️⃣/updateuser - изменить профиль пользователя. \n' \
                '4️⃣/online - добавляется доступ к просмотру чужого онлайна указав его ник в конце. \n' \
                '4️⃣/setjb - закрыть или открыть, закрепить или открепить и установить префикс или убрать префикс к жалобе. \n' \
                '4️⃣/getid - найти ID аккаунта по нику в логах. \n' \
                '4️⃣/pin - закрепить пересланное вами сообщение в беседе. \n' \
                '4️⃣/get_categories - Вывести все категории в разделе. \n' \
                '4️⃣/get_category - Вывести название категории. \n' \
                '4️⃣/get_threads - Вывести все темы в разделе. \n' \
                '4️⃣/get_post - Вывести всю информацию по посту. \n' \
                '4️⃣/edit_post - Редактирование поста. \n' \
                '4️⃣/set_unread - Установить все темы в выбранном разделе прочитанными. \n' \
                '4️⃣/send_message - Отправить сообщение в тему. \n' \
                '4️⃣/get_thread - Вывести название темы и содержание первого поста. \n' \
                '4️⃣/close_thread - Закрыть тему. \n' \
                '4️⃣/pin_thread - Закрепить тему. \n' \
                '🎿Присваивается возможность одобрять лидера и заместителя. \n' \
                '🎿Присваивается возможность одобрять лидера и заместителя.# \n'
    if dostup >= 5:
        info2 += '5️⃣/chat_id - посмотреть ID беседы у страничного бота. \n' \
                 '5️⃣/cinfo - вывод информации о беседе в которой была прописана команда. \n' \
                 '5️⃣/sinfo - посмотреть скрытую статистику лидера/заместителя/администратора, ЗАПРЕЩЕНО прописывать при игроках. \n' \
                 '🎿Присваивается возможность одобрять помощников и следящих. \n' \
                 '🎿Присваивается возможность заносить и выносить из черного списка на сайте \n'
    if dostup >= 6:
        info2 += '6️⃣/loadlogs - загрузить логи за указанную вами дату.\n' \
                 '6️⃣/ulog stats - посмотреть статистику аккаунта в логах.\n' \
                 '6️⃣/ulog connect - подключить бота к логам.\n' \
                 '6️⃣/ulog disconnect - отключить бота от логов.\n'
    if dostup >= 7:
        info2 += '🎿Присваивается возможность одобрять ЗГСа и ПГСа.\n'
    if dostup >= 8:
        info2 += '8️⃣/checksoldip - проверить нахождение IP в базе данных SAMP Store.\n' \
                 '8️⃣/listsoldips - вывести список IP находящихся в базе данных SAMP Store.\n' \
                 '8️⃣/addsoldip - добавить IP в базу данных SAMP Store.\n' \
                 '8️⃣/removesoldip - удалить IP из базы данных SAMP Store.\n' \
                 '8️⃣/checkaban - проверить нахождение никнейма, айди аккаунта или вывести список заблокированных аккаунтов на IP автоматически выданых системой.\n' \
                 '🎿Присваивается возможность проверять формы новых лидеров и заместителей.\n'
    if dostup >= 9:
        info2 += '9️⃣/restart - перезапуск бота.\n' \
                 '🎿Присваивается возможность одобрять ГС, Тех и Дет.Сад.\n'
    if dostup >= 10:
        info2 += '🎿Присваивается возможность одобрять куратора.\n'
    if dostup == 11:
        info2 += '⚙/test - отправить функционал на тестирование. \n' \
                 '⚙/testlist - вывести список тестов (для тестировщиков).\n' \
                 '⚙/buglist - вывести список баг репортов (для тестироващиков)\n' \
                 '⚙/formpolling - запустить поллинг форм в базу данных'
    if dostup >= 5:
        await message.answer(info)
        await message.answer(info2)
    else:
        await message.answer(info)


@bl.chat_message(CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), text='/peer_id')
async def cmd_peer_id(message: Message):
    result_id = '💬 ID Беседы: ' + str(message.peer_id) + ' 💬'
    await message.answer(result_id)


@bl.message(CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), text='/dostup')
async def cmd_dostup(message: Message):
    await message.answer(f'🔢 Ваш уровень доступа: {await get_user_dostup(message.from_id)}')


@bl.message(CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), text=['/ao', '/ao <ping>'])
async def cmd_ao(message: Message, ping=None):
    if ping is not None:
        try:
            uid = re.findall(r'[0-9]+', ping)[0]
        except:
            await message.answer('⚠ Упоминание введено некорректно или такого пользователя не существует')
        users_info = await bot.api.users.get(uid)
        await message.answer(f'ID Пользователя {ping}({users_info[0].first_name} {users_info[0].last_name}): {uid}')
    else:
        await message.answer('⚙ Используйте следующий синтаксис: /ao [@Упоминание]')


# Команды для 4 уровня доступа и выше


@bl.message(CheckUserDostup([4, 5, 6, 7, 8, 9, 10, 11]),
            text=['/formaccess', '/formaccess <screen_name> <type_form:int>'])
async def cmd_formaccess(message: Message, screen_name=None, type_form: int = None):
    user_dostup = await get_user_dostup(message.from_id)
    if screen_name is not None:
        if (type_form is not None) and (type_form >= 0 and type_form <= 5):
            # Добыча id пользователя из упоминания
            try:
                uid = re.findall(r'[0-9]+', screen_name)[0]
            except:
                await message.answer('⚠ Упоминание введено некорректно или такого пользователя не существует')
            # Проверка есть ли пользователь у бота в друзьях
            if int(uid) == int(message.from_id):
                await message.answer('⚠ Нельзя выдать форму самому себе')
                return
            is_friend = await check_friends_and_add(uid)
            if is_friend == 174:
                await message.answer('⚠ Нельзя выдать форму самому себе')
                return
            elif is_friend == 175:
                await message.answer('⚠ У данного пользователя бот находится в черном списке')
                return
            elif is_friend == 200:
                await message.answer(
                    '⚠ Данного пользователя нет в друзьях у бота, если бот вам отправил заявку, примите её, если нет, добавьте бота в друзья вручную')
                return
            # Проверки если данный пользователь админ или лидер или он уже есть в формах бд
            status_code_formaccess = await check_user_in_formaccess(uid)
            if status_code_formaccess == 0:
                await message.answer('⚠ При проверке пользователя на наличие в базе данных произошла неизвестная ошибка')
                return
            elif status_code_formaccess == 11:
                await message.answer(
                    '⚠ Пользователь, которому вы хотите выдать доступ к заполению формы, является администратором. Кикнете его с причиной "Перезаполнение" и выдайте форму снова.')
                return
            elif status_code_formaccess == 12:
                await message.answer(
                    '⚠ Пользователь, которому вы хотите выдать доступ к заполнению формы, является лидером/заместителем. Кикнете его с приной "Перезаполнение" и выдайте форму снова.')
                return
            elif status_code_formaccess == 13:
                await message.answer(
                    '⚠ Пользователь, которому вы хотите выдать доступ к заполнению формы уже его имеет и в данный момент находится на этапе заполнения.')
                return
            elif status_code_formaccess == 14:
                await message.answer(
                    '⚠ Пользователь, которому вы хотите выдать доступ к заполнению формы уже его имеет и в данный момент находится на этапе одобрения заявки администрацией.')

            # Id админа выдавшего форму
            adm_id = message.from_id
            # Имя админа выдавшего форму
            adm_name = await get_user_name(adm_id)
            # Имя пользователя которому выдана форма
            user_name = await get_user_fullname_user_bot(uid)
            # Сообщение администратору при успешной отправке формы
            success_message_adm = f'🌐 Доступ к заполнению выдан успешно 🌐\n' \
                                  f'👤 Доступ выдан пользователю: [id{uid}|{user_name}]\n' \
                                  f'🕒 Доступ был выдан на 24 часа.\n' \
                                  f'📝 Оповещение о выдаче доступа было отправлено в личные сообщения пользователю!.'
            # Формирование ссылки для заполнения формы на сайте
            if type_form == 0:
                form_uri = 'ld_form_auth.php'
            elif type_form > 0 and type_form < 6:
                form_uri = 'adm_form_auth.php'
            # Сообщение пользователю в личку от юзер бота
            user_send_message = f'👋🏻 Привет {user_name},\n\n' \
                                f'🆕 Вашему вк был выдан доступ к заполнению формы по запросу [id{adm_id}|{adm_name}], при возникновении любых проблем пишите ему.\n' \
                                f'🌐 Ссылка для заполнения этой формы: https://jantugei.ru/forms/{form_uri}\n' \
                                f'🕒 У вас есть ровно сутки на заполнение формы, в ином случае вы потеряете право к заполению формы.\n\n' \
                                f'© By Jantugei Inc.'
            # Сообщение администратору об успешной отправке в личку пользователю или об неудачной
            success_user_send_message = '✅ Отправка в личные сообщения успешна ✅'
            error_user_send_message = '🚫 Произвошла неизвестная ошибка при отправке в личные сообщения 🚫'
            # Сверка по доступам и возможности выдать ту или иную форму
            if user_dostup == 11 and type_form in [0, 1, 2, 3, 4, 5]:
                if is_friend:
                    await set_formaccess(uid, adm_id, adm_name, type_form)  # Запись формы в бд
                    await message.answer(success_message_adm)
                    is_send_user = await send_form_message(uid, user_send_message)
                    if is_send_user:
                        await message.answer(success_user_send_message)
                    else:
                        await message.answer(error_user_send_message)
            elif user_dostup >= 10 and type_form in [0, 1, 2, 3]:
                if is_friend:
                    await set_formaccess(uid, adm_id, adm_name, type_form)
                    await message.answer(success_message_adm)
                    is_send_user = await send_form_message(uid, user_send_message)
                    if is_send_user:
                        await message.answer(success_user_send_message)
                    else:
                        await message.answer(error_user_send_message)
            elif user_dostup >= 9 and type_form in [0, 1, 2]:
                if is_friend:
                    await set_formaccess(uid, adm_id, adm_name, type_form)
                    await message.answer(success_message_adm)
                    is_send_user = await send_form_message(uid, user_send_message)
                    if is_send_user:
                        await message.answer(success_user_send_message)
                    else:
                        await message.answer(error_user_send_message)
            elif user_dostup >= 8 and type_form in [0, 1]:
                if is_friend:
                    await set_formaccess(uid, adm_id, adm_name, type_form)
                    await message.answer(success_message_adm)
                    is_send_user = await send_form_message(uid, user_send_message)
                    if is_send_user:
                        await message.answer(success_user_send_message)
                    else:
                        await message.answer(error_user_send_message)
            elif user_dostup >= 4 and type_form == 0:
                if is_friend:
                    await set_formaccess(uid, adm_id, adm_name, type_form)
                    await message.answer(success_message_adm)
                    is_send_user = await send_form_message(uid, user_send_message)
                    if is_send_user:
                        await message.answer(success_user_send_message)
                    else:
                        await message.answer(error_user_send_message)
            else:
                await message.answer('⚠ У вас нет прав для выдачи данной формы')
        else:
            await message.answer('🔢 Выберите тип формы. Чтобы посмотреть список введите /formaccess')
    else:
        syntax_message = "⚠ Используйте следующий синтаксис: /formaccess [@Упоминание] [Тип формы]\n\n" \
                         "🔢 Тип формы (Выдача доступа к заполнению формы с этим доступом):\n" \
                         "💠 0 - Лидер/Заместитель\n" \
                         "🔯 1 - Следящие / ПГС / ЗГС / ГС Гос / Нелегалы\n" \
                         "🔮 2 - Дет.Сад/Тех.Администратор\n" \
                         "🔱 3 - Куратор\n" \
                         "👑 4 - Главный администратор/Заместитель Главного Администратора\n" \
                         "🎿 5 - Руководство Jantugei Inc"
        await message.answer(syntax_message)


# Команды для 11 уровня доступа

@bl.message(CheckUserDostup(11), text=['/test', '/test <text>'])
async def cmd_test(message: Message, text=None):
    if text is not None:
        adm_name = await get_user_name(message.from_id)
        try:
            await set_test_info(adm_name, text)
            await message.answer('✅ Тест успешно записан и передан тестироващикам!')
        except:
            await message.answer('⚠ Неизвестная ошибка!')
    else:
        await message.answer('⚙ Используй следующий синтаксис: /test [суть теста]')


@bl.message(CheckUserDostup(11), text='/testlist')
async def cmd_testlist(message: Message):
    testlist_text = await get_testlist()
    await message.answer(testlist_text)


@bl.message(CheckUserDostup(11), text=['/bug', '/bug <id:int>', '/bug <id:int> <text>'])
async def cmd_bug(message: Message, id: int = None, text=None):
    if id is not None:
        if text is not None:
            adm_name = await get_user_name(message.from_id)
            msg = await for_cmd_bug(adm_name, id, text)
            await message.answer(msg)
        else:
            await message.answer('Напишите суть бага. Если багов нет, напишите "Баги отсутствуют"')
    else:
        await message.answer('Введите id тест репорта.')


@bl.message(CheckUserDostup(11), text='/buglist')
async def cmd_buglist(message: Message):
    buglist_text = await get_buglist()
    await message.answer(buglist_text)


@bl.message(CheckUserDostup(11), text=['/fixbug', '/fixbug <id:int>'])
async def cmd_fixbug(message: Message, id: int = None):
    if id is not None:
        msg = await for_cmd_fixbug(id)
        await message.answer(msg)
    else:
        await message.answer('Введите id баг репорта.')


@bl.message(CheckUserDostup(11), text='/formpolling')
async def polling_form_done(message: Message):
    await message.answer('🌐 Функция поллинга базы данных запущена 🌐')
    try:
        while True:
            is_form_done = await get_info_from_formaccess_done()  # Поиск инфы в таблицах с формами
            if is_form_done == 1:
                await message.answer('⚠ Найдена форма на администратора')  # Если есть форма на админа
                forms_info_adm = await get_info_form_adm()  # Дописать распределение по беседам в зависимости от доступа!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                new_form_admin_message = '🆕 Поступила новая форма на администратора 🆕\n\n'
                keyboard = (  # Объявление кнопок в сообщении
                    Keyboard(inline=True)
                        .add(Callback("🌀 Одобрить", {"cmd": "accept_admin_form"}), color=KeyboardButtonColor.POSITIVE)
                        .add(Callback("⭕ Отказать", {"cmd": "decline_admin_form"}), color=KeyboardButtonColor.NEGATIVE)
                )
                for row in forms_info_adm:  # Формирование сообщения в конфу
                    new_form_admin_message += f'👤 Игровой ник администратора: [id{row[1]}|{row[3]}][D:{row[11]}]\n' \
                                              f'🔢 Возраст: {row[2]}\n' \
                                              f'👥 Должность: {row[4]}\n' \
                                              f'💻 Discord: {row[7]}\n' \
                                              f'🔧 Ссылка на форумный аккаунт: {row[6]}\n' \
                                              f'🗾 Администратор выдавший форму: [id{row[9]}|{row[8]}]\n' \
                                              f'📅 Дата выдачи формы: {row[10]}'
                    # Отправка сообщения в беседу с id = peer_id
                    # Для лидеров изменить id беседы когда будет беседа
                    await bot.api.messages.send(peer_id=DEVELOPER_DIALOG_ID, message=new_form_admin_message,
                                                random_id=0, keyboard=keyboard)
                    new_form_admin_message = '🆕 Поступила новая форма на администратора 🆕\n'  # Обновление строки
            elif is_form_done == 2:
                await message.answer('⚠ Найдена форма на лидера')  # Если есть форма на лидера
                forms_info_leader = await get_info_form_leader()  # Добыча информации из таблицы с формой лидера
                new_form_leader_message = '🆕 Поступила новая форма на лидера/заместителя 🆕\n\n'
                keyboard = (  # Объявление кнопок в сообщении
                    Keyboard(inline=True)
                        .add(Callback("🌀 Одобрить", {"cmd": "accept_leader_form"}), color=KeyboardButtonColor.POSITIVE)
                        .add(Callback("⭕ Отказать", {"cmd": "decline_leader_form"}), color=KeyboardButtonColor.NEGATIVE)
                )
                for row in forms_info_leader:  # Формирование сообщения в конфу
                    new_form_leader_message += f'👤 Игровой ник: [id{row[1]}|{row[3]}]\n' \
                                               f'🔢 Возраст: {row[2]}\n' \
                                               f'💼 Фракция: {row[5]}\n' \
                                               f'👥 Должность: {row[4]}\n' \
                                               f'💻 Discord: {row[7]}\n' \
                                               f'🔧 Ссылка на форумный аккаунт: {row[6]}\n' \
                                               f'🗾 Администратор выдавший форму: [id{row[9]}|{row[8]}]\n' \
                                               f'📅 Дата выдачи формы: {row[10]}'
                    # Отправка сообщения в беседу с id = peer_id
                    # Для лидеров изменить id беседы когда будет беседа
                    await bot.api.messages.send(peer_id=DEVELOPER_DIALOG_ID, message=new_form_leader_message,
                                                random_id=0, keyboard=keyboard)
                    new_form_leader_message = '🆕 Поступила новая форма на лидера/заместителя 🆕\n'  # Обновление строки
            elif is_form_done == 3:
                await message.answer('⚠ Найдена форма на лидера и на администратора')  # Если есть форма на лидера и на админа
                forms_info_leader = await get_info_form_leader()  # Добыча информации из таблицы с формой лидера
                forms_info_adm = await get_info_form_adm()  # Дописать распределение по беседам в зависимости от доступа!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                new_form_leader_message = '🆕 Поступила новая форма на лидера/заместителя 🆕\n\n'
                new_form_admin_message = '🆕 Поступила новая форма на администратора 🆕\n\n'
                keyboard = (  # Объявление кнопок в сообщении для формы лидера
                    Keyboard(inline=True)
                        .add(Callback("🌀 Одобрить", {"cmd": "accept_leader_form"}), color=KeyboardButtonColor.POSITIVE)
                        .add(Callback("⭕ Отказать", {"cmd": "decline_leader_form"}), color=KeyboardButtonColor.NEGATIVE)
                )
                keyboard2 = (  # Объявление кнопок в сообщении для формы админа
                    Keyboard(inline=True)
                        .add(Callback("🌀 Одобрить", {"cmd": "accept_admin_form"}), color=KeyboardButtonColor.POSITIVE)
                        .add(Callback("⭕ Отказать", {"cmd": "decline_admin_form"}), color=KeyboardButtonColor.NEGATIVE)
                )
                for row in forms_info_leader:  # Формирование сообщения в конфу
                    new_form_leader_message += f'👤 Игровой ник: [id{row[1]}|{row[3]}]\n' \
                                               f'🔢 Возраст: {row[2]}\n' \
                                               f'💼 Фракция: {row[5]}\n' \
                                               f'👥 Должность: {row[4]}\n' \
                                               f'💻 Discord: {row[7]}\n' \
                                               f'🔧 Ссылка на форумный аккаунт: {row[6]}\n' \
                                               f'🗾 Администратор выдавший форму: [id{row[9]}|{row[8]}]\n' \
                                               f'📅 Дата выдачи формы: {row[10]}'
                for row in forms_info_adm:  # Формирование сообщения в конфу
                    new_form_admin_message += f'👤 Игровой ник администратора: [id{row[1]}|{row[3]}][D:{row[11]}]\n' \
                                              f'🔢 Возраст: {row[2]}\n' \
                                              f'👥 Должность: {row[4]}\n' \
                                              f'💻 Discord: {row[7]}\n' \
                                              f'🔧 Ссылка на форумный аккаунт: {row[6]}\n' \
                                              f'🗾 Администратор выдавший форму: [id{row[9]}|{row[8]}]\n' \
                                              f'📅 Дата выдачи формы: {row[10]}'
                    # Отправка сообщения в беседу с id = peer_id лидерская форма
                    # Для лидеров изменить id беседы когда будет беседа
                    await bot.api.messages.send(peer_id=DEVELOPER_DIALOG_ID, message=new_form_leader_message,
                                                random_id=0, keyboard=keyboard)
                    # Отправка сообщения в беседу с id = peer_id админская форма
                    await bot.api.messages.send(peer_id=DEVELOPER_DIALOG_ID, message=new_form_admin_message,
                                                random_id=0, keyboard=keyboard2)
                    new_form_leader_message = '🆕 Поступила новая форма на лидера/заместителя 🆕\n'  # Обновление строки лидерской формы
                    new_form_admin_message = '🆕 Поступила новая форма на администратора 🆕\n'  # Обновление строки админской формы

            else:
                await message.answer('✅ Ничего не найдено')  # Убрать, когда будет полностью рабочая система
            await asyncio.sleep(60)  # Задержка поллинга таблицы с формами
    except:
        await message.answer('⚠ По неизвестной причине поллинг базы данных прекращен')
        print('⚠ По неизвестной причине поллинг базы данных прекращен')


@bl.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def click_button_form(event: GroupTypes.MessageEvent):
    dostup = await get_user_dostup(event.object.user_id)
    message_info = await bot.api.messages.get_by_conversation_message_id(peer_id=event.object.peer_id,
                                                                         conversation_message_ids=event.object.conversation_message_id)
    pre_user_id = re.findall(r'\[id[0-9]+', str(message_info))[0]
    user_id = re.findall(r'[0-9]+', pre_user_id)[0]
    if dostup >= 4:
        adm_id = event.object.user_id
        adm_name = await get_user_name(adm_id)
        user_name = await get_user_name(user_id)
        is_remove = ''
        message_decline = f'[id{event.object.user_id}|{adm_name}] отказал форму'
        message_accept = f'[id{event.object.user_id}|{adm_name}] одобрил форму'
        message_remove_form = '✅ Форма успешно удалена из базы данных. Все доступы к заполнению формы сняты.'
        message_remove_form_error = '⚠ Произошла ошибка при удалении формы из базы данных или форма была удалена ранее.'
        message_for_user = '✅ Отправка в личные сообщения успешна'
        message_for_user_error = '⚠ Произошла ошибка при отправке в личные сообшения.'
        if event.object.payload["cmd"] == "accept_leader_form":
            await bot.api.messages.send(peer_id=event.object.peer_id, message='✅ Кнопка Одобрить работает', random_id=0)
            # Дописать одобрение формы лидера

        elif (event.object.payload["cmd"] == "decline_leader_form") or \
                (event.object.payload["cmd"] == "decline_admin_form"):
            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_decline, random_id=0)
            if event.object.payload["cmd"] == "decline_leader_form":
                is_remove = await remove_formaccess_done_leader(user_id)
            elif event.object.payload["cmd"] == "decline_admin_form":
                is_remove = await remove_formaccess_done_admin(user_id)
            if is_remove:
                await bot.api.messages.send(peer_id=event.object.peer_id, message=message_remove_form, random_id=0)
                is_send_user_message = await send_user_message_formdecline(user_id, adm_id, adm_name)
                if is_send_user_message:
                    await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user, random_id=0)
                else:
                    await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user_error,
                                                random_id=0)
            else:
                await bot.api.messages.send(peer_id=event.object.peer_id, message=message_remove_form_error,
                                            random_id=0)

        elif event.object.payload["cmd"] == "accept_admin_form":
            await bot.api.messages.send(peer_id=event.object.peer_id,
                                        message='✅ Кнопка Одобрить для формы администратора работает', random_id=0)
            # Дописать одобрение формы админа
