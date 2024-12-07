import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import URLInputFile
from datetime import datetime
import random
from keep_alive import keep_alive
keep_alive()


# Укажите ваш токен бота, ID канала и ID администратора
BOT_TOKEN = "7931487253:AAEs9j_JOu6aqnQ-nnG8U3RHK5sQOwT4mq0"
CHANNEL_ID = "-1002311771602"  # Например: "@mychannel"
ADMIN_ID = 1306241821  # Замените на ваш Telegram ID

# Укажите путь к папке с фотографиями
PHOTO_FOLDER = "test_photo"

# Создаем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def send_message_to_admin(message: str):
    """Отправка сообщения администратору."""
    try:
        await bot.send_message(ADMIN_ID, message)

        image = URLInputFile(
            "https://cataas.com/cat?position=center&html=false&json=false",
            filename="python-logo.png"
        )
        await bot.send_photo(chat_id=ADMIN_ID, photo=image)
    except Exception as e:
        print(f"Ошибка при отправке сообщения администратору: {e}")


async def publish_photo():
    """Основная логика публикации фотографии каждый час."""
    try:
        # Создаем объект InputFile и отправляем фотографию
        image = URLInputFile(
            "https://cataas.com/cat?position=center&html=false&json=false",
            filename="python-logo.png"
        )
        await bot.send_photo(chat_id=CHANNEL_ID, photo=image, caption="@kotekets")
        await send_message_to_admin("Фото отправлено")
    except Exception as e:
        print(f"Ошибка при отправке фото: {e}")
        await send_message_to_admin(f"Фото не отправлено: {e}")


async def periodic_task():
    """Задача, которая запускается каждый час для отправки фото."""
    while True:
        await publish_photo()  # Публикуем фото
        wait_time = random.randint(3000, 4000)
        await asyncio.sleep(3600)  # Отправляем фото раз в час


# Главная функция
async def main():
    # Уведомляем администратора, что бот запущен
    await send_message_to_admin("Бот запущен и готов к работе!")

    # Запускаем задачу для публикации фото
    await periodic_task()


if __name__ == "__main__":
    asyncio.run(main())
