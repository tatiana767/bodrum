'''Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'.
Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью
'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.'''


from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

api = " "
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

KB = ReplyKeyboardMarkup()
B1 = KeyboardButton(text = "Calculate")
B2 = KeyboardButton(text = "Information")
KB.row(B1,B2)
#KB.add(B1)
#KB.add(B2)


class UserState(StatesGroup):
    age  = State()
    growth = State()
    weight = State()




#@dp.message_handler(text = ['calories','/calories'])
@dp.message_handler(text = "Calculate")
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
    await KB.clean()

@dp.message_handler(text = "Information")
async def information(message):
    await message.answer('Course : Urban Python Beginner\n'
                         'Student Meshcheryakova Tatiana')



@dp.message_handler(text = "/start")
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message. answer("Привет! Я бот помогающий твоему здоровью.нажмите кнопку calculate чтобы вычислить дневную норму калорий", reply_markup = KB)


@dp.message_handler()
async def all_messages(message):

    await message.answer("Привет! Я бот помогающий твоему здоровью. нажмите кнопку calculate чтобы вычислить дневную норму калорий ")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
