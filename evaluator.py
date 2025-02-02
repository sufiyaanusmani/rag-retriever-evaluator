from openai import OpenAI
from config import Config


def evaluate_retrievers(query, overlapping_chunks, retriever_1_only_chunks, retriever_2_only_chunks):
    
    prompt = f"""Analyze the relevance of text chunks to the following query: "{query}"

Chunk Categories:
1. Overlapping Chunks (50%+ similarity): {overlapping_chunks}
2. Chunks from Retriever 1 Only: {retriever_1_only_chunks}
3. Chunks from Retriever 2 Only: {retriever_2_only_chunks}

For each category, please:
- Rate the relevance of each chunk on a scale of 1-10
- Provide a brief explanation for the relevance score
- Highlight any significant insights about the retriever's performance

Format your response as a JSON with the following structure:
{{
    "overlapping_chunks": [
        {{"chunk": "chunk text", "relevance_score": 7, "explanation": "..."}}
    ],
    "retriever_1_only_chunks": [
        {{"chunk": "chunk text", "relevance_score": 5, "explanation": "..."}}
    ],
    "retriever_2_only_chunks": [
        {{"chunk": "chunk text", "relevance_score": 8, "explanation": "..."}}
    ],
    "overall_assessment": "Summary of retriever performance"
}}"""
    
    client = OpenAI(api_key=Config.OPENAI_API_KEY)
    completion = client.chat.completions.create(
        mode="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "User: " + prompt},
            {"role": "user", "content": "I want to evaluate the relevance of text chunks to a query."}
        ]
    )

    return completion.choices[0].message