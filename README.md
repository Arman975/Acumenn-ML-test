# Acumenn-ML-test
Stock Market Analysis prediction model using ML and AI algorithms


-----------------------------------------------------Problem Statement-------------------------------------------------------------------

Your task is to write a machine learning model that can predict whether to
buy or sell a stock based on a combination of four stock indicators. The four
indicators are:
• RSI (Relative Strength Index) greater than 30 and less than 60
• Exponential Moving Average (EMA) 50 is greater than 200 EMA
• 13 EMA is greater than 26 EMA
• MACD (Moving Average Convergence Divergence) is positive
If a stock satisfies any three of these four conditions, it is considered a BUY.
• RSI is greater than 60
• EMA 200 is greater than 50 EMA
• 26 EMA is greater than 13 EMA
• MACD is negative
If a stock satisfies any three of these four conditions, it is considered a
SELL.
You should train your model on multiple stocks and backtest it with a
$100,000 investment in Apple Inc’s (AAPL) stock from year 2000 to see how
much money would have been made until today. You can fetch the data from
the yfinance Python library.
Note that you should not train your model on Apple Inc’s (AAPL) stock price
alone. You should use multiple other stocks for training and only then test on
AAPL's stock.


-----------------------------------------------------Solution Approach---------------------------------------------------------

* Collect data: You can use yfinance Python library to fetch historical stock data for AAPL as well as other stocks. It is important to collect data for multiple stocks for training to avoid overfitting to AAPL's stock price.

* Preprocess data: The data needs to be preprocessed before it can be used for training the model. You should clean the data by removing any missing values, normalize the data if necessary, and split it into training and testing sets.

* Feature engineering: You need to extract features from the data that are relevant to predicting whether to buy or sell a stock. In this case, you already have four indicators to work with. You can also consider creating additional features such as price momentum or volume indicators.

* Train the model: You can use a machine learning algorithm such as logistic regression or a decision tree to train the model. You should use the training set to train the model and the testing set to evaluate its performance.

* Backtesting: Once the model is trained, you can backtest it with a $100,000 investment in AAPL's stock from year 2000 to see how much money would have been made until today. You can simulate trades based on the model's predictions and calculate the returns.

* Evaluate and improve the model: You should evaluate the model's performance and identify areas for improvement. You can try different algorithms, hyperparameters, or feature sets to improve the model's accuracy.

* Deploy the model: Once the model is satisfactory, you can deploy it to make real-time predictions on AAPL's stock price. You can use an API or a web interface to provide access to the model.




