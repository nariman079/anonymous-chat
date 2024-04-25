import uuid
from typing import Dict

from starlette.websockets import WebSocket, WebSocketDisconnect


class Room:
    """
    Комнаты
    """

    def __init__(self):
        self.clients = []


class ConnectFreeChat:
    """
    Получение и подключение к свободному чату
    """

    __min_client_count = 1

    def __init__(
            self,
            websocket: WebSocket,
            room_list: Dict[str, Room]
    ):
        self._websocket = websocket
        self._room_list = room_list

    def _find_free_chat_or_create_new_room(self) -> None:
        """ Поиск или создание новой комнаты """
        for room_id, room in self._room_list.items():
            if len(room.clients) <= self.__min_client_count:
                self.room: Room = room
                self.room_id: str = room_id
                break
        else:
            self.room_id = uuid.uuid4().__str__()
            self.room: Room = Room()
            self._room_list[self.room_id] = self.room

    async def _connect_to_room(self):
        """ Подключение к комнате """
        await self._websocket.accept()

        try:
            while True:
                websocket_message = await self._websocket.receive_json()
                for client in self.room.clients:
                    client: WebSocket
                    if client != self._websocket:
                        await client.send_json(websocket_message)
                    await client.send_json(websocket_message)
        except WebSocketDisconnect:
            self.room.clients.remove(self._websocket)
            if not self.room.clients:
                del self._room_list[self.room_id]
        finally:
            await self._websocket.close()

    async def executor(self):
        self._find_free_chat_or_create_new_room()
        await self._connect_to_room()