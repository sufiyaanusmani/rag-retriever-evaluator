from difflib import SequenceMatcher
from typing import List, Dict, Any


def calculate_similarity(chunk1: str, chunk2: str) -> float:
    """
    Calculate similarity between two chunks using SequenceMatcher
    
    :param chunk1: First text chunk
    :param chunk2: Second text chunk
    :return: Similarity ratio (0-1)
    """
    return SequenceMatcher(None, chunk1, chunk2).ratio()


def find_overlapping_chunks(
        retriever_1_chunks: List[str], 
        retriever_2_chunks: List[str],
        overlap_threshold: float
    ) -> Dict[str, List[str]]:
    """
    Find overlapping chunks with fuzzy matching
    
    :param old_retriever_chunks: Chunks from the original retriever
    :param new_retriever_chunks: Chunks from the new retriever
    :return: Dictionary of overlapping chunks
    """
    overlapping_chunks = []
    retriever_1_only_chunks = list(retriever_1_chunks)
    retriever_2_only_chunks = list(retriever_2_chunks)

    for old_chunk in retriever_1_chunks:
        for new_chunk in retriever_2_chunks:
            similarity = calculate_similarity(old_chunk, new_chunk)
            if similarity >= overlap_threshold:
                overlapping_chunks.append(old_chunk)
                
                # Remove from unique chunks lists
                if old_chunk in retriever_1_only_chunks:
                    retriever_1_only_chunks.remove(old_chunk)
                if new_chunk in retriever_2_only_chunks:
                    retriever_2_only_chunks.remove(new_chunk)

    return {
        "overlapping_chunks": overlapping_chunks,
        "retriever_1_only_chunks": retriever_1_only_chunks,
        "retriever_2_only_chunks": retriever_2_only_chunks
    }