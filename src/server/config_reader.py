from pathlib import Path
from typing import AsyncGenerator

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from tortoise import Tortoise


ROOT_DIR = Path(__file__).parent.parent


class Config(BaseSettings):
    BOT_TOKEN: SecretStr
    DB_URL: SecretStr
    
    WEBHOOK_URL: str = "https://rndgr-194-85-249-14.a.free.pinggy.link"
    WEBAPP_URL: str = "https://9d55-194-85-249-14.ngrok-free.app"
    
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / "server" / ".env",
        env_file_encoding="utf-8",
    )
    
    
config = Config()
    
TORTOISE_ORM = {
    "connections": {"default": config.DB_URL.get_secret_value()},
    "apps": {
        "models": {
            "models": ["db.models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def lifespan(app: FastAPI) -> AsyncGenerator:
    await bot.set_webhook(
        url=f"{config.WEBHOOK_URL}/weebhook",
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    
    await Tortoise.init(TORTOISE_ORM)
    
    yield
    await Tortoise.close_connections()
    await bot.session.close()
        
bot = Bot(config.BOT_TOKEN.get_secret_value())
dp = Dispatcher()
app = FastAPI(lifespan=lifespan)

