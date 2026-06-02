import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

TOKEN = "8811950693:AAEduy9KwB5jRFN0_FIAXMk8dSuPd53L3s4"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! Это твой первый бот, запущенный на Linux!"
    )


@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал мне: {message.text}")


async def main():
    print("Бот успешно запущен и слушает команды...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
