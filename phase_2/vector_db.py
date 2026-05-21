import os
import chromadb
from loguru import logger

class VectorDB:
    def __init__(self):
        db_dir = os.path.join(os.path.dirname(__file__), "chroma_db")
        os.makedirs(db_dir, exist_ok=True)
        self.client = chromadb.PersistentClient(path=db_dir)
        self.collection = self.client.get_or_create_collection("groww_faq")
        logger.info("ChromaDB initialized.")
