from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token
from news import fresh_news, get_news

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
	start_buttons = ['All_news', 'Fresh_news', 'Last_five']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer("Привет! Я Бот JournalistKz созданный мастером @Meteorit0s. \n\n Используя кнопки, вы можете получать новости из мира спорта в KZ.", reply_markup=keyboard)

@dp.message_handler(Text(equals="Fresh_news"))
async def get_fresh(message:types.Message):
	ans = fresh_news()
	for i in ans:
		await message.answer(i)


@dp.message_handler(Text(equals="All_news"))
async def get_all(message:types.Message):
	all_of = get_news()
	for j in all_of:
		await message.answer(j)


@dp.message_handler(Text(equals="Last_five"))
async def pos_five(message:types.Message):
	alll = get_news()
	for x in range(0, 5):
		await message.answer(alll[x])


if __name__ == '__main__':
	executor.start_polling(dp)