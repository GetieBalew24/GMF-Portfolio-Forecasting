import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import logging

# Configure logging
logging.basicConfig(filename='data_processing.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataProcessor:    
    def __init__(self):
        """Initialize the DataProcessor with an empty data dictionary."""
        self.data = {}
        
    def get_data(self, symbols, start_date, end_date):
        """
        Fetch historical data for the given symbols within the specified date range.
        Uses Yahoo Finance as the data source.
        """
        for symbol in symbols:
            try:
                logging.info(f"Fetching data for {symbol} from {start_date} to {end_date}")
                df = yf.download(symbol, start=start_date, end=end_date)
                df.reset_index(inplace=True)
                self.data[symbol] = df
                logging.info(f"Data fetched successfully for {symbol}")
            except Exception as e:
                logging.error(f"Error fetching data for {symbol}: {e}")
        return self.data
    
    def clean_data(self):
        """
        Clean data by handling missing values using forward fill and dropping rows 
        with remaining null values.
        """
        for symbol, df in self.data.items():
            try:
                logging.info(f"Cleaning data for {symbol}")
                df['Date'] = pd.to_datetime(df['Date'])
                df.fillna(method='ffill', inplace=True)
                df.dropna(inplace=True)
                logging.info(f"Data cleaned successfully for {symbol}")
            except Exception as e:
                logging.error(f"Error cleaning data for {symbol}: {e}")
        return self.data
    def basic_statistics(self):
        """
        Compute and return basic statistical summaries (mean, std, etc.) for each symbol.
        """
        stats = {}
        for symbol, df in self.data.items():
            try:
                logging.info(f"Calculating basic statistics for {symbol}")
                stats[symbol] = df.describe()
            except Exception as e:
                logging.error(f"Error calculating statistics for {symbol}: {e}")
        return stats
    def plot_closing_prices(self):
        """
        Plot the closing prices over time for each symbol.
        """
        for symbol, df in self.data.items():
            try:
                logging.info(f"Plotting closing prices for {symbol}")
                plt.figure(figsize=(14, 6))
                plt.plot(df['Date'], df['Close'], label=f'{symbol} Close Price')
                plt.title(f'{symbol} Closing Price Over Time')
                plt.xlabel('Date')
                plt.ylabel('Closing Price')
                plt.legend()
                plt.show()
            except Exception as e:
                logging.error(f"Error plotting closing prices for {symbol}: {e}")