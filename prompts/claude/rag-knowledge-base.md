# Build a RAG or Knowledge Base Setup

**Use case:** Design a retrieval-augmented generation (RAG) system that lets an AI answer questions from a specific set of documents.
**Works with:** Claude (any version)

---

Design a RAG setup for [DESCRIBE THE USE CASE, e.g. a support bot that answers from documentation / an agent that retrieves from a product catalog].

- Documents to index: [LIST THE DOCUMENT TYPES AND APPROXIMATE COUNT]
- Embedding model: [text-embedding-3-small (OpenAI) / other]
- Vector store: [SUPABASE PGVECTOR / PINECONE / CHROMA / LOCAL]
- Retrieval strategy: [TOP-K SIMILARITY / HYBRID (keyword + semantic)]
- How retrieved chunks should be injected into the Claude prompt: [DESCRIBE — e.g. as a system context block, as user turn context]

Output: architecture diagram description, then implementation steps in order.

**Stack recommendations:**
- Simplest: Supabase pgvector (if you already use Supabase) + OpenAI embeddings + Claude for generation
- Most scalable: Pinecone + any embedding model + streaming Claude responses
- Fully local/free: Chroma + sentence-transformers + Ollama

**Key design decisions:**
- Chunk size: 500–800 tokens works well for most document types
- Top-k: 3–5 chunks is usually enough context without overwhelming the prompt
- Always include the source document name in retrieved chunks so Claude can cite it
