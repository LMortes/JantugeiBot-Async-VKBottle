import re
import discord
from vkbottle import GroupTypes, GroupEventType, Keyboard, Callback, KeyboardButtonColor
from vkbottle.bot import Message
from vkbottle.framework.labeler import BotLabeler
from check_dostup_rule import CheckUserDostup
from db_connect import *
from dialog_ids import *
from request_functions import *
from user_bot_functions import *
from message_constructor import *
from vkbottle.dispatch.rules.base import VBMLRule

bl = BotLabeler()
POLLING_IS_ON = True


# Команда для всех


@bl.message(VBMLRule('/status'))
async def cmd_status(message: Message):
    status = '⚙ Все системы работают в штатном режиме.\n' \
             '♻ Текущая версия бота - 0.1'
    await message.answer(status)


# Команды для 0 уровня доступа(лидер/зам) и выше


@bl.message(VBMLRule('/help'), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_help(message: Message):
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
                '0️⃣/info - посмотреть статистику пользователя(без параметров - своя статистика). \n' \
                '0️⃣/members - вывести актуальный список пользователей. \n' \
                '0️⃣/warnhistory - вывести историю выдачи или снятия наказаний у пользователя. \n' \
                '0️⃣/scorehistory - вывести историю выдачи или снятия баллов у пользователя. \n' \
                '0️⃣/dayshistory - вывести историю выдачи или снятия дней к сроку у пользователя. \n' \
                '0️⃣/getip - вывести информацию о айпи адресе. \n' \
                '0️⃣/fonline - вывести информацию о онлайне фракции.\n'
    if dostup >= 1:
        info += '1️⃣/online - посмотреть свой онлайн прямиком из логов. \n' \
                '1️⃣/checkblacklist - проверить находится ли пользователь в чс организаций по нику. \n'
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


@bl.message(VBMLRule('/dostup'), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_dostup(message: Message):
    await message.answer(f'🔢 Ваш уровень доступа: {await get_user_dostup(message.from_id)}')


@bl.chat_message(VBMLRule('/peer_id'), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_peer_id(message: Message):
    result_id = '💬 ID Беседы: ' + str(message.peer_id) + ' 💬'
    await message.answer(result_id)


@bl.message(VBMLRule(['/ao', '/ao <ping>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
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


@bl.message(VBMLRule(['/info', '/info <screen_name>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_info(message: Message, screen_name=None):
    dostup = await get_user_dostup(message.from_id)
    if screen_name is not None:  # Дописать info с параметрами
        try:
            uid = re.findall(r'[0-9]+', screen_name)[0]
            leader_info = await get_info_leader(uid)
            admin_info = await get_admin_info(uid)
            if leader_info["status"]:
                message_info_leader = await construct_message_info_leader(leader_info)
                await message.answer(message_info_leader)
            elif admin_info["status"]:
                message_info_admin = await construct_message_info_admin(admin_info)
                await message.answer(message_info_admin)
            else:
                await message.answer('⚠ Данный пользователь не найден в базе данных')
                pass  # Тут будет добыча из архива с доступом
        except:
            try:
                nickname = re.findall(r'\w+_\w+', screen_name)[0]
                leader_info = await get_info_leader_by_name(nickname)
                admin_info = await get_admin_info_by_name(nickname)
                if leader_info["status"]:
                    message_info_leader = await construct_message_info_leader(leader_info)
                    await message.answer(message_info_leader)
                elif admin_info["status"]:
                    message_info_admin = await construct_message_info_admin(admin_info)
                    await message.answer(message_info_admin)
                else:
                    await message.answer('⚠ Данный пользователь не найден в базе данных')
                    pass  # Тут будет добыча из архива с доступом
            except:
                if screen_name.startswith('@'):
                    await message.answer('⚠ Упоминание введено некорректно')
                else:
                    await message.answer('⚠ Используйте следующий синтаксис: /info Nick_Name или /info [@Упоминание]')
    else:
        if dostup == 0:
            leader_info = await get_info_leader(message.from_id)

            if leader_info["status"]:
                message_info_leader = await construct_message_info_leader(leader_info)
                await message.answer(message_info_leader)
        else:
            admin_info = await get_admin_info(message.from_id)
            if admin_info["status"]:
                message_info_admin = await construct_message_info_admin(admin_info)
                await message.answer(message_info_admin)


@bl.message(VBMLRule('/members'), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_members(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')


@bl.message(VBMLRule('/warnhistory'), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_warnhistory(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')


@bl.message(VBMLRule(['/scorehistory', '/scorehistory <screen_name>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_scorehistory(message: Message, screen_name=None):
    if screen_name is not None:
        screen_name_pat = re.compile("\[id[0-9]+")
        nickname_pat = re.compile("\w+_\w+")
        leader_info_scorehistory = {}
        message_not_find = '⚠ У пользователя с данным упоминанием/никнеймом не найдено записей изменений баллов'
        if re.match(screen_name_pat, screen_name):
            uid = re.findall(r'[0-9]+', screen_name)[0]
            info_scorehistory = await get_scorehistory_info_by_id(uid)
            if info_scorehistory["status"]:
                leader_info = await get_info_leader(uid)
                if leader_info["status"]:
                    leader_info_scorehistory = {
                        "vk_id": leader_info["leader_info"][1],
                        "name": leader_info["leader_info"][2],
                        "score": leader_info["leader_info"][10],
                    }
                    message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, leader_info_scorehistory)
                else:
                    admin_info = await get_admin_info(uid)
                    if admin_info["status"]:
                        admin_info_scorehistory = {
                            "vk_id": admin_info["admin_info"][1],
                            "name": admin_info["admin_info"][2],
                            "score": admin_info["admin_info"][10],
                        }
                        message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, admin_info_scorehistory)
                    else:
                        await message.answer('⚠ Данный пользователь снят! Команда на доработке, будет подтяжка из архива.')  # Дописать добычу данных из архива
                        message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, leader_info_scorehistory)
                await message.answer(message_info_scorehistory)
            else:
                await message.answer(message_not_find)
        elif re.match(nickname_pat, screen_name):
            nickname = screen_name
            info_scorehistory = await get_scorehistory_info_by_nickname(nickname)
            if info_scorehistory["status"]:
                leader_info = await get_info_leader_by_name(nickname)
                if leader_info["status"]:
                    leader_info_scorehistory = {
                        "vk_id": leader_info["leader_info"][1],
                        "name": leader_info["leader_info"][2],
                        "score": leader_info["leader_info"][10],
                    }
                    message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, leader_info_scorehistory)
                else:
                    admin_info = await get_admin_info_by_name(nickname)
                    if admin_info["status"]:
                        admin_info_scorehistory = {
                            "vk_id": admin_info["admin_info"][1],
                            "name": admin_info["admin_info"][2],
                            "score": admin_info["admin_info"][10],
                        }
                        message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, admin_info_scorehistory)
                    else:
                        await message.answer('Данный пользователь снят! Команда на доработке, будет подтяжка из архива.')  # Дописать добычу данных из архива
                        message_info_scorehistory = await construct_message_scorehistory(info_scorehistory, leader_info_scorehistory)
                await message.answer(message_info_scorehistory)
            else:
                await message.answer(message_not_find)
        else:
            await message.answer('⚠ Никнейм/упоминание введено некорректно. Формат: @Упоминание/Nick_Name')
    else:
        await message.answer('⚠ Используйте следующий синтаксис: /scorehistory [@Упоминание] или /scorehistory Nick_Name')


@bl.message(VBMLRule(['/dayshistory', '/dayshistory <screen_name>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_dayshistory(message: Message, screen_name=None):
    if screen_name is not None:
        screen_name_pat = re.compile("\[id[0-9]+")
        nickname_pat = re.compile("\w+_\w+")
        leader_info_dayshistory = {}
        message_not_find = '⚠ У пользователя с данным упоминанием/никнеймом не найдено записей изменений дней к сроку'
        if re.match(screen_name_pat, screen_name):
            uid = re.findall(r'[0-9]+', screen_name)[0]
            info_dayshistory = await get_dayshistory_info_by_id(uid)
            if info_dayshistory["status"]:
                leader_info = await get_info_leader(uid)
                if leader_info["status"]:
                    leader_info_dayshistory = {
                        "vk_id": leader_info["leader_info"][1],
                        "name": leader_info["leader_info"][2],
                        "start_date": leader_info["leader_info"][7],
                        "end_date": leader_info["leader_info"][8]
                    }
                    message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, leader_info_dayshistory)
                else:
                    admin_info = await get_admin_info(uid)
                    if admin_info["status"]:
                        admin_info_dayshistory = {
                            "vk_id": admin_info["admin_info"][1],
                            "name": admin_info["admin_info"][2],
                            "start_date": admin_info["admin_info"][8],
                            "end_date": admin_info["admin_info"][8],
                        }
                        message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, admin_info_dayshistory)
                    else:
                        await message.answer('⚠ Данный пользователь снят! Команда на доработке, будет подтяжка из архива.')  # Дописать добычу данных из архива
                        message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, leader_info_dayshistory)
                await message.answer(message_info_dayshistory)
            else:
                await message.answer(message_not_find)
        elif re.match(nickname_pat, screen_name):
            nickname = screen_name
            info_dayshistory = await get_dayshistory_info_by_nickname(nickname)
            if info_dayshistory["status"]:
                leader_info = await get_info_leader_by_name(nickname)
                if leader_info["status"]:
                    leader_info_dayshistory = {
                        "vk_id": leader_info["leader_info"][1],
                        "name": leader_info["leader_info"][2],
                        "start_date": leader_info["leader_info"][7],
                        "end_date": leader_info["leader_info"][8]
                    }
                    message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, leader_info_dayshistory)
                else:
                    admin_info = await get_admin_info_by_name(nickname)
                    if admin_info["status"]:
                        admin_info_dayshistory = {
                            "vk_id": admin_info["admin_info"][1],
                            "name": admin_info["admin_info"][2],
                            "start_date": admin_info["admin_info"][8],
                            "end_date": admin_info["admin_info"][8],
                        }
                        message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, admin_info_dayshistory)
                    else:
                        await message.answer('Данный пользователь снят! Команда на доработке, будет подтяжка из архива.')  # Дописать добычу данных из архива и проверку на адм
                        message_info_dayshistory = await construct_message_dayshistory(info_dayshistory, leader_info_dayshistory)
                await message.answer(message_info_dayshistory)
            else:
                await message.answer(message_not_find)
        else:
            await message.answer('⚠ Никнейм/упоминание введено некорректно. Формат: @Упоминание/Nick_Name')
    else:
        await message.answer('⚠ Используйте следующий синтаксис: /dayshistory [@Упоминание] или /dayshistory Nick_Name')


@bl.message(VBMLRule(['/getip', '/getip <ip>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_getip(message: Message, ip=None):
    if ip is not None:
        pat_ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if re.match(pat_ip, ip):
            response_ip_information = await api_prikol_get_ip(ip)
            if response_ip_information["status"]:
                message_ip_infomation = await construct_message_ip_information(response_ip_information)
                await message.answer(message_ip_infomation)
            else:
                await message.answer(
                    '⚠ Такого IP адреса не существует. Если это ошибка, обратитесь к руководству Jantugei Inc.')
        else:
            await message.answer('⚠ Неверный формат IP адреса или такого IP адреса не существует.')
    else:
        await message.answer('⚠ Используйте следующий синтаксис: /getip [ip] | Формат IP: x.x.x.x')


@bl.message(VBMLRule(['/fonline', '/fonline <server:int>', '/fonline <server:int> <fraction:int>']), CheckUserDostup([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_fonline(message: Message, server: int = None, fraction: int = None):
    message_syntax = '⚠ Используйте следующий синтаксис: /fonline [номер сервера(1-24)] [id фракции(1-29)]\n\n' \
                     '🔢 Доступные ID фракций:\n' \
                     '1 - LSPD🚨\n' \
                     '2 - RCPD🚨\n' \
                     '3 - FBI🚨\n' \
                     '4 - SFPD🚨\n' \
                     '5 - LSMC🚑\n' \
                     '6 - Правительство🗽\n' \
                     '7 - ТСР🚧\n' \
                     '8 - SFMC🚑\n' \
                     '9 - Автошкола🗾\n' \
                     '10 - СМИ ЛС📟\n' \
                     '11 - Grove🔫\n' \
                     '12 - Vagos🔫\n' \
                     '13 - Ballas🔫\n' \
                     '14 - Aztec🔫\n' \
                     '15 - Rifa🔫\n' \
                     '16 - RM🔪\n' \
                     '17 - Yakuza🔪\n' \
                     '18 - LCN🔪\n' \
                     '19 - Warlock MC🔪\n' \
                     '20 - Army LS🚧\n' \
                     '21 - Центральный банк💳\n' \
                     '22 - LVMC🚑\n' \
                     '23 - LVPD🚨\n' \
                     '24 - СМИ ЛВ📟\n' \
                     '25 - Night Wolves🔫\n' \
                     '26 - СМИ СФ📟\n' \
                     '27 - Army SF🚧\n' \
                     '29 - Страховая Компания📝'
    if server is not None:
        if 1 <= server <= 24:
            if fraction is not None:
                if (1 <= fraction <= 29) and (fraction != 28):
                    fonline_list = await api_prikol_fonline(server, fraction)
                    if fonline_list["status"]:
                        message_fonline = await construct_message_fonline(fonline_list["response_fonline"])
                        await message.answer(message_fonline)
                    else:
                        await message.answer('⚠ Произошла системная ошибка. Скорее всего вы ввели некорректные данные. Если это не так, обратитесь к руководству Jantugei Inc')
                else:
                    await message.answer('⚠ Такой фракции не существует. Ознакомьтесь со списком доступных фракций. Введите /fonline')
            else:
                await message.answer('⚠ Вы не ввели ID фракции. Ознакомьтесь со списком доступных фракций. Введите /fonline')
        else:
            await message.answer('⚠ Такого сервера не существует. Введите номер сервера от 1-24')
    else:
        await message.answer(message_syntax)


# Команды для 1 уровня доступа и выше

@bl.message(VBMLRule('/online'), CheckUserDostup([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_online(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')


@bl.message(VBMLRule(['/checkblacklist', '/checkblacklist <nickname>']),
            CheckUserDostup([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_checkblacklist(message: Message, nickname=None):
    if nickname is not None:
        try:
            nickname = re.findall(r'\w+_\w+', nickname)[0]
        except:
            await message.answer(
                '⚠ Никнейм пользователя введен некорректно. Формат: Nick_Name.')  # Пасхалка для тестеров, проверка качества работы
            return
        player_info_black = await get_info_blacklist_by_name(nickname)
        if player_info_black["status"]:
            message_player_info_black = await construct_message_info_blacklist(player_info_black)
            await message.answer(message_player_info_black)
        else:
            await message.answer('⚠ Данный пользователь не находится в черном списке.')
    else:
        await message.answer('♻ Используйте следующий синтаксис: /checkblacklist Nick_Name')


# Команды для 3 уровня доступа и выше


@bl.message(VBMLRule('/clrbuttons'), CheckUserDostup([3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_clrbuttons(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')


@bl.message(VBMLRule('/checknick'), CheckUserDostup([3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_checknick(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')


@bl.message(VBMLRule('/formslist'), CheckUserDostup([3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_formslist(message: Message):
    forms_info = await get_info_formaccess()
    if forms_info["status"]:
        try:
            message_info_formaccess = await construct_message_info_formaccess(forms_info)
            await message.answer(message_info_formaccess)
        except Exception as er:
            print('⚠ Ошибка в команде /formslist. Текст ошибки: ', er)
    else:
        await message.answer('⚠ На данный момент нет пользователей с доступом к форме')


@bl.message(VBMLRule('/getdsid'), CheckUserDostup([3, 4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_getdsid(message: Message):
    await message.answer('⚠ Данная команда находится на этапе разработки')
    # if screen_name is not None:
    #     try:
    #         intents = discord.Intents.default()
    #         intents.message_content = True
    #         client = discord.Client(intents=intents)
    #
    #
    #         id_dis = discord.utils.get(client.get_all_members(), name="LPollot", discriminator="1985")
    #     except Exception as er:
    #         print(er)
    #     print(id_dis)
    # else:
    #     await message.answer('⚠ Используйте следующий синтаксис: /getdsid [Имя пользователя]. Формат: Example#1234')

# Команды для 4 уровня доступа и выше

@bl.message(VBMLRule(['/msg', '/msg <chat_id> <text>']), CheckUserDostup([4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_msg(message: Message, chat_id=None, text=None):
    user_dostup = await get_user_dostup(message.from_id)
    dialogs = {
        "develop": DEVELOPER_DIALOG_ID,
        "testers": TESTERS_DIALOG_ID,
        "botfunc": FUNC_BOT_DIALOG_ID,
        "bottest": TEST_BOT_DIALOG_ID,
    }
    dialogs_names = list(dialogs.keys())
    if (chat_id is not None) and (chat_id in dialogs_names):
        if text is not None:
            admin_info = await get_admin_info(message.from_id)
            user_ids = []
            chat_id = dialogs[chat_id]
            try:
                objects_chat = await bot.api.messages.get_conversation_members(peer_id=chat_id)
            except:
                await message.answer('⚠ Сообщение не отправлось, скорее всего вы ввели несуществующий ID беседы')
                return
            for member in objects_chat.profiles:
                user_ids.append(member.id)
            message_text = await construct_message_cmdmsg(admin_info, text, user_ids)
            await bot.api.messages.send(peer_id=chat_id, message=message_text, random_id=0)
            await message.answer(f'♻ Сообщение успешно отправлено в беседу с ID: {chat_id}')
        else:
            await message.answer('⚠ Вы не ввели текст для отправки.')
    else:
        syntax_message = '⚠ Используйте следующий синтаксис: /msg [имя беседы] [Текст]\n' \
                         'Имена бесед:\n'
        id_dialogs = '[Тут будут другие беседы для следящих]\n'
        id_dialogs_develop = f'{list(dialogs.keys())[0]} - Беседа разработчиков Jantugei Inc\n'\
                             f'{list(dialogs.keys())[1]} - Беседа тестировщиков\n'\
                             f'{list(dialogs.keys())[2]} - Беседа с функциями бота\n'\
                             f'{list(dialogs.keys())[3]} - Беседа для тестов бота\n'
        syntax_message += id_dialogs
        if user_dostup == 11:
            syntax_message += id_dialogs_develop
        await message.answer(syntax_message)


@bl.message(VBMLRule(['/formremove', '/formremove <screen_name>']), CheckUserDostup([4, 5, 6, 7, 8, 9, 10, 11]))
async def cmd_formremove(message: Message, screen_name=None):
    if screen_name is not None:
        # Добыча id пользователя из упоминания
        try:
            uid = re.findall(r'[0-9]+', screen_name)[0]
        except:
            await message.answer('⚠ Упоминание введено некорректно или такого пользователя не существует')
        is_find_form_done = await is_find_current_form_done(uid)
        if not is_find_form_done:
            is_delete_formaccess = await remove_formaccess(uid)
            if is_delete_formaccess:
                await message.answer(f'Доступ к заполнению формы у [id{uid}|Пользователя] успешно снят.')
                adm_id = message.from_id
                adm_name = await get_user_name(adm_id)
                is_send_user_message = await send_user_message_formdecline(uid, adm_id, adm_name)
                if is_send_user_message:
                    await message.answer('✅ Отправка в личные сообщения успешна ✅')
                else:
                    await message.answer('🚫 Произвошла неизвестная ошибка при отправке в личные сообщения 🚫')
            else:
                await message.answer('⚠ Данный пользователь не имеет доступа к заполнению формы')
        else:
            message_find_form_done = '⚠ Данный пользователь находится на стадии одобрения, то есть он уже заполнил форму. В случае если это не так, обратитесь к руководству Jantugei Inc.'
            await message.answer(message_find_form_done)
    else:
        syntax_message = '⚠ Используйте следующий синтаксис: /formremove [@Упоминание]'
        await message.answer(syntax_message)


@bl.message(VBMLRule(['/formaccess', '/formaccess <screen_name> <type_form:int>']),
            CheckUserDostup([4, 5, 6, 7, 8, 9, 10, 11]))
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
                await message.answer(
                    '⚠ При проверке пользователя на наличие в базе данных произошла неизвестная ошибка')
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

@bl.message(VBMLRule(['/test', '/test <text>']), CheckUserDostup(11))
async def cmd_test(message: Message, text=None):
    if text is not None:
        adm_name = await get_user_name(message.from_id)
        try:
            await set_test_info(adm_name, text)
            await message.answer('✅ Тест успешно записан и передан тестироващикам!')
            await bot.api.messages.send(peer_id=TESTERS_DIALOG_ID,
                                        message='🔔 Поступил новый тест-репорт. Чтобы вывести список введите - /testlist 🔔',
                                        random_id=0)
        except:
            await message.answer('⚠ Неизвестная ошибка!')
    else:
        await message.answer('⚙ Используй следующий синтаксис: /test [суть теста]')


@bl.message(VBMLRule('/testlist'), CheckUserDostup(11))
async def cmd_testlist(message: Message):
    testlist_text = await get_testlist()
    await message.answer(testlist_text)


@bl.message(VBMLRule(['/bug', '/bug <id:int>', '/bug <id:int> <text>']), CheckUserDostup(11))
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


@bl.message(VBMLRule('/buglist'), CheckUserDostup(11))
async def cmd_buglist(message: Message):
    buglist_text = await get_buglist()
    await message.answer(buglist_text)


@bl.message(VBMLRule(['/fixbug', '/fixbug <id:int>']), CheckUserDostup(11))
async def cmd_fixbug(message: Message, id: int = None):
    if id is not None:
        msg = await for_cmd_fixbug(id)
        await message.answer(msg)
    else:
        await message.answer('Введите id баг репорта.')


@bl.message(VBMLRule('/formpolling'), CheckUserDostup(11))
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
                                              f'Префикс: {row[12]}\n' \
                                              f'Уровень администратора: {row[13]}\n' \
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
                await message.answer(
                    '⚠ Найдена форма на лидера и на администратора')  # Если есть форма на лидера и на админа
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
                                              f'Префикс: {row[12]}\n' \
                                              f'Уровень администратора: {row[13]}\n' \
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

            # else:
            #     await message.answer('✅ Ничего не найдено')  # Убрать, когда будет полностью рабочая система

            await asyncio.sleep(120)  # Задержка поллинга таблицы с формами
    except Exception as err:
        await message.answer('⚠ По неизвестной причине поллинг базы данных прекращен')
        print('⚠ По неизвестной причине поллинг базы данных прекращен. Ошибка: ', err)


@bl.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def click_button_form(event: GroupTypes.MessageEvent):
    try:
        dostup = await get_user_dostup(event.object.user_id)
        # Добыча id юзера из сообщения формы
        message_info = await bot.api.messages.get_by_conversation_message_id(peer_id=event.object.peer_id,
                                                                             conversation_message_ids=event.object.conversation_message_id)
        pre_user_id = re.findall(r'\[id[0-9]+', str(message_info))[0]
        user_id = re.findall(r'[0-9]+', pre_user_id)[0]
        is_find_form_done = await is_find_current_form_done(user_id)
        if dostup >= 4:
            # Проверка, действительна ли в данный момент эта форма
            if is_find_form_done:
                # Добыча имени юзера по id
                user_info = await get_current_info_form_done(user_id)
                user_name = user_info[3]
                # Добыча id и name админа выдавшего форму
                adm_id = event.object.user_id
                adm_name = await get_user_name(adm_id)
                # Сообщения статусов
                is_remove = ''
                message_decline = f'[id{event.object.user_id}|{adm_name}] отказал форму [id{user_id}|{user_name}]'
                message_accept = f'[id{event.object.user_id}|{adm_name}] одобрил форму [id{user_id}|{user_name}]'
                message_set = f'[id{user_id}|{user_name}] успешно добавлен в базу данных. Все доступы для заполнения форм сняты.'
                message_set_error = f'Произошла ошибка при добавлении [id{user_id}|{user_name}] в базу данных!'
                message_remove_form = '✅ Форма успешно удалена из базы данных. Все доступы к заполнению формы сняты.'
                message_remove_form_error = '⚠ Произошла ошибка при удалении формы из базы данных или форма была удалена ранее.'
                message_for_user = '✅ Отправка в личные сообщения успешна'
                message_for_user_error = '⚠ Произошла ошибка при отправке в личные сообшения.'
                # После нажатия на кнопку одобрить для лидерской формы
                if event.object.payload[
                    "cmd"] == "accept_leader_form":  # Дописать добавление ролей в дискорде и добавлене в беседы
                    await bot.api.messages.send(peer_id=event.object.peer_id, message=message_accept, random_id=0)
                    is_set_leader = await set_leader(user_id)
                    if is_set_leader:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_set, random_id=0)
                        is_send_user_message_accept = await send_user_message_formaccept(user_id, user_name, adm_id,
                                                                                         adm_name)
                        if is_send_user_message_accept:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user,
                                                        random_id=0)
                        else:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user_error,
                                                        random_id=0)
                    else:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_set_error,
                                                    random_id=0)
                # После нажатия на кнопку отклонить на лидерской и админской форме
                elif (event.object.payload["cmd"] == "decline_leader_form") or \
                        (event.object.payload["cmd"] == "decline_admin_form"):
                    await bot.api.messages.send(peer_id=event.object.peer_id, message=message_decline, random_id=0)
                    if event.object.payload["cmd"] == "decline_leader_form":
                        is_remove = await remove_formaccess_done_leader(user_id)
                    elif event.object.payload["cmd"] == "decline_admin_form":
                        is_remove = await remove_formaccess_done_admin(user_id)
                    if is_remove:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_remove_form,
                                                    random_id=0)
                        is_send_user_message = await send_user_message_formdecline(user_id, adm_id, adm_name)
                        if is_send_user_message:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user,
                                                        random_id=0)
                        else:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user_error,
                                                        random_id=0)
                    else:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_remove_form_error,
                                                    random_id=0)
                # После нажатия на кнопку одобрить на админской форме
                elif event.object.payload["cmd"] == "accept_admin_form":
                    await bot.api.messages.send(peer_id=event.object.peer_id,
                                                message=message_accept, random_id=0)
                    is_set_admin = await set_admin(user_id)
                    if is_set_admin:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_set, random_id=0)
                        is_send_user_message_accept = await send_user_message_formaccept(user_id, user_name, adm_id,
                                                                                         adm_name)
                        if is_send_user_message_accept:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user,
                                                        random_id=0)
                        else:
                            await bot.api.messages.send(peer_id=event.object.peer_id, message=message_for_user_error,
                                                        random_id=0)
                    else:
                        await bot.api.messages.send(peer_id=event.object.peer_id, message=message_set_error,
                                                    random_id=0)
    except Exception as er:
        print(er)
