from pydantic import BaseModel, Field
from typing import Optional, Dict

TICKER_TO_SECTOR_NAME: Dict[str, str] = {
    "XLK": "Technology",
    "XLF": "Finance",
    "XLE": "Energy",
    "XLV": "Healthcare",
    "XLY": "Consumer Discretionary",
    "XLP": "Consumer Staples",
    "XLI": "Industrials",
    "XLB": "Materials",
    "XLC": "Communication Services",
    "XLU": "Utilities",
    "XLRE": "Real Estate",
}

class MarketComparison(BaseModel):
    """Base model for metrics that require current vs previous comparison."""
    current_value: float = Field(..., description="The value for the most recent session.")
    previous_value: float = Field(..., description="The value for the previous session to determine trend.")

class MarketInfo(BaseModel):
    """
    Pydantic model defining the structure for sectoral ETF metrics,
    supporting trend analysis (current vs previous values).
    """
    ticker: str = Field(..., description="The sectoral ETF symbol (e.g., XLK).")
    sector: str = Field(..., description="The human-readable name of the sector.")
    
    last_close_price: Optional[MarketComparison] = Field(None, description="Current and previous closing price.")
    market_cap: Optional[MarketComparison] = Field(None, description="Current and previous market capitalization.")
    volume: Optional[MarketComparison] = Field(None, description="Current and previous trading volume.")