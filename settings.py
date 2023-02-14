from vkbottle.bot import Bot
from vkbottle import API
from vkbottle.framework.labeler import BotLabeler
TOKEN = 'vk1.a.91FCwNF-7USpormLCs3yIDLnXxP6G6PXB31FeSh16dvZWZFCRgHJ2tvc_eg_s29qkQlBD_Y4r0Vs8T3qcqeDZArU9_mJFe5SOUxIqgr_5AUMh7PAAAxKWsVKWSHGE67xuIdC8vXF6GEAoOBGhJX7MG1kGUUG6bO5vr_hpfRu1dKEm1Z92ZxLHYIAYtwmFuPOdUSWiBYLtWY-rUFLcv9lzg'
USER_TOKEN = 'vk1.a.sFYE9YdsmXtn167iFyhCVKR1lJGwZUz3HE_JNL7EMHsnuIoFQ6ghDmsoRZGo-q9m5JY3sYUDFw7uJoGfhdvApo72NdsjNBihL4XLZbhwHrk0dscKf3WfS1TkDZjsdlKQgwmPGJeYKNOIXLogKPSXfDo3A4B0M2w8zOxB1gCsmTa4nj8XyPMM9a88lXHKknsTHrP4HQctO2MedV9ixkLdkw'
USER_BOT_ID = '781789546'
APP_ID = '51531335'
GROUP_ID = '217675080'


labeler = BotLabeler()
bot = Bot(token=TOKEN, labeler=labeler)
api = API(USER_TOKEN)
