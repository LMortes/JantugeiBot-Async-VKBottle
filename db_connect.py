import asyncio
import aiomysql

host = '92.53.99.174'
user = 'jantugei.ru'
password = 'aM0yC8jI0f'
db_name = 'jantugei.ru'
loop = asyncio.get_event_loop()

async def connection(loop):
    try:
        # global conn
        conn = await aiomysql.connect(host=host,
                                      user=user, password=password, db=db_name,
                                      loop=loop)
        # print('Подключение к базе данных прошло успешно')
        return conn
    except:
        print('Возникла ошибка при подключении к базе данных')

# Геттеры

async def get_user_dostup(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT dostup FROM admins WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount <= 0:
                await cur.execute("SELECT id FROM leaders WHERE vk_id=%s", user_id)
                await conn.commit()
                if cur.rowcount <= 0:
                    return -1
                else:
                    return 0
            else:
                r = await cur.fetchone()
                return r[0]

# Каждые 3 минуты чекает базу на наличие заполненных форм
async def get_info_from_formaccess_done():
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM form_done_leader")
            await conn.commit()
            if cur.rowcount > 0:
                await cur.execute("SELECT * FROM form_done_adm")
                await conn.commit()
                if cur.rowcount > 0:
                    return 3  # Найдены формы и на лидера и на админа
                else:
                    return 2  # Найдена форма на лидера
            else:
                await cur.execute("SELECT * FROM form_done_adm")
                await conn.commit()
                if cur.rowcount > 0:
                    return 1  # Найдена форма на админа
                else:
                    return 0  # Ничего не найдено

            # if cur.rowcount <= 0:
            #     await cur.execute("SELECT * FROM form_done_adm")
            #     await conn.commit()
            #     if cur.rowcount <= 0:
            #         return 0 # Ничего не найдено
            #     else:
            #         return 1    # Найдена форма на админа
            # else:
            #     return 2    # Найдена форма на лмдера


# Доделать, разделение 3 тестов в разные переменные
async def get_testlist():
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM test_report")
            await conn.commit()
            row = await cur.fetchall()
            count_tests = cur.rowcount
            test_text = ''
            if count_tests != 0:
                for rows in range(count_tests):
                    test_text += f'⚙ Тест репорт от {row[rows][1]}\n💬 Суть тест репорта: {row[rows][2]}\n📅 Дата тест репорта: {row[rows][3]}\n\nИспользуй /bug {row[rows][0]} [Что исправить]\n\n'
            result_test_text = f'⚠ Найдено {count_tests} тест репортов\n\n' + test_text
            return result_test_text


async def get_buglist():
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM bug_report")
            await conn.commit()
            row = await cur.fetchall()
            count_bugs = cur.rowcount
            bug_text = ''
            count_unfixed_bugs = 0
            if count_bugs != 0:
                for rows in range(count_bugs):
                    if row[rows][5] == 0:
                        bug_text += f'♻ Баг репорт от {row[rows][1]}\n⚙ Что тестировалось: {row[rows][2]}\n💬 Найденные баги: {row[rows][3]}\n📅 Дата баг репорта: {row[rows][4]}\n\nДля закрытия баг репорта используй /fixbug {row[rows][0]}\n\n'
                        count_unfixed_bugs += 1
            result_bug_text = f'⚠ Найдено {count_unfixed_bugs} баг репортов\n\n' + bug_text
            return result_bug_text


async def for_cmd_bug(adm_name, test_id, bug_text):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT test_text FROM test_report WHERE id=%s", test_id)
            await conn.commit()
            count_rows_delete = cur.rowcount
            try:
                row = await cur.fetchone()
                last_text = row[0]
            except:
                pass
        if count_rows_delete != 0 and count_rows_delete != -1:
            async with conn.cursor() as cur:
                await cur.execute("DELETE FROM `test_report` WHERE id=%s", test_id)
                await conn.commit()
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO `bug_report`(`adm_name`, `last_text`, `bug_text`, `date`, `is_fixed`) VALUES (%s, %s, %s, CURRENT_DATE(), 0)",
                    (adm_name, last_text, bug_text))
                await conn.commit()
        if count_rows_delete == 0 or count_rows_delete == -1:
            result_message = f'⛔ Тест репорта под номером {test_id} не существует'
        else:
            result_message = f'✅ Тест репорт под номером {test_id} успешно отправлен на фикс.'
        return result_message


