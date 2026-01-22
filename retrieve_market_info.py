import yfinance as yf
import numpy as np
from typing import Dict, Any, Optional
from models.model_market import TICKER_TO_SECTOR_NAME 

def fetch_current_market_data(ticker_symbol: str) -> Optional[Dict[str, Any]]:
    """
    Fetches the current and previous market data (price, cap, volume) 
    for the Sector Analysis module.
    """
    ticker_upper = ticker_symbol.upper()
    sector_name = TICKER_TO_SECTOR_NAME.get(ticker_upper, f"Unknown Sector ({ticker_upper})")

    try:
        stock = yf.Ticker(ticker_upper)
        history = stock.history(period="2d")
        
        if history.empty or len(history) < 2:
            return None

        current_session = history.iloc[-1]
        previous_session = history.iloc[-2]
        
        info = stock.info

        curr_price = float(current_session['Close'])
        prev_price = float(previous_session['Close'])

        curr_market_cap = int(info.get('marketCap', 0))
        prev_market_cap = int((curr_market_cap * prev_price) / curr_price) if curr_price != 0 else 0

        curr_volume = int(info.get('volume', 0))
        prev_volume = int(info.get('averageVolume') or previous_session['Volume'])

        return {
            "ticker": ticker_upper,
            "sector": sector_name,
            "last_close_price": {
                "current_value": round(curr_price, 3),
                "previous_value": round(prev_price, 3)
            },
            "market_cap": {
                "current_value": curr_market_cap,
                "previous_value": prev_market_cap
            },
            "volume": {
                "current_value": curr_volume,
                "previous_value": prev_volume
            }
        }
        
    except Exception as e:
        print(f"Error fetching yfinance data for {ticker_upper}: {e}")
        return None