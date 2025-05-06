import json
import logging
import pandas as pd
import numpy as np
from typing import Dict, Any, List, Optional
from datetime import datetime
from fastapi import HTTPException
from .llm_service import LLMService
from .prompt_helper_service import PromptHelperService


class OrderService:
    def __init__(self) -> None:
        self.llm = LLMService().get_llm()
        self.order_query_analysis_prompt = PromptHelperService().get_order_query_analysis_prompt
        self.response_formatting_prompt = PromptHelperService().get_respose_formatting_prompt()
    
    def process_order_query(self,):
        try:
            pass
        except Exception as e:
            return HTTPException(status_code=500, detail=f"Error handling order query: {str(e)}")