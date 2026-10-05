from fastapi import FastAPI

from src.api.demo import router as demo_router
from src.api.users import router as users_router
from src.core.config import APP_TITLE, APP_VERSION

app = FastAPI(title=APP_TITLE, version=APP_VERSION)
app.include_router(demo_router)
app.include_router(users_router)
