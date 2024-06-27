# websocket_server.py
import asyncio
import websockets
import json
import random
import datetime


async def stock_data_simulator(websocket, path):
    try:
        while True:
            price = round(random.uniform(100, 500), 2)
            data = {
                "timestamp": datetime.datetime.now().isoformat(),
                "price": price
            }
            await websocket.send(json.dumps(data))
            print(f"Sent data: {data}")  # For debugging
            await asyncio.sleep(1)  # Adjust the interval as needed
    except websockets.exceptions.ConnectionClosedOK:
        print("Client disconnected.")
    except Exception as e:
        print(f"Error in stock_data_simulator: {e}")

start_server = websockets.serve(stock_data_simulator, "localhost", 6789)

print("WebSocket server started at ws://localhost:6789")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
