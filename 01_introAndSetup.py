#FAST API (alternative of Express.js in MERN)
"""
FastAPI is a modern, high-performance web framework
for building APIs with python

Built on top of 2 libraries
1. Starlette -> manages how your API receives requests and sends responses.
2. Pydantic  -> data validation for API (correct and right format)               (Joi or Zod in Node.js)


Philosophy of FastAPI
1. fast to run
2. fast to code
    2.1 Automatic input validation
    2.2 Auto-generated interactive documentation
    2.3 Seamless integration with modern ecosysmtes (ML Libraries, OAuth, JWT, etc.)


web server -> SGI (Server Gateway interface) -> API code
for flask
gunicorn (server) -> WSGI (werkzeug) -> synchronous endpoint

for fastAPI (supports async/await)
uvicorn (server)  -> ASGI (Starlette) -> Asynchronous endpoint


SETUP
-> python -m venv <myenv>           #create virtual environment
-> myenv(back_slash)Scripts(back_slash)activate
-> pip install fastapi uvicorn pydantic

-> uvicorn 01_introAndSetup:app --reload
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "message" : "Hello world"
    }


@app.get("/about")
def about():
    return{
        "message" : "This is my personal learing FastAPI codes"
    }