import logging
from aiogram import types
from aiogram.types import Message, InputFile
from keyboards.default.button import foymenu
from keyboards.default.adminbutton import adminmenu

from keyboards.inline.botton import royhatdanotish, admin
from loader import dp


@dp.message_handler(text="Ilovani yuklash")
async def send_apk(message: Message):
    await message.answer_document('BQACAgIAAxkBAANTZg_ILpJtFKrqY5T5_U6NewgAATIWAAI7QgACpaVASKuWEly6brNENAQ',
                                  caption='Bu ilova faqat Android uchun !', )


@dp.message_handler(text="Web-siteni ko'rish")
async def select_loc(message: Message):
    photo_file = InputFile(path_or_bytesio="downloads/rasm.jpg")
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer_photo(photo_file, caption="Web-siteni ochish uchun tugmani bosing !",
                               reply_markup=royhatdanotish)


@dp.message_handler(text="Admin-panel ilovasini yuklash !")
async def send_apk(message: Message):
    await message.answer_document('BQACAgIAAxkBAANVZg_IqiCmFz54vzg7Pxi8fHGMg4MAAvdHAAITD4FIvfIJsEoFiFI0BA',
                                  caption='Bu ilova faqat Android uchun !', )


@dp.message_handler(text="Admin Panelni ko'rish")
async def select_loc(message: Message):
    photo_file = InputFile(path_or_bytesio="downloads/rasm.jpg")
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer_photo(photo_file, caption="Web-siteniochish uchun tugmani bosing !",
                               reply_markup=admin)
