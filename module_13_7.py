'''Задача "Ещё больше выбора":
Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
'''



from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


KP = ReplyKeyboardMarkup()
P1 = KeyboardButton(text = "Calculate")
P2 = KeyboardButton(text = "Information")
KP.row(P1,P2)

KB = InlineKeyboardMarkup()
B1 = InlineKeyboardButton(text = "Рассчитать ", callback_data = "calories" )
B2 = InlineKeyboardButton(text = "Формулы расчёта", callback_data = 'formulas')
KB.row(B1,B2)
#KB.add(B1)
#KB.add(B2)


class UserState(StatesGroup):
    age  = State()
    growth = State()
    weight = State()



@dp.message_handler(commands = ['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! нажмите кнопку calculate чтобы начать работу", reply_markup = KP)



@dp.message_handler(text="Calculate")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = KB)


@dp.callback_query_handler(text = "formulas")
async def get_formulas(call):
    print('my tut!')
    await call.message.answer(' для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5;/n для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()

#@dp.message_handler(text = ['calories','/calories'])
@dp.callback_query_handler(text = "calories")
async def set_age(call):
    print('my tut!')
    await call.message.answer('Введите свой возраст:')
    await call.answer()
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





@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
