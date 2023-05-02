import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    if data['e'] == 'kline':
        symbol = data['s']
        event_time = data['E']
        kline = data['k']
        open_price = kline['o']
        close_price = kline['c']
        high_price = kline['h']
        low_price = kline['l']
        print(f"{symbol} - Event Time: {event_time}, Open: {open_price}, Close: {close_price}, High: {high_price}, Low: {low_price}")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### Connection Closed ###")

def on_open(ws):
    print("### Connection Opened ###")

    # Subscribe to a stream
    stream_payload = {
        "method": "SUBSCRIBE",
        "params": [
            "btcusdt@kline_1m",
            "ethusdt@kline_1m"
        ],
        "id": 1
    }

    ws.send(json.dumps(stream_payload))

if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://fstream.binance.com/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
