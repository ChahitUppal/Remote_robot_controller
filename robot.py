import asyncio
import websockets

async def handle_client(websocket, path=None):  # Make `path` optional
    try:
        async for message in websocket:
            print(f"Received Command: {message}")
            # You can send a response back to the client if needed
            await websocket.send(f"Echo: {message}")
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def start_server():
    server = await websockets.serve(handle_client, "0.0.0.0", 8765)
    print("WebSocket Server Started on ws://localhost:8765")
    await server.wait_closed()

# Run the server
asyncio.run(start_server())