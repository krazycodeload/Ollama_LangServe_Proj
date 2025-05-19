from fastapi import FastAPI
from langserve import add_routes
from detect_translate_chain import final_chain

app = FastAPI()

add_routes(
    app,
    final_chain,
    path="/translate"
)
