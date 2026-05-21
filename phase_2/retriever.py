from loguru import logger
from vector_db import VectorDB

class Retriever:
    def __init__(self):
        self.db = VectorDB()
        
    def retrieve(self, query: str, n_results: int = 1) -> list:
        results = self.db.collection.query(
            query_texts=[query],
            n_results=n_results
        )
        return results["documents"]
