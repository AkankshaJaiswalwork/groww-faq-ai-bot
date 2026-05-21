class Chunker:
    @staticmethod
    def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list:
        chunks = []
        words = text.split()
        for i in range(0, len(words), chunk_size - chunk_overlap):
            chunk = " ".join(words[i:i + chunk_size])
            chunks.append(chunk)
        return chunks
