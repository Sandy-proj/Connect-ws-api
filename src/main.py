from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from .api.views import router as api_router
from .application.settings import settings
from .db.utils import get_mongo_client

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Tasks to be done at the start of the application server.
    client = get_mongo_client()
    app.mongodb = client.get_database(settings.MONGODB_NAME)  # type: ignore[attr-defined]

    yield

    # Tasks to be done while stopping the application server.
    client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def health_check() -> dict[str, str]:
    return {"Status": "OK"}
