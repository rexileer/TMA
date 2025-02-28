from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from bot.keyboards import main_markup
from db import User

router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    user = await User.filter(id=message.from_user.id).exists()
    if not user:
        await User.create(id=message.from_user.id, name=message.from_user.first_name)
        
    await message.answer("Open My First TMA!", reply_markup=main_markup) 