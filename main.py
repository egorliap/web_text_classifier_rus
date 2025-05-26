from fastapi import Depends, FastAPI

from scr.router import router
from scr.dependencies import api_key_check


app = FastAPI(
    title="Text Classification API",
    description="API для классификации текста с использованием предобученной модели",
    version="1.0.0",
    dependencies=[Depends(api_key_check)],
)

app.include_router(router)