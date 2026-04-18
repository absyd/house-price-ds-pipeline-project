from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(df):
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, model.score(X_test, y_test)