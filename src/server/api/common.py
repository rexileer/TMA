from fastapi import APIRouter, Request

from aiogram.types import Update

from config_reader import bot, dp

router = APIRouter()


@router.post("/weebhook")
async def weebhook(request: Request) -> None:
    update = Update.model_validate(await request.json(), context={"bot": bot})
    await dp.feed_update(bot,update)