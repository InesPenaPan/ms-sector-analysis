import yfinance as yf
from typing import Dict, Any, Optional
from models.model_market import TICKER_TO_SECTOR_NAME 

def fetch_current_market_data(ticker_symbol: str) -> Optional[Dict[str, Any]]:
    """
    Fetches the current price, market capitalization, and trading volume 
    for a given stock ticker from the yfinance API.
    """
    ticker_upper = ticker_symbol.upper()
    
    sector_name = TICKER_TO_SECTOR_NAME.get(ticker_upper, f"Unknown Sector ({ticker_upper})")

    try:
        stock = yf.Ticker(ticker_upper)
        info = stock.info
        
        last_price = info.get('regularMarketPrice')
        market_cap_val = info.get('marketCap')
        volume_val = info.get('volume')
        
        if last_price is None or market_cap_val is None:
            return None
        
        return {
            "ticker": ticker_upper,
            "sector": sector_name,
            "last_close_price": last_price,
            "market_cap": market_cap_val,
            "volume": volume_val,
        }
        
    except Exception as e:
        print(f"Error fetching yfinance data for {ticker_upper}: {e}")
        return None