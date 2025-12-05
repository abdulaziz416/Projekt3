from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bson import ObjectId

import database  # <-- lägg märke till att vi importerar hela modulen


class Resolution(BaseModel):
    id: str | None = None
    text: str


app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    database.connect_to_mongo()


@app.on_event("shutdown")
async def shutdown_event():
    database.close_mongo_connection()


def serialize_resolution(doc) -> dict:
    """Gör om Mongo-dokument till JSON-vänligt dict."""
    return {
        "id": str(doc["_id"]),
        "text": doc["text"],
    }


@app.get("/resolutions")
async def list_resolutions():
    if database.resolutions_collection is None:
        raise HTTPException(status_code=500, detail="DB not initialized")

    docs = []
    async for doc in database.resolutions_collection.find():
        docs.append(serialize_resolution(doc))
    return docs


@app.post("/resolutions")
async def create_resolution(resolution: Resolution):
    if database.resolutions_collection is None:
        raise HTTPException(status_code=500, detail="DB not initialized")

    doc = {"text": resolution.text}
    result = await database.resolutions_collection.insert_one(doc)
    created = await database.resolutions_collection.find_one(
        {"_id": result.inserted_id}
    )
    return serialize_resolution(created)


@app.delete("/resolutions/{resolution_id}")
async def delete_resolution(resolution_id: str):
    if database.resolutions_collection is None:
        raise HTTPException(status_code=500, detail="DB not initialized")

    if not ObjectId.is_valid(resolution_id):
        raise HTTPException(status_code=400, detail="Invalid id")

    result = await database.resolutions_collection.delete_one(
        {"_id": ObjectId(resolution_id)}
    )
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Resolution not found")

    return {"status": "deleted"}


@app.get("/health")
async def health():
    return {"status": "ok"}
