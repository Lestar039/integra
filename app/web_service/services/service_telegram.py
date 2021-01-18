from bot_config import INTEGRA_DATE_BOT

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = INTEGRA_DATE_BOT


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Welcome, {message.from_user.username}!\nCommand list:\n/help\n/show_id")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(f"Command list:\n/help\n/show_id")


@dp.message_handler(commands=['show_id'])
async def process_show_id_command(message: types.Message):
    await message.reply(f"Set the Telegram chat ID - {message.from_user.id} \n"
                        f"in your Profile for receive any alerts")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
