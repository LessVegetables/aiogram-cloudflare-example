import typing_inspection
import typing_extensions
import pydantic_core
import annotated_types
import propcache
import multidict
import idna
import yarl
import frozenlist
import attrs
import aiosignal
import aiohappyeyeballs
import pydantic
import certifi

import aiohttp


# from urllib.parse import urlparse

# from aiogram import Bot
# from workers import Response, WorkerEntrypoint

# from .bot import dp


# def get_base_url(request) -> str:
#     url = urlparse(request.url)
#     return f"{url.scheme}://{url.netloc}"


# class Default(WorkerEntrypoint):
#     async def fetch(self, request):
#         path = urlparse(request.url).path
#         method = request.method.upper()

#         if method == "GET" and path == "/":
#             return Response("OK", status=200)

#         if method == "POST" and path == "/webhook":
#             received_secret = request.headers.get("X-Telegram-Bot-Api-Secret-Token")
#             expected_secret = self.env.TELEGRAM_SECRET

#             if not received_secret or received_secret != expected_secret:
#                 return Response("Unauthorized", status=401)

#             update = await request.json()

#             async with Bot(token=self.env.BOT_TOKEN) as bot:
#                 await dp.feed_raw_update(bot, update)

#             return Response("OK", status=200)

#         if method == "POST" and path == "/register":
#             admin_key = request.headers.get("X-Admin-Key")
#             if not admin_key or admin_key != self.env.ADMIN_KEY:
#                 return Response("Forbidden", status=403)

#             webhook_url = f"{get_base_url(request)}/webhook"

#             async with Bot(token=self.env.BOT_TOKEN) as bot:
#                 await bot.set_webhook(
#                     url=webhook_url,
#                     secret_token=self.env.TELEGRAM_SECRET,
#                     drop_pending_updates=True,
#                 )

#             return Response(f"Webhook registered: {webhook_url}", status=200)

#         if method == "POST" and path == "/unregister":
#             admin_key = request.headers.get("X-Admin-Key")
#             if not admin_key or admin_key != self.env.ADMIN_KEY:
#                 return Response("Forbidden", status=403)

#             async with Bot(token=self.env.BOT_TOKEN) as bot:
#                 await bot.delete_webhook(drop_pending_updates=False)

#             return Response("Webhook removed", status=200)

#         return Response("Not Found", status=404)


from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response("hello")