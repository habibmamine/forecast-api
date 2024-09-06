from prophet import Prophet
import pandas as pd

def predict(receivedData, numMonths):

    preparedData = {"ds": receivedData["dates"], "y":receivedData["ordered"] }

    data = pd.DataFrame(preparedData)

    model = Prophet(interval_width=0.95) 
    model.fit(data)
    future = model.make_future_dataframe(periods=numMonths, freq='MS')  # Predicting next 12 hours (48 periods of 15 minutes)
    future = future[future['ds'] > data['ds'].max()]

    forecast = model.predict(future)

    dates = []
    values = []

    for i in range( len(forecast['ds'])):
        dates.append(forecast['ds'][i])

    for i in range( len(forecast['yhat'])):
        values.append(abs(forecast['yhat'][i]))

    return {'dates': dates, 'values': values}