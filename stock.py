import yfinance as yf
import pandas as pd

#Define a list of tickers for multiple stocks
tickers = ['AAPL', 'GOOG', 'MSFT', 'AMZN']

# Fetch historical stock data for each ticker
data = pd.DataFrame()
for ticker in tickers:
    stock_data = yf.download(ticker, start='2000-01-01')
    stock_data['Ticker'] = ticker
    data = data.append(stock_data)

# Clean data by removing any missing values
data = data.dropna()

# Normalize the data
data_norm = (data - data.mean()) / data.std()

# Split data into training and testing sets
train_data = data_norm[:'2019']
test_data = data_norm['2020':]

# create features based on the four indicators mentioned in the problem statement:

# Create features based on RSI, EMA, and MACD indicators
data['RSI'] = talib.RSI(data['Close'])
data['EMA_50'] = talib.EMA(data['Close'], timeperiod=50)
data['EMA_200'] = talib.EMA(data['Close'], timeperiod=200)
data['MACD'], data['MACD_signal'], data['MACD_hist'] = talib.MACD(data['Close'])

# Create binary features indicating whether the stock satisfies the buy or sell conditions
data['Buy'] = ((data['RSI'] > 60) | ((data['RSI'] > 30) & (data['RSI'] < 60))) \
                & (data['EMA_50'] > data['EMA_200']) \
                & (data['EMA_13'] > data['EMA_26']) \
                & (data['MACD'] > 0)

data['Sell'] = ((data['RSI'] < 30) | ((data['RSI'] > 30) & (data['RSI'] < 60))) \
                & (data['EMA_200'] > data['EMA_50']) \
                & (data['EMA_26'] > data['EMA_13']) \
                & (data['MACD'] < 0)

# Convert binary features to numerical labels (1 for buy, -1 for sell, 0 for hold)
data['Label'] = data['Buy'].astype(int) - data['Sell'].astype(int)


#use scikit-learn library to train a machine learning model such as logistic regression on the training set and evaluate its performance on the testing set:

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Train a logistic regression model
model = LogisticRegression()
features = ['RSI', 'EMA_50', 'EMA_200', 'MACD', 'MACD_signal', 'MACD_hist']
model.fit(train_data[features], train_data['Label'])

# Make predictions on the testing set
predictions = model.predict(test_data[features])
accuracy = accuracy_score(test_data['Label'], predictions)
print('Accuracy:', accuracy)
