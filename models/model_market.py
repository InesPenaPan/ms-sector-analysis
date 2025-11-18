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

class MarketInfo(BaseModel):
    """
    Pydantic model defining the structure for current market metrics 
    of a single Sector Exchange-Traded Fund (ETF) fetched from yfinance.
    """

    ticker: str = Field(..., description="The sectoral ETF symbol (e.g., XLK).")
    sector: str = Field(..., description="The human-readable name of the sector.")
    
    last_close_price: Optional[float] = Field(None, description="Latest closing/trading price of the ETF.")
    market_cap: Optional[int] = Field(None, description="Market capitalization of the ETF.")
    volume: Optional[int] = Field(None, description="Recent trading volume of the ETF.")