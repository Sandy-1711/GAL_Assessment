from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

def embed_and_store_in_pinecone(text_chunks: list[str], index_name: str = "e-commerce-products"):
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
    vectorstore = PineconeVectorStore(
        index_name=index_name,
        embedding=embeddings,
        pinecone_api_key=PINECONE_API_KEY
    )
    vectorstore.add_texts(text_chunks)
    print(f"✅ Successfully stored {len(text_chunks)} chunks into Pinecone.")
