from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from bot.handlers import setup_routers as bot_setup_routers
from api import setup_routers as api_setup_routers

from config_reader import config, dp, app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dp.include_router(bot_setup_routers())
app.include_router(api_setup_routers())

if __name__ == "__main__":
    uvicorn.run(app, host=config.APP_HOST, port=config.APP_PORT)