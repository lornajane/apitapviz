from abc import ABC, abstractmethod
from models import Document, Flow, Step
from typing import List, Dict
import re

class BaseFormatter:
    @staticmethod
    def _clean_text(text: str) -> str:
        """Remove special characters and normalize whitespace."""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text).strip()
    
    @abstractmethod
    def format(self, document: Document) -> str:
        """Abstract method that must be implemented by concrete formatters."""
        raise NotImplementedError

