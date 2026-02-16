from fastapi import FastAPI

app = FastAPI()

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(2)  # non-blocking wait
    return {"message": "Done after 2 seconds"}