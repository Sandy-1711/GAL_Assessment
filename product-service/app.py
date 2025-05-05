from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import logging
import logging.config
import config
# import router from product_router

logging.config.dictConfig(config.LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="E-Commerce Product service",
    description="Product service that uses the pinecone db along with llm to respond to user queries redirected from chat service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "service":"E-Commerce Product Service",
        "version":"1.0.0",
        "status":"operational"
    }


@app.get("/health")
async def health_check():
    """Health cheack endpoint"""
    return {"status":"healthy"}

if __name__ == "__main":
    logger.info("Starting E-commerce product service")
    uvicorn.run(app,host="0.0.0.0", port=8001)