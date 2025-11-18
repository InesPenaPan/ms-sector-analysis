import pandas as pd
from pytrends.request import TrendReq
from typing import Optional
import time
from models.model_trends import TrendsAnalysisResult, KeywordSuggestion, InterestOverTimeResult, TrendDataPoint
from pytrends import exceptions 

def trends_analysis(industry_name: str) -> Optional[TrendsAnalysisResult]:
    """
    Connects to Google Trends to get keyword suggestions for the provided industry 
    using a retry mechanism (exponential backoff) to handle rate-limiting issues (429s).
    """
    if not industry_name:
        print("Error: The industry name cannot be empty.")
        return None

    MAX_ATTEMPTS = 5
    
    # Initialize Pytrends connection
    try:
        pytrends = TrendReq(hl='en-US', tz=360, retries=5, backoff_factor=0.5) 
    except Exception as e:
        print(f"FATAL: Error initializing Pytrends client: {e}")
        return None

    for attempt in range(MAX_ATTEMPTS):
        try:
            suggestions_list = pytrends.suggestions(keyword=industry_name)
            
            if not suggestions_list:
                return TrendsAnalysisResult(industry_name=industry_name, suggestions=[])

            df = pd.DataFrame(suggestions_list)
            
            suggestion_dicts = df[['title', 'type']].to_dict('records')

            return TrendsAnalysisResult(
                industry_name=industry_name,
                suggestions=suggestion_dicts
            )

        except exceptions.ResponseException as e:
            if attempt < MAX_ATTEMPTS - 1:
                wait_time = 2 ** attempt
                print(f"Pytrends Rate Limit Error (429) on attempt {attempt + 1}. Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time) 
            else:
                print(f"FINAL FAILURE: Pytrends failed after {MAX_ATTEMPTS} attempts. Error: {e}")
                return None
        
        except Exception as e:
            print(f"Unexpected error getting suggestions for '{industry_name}': {e}")
            return None
            
    return None

def time_series_analysis(keyword: str, start_date: str, end_date: str) -> Optional[InterestOverTimeResult]:
    """
    Fetches Google Trends 'Interest Over Time' data for a single keyword 
    between specified dates using a retry mechanism.
    """
    
    if not keyword:
        print("Error: Keyword cannot be empty.")
        return None

    MAX_ATTEMPTS = 5
    TIME_FRAME = f"{start_date} {end_date}"
    
    try:
        pytrends = TrendReq(hl='en-US', tz=360, retries=5, backoff_factor=0.5)
    except Exception as e:
        print(f"FATAL: Error initializing Pytrends client: {e}")
        return None

    for attempt in range(MAX_ATTEMPTS):
        try:
            # Build Payload (Define the search parameters)
            pytrends.build_payload(
                kw_list=[keyword],          # List of keywords (must be a list)
                cat=0,                      # All categories
                timeframe=TIME_FRAME,       # Specific date range
                geo='',                     # Worldwide search
                gprop=''                    # Web search (default)
            )
            
            # Fetch Interest Over Time Data
            df = pytrends.interest_over_time() 
            
            if df.empty or 'isPartial' not in df.columns:
                print("Warning: Received empty or malformed DataFrame.")
                return InterestOverTimeResult(keyword=keyword, timeframe=TIME_FRAME, results=[])

            # Process and Format the Output
            df.reset_index(inplace=True)
            df.rename(columns={'index': 'date', keyword: 'interest_level'}, inplace=True)
            df.drop(columns=['isPartial'], inplace=True) # Remove the isPartial column

            # Convert to list of dicts for Pydantic model
            data_points = df[['date', 'interest_level']].to_dict('records')
            
            # Ensure date is string and interest_level is int
            final_results = [
                TrendDataPoint(date=str(d['date'].date()), interest_level=int(d['interest_level']))
                for d in data_points
            ]
            
            return InterestOverTimeResult(
                keyword=keyword,
                timeframe=TIME_FRAME,
                results=final_results
            )

        except exceptions.ResponseException as e:
            if attempt < MAX_ATTEMPTS - 1:
                wait_time = 2 ** attempt
                print(f"Pytrends Rate Limit Error (429) on attempt {attempt + 1}. Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time) 
            else:
                print(f"FINAL FAILURE: Pytrends failed after {MAX_ATTEMPTS} attempts. Error: {e}")
                return None
        
        except Exception as e:
            print(f"Unexpected error getting time series for '{keyword}': {e}")
            return None
            
    return None