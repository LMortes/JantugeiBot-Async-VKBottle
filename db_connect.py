import asyncio
import aiomysql

host = '92.53.99.174'
user = 'jantugei.ru'
password = 'aM0yC8jI0f'
db_name = 'jantugei.ru'


async def connection(loop):
    try:
        global conn
        conn = await aiomysql.connect(host=host,
                                      user=user, password=password, db=db_name,
                                      loop=loop)
        print('Подключение к базе данных прошло успешно')

    except:
        print('Возникла ошибка при подключении к базе данных')

# Геттеры

# Доделать, разделение 3 тестов в разные переменные
async def get_testlist():
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


async def get_user_dostup(user_id):
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


async def get_user_name(user_id):
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

# Сеттеры


async def set_test_info(adm_name, test_text):
    async with conn.cursor() as cur:
        await cur.execute("INSERT INTO `test_report`(`adm_name`, `test_text`, `date`) VALUES (%s, %s, CURRENT_DATE())", (adm_name, test_text,))
        await conn.commit()
    return True
