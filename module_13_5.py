
from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age  = State()
    growth = State()
    weight = State()




@dp.message_handler(text = ['calories','/calories'])
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state = UserState.age)
async def set_grouth(message, state):
    await state.update_data(first=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(second = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(third = message.text)
    data =  await state.get_data()
    calories = 10 * int(data['third']) + 6.25*int(data['second']) - 5*int(data['first']) - 161
    await message.answer(f"Ваша дневная норма калорий: {calories} ")
    await state.finish()


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /calories, чтобы начать общение.')

    await message.answer("Введите команду /calories, чтобы начать общение.")


async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message. answer("Привет! Я бот помогающий твоему здоровью")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
