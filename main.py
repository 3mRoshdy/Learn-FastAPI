from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return { "message": "Hello World" }

@app.get('/people/{person_name}')
async def greet_person(
    person_name: str, extras: Optional[str] = None
):
    response = {"message": "Hello there %s!" % person_name}
    if extras:
        response.update({"extras": extras})
    return response
