import datetime
import re

from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler
from check_dostup_rule import CheckUserDostup
from db_connect import *
from settings import bot, USER_BOT_ID
from user_bot_functions import *
import time
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
                '0️⃣/warnhistory - вывести историю выдачи или снятия наказаний у пользователя. \n'\
                '0️⃣/scorehistory - вывести историю выдачи или снятия баллов у пользователя. \n'\
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
                 '⚙/buglist - вывести список баг репортов (для тестироващиков)'
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
    await message.answer(f'Ваш уровень доступа: {await get_user_dostup(message.from_id)}')


@bl.message(CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), text=['/ao', '/ao <ping>'])
async def cmd_ao(message: Message, ping=None):
    if ping is not None:
        try:
            uid = re.findall(r'[0-9]+', ping)[0]
        except:
            await message.answer('Упоминание введено некорректно или такого пользователя не существует')
        users_info = await bot.api.users.get(uid)
        await message.answer(f'ID Пользователя {ping}({users_info[0].first_name} {users_info[0].last_name}): {uid}')
    else:
        await message.answer('⚙ Используйте следующий синтаксис: /ao [@Упоминание]')


# Команды для 4 уровня доступа и выше


@bl.message(CheckUserDostup([4, 5, 6, 7, 8, 9, 10, 11]), text=['/formaccess', '/formaccess <screen_name> <type_form:int>'])
async def cmd_formaccess(message: Message, screen_name=None, type_form: int = None):
    user_dostup = await get_user_dostup(message.from_id)
    if screen_name is not None:
        if (type_form is not None) and (type_form >= 0 and type_form <=5):
            # Добыча id пользователя из упоминания
            try:
                uid = re.findall(r'[0-9]+', screen_name)[0]
            except:
                await message.answer('Упоминание введено некорректно или такого пользователя не существует')
            # Проверка есть ли пользователь у бота в друзьях
            if int(uid) == int(message.from_id):
                await message.answer('Нельзя выдать форму самому себе')
                return
            is_friend = await check_friends_and_add(uid)
            if is_friend == 174:
                await message.answer('Нельзя выдать форму самому себе')
                return
            elif is_friend == 175:
                await message.answer('У данного пользователя бот находится в черном списке')
                return
            elif is_friend == 200:
                await message.answer('Данного пользователя нет в друзьях у бота, если бот вам отправил заявку, примите её, если нет, добавьте бота в друзья вручную')
                return
            # Проверки если данный пользователь админ или лидер или он уже есть в формах бд
            status_code_formaccess = await check_user_in_formaccess(uid)
            if status_code_formaccess == 0:
                await message.answer('При проверке пользователя на наличие в базе данных произошла неизвестная ошибка')
                return
            elif status_code_formaccess == 11:
                await message.answer('Пользователь, которому вы хотите выдать доступ к заполению формы, является администратором. Кикнете его с причиной "Перезаполнение" и выдайте форму снова.')
                return
            elif status_code_formaccess == 12:
                await message.answer('Пользователь, которому вы хотите выдать доступ к заполнению формы, является лидером/заместителем. Кикнете его с приной "Перезаполнение" и выдайте форму снова.')
                return
            elif status_code_formaccess == 13:
                await message.answer('Пользователь, которому вы хотите выдать доступ к заполнению формы уже его имеет и в данный момент находится на этапе заполнения.')
                return
            elif status_code_formaccess == 14:
                await message.answer('Пользователь, которому вы хотите выдать доступ к заполнению формы уже его имеет и в данный момент находится на этапе одобрения заявки администрацией.')

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
                    await set_formaccess(uid, adm_id, adm_name, type_form) # Запись формы в бд
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
                await message.answer('У вас нет прав для выдачи данной формы')
        else:
            await message.answer('Выберите тип формы. Чтобы посмотреть список введите /formaccess')
    else:
        syntax_message = "⚙ Используйте следующий синтаксис: /formaccess [@Упоминание] [Тип формы]\n\n" \
                         "🔢 Тип формы (Выдача доступа к заполнению формы с этим доступом):\n" \
                         "🗂 0 - Лидер/Заместитель\n" \
                         "🗂 1 - Следящие / ПГС / ЗГС / ГС Гос / Нелегалы\n" \
                         "🗂 2 - Дет.Сад/Тех. администратор\n" \
                         "🗂 3 - Куратор\n" \
                         "🗂 4 - Главный администратор/Заместитель главного администратора\n" \
                         "🗂 5 - Руководство Jantugei Inc"
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
            await message.answer('Неизвестная ошибка!')
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
async def cmd_fixbug(message: Message, id : int = None):
    if id is not None:
        msg = await for_cmd_fixbug(id)
        await message.answer(msg)
    else:
        await message.answer('Введите id баг репорта.')





