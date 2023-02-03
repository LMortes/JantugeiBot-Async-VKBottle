from vkbottle.bot import Bot
from vkbottle.framework.labeler import BotLabeler
TOKEN = 'vk1.a.91FCwNF-7USpormLCs3yIDLnXxP6G6PXB31FeSh16dvZWZFCRgHJ2tvc_eg_s29qkQlBD_Y4r0Vs8T3qcqeDZArU9_mJFe5SOUxIqgr_5AUMh7PAAAxKWsVKWSHGE67xuIdC8vXF6GEAoOBGhJX7MG1kGUUG6bO5vr_hpfRu1dKEm1Z92ZxLHYIAYtwmFuPOdUSWiBYLtWY-rUFLcv9lzg'
APP_ID = '51531335'
GROUP_ID = '217675080'

labeler = BotLabeler()
bot = Bot(token=TOKEN, labeler=labeler)