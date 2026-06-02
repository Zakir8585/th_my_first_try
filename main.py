import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

current_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(current_dir, ".env")
load_dotenv(dotenv_path=env_path)

TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_main_keyboard():
    buttons = [
        [InlineKeyboardButton(text="🚀 Запустить парсер", callback_data="run_parser")],
        [
            InlineKeyboardButton(
                text="📂 Мой GitHub", url="https://github.com/Zakir8585"
            )
        ],
    ]

    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    user_name = message.from_user.full_name

    await message.answer(
        text=f"Привет, {user_name}! Я твой первый продвинутый бот. Выбери действие на кнопках ниже:",
        reply_markup=get_main_keyboard(),
    )
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(f"Ты написал мне: {message.text}")

@dp.callback_query(lambda callback: callback.data == "run_parser")
async def process_run_parser(callback: types.CallbackQuery):
    await callback.answer(text="Парсер запускается...")
    await callback.message.answer("Имитация парсинга: Сбор данных с сайтов успешно завершен! Собрано 42 товара.")

async def main():
    print("Бот успешно запущен и слушает команды...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())