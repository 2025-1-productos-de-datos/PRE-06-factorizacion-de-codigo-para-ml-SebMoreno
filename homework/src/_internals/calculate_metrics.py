from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def calculate_metrics(model, x, y):
    y_pred = model.predict(x)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return mse, mae, r2
