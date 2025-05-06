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

class OrderService:
    def __init__(self) -> None:
        self.llm = LLMService().get_llm()
        self.order_query_analysis_prompt = PromptHelperService().get_order_query_analysis_prompt
        self.response_formatting_prompt = PromptHelperService().get_respose_formatting_prompt()
        self.mockapi_service = MockAPI.get_mockapi_service()

    def process_order_query(self, customer_id, user_query):
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

                  

        except Exception as e:
            return HTTPException(status_code=500, detail=f"Error handling order query: {str(e)}")