from aiogram.dispatcher.filters.state import State , StatesGroup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from crud_functions import get_all_products, is_included, add_user, close_connection
from aiogram.dispatcher import FSMContext
import asyncio







api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())


KP = InlineKeyboardMarkup()
B1 = InlineKeyboardButton(text = "Рассчитать ", callback_data = "calories" )
B2 = InlineKeyboardButton(text = "Формулы расчёта", callback_data = 'formulas')
KP.row(B1,B2)


KB = ReplyKeyboardMarkup(
          keyboard= [
              [
                  KeyboardButton(text = 'Рассчитать'),
                  KeyboardButton(text = 'О нас'),
                  KeyboardButton(text = 'КУПИТЬ'),
                  KeyboardButton(text = 'РЕГИСТРАЦИЯ')
              ]
          ],
          resize_keyboard = True
)


KD = InlineKeyboardMarkup(
    inline_keyboard= [
        [InlineKeyboardButton(text = "Product1" , callback_data='product_buying')],
        [InlineKeyboardButton(text = "Product2" , callback_data='product_buying')],
        [InlineKeyboardButton(text = "Product3" , callback_data='product_buying')],
        [InlineKeyboardButton(text = "Product4" , callback_data='product_buying')]
    ], resize_keyboard = True
)

class UserState(StatesGroup):
    age  = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    user_name  = State()
    user_age = State()
    user_email = State()
    user_balance = State()




@dp.message_handler(commands = ['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer("Привет! нажмите кнопку Рассчитать чтобы начать работу", reply_markup = KB)



@dp.message_handler(text="Рассчитать")
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup = KP)




@dp.message_handler(text="КУПИТЬ")
async def get_buying_list(message):
  #  for i in range(1,5):
  products = get_all_products()
  for product in products:
      with open(f'shopping{product[0]}.jpg', "rb") as img:
           await message.answer_photo(img,f"Название: {product[1]}| Описание: {product[2]} | Цена: <{product[3]}>")

  await message.answer('Выберите продукт для покупки:', reply_markup=KD)


@dp.callback_query_handler(text = "product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

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


@dp.message_handler(text = "РЕГИСТРАЦИЯ")
async def sing_up(message):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await RegistrationState.user_name.set()

@dp.message_handler(state = RegistrationState.user_name)
async def set_username(message, state):

    if is_included(message.text) == False:
            await state.update_data(first=message.text)
            await message.answer('Введите свой email:')
            await RegistrationState.user_email.set()
    else:
        await message.answer("Пользователь существует, введите другое имя:")
        await RegistrationState.user_name.set()

@dp.message_handler(state = RegistrationState.user_email)
async def set_email(message, state):
    await state.update_data(second = message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.user_age.set()



@dp.message_handler(state = RegistrationState.user_age)
async def set_email(message, state):
    await state.update_data(third = message.text)
    data  = await state.get_data()
    print("!!!", data['first'], data['second'], data['third'])
    add_user(data['first'], data['second'], data['third'])
    if is_included(data['first']) == True:
            a = data['first']
            await message.answer(f'пользователь {a}  успешно добавлен')
            await state.finish()
            await KB.clean()

    else :
        await message.answer('хм... какой то косяк')




@dp.message_handler(text = "О нас")
async def information(message):
    await message.answer('Course : Urban Python Beginner\n'
                         'Student Meshcheryakova Tatiana')





@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer("Введите команду /start, чтобы начать общение.")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


