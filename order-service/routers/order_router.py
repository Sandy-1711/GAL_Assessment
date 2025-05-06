from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
from services.prompt_helper_service import PromptHelperService
from services.llm_service import LLMService
from services.order_service import OrderService

router = APIRouter(
    prefix="/orders",
    tags=["order"],
    responses={404:{"description":"Not found"}}
)

class OrderQueryRequest(BaseModel):
    query: str
    customer_id: str
    metadata: Optional[Dict[str, Any]] = None

class OrderQueryResponse(BaseModel):
    response: str
    metadata: Optional[Dict[str, Any]] = None

def get_order_service():
    return OrderService()

@router.post("/query", response_model=OrderQueryResponse)
async def handle_order_query(
    request: OrderQueryRequest,
    order_service: OrderService = Depends(get_order_service)
):
    """Processes order-related queries and fetch data from the mock API"""
    try:
        customer_id = request.customer_id
        user_query = request.query
        print(f"Received query: {user_query}")
        
        if not customer_id:
            return OrderQueryResponse(
                response="I'd be happy to help with your order information. Could you please provide your Customer ID?"
            )
        
        # 1. Process the order query using order service
        order_service.process_order_query(customer_id, user_query)
      
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
    

@router.get("/health")
async def health_check():
    """Simple health check endpoint"""
    return {"status":"ok"}