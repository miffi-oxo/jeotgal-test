import discord
from discord.ext import commands, tasks
import datetime
import requests

# 디스코드 봇 설정
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['$', ], intents=intents)

# 타임아웃 관련 딕셔너리
MSG_TO_TIMEOUT = {}


# HTTP PATCH 요청을 통해 타임아웃 적용하는 함수
def timeout_user(bot, user_id, guild_id, expiration):
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    headers = {"Authorization": f"Bot {bot.http.token}"}
    json = {"communication_disabled_until": expiration.isoformat() if expiration else None}
    session = requests.patch(url, json=json, headers=headers)
    return session.status_code == 204


# 타임아웃 클래스
class Timeout:
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
        self.target_user = message.author
        self.channel = message.channel
        self.guild = message.guild
        self.expire_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)

    # 타임아웃 적용
    async def apply_timeout(self):
        if self.target_user != self.bot.user:
            status = timeout_user(self.bot, self.target_user.id, self.guild.id, self.expire_at)
            if status:
                await self.channel.send(f"{self.target_user.mention}님이 60초 동안 타임아웃되었습니다.")
            #else:

    # 타임아웃 해제
    async def expire(self):
        if datetime.datetime.utcnow() > self.expire_at:
            return True
        return False


@bot.event
async def on_ready():
    print('봇이 로그인하였습니다.')


@bot.event
async def on_message(message):
    channel = message.channel
    author = message.author

    if author.bot:
        return
		
		# 오소리 금칙어 리스트
		# 이모지 :badger:는 필터링 실패
    badget_list = ["오소리", "오쏘리", "5소리", "소리님", "badger", "🦡", "족제비", "파이브사운드"]
    if any(word in message.content for word in badget_list):
        to = Timeout(bot, message)
        MSG_TO_TIMEOUT[message] = to
        await to.apply_timeout()

    await bot.process_commands(message)


@tasks.loop(seconds=10)
async def check_timeouts():
    expired = []

    for msg in MSG_TO_TIMEOUT:
        to = MSG_TO_TIMEOUT[msg]

        if await to.expire():
            expired.append(msg)

    for msg in expired:
        MSG_TO_TIMEOUT.pop(msg)

async def main():
	async with bot:
		pool.start()
		with open('/home/miffi_oxo/jeotgal-test/token.txt') as f:
			TOKEN = f.read()
		await bot.start(TOKEN)

if __name__ == '__main__':
	asyncio.run(main())
