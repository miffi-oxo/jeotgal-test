import discord
from discord.ext import commands, tasks
import datetime
import requests
import NMwordDetection.word_detection as word_detection # 비속어 필터링
import NMwordDetection.filter1 as filter1
import NMwordDetection.filter2 as filter2

a = word_detection.word_detection()
lst = a.load_word_list("/home/miffi_oxo/jeotgal-test/Badwords.txt")

global duration
duration = 60

intents = discord.Intents().all()
bot = commands.Bot(command_prefix=['$', ], intents=intents)

MSG_TO_TIMEOUT = {}


def timeout_user(bot, user_id, guild_id, expiration):
    url = "https://discord.com/api/v9/" + f'guilds/{guild_id}/members/{user_id}'

    headers = {"Authorization": f"Bot {bot.http.token}"}
    if expiration is not None:
        until = expiration.isoformat()
    json = {'communication_disabled_until': until}

    session = requests.patch(url, json=json, headers=headers)
    return session.status_code


class Timeout:
    def __init__(self, bot, message, **kwargs):
        self.bot = bot
        self.activated = True
        self.message = message
        self.feedback_message = None
        self.target_users = message.author
        self.channel = message.channel
        self.guild = message.guild
        self.expire_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=30)

        for kw in kwargs:
            if kw not in duration:
                raise ValueError

            duration[kw] = kwargs[kw]

    # 타임아웃 기능
    async def execute_timeout(self):
        self.activated = False
        if self.target_users != self.bot.user:
            self.expire_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=duration)
            status = timeout_user(self.bot, self.target_users.id, self.guild.id, self.expire_at)
            users = self.target_users
            if status == 200:  # HTTP Patch success
                self.feedback_message = await self.channel.send(f"{users.mention}에게 타임아웃을 적용합니다. 반성하세요.")

    async def expire(self):
        if datetime.datetime.utcnow() > self.expire_at:
            users = self.target_users
            """
            if self.feedback_message:
                await self.channel.send(f"{users.mention}에게 적용된 타임아웃을 해제합니다.")  # 봇 메시지
            """
            return True
        else:
            return False


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    channel = message.channel
    author = message.author
    if message.content.startswith('$duration'):  # 타임아웃 시간 설정
        global duration
        if len(message.content) > 9:
            duration = int(message.content[9:])
        await channel.send(f"타임아웃 시간: {duration}")
    if author.bot:
        return None
    detection_result = a.word_detect(message.content, 0.7)
    # if any(word in detection_result for word in lst):
    for filter_result in detection_result.values():
        if isinstance(filter_result, dict) and 'result' in filter_result and filter_result['result']:
            to = Timeout(bot, message)
            MSG_TO_TIMEOUT[message] = to
            await to.execute_timeout()
        
    await bot.process_commands(message)


@tasks.loop(seconds=10)
async def pool():
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
