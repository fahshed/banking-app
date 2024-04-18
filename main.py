from fastapi import FastAPI

from api.api_v1 import router as account_router


app = FastAPI(title="Banking with Fahim")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Service using FastAPI and pymongo"}


app.include_router(account_router, tags=["Account"], prefix="/account")