from fastapi import FastAPI, HTTPException, status
from py_eureka_client import eureka_client

from typing import List
from models.model_market import MarketInfo, TICKER_TO_SECTOR_NAME
from models.model_trends import TrendsAnalysisResult, InterestOverTimeResult
from retrieve_market_info import fetch_current_market_data
from trends_analysis import trends_analysis, time_series_analysis

# FastAPI initialization
app = FastAPI(
    title="MS-MarketData Microservice",
)

@app.on_event("startup")
async def startup_event():
    await eureka_client.init_async(
        eureka_server="http://eureka-server:8761",
        app_name="ms-news",
        instance_port=8002
    )

# ----------------------------------------------------------------------
# Market Information Endpoint
# ----------------------------------------------------------------------

@app.get(
    "/market/{ticker}", 
    response_model=MarketInfo, 
    summary="Gets the current price, market cap, and volume of the sectoral ETF."
)
def get_market_data(ticker: str):
    ticker_upper = ticker.upper()

    if ticker_upper not in TICKER_TO_SECTOR_NAME:
        supported_tickers_list = ", ".join(TICKER_TO_SECTOR_NAME.keys())
        raise HTTPException(
            status_code=404, 
            detail=f"Ticker '{ticker_upper}' not recognized as a sectoral ETF. Supported: {supported_tickers_list}"
        )

    try:
        market_data = fetch_current_market_data(ticker_upper)
        
        if market_data is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
                detail=f"Could not retrieve punctual data for '{ticker_upper}'. Invalid ticker or source service is down."
            )

        return market_data
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error during processing for {ticker_upper}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Internal Server Error processing the request."
        )

# ----------------------------------------------------------------------
# Tredn analysis Endpoint
# ----------------------------------------------------------------------

@app.get(
    "/trends/{ticker}",
    response_model=TrendsAnalysisResult,
    summary="Gets keyword suggestions from Google Trends based on the sector ETF ticker."
)
def get_trends_analysis(ticker: str):
    ticker_upper = ticker.upper()

    if ticker_upper not in TICKER_TO_SECTOR_NAME:
        supported_tickers_list = ", ".join(TICKER_TO_SECTOR_NAME.keys())
        raise HTTPException(
            status_code=404, 
            detail=f"Ticker '{ticker_upper}' not recognized as a sectoral ETF. Supported: {supported_tickers_list}"
        )
    
    industry_name = TICKER_TO_SECTOR_NAME[ticker_upper]
    
    try:
        analysis_result = trends_analysis(industry_name)
        
        if analysis_result is None:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not retrieve trends data for '{industry_name}'. Pytrends service failed or timed out."
            )
        
        return analysis_result
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error during trends analysis for {ticker_upper}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error processing the trends request."
        )
    
@app.get("/time-series/{keyword}", response_model=InterestOverTimeResult)
def get_time_series(keyword: str, start_date: str, end_date: str):
    result = time_series_analysis(keyword, start_date, end_date)
    
    if result is None:
        raise HTTPException(status_code=503, detail="Failed to retrieve time series data.")
    return result