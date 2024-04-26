# from fastapi.testclient import TestClient
# from starlette.websockets import WebSocketDisconnect, WebSocket
#
# from src import app
#
#
# @app.websocket('/ws/tests/')
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     try:
#
#         data = 'message'
#         await websocket.send_text(data)
#     except WebSocketDisconnect:
#         await websocket.close()


# def test_connect_websocket():
#     client = TestClient(app, raise_server_exceptions=False)
#
#     with client.websocket_connect('/ws/tests/') as websocket:
#         data = websocket.receive_text()
#         assert data == 'message'
#
#
# def test_connect_free_chat():
#     client = TestClient(app, raise_server_exceptions=False)
#
#     with client.websocket_connect('/ws/chats/free-chat/') as websocket:
#         data = websocket.receive_text()
#         assert data == 'ddd'
