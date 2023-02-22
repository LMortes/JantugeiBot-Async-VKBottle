from settings import PRIKOL_TOKEN
import aiohttp

headers = {
    'Authorization': f'Bearer {PRIKOL_TOKEN}'
}


async def api_prikol_get_ip(ip):
    request_uri = f'https://api.vprikol.dev/ip?language=ru&ip={ip}'
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(request_uri) as response:
            if response.status == 200:
                response_json = await response.json()
                response_ip = {
                    "response_ip": response_json,
                    "status": True,
                }
            else:
                response_ip = {
                    "response_ip": {},
                    "status": False,
                }
            return response_ip

