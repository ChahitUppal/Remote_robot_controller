import asyncio
import websockets

async def send_commands():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        while True:
            command = input("Enter command (forward, backward, left, right, stop, exit): ").strip().lower()
            if command == "exit":
                break
            await websocket.send(command)
            print(f"Sent: {command}")

asyncio.run(send_commands())