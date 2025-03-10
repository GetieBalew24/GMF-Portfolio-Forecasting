import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model_builder import TimeSeriesForecaster
from datetime import timedelta

class MarketForecaster:
    def __init__(self, forecaster, model_name, forecast_periods=180):
        """
        Initialize the MarketForecaster.

        Parameters:
        forecaster (TimeSeriesForecaster): Instance of TimeSeriesForecaster with trained models.
        model_name (str): The model name to use for forecasting ('ARIMA', 'SARIMA', or 'LSTM').
        forecast_periods (int): Number of days to forecast.
        """
        self.forecaster = forecaster
        self.model_name = model_name
        self.forecast_periods = forecast_periods

    def generate_forecast(self):
        """
        Generate future forecasts using the specified model.
        """
        try:
            print(f"Generating forecast for {self.forecast_periods} days using {self.model_name} model.")
            if self.model_name in ['ARIMA', 'SARIMA']:
                # For ARIMA/SARIMA models, directly forecast using the trained model
                forecast = self.forecaster.model[self.model_name].predict(n_periods=self.forecast_periods)
                return forecast
            elif self.model_name == 'LSTM':
                # For LSTM, use the sequence prediction approach
                data = np.array(self.forecaster.train[self.forecaster.column].values[-self.forecaster.model['LSTM']['seq_length']:].reshape(-1, 1))
                forecast = []
                for _ in range(self.forecast_periods):
                    pred = self.forecaster.model['LSTM']['model'].predict(data.reshape(1, -1, 1))
                    forecast.append(pred[0, 0])
                    data = np.append(data[1:], pred[0, 0]).reshape(-1, 1)
                return forecast
            else:
                raise ValueError("Invalid model name specified")
        except Exception as e:
            print(f"Error in generating forecast: {e}")
            raise

    def plot_forecast(self, forecast):
        """
        Plot historical data and the forecast with confidence intervals.
        """
        try:
            forecast_index = pd.date_range(start=self.forecaster.test.index[-1] + timedelta(days=1), periods=self.forecast_periods, freq='D')
            plt.figure(figsize=(12, 6))
            plt.plot(self.forecaster.test.index, self.forecaster.test[self.forecaster.column], label='Historical')
            plt.plot(forecast_index, forecast, label='Forecast', linestyle='--')

            # Add confidence intervals for ARIMA/SARIMA if available
            if self.model_name in ['ARIMA', 'SARIMA']:
                conf_int = self.forecaster.model[self.model_name].predict(n_periods=self.forecast_periods, return_conf_int=True)[1]
                plt.fill_between(forecast_index, conf_int[:, 0], conf_int[:, 1], color='pink', alpha=0.3, label='Confidence Interval')

            plt.title(f"{self.model_name} Model Forecast for Tesla's Stock Prices")
            plt.xlabel('Date')
            plt.ylabel(self.forecaster.column)
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error in plotting forecast: {e}")
            raise

    def analyze_forecast(self, forecast):
        """
        Analyze the forecast to provide insights on trends and risks.
        """
        # Calculate basic trend information
        trend = "upward" if forecast[-1] > forecast[0] else "downward" if forecast[-1] < forecast[0] else "stable"
        print(f"Forecasted Trend: {trend}")

        # Calculate volatility
        forecast_std = np.std(forecast)
        print(f"Forecasted Volatility (Standard Deviation): {forecast_std:.4f}")

        # Analysis summary
        print("\nAnalysis Summary:")
        print(f"- Long-term Trend: {trend.capitalize()}")
        print(f"- Expected Volatility: {'High' if forecast_std > 0.02 else 'Low'}")
        print("- Market Opportunities: Potential buy/sell opportunities based on trend and volatility.")
        print("- Risks: Consider risks if volatility is high or trend is downward.")