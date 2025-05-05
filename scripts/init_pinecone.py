from pinecone import Pinecone, ServerlessSpec
# from utils.config import PINECONE_API_KEY
import os
from dotenv import load_dotenv
load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
print(PINECONE_API_KEY)
def initialize_index(index_name="e-commerce-products", dimension=1536):
    pc = Pinecone(api_key=PINECONE_API_KEY)
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=dimension,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print(f"✅ Created Pinecone index '{index_name}'")
    else:
        print(f"ℹ️ Index '{index_name}' already exists")
