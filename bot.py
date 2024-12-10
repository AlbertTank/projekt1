from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

API_TOKEN = "7171607576:AAG5y6054VyLTJVU-nn5Vh8CNoUWBmZsnQE"  # Убедись, что вставил правильный токен

# Создаем бота
bot = Bot(token=API_TOKEN)
# Создаем диспетчер
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def send_welcome(message: Message):
    await message.answer("Привет! Это твой новый бот.")

# Главная функция
async def main():
    print("Запуск бота...")
    try:
        # Запуск бота с использованием метода start_polling
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())