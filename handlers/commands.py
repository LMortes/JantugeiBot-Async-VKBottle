import re

from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler
from check_dostup_rule import CheckUserDostup
from db_connect import *
from settings import bot

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


