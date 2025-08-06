from fastapi import FastAPI

from handlers.items import router as crud_router


app: FastAPI = FastAPI()

app.include_router(crud_router)
