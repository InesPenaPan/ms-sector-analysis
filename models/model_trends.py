from pydantic import BaseModel, Field
from typing import List

class KeywordSuggestion(BaseModel):
    """
    Represents a single keyword suggestion returned by the Pytrends 'suggestions' function.
    This structure helps the user identify related search terms and topics.
    """
    title: str = Field(..., description="The suggested keyword or phrase from Google Trends.")
    type: str = Field(..., description="The type of entity suggested (e.g., 'Topic' or 'Search Term').")


class TrendsAnalysisResult(BaseModel):
    """
    The Pydantic model for the keyword suggestion analysis endpoint. 
    It contains the queried industry term and the list of related suggestions.
    """
    industry_name: str = Field(..., description="The name of the industry that was queried.")
    suggestions: List[KeywordSuggestion] = Field(..., description="A list of top keyword suggestions related to the industry.")

class TrendDataPoint(BaseModel):
    """
    Represents a single data point in the 'Interest Over Time' series.
    """
    date: str = Field(..., description="The date (YYYY-MM-DD) for this data point.")
    interest_level: int = Field(..., description="Search interest relative to the peak (0-100).")

class InterestOverTimeResult(BaseModel):
    """
    The Pydantic model for the 'Interest Over Time' analysis endpoint.
    It encapsulates the metadata of the query and the historical results.
    """
    keyword: str = Field(..., description="The keyword queried.")
    timeframe: str = Field(..., description="The time period of the analysis.")
    results: List[TrendDataPoint] = Field(..., description="The list of historical interest levels.")