async def for_cmd_fixbug(bug_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT bug_text FROM bug_report WHERE id=%s AND is_fixed=0", bug_id)
            await conn.commit()
            count_rows_bugs = 0
            try:
                count_rows_bugs = cur.rowcount
            except:
                pass
        if count_rows_bugs != 0 and count_rows_bugs != -1:
            async with conn.cursor() as cur:
                await cur.execute("UPDATE bug_report SET `is_fixed`=1 WHERE id=%s", bug_id)
                await conn.commit()
        if count_rows_bugs == 0 or count_rows_bugs == -1:
            result_message = f'⛔ Баг репорта под номером {bug_id} не существует'
        else:
            result_message = f'✅ Баг репорт под номером {bug_id} пофикшен и занесен в архив.'
        return result_message




async def get_user_name(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT server_name FROM admins WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount <= 0:
                await cur.execute("SELECT server_name FROM leaders WHERE vk_id=%s", user_id)
                await conn.commit()
                if cur.rowcount <= 0:
                    return 0
                else:
                    leader_name = await cur.fetchone()
                    return leader_name[0]
            else:
                admin_name = await cur.fetchone()
                return admin_name[0]


async def check_user_in_formaccess(user_id):
    # 0 - Неизвестная ошибка
    # 10 - Все ок
    # 11 - Пользователь админ
    # 12 - Пользователь лидер/зам
    # 13 - Пользователю уже выдана форма (этап заполнения)
    # 14 - Пользователю уже выдана форма (этап одобрения)
    statusCode = 0
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT is_check FROM formaccess WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount <= 0:
                await cur.execute("SELECT id FROM leaders WHERE vk_id=%s", user_id)
                await conn.commit()
                if cur.rowcount <= 0:
                    await cur.execute("SELECT id FROM admins WHERE vk_id=%s", user_id)
                    await conn.commit()
                    if cur.rowcount <= 0:
                        statusCode = 10
                        return statusCode
                    else:
                        statusCode = 11
                        return statusCode
                else:
                    statusCode = 12
                    return statusCode
            else:
                row = await cur.fetchone()
                is_check = row[0]
                if is_check:
                    statusCode = 14
                    return statusCode
                else:
                    statusCode = 13
                    return statusCode
        return statusCode


async def get_info_form_leader():  # Добыть все строки из таблицы form_done_leader
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM form_done_leader")
            await conn.commit()
            form_info = await cur.fetchall()
            return form_info


# Добыть все строки из таблицы form_done_adm
async def get_info_form_adm():  # Дописать в распределение по беседам в зависимости от доступа
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM form_done_adm")
            await conn.commit()
            form_info = await cur.fetchall()
            return form_info


# Добыть строку из таблицы form_done_* по конкретному id
async def get_current_info_form_done(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM form_done_leader WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                info = await cur.fetchall()
            else:
                await cur.execute("SELECT * FROM form_done_adm WHERE vk_id=%s", user_id)
                await conn.commit()
                info = await cur.fetchall()
        return info[0]


async def get_info_leader(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM leaders WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                leader_info = await cur.fetchone()
                response_leader_info = {
                    "leader_info": leader_info,
                    "status": True
                }
            else:
                response_leader_info = {
                    "leader_info": [],
                    "status": False
                }
        return response_leader_info

async def get_admin_info(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM admins WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                admin_info = await cur.fetchone()
                response_admin_info = {
                    "admin_info": admin_info,
                    "status": True
                }
            else:
                response_admin_info = {
                    "admin_info": [],
                    "status": False
                }
        return response_admin_info


async def get_info_leader_by_name(nickname):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM leaders WHERE server_name=%s", nickname)
            await conn.commit()
            if cur.rowcount > 0:
                leader_info = await cur.fetchone()
                response_leader_info = {
                    "leader_info": leader_info,
                    "status": True
                }
            else:
                response_leader_info = {
                    "leader_info": [],
                    "status": False
                }
        return response_leader_info


async def get_admin_info_by_name(nickname):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM admins WHERE server_name=%s", nickname)
            await conn.commit()
            if cur.rowcount > 0:
                admin_info = await cur.fetchone()
                response_admin_info = {
                    "admin_info": admin_info,
                    "status": True
                }
            else:
                response_admin_info = {
                    "admin_info": [],
                    "status": False
                }
        return response_admin_info


# Есть ли записи по id в таблицах form_done_leader и form_done_adm
async def is_find_current_form_done(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM form_done_leader WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                return True
            else:
                await cur.execute("SELECT * FROM form_done_adm WHERE vk_id=%s", user_id)
                await conn.commit()
                if cur.rowcount > 0:
                    return True
                else:
                    return False


async def get_info_blacklist_by_name(nickname):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM blacklist WHERE server_name=%s", nickname)
            await conn.commit()
            if cur.rowcount > 0:
                row_player_info = await cur.fetchone()
                player_info_black = {
                    "player_info": row_player_info,
                    "status": True,
                }
            else:
                player_info_black = {
                    "player_info": [],
                    "status": False,
                }
        return player_info_black


async def get_info_formaccess():
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM formaccess")
            if cur.rowcount > 0:
                rows_info_formaccess = await cur.fetchall()
                info_formaccess = {
                    "info_formaccess": rows_info_formaccess,
                    "status": True,
                }
            else:
                info_formaccess = {
                    "info_formaccess": [],
                    "status": False
                }
        return info_formaccess

# Сеттеры и удаление


async def set_test_info(adm_name, test_text):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("INSERT INTO `test_report`(`adm_name`, `test_text`, `date`) VALUES (%s, %s, CURRENT_DATE())",
                              (adm_name, test_text,))
            await conn.commit()
        return True


async def set_formaccess(uid, adm_id, adm_name, type_form):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                "INSERT INTO `formaccess`(`vk_id`, `type_form`, `vk_id_adm`, `name_adm`, `is_check`) VALUES (%s, %s, %s, %s, 0)",
                (uid, type_form, adm_id, adm_name))
            await conn.commit()
        return True


async def set_leader(user_id):
    async with await connection(loop) as conn:
        try:
            async with conn.cursor() as cur:  # Добыча информации из form_done_leader
                await cur.execute("SELECT * FROM form_done_leader WHERE vk_id=%s", user_id)
                await conn.commit()
                form_leader_info = await cur.fetchone()
            async with conn.cursor() as cur:  # Занесение лидера в общую талицу leaders
                await cur.execute(
                    "INSERT INTO `leaders`(`vk_id`, `server_name`, `org`, `status`, `vigs`, `warns`, `start_date`, `end_date`, `score`, `age_reallife`, `forumprofile`, `discord`) VALUES (%s, %s, %s, %s, 0, 0, CURRENT_DATE(), TIMESTAMPADD(DAY, 30, CURRENT_DATE()), 0, %s, %s, %s)",
                    (form_leader_info[1],
                     form_leader_info[3],
                     form_leader_info[5],
                     form_leader_info[4],
                     form_leader_info[2],
                     form_leader_info[6],
                     form_leader_info[7]))
                await conn.commit()
            is_remove = await remove_formaccess_done_leader(user_id)  # Удаление лидера из formaccess и form_done_leader
            return True
        except:
            return False


async def set_admin(user_id):
    async with await connection(loop) as conn:
        try:
            async with conn.cursor() as cur:  # Добыча информации из form_done_adm
                await cur.execute("SELECT * FROM form_done_adm WHERE vk_id=%s", user_id)
                await conn.commit()
                form_adm_info = await cur.fetchone()
            async with conn.cursor() as cur:  # Занесение админа в общую таблицу admins
                await cur.execute("INSERT INTO `admins`(`vk_id`, `server_name`, `age`, `prefix`, `post`, `dostup`, `adm_lvl`, `start_date`, `adm_days`, `score`, `forumprofile`, `discord`) VALUES (%s, %s, %s, %s, %s, %s, %s, CURRENT_DATE(), 0, 0, %s, %s)",
                    (form_adm_info[1],
                     form_adm_info[3],
                     form_adm_info[2],
                     form_adm_info[12],
                     form_adm_info[4],
                     form_adm_info[11],
                     form_adm_info[13],
                     form_adm_info[6],
                     form_adm_info[7]))
                await conn.commit()
            is_remove = await remove_formaccess_done_admin(user_id)  # Удаление админа из formaccess и form_done_adm
            return True
        except Exception as er:
            print(er)
            return False


async def remove_formaccess(user_id):
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("DELETE FROM `formaccess` WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                return True  # Если форма найдена, то она удаляется и возвращается True
            else:
                return False  # Если форма не найдена возвращается False


async def remove_formaccess_done_leader(user_id):
    await remove_formaccess(user_id)
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("DELETE FROM `form_done_leader` WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                return True
            else:
                return False


async def remove_formaccess_done_admin(user_id):
    await remove_formaccess(user_id)
    async with await connection(loop) as conn:
        async with conn.cursor() as cur:
            await cur.execute("DELETE FROM `form_done_adm` WHERE vk_id=%s", user_id)
            await conn.commit()
            if cur.rowcount > 0:
                return True
            else:
                return False
