import os
import json
from loguru import logger
from vector_db import VectorDB

def ingest_data():
    db = VectorDB()
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "phase_1", "data")
    if not os.path.exists(data_dir):
        logger.error("Data directory does not exist.")
        return
        
    for file in os.listdir(data_dir):
        if file.endswith("_structured.json"):
            with open(os.path.join(data_dir, file), "r") as f:
                data = json.load(f)
                content = json.dumps(data)
                db.collection.upsert(
                    ids=[data["fund_id"]],
                    documents=[content],
                    metadatas=[{"fund_name": data["fund_name"]}]
                )
    logger.info("Ingestion completed successfully.")

if __name__ == "__main__":
    ingest_data()
