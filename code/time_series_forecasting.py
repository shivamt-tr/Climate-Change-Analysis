import pandas as pd
import numpy as np
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense

class TimeSeriesForecasting(object):

    """
    Class for TimeSeriesForecasting using LSTM network

    Parameters and Attributes:
    -------------------------
    data: numpy array
        input data samples
    date_column: dataframe column name containing date values
    values_column: dataframe column name containing data values to run the forecasting algorithm
    
    Example:
    --------
    >>> model = TimeSeriesForecasting(df, 'Date', 'Emission')
    >>> model.train(split=0.75, look_back=3, n_iter=256)
    >>> forecast_dates, forecast_values = model.predict(n_pred=30)
    
    References:
    ----------
    https://towardsdatascience.com/time-series-forecasting-with-recurrent-neural-networks-74674e289816
    """

    def __init__(self, data, date_column, values_column):
        
        # assign values to class attributes
        self.model = None
        self.look_back = None
        self.data = data
        self.date_column = date_column
        self.values_column = values_column

        # convert the time column to datetime and set this column as the index
        self.data[date_column] = pd.to_datetime(self.data[date_column])
        self.data.set_axis(self.data[date_column], inplace=True)

    def train(self, split=0.75, look_back=3, n_iter=256):

        self.look_back = look_back

        # convert values column to a numpy array
        self.X = self.data[self.values_column].values.reshape(-1, 1)

        # split the data into train and test set
        split_index = int(split*len(self.X))
        X_train, X_test = self.X[:split_index], self.X[split_index:]
        y_test, y_test = self.data[self.date_column][:split_index], self.data[self.date_column][split_index:]
        
        # generate time series from the train and test data
        time_series_generator_train = TimeseriesGenerator(X_train, X_train, length=self.look_back, batch_size=2)
        time_series_generator_test = TimeseriesGenerator(X_test, X_test, length=self.look_back, batch_size=1)

        # construct LSTM model and train
        self.model = Sequential()
        self.model.add(LSTM(10, activation='relu', input_shape=(self.look_back, 1)))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mse')
        self.model.fit_generator(time_series_generator_train, epochs=n_iter, verbose=2)

        # run prediction on test_data
        # pred = model.predict_generator(test_generator)

        return self

    def predict(self, n_pred=30):

        # get the list of next n_pred dates for which we will predict the values
        last_date = self.data[self.date_column].values[-1]
        next_dates = pd.date_range(last_date, periods=n_pred+1, freq='Y').tolist()
        
        ########### edit the code below
        prediction_list = self.X[-self.look_back:]
        
        for _ in range(n_pred):
            x = prediction_list[-self.look_back:]
            x = x.reshape((1, self.look_back, 1))
            out = self.model.predict(x)[0][0]
            prediction_list = np.append(prediction_list, out)
        prediction_list = prediction_list[self.look_back-1:]
            
        return next_dates, prediction_list
