import json
import logging
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional
from datetime import datetime
from fastapi import HTTPException
from .llm_service import LLMService
from .prompt_helper_service import PromptHelperService
from .mockapi_service import MockAPI
from .post_processing_service import PostProcessingService
from .response_formatter_service import ResponseFormatterService

class OrderService:
    def __init__(self) -> None:
        self.llm = LLMService()
        self.order_query_analysis_prompt = PromptHelperService().get_order_query_analysis_prompt()
        self.response_formatting_prompt = PromptHelperService().get_respose_formatting_prompt()
        self.mockapi_service = MockAPI()
        self.post_processing_service = PostProcessingService()
        self.response_formatter_service = ResponseFormatterService()

    async def process_order_query(self, customer_id, user_query):
        try:

            analysis_chain = self.order_query_analysis_prompt | self.llm
            analysis_result = analysis_chain.invoke({
                "customer_id": customer_id,
                "query": user_query
            })
            print(f"Analysis result: {analysis_result.content}")

            try:
                analysis_data = json.loads(analysis_result.content)
                print(f"Query analysis: {analysis_data}")
            except json.JSONDecodeError:
                return f"Failed to parse query analysis output: {analysis_result.content}"
            
            endpoint = analysis_data.get("endpoint", "")
            parameters = analysis_data.get("parameters", {})
            api_data = self.mockapi_service.call_mock_api(endpoint, parameters)
            if not api_data or (isinstance(api_data, list) and len(api_data) == 0):
                return f"I couldn't find any order information for customer ID {customer_id} matching your query. Please check your customer ID or try a different query."
            
            processed_data = self.post_processing_service.apply_post_processing(api_data, analysis_data.get("post_processing", {}), analysis_data.get("query_type", ""))
            print(processed_data)
            # Format the response using the LLM
            formatted_response = await self.response_formatter_service.format_response(user_query, customer_id, processed_data, self.response_formatting_prompt, self.llm)
        
            return {
                "response": formatted_response,
                "metadata": {
                    "raw_data": processed_data if isinstance(processed_data, dict) else [item for item in processed_data][:5]
                }
            }



        except Exception as e:
            return HTTPException(status_code=500, detail=f"Error handling order query: {str(e)}")