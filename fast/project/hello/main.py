from typing import Union
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
 <body>
 <h1>WebSocket Chat</h1>
 <form action="" onsubmit="sendMessage(event)">
    <input type="text" id="messageText"
        autocomplete="off"/>
    <button>Send</button>
 </form>
 
 <ul id='messages'>
 </ul>

<script>
 var ws = new WebSocket("ws://localhost:8000/ws");
 ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var content = document.createTextNode(event.data)

 message.appendChild(content)
    messages.appendChild(message)
    };
 function sendMessage(event) {
    var input = document.getElementById("messageText")
    console.log(ws)
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
 }
 </script>
 </body>
"""


@app.get("/")
async def get():
 return HTMLResponse(html)



clients = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
 await websocket.accept()
 clients.append(websocket)

 while True:
    data = await websocket.receive_text()
    disconnected = []
    for client in clients:
         try:
            await client.send_text(f"Message text was: {data}")
         #await websocket.send_text(f"Message text was: {data}")
         except:
                disconnected.append(client)

    for dc in disconnected:
       clients.remove(dc)

@app.post("/")
def read_root():
 return {"post": "fast"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None,):
 return {"item_id": item_id, "q": q}