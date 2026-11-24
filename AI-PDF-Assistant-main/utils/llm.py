import os

def generate_answer(client,context,question):
    prompt = f"""You are a helpful AI assistant.

Answer the question ONLY from the provided context.

If the answer is not present in the context, reply:

"I couldn't find the answer in the provided document."

------------------------
Context:

{context}

------------------------
Question:
{question}

Answer:
"""
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
    except Exception:
        # Fallback to gemini-2.5-flash-lite or gemini-3.8-flash if primary encounters temporary issues
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

    return response.text