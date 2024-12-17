import os
from dotenv import load_dotenv
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram import F
from ultralytics import YOLO


load_dotenv()


BOT_TOKEN = os.getenv("TG_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_file_name() -> str:
    t = datetime.now()
    return f"photo_{t.day}-{t.month}-{t.year}_{t.hour}-{t.minute}-{t.second}"


def path_to_save_photo(file_name: str) -> str:
    model = YOLO("bot/best.pt")
    file_path = f"data/{file_name}.jpg"

    results = model.predict(file_path)
    result = results[0]
    result.boxes

    res = result[0]
    path_to_save_photo = f"data/res_{file_name}.jpg"
    res.save(filename=path_to_save_photo)

    return path_to_save_photo


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        (
            "Привет!\n"
            "Я бот для поиск лесных пожаров на спутниковом снимке.\n"
            "\n"
            "Пришли мне фото и я помогу тебе."
        )
    )


@dp.message(F.photo)
async def get_photo(message: Message):
    photo = message.photo[-1]
    file_id = photo.file_id
    file = await bot.get_file(file_id)
    file_name = get_file_name()
    file_path = f"data/{file_name}.jpg"

    await bot.download_file(file.file_path, file_path)
    await message.answer(text="Фото обрабатывается.")
    photo = FSInputFile(
        path_to_save_photo(file_name),
    )
    await message.answer_photo(photo)


@dp.message()
async def send_echo(message: Message):
    await message.reply(text="Это не фото")


if __name__ == "__main__":
    dp.run_polling(bot)
