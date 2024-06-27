# WebSocket

This Python code sets up a WebSocket server that simulates sending stock data to clients at regular intervals. Let's break down the key components and functionalities:

Imports:
asyncio: Provides tools for asynchronous programming.
websockets: Library for WebSocket server and client.
json: Used for JSON serialization.
random: Generates random numbers.
datetime: Handles timestamps.

Async Function stock_data_simulator(websocket, path):
This is the core function executed for each WebSocket connection established.
While Loop: Runs indefinitely until the connection is closed.
Generate Stock Data: Randomly generates a stock price between 100 and 500.
Data Format: Constructs a JSON object containing the current timestamp and the generated price.
Send Data: Sends the JSON data to the connected client using await websocket.send(json.dumps(data)).
Debugging: Prints the sent data for debugging purposes.
Delay: await asyncio.sleep(1) pauses execution for 1 second before sending the next update. This interval (1 second) can be adjusted based on requirements.

Exception Handling:
ConnectionClosedOK: Catches this exception when the client disconnects normally.
Generic Exception: Catches any other exceptions that might occur during data generation or transmission.

WebSocket Server Setup:
start_server = websockets.serve(stock_data_simulator, "localhost", 6789): Configures the WebSocket server to listen on localhost at port 6789 and handle connections using the stock_data_simulator function.

Server Start and Event Loop:
Prints a message indicating the server has started.
asyncio.get_event_loop().run_until_complete(start_server): Starts the WebSocket server.
asyncio.get_event_loop().run_forever(): Keeps the event loop running indefinitely to handle incoming WebSocket connections and data transmissions.
