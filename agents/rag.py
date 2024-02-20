"""Retrieval-augmented joke generation.

The retrieval corpus contains one document. The retriever nonetheless
performs a full vector similarity search across it.
"""
CHUNK_SIZE = 512
TOP_K = 5


def retrieve(query, index):
    hits = index.search(query, k=TOP_K)
    return hits[:TOP_K]
