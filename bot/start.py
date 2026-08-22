from aiogram import Bot, Router, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from core.config import settings
from bot_ui import texts, keyboard



bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
router = (Router())

########## FSM_RegisterState ########

class RegisterCountry(StatesGroup):
    name = State()
    again_name = State()
    edit_name = State()
    confirm = State()



@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(texts.start, reply_markup=keyboard.inline_start_markup)



@router.callback_query(F.data == "register")
async def register_country_handler(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RegisterCountry.name)
    await callback.message.answer(texts.register_country)



@router.message(RegisterCountry.name)
async def enter_country_name_handler(message: Message, state: FSMContext):
    country_name = message.text
    if country_name in ["amir", "hassan", "nima"]:
        await message.answer("اسم انتخابی وجود دارد لطفا یه اسم دیگه وارد کنید")
        await state.set_state(RegisterCountry.again_name)
    if country_name not in ["amir", "hassan", "nima"]:
        await message.answer("اسم انتخاب شد")
        await message.answer(text=texts.register_country_accepted(country_name),reply_markup=keyboard.inline_confirmandedit_country_name)
        await state.set_state(RegisterCountry.confirm)



@router.message(RegisterCountry.again_name)
async def enter_country_name_agian_handler(message: Message, state: FSMContext):
    country_name = message.text
    if country_name in ["amir", "hassan", "nima"]:
        await message.answer("اسم انتخابی وجود دارد ")
        await state.set_state(RegisterCountry.again_name)

    if country_name not in ["amir", "hassan", "nima"]:
        await message.answer("اسم انتخاب شد")
        await message.answer(text=texts.register_country_accepted(country_name),reply_markup=keyboard.inline_confirmandedit_country_name)
        await state.set_state(RegisterCountry.confirm)



    # here I should check the database and handle it by if, and if the name
    # exists in database, again i should set state in RegisterCountry.name



@router.callback_query(RegisterCountry.confirm)
async def confirm_country_name_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == "confirm_country_name":
        await callback.answer("test")
        await callback.message.answer("نام امپراتوری شما ثبت شد")
        await state.clear()
    if callback.data == "edit_country_name":
        await callback.message.answer("بسیار خب شما اکنون در مرحله ویرایش اسم هستید اسم مورد نظر را وارد کنید")
        await state.set_state(RegisterCountry.edit_name)


@router.message(RegisterCountry.edit_name)
async def edit_country_name_handler(message: Message, state: FSMContext):
    pass
    # here I should check the database and handle it by if, and if the name
    # exists in database, again i should set state in RegisterCountry.name

@router.callback_query()
async def confirm_country_agdsfian_handler(callback: CallbackQuery, state: FSMContext):
    if callback.data == "confirm_country_name":
        await callback.message.answer("alan shod")