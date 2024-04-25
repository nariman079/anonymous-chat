from typing import Dict

from fastapi import APIRouter
from starlette.websockets import WebSocket

from src.services import chat_services

chat_router = APIRouter(
    prefix='/ws/chats'
)

room_list: Dict[str, chat_services.Room] = {}


@chat_router.websocket('/free-chat/')
async def free_chat(websocket: WebSocket) -> None:
    """ Endpoint для подключения в свободному чату """
    connect_free_chat = chat_services.ConnectFreeChat(
        websocket=websocket,
        room_list=room_list
    )
    await connect_free_chat.executor()
