import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import seaborn as sns

class PortfolioOptimization:
    def __init__(self, tsla_data, bnd_data, spy_data):
        """
        Initializes the PortfolioOptimization class with data for each asset.
        
        :param tsla_data: DataFrame for Tesla stock.
        :param bnd_data: DataFrame for Vanguard Total Bond Market ETF.
        :param spy_data: DataFrame for S&P 500 ETF.
        """
        tsla_data['Close'] = pd.to_numeric(tsla_data['Close'], errors='coerce')
        bnd_data['Close'] = pd.to_numeric(bnd_data['Close'], errors='coerce')
        spy_data['Close'] = pd.to_numeric(spy_data['Close'], errors='coerce')

        # Calculate daily returns for each asset
        self.tsla_returns = tsla_data['Close'].pct_change().dropna()
        self.bnd_returns = bnd_data['Close'].pct_change().dropna()
        self.spy_returns = spy_data['Close'].pct_change().dropna()

        # Calculate annualized returns for each asset
        self.tsla_annualized_return = self.tsla_returns.mean() * 252
        self.bnd_annualized_return = self.bnd_returns.mean() * 252
        self.spy_annualized_return = self.spy_returns.mean() * 252

        # Calculate the covariance matrix between returns (only necessary for optimization)
        self.cov_matrix = np.cov([self.tsla_returns, self.bnd_returns, self.spy_returns]) * 252
    def optimize_portfolio(self):
        """
        Optimizes the portfolio weights to maximize the Sharpe ratio.
        
        :return: The optimal portfolio weights.
        """
        # Initial guess for the portfolio weights (equal weights)
        initial_weights = np.array([1/3, 1/3, 1/3])

        # Constraints: the sum of weights should be 1
        constraints = ({'type': 'eq', 'fun': lambda weights: np.sum(weights) - 1})
        
        # Bounds for the weights: each weight should be between 0 and 1
        bounds = [(0, 1) for _ in range(3)]

        # Optimize portfolio
        optimal_weights = minimize(self.negative_sharpe_ratio, initial_weights, args=(self.tsla_annualized_return,                                  self.bnd_annualized_return,                                  self.spy_annualized_return,                                   self.cov_matrix),
        method='SLSQP', bounds=bounds, constraints=constraints)
        return optimal_weights.x
    def negative_sharpe_ratio(self, weights, tsla_annualized_return, bnd_annualized_return, spy_annualized_return, cov_matrix):
        """
        The objective function for portfolio optimization, which minimizes the negative Sharpe ratio.
        
        :param weights: Portfolio weights for each asset.
        :param tsla_annualized_return: Annualized return of Tesla.
        :param bnd_annualized_return: Annualized return of Bond ETF.
        :param spy_annualized_return: Annualized return of S&P 500 ETF.
        :param cov_matrix: Covariance matrix of the asset returns.
        :return: Negative Sharpe ratio (we minimize this to maximize the Sharpe ratio).
        """
        portfolio_return = np.dot(weights, [tsla_annualized_return, bnd_annualized_return, spy_annualized_return])
        portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        return -portfolio_return / portfolio_volatility  # We negate the Sharpe Ratio to minimize
