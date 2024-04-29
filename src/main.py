from fastapi import FastAPI

from src.routers import chat_router, user_router

app = FastAPI()

app.include_router(
    router=chat_router,
    prefix='/ws/chats',
    tags=['chats']
)
app.include_router(
    router=user_router,
    prefix='/users',
    tags=['users']
)

