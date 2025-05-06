from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
import uvicorn
import logging.config
import config


logging.config.dictConfig(config=config.LOGGING_CONFIG)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="E-Commerce Order Service",
    description="Order service that uses mockapi to provide order related user responses",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],   
)

@app.get("/")
async def root():
    """Root endpoint for order service"""
    return {
        "services":"E-Commerce Order Service",
        "version":"1.0.0",
        "status":"operational"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status":"healthy"}

if __name__ == "__main__":
    logger.info("Starting E-Commerce Order Service")
    uvicorn.run(app,host="0.0.0.0", port="8002")