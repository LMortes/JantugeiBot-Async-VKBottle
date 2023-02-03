from typing import Union, List
from vkbottle.dispatch.rules import ABCRule
from vkbottle.bot import Message
from db_connect import get_user_dostup

class CheckUserDostup(ABCRule[Message]):
    def __init__(self, dostups: Union[List[int], int]):
        if not isinstance(dostups, list):
            dostups = [dostups]
        self.udostups = dostups

    async def check(self, event: Message) -> bool:
        user_id = event.from_id
        dostup = await get_user_dostup(user_id)
        return dostup in self.udostups
