import os
import pandas as pd
from sqlalchemy import create_engine
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
import mlflow
from mlflow.sklearn import save_model


# MLFlow configs

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "http://minio:8081"
os.environ['AWS_ACCESS_KEY_ID'] = 'minioadmin'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'minioadmin'
mlflow.set_tracking_uri("http://mlflow_server:5000")
mlflow.set_experiment("mlflow_training_tracking")

DATABASE_URI = 'mysql+pymysql://modeldbuser:modeldbpass@modeldb:3306/modeldb'
TABLE_NAME = 'dataset_covertype_table'
RANDOM_STATE = 42



def get_training_data():
    engine = create_engine(DATABASE_URI)
    train_df = pd.read_sql('training_data', engine)
    return train_df

def get_test_data():
    engine = create_engine(DATABASE_URI)
    test_df = pd.read_sql('test_data', engine)
    return test_df


def train_random_forest(): 

    df = get_training_data()
    y_train = df['Cover_Type']
    X_train = df.drop(columns=['Cover_Type'])
    
    # One hot encoding
    non_numerical_features = ["Wilderness_Area", "Soil_Type"]
    column_transform = make_column_transformer((OneHotEncoder(handle_unknown='ignore'),
                                                non_numerical_features), remainder='passthrough')

    #Pipeline

    pipeline = Pipeline(steps=[
        ("column_transformer", column_transform),
        ("scaler", StandardScaler(with_mean=False)),
        ("random_forest", RandomForestClassifier())
    ]) 

    param_grid = { 
        "random_forest__max_depth":[5,10,15],
        "random_forest__n_estimators":[100,150,200]
    }


    mlflow.autolog(log_model_signatures=True, log_input_examples=True)
    with mlflow.start_run(run_name="random_forest_run") as run:
        model_name = "random_forest"
        search_rf = GridSearchCV(pipeline, param_grid, n_jobs=2)

        search_rf.fit(X_train, y_train)
                # Log best parameters and best score
        mlflow.log_params(search_rf.best_params_)
        mlflow.log_metric("best_score", search_rf.best_score_)

        # Log the model
        mlflow.sklearn.log_model(search_rf.best_estimator_, model_name)

        # Register the model
        model_uri = f"runs:/{run.info.run_id}/{model_name}"
        mlflow.register_model(model_uri, model_name)
        mlflow.end_run()


def train_gbm():

    df = get_training_data()

    y_train = df['Cover_Type']
    X_train = df.drop(columns=['Cover_Type'])

    non_numerical_features = ["Wilderness_Area", "Soil_Type"]
    column_transform = make_column_transformer(
        (OneHotEncoder(handle_unknown='ignore'), non_numerical_features),
        remainder='passthrough'
    )

    pipeline = Pipeline(steps=[
        ("column_transform", column_transform),
        ("scaler", StandardScaler(with_mean=False)),
        ("gbm", GradientBoostingClassifier())
    ])

    param_grid = {
        "gbm__learning_rate": [0.01, 0.1, 0.5],
        "gbm__n_estimators": [100, 200, 300]
    }



    mlflow.autolog(log_model_signatures=True, log_input_examples=True)
    with mlflow.start_run(run_name="gbm_run") as run:
        model_name = "gbm"
        search_gb = GridSearchCV(pipeline, param_grid, n_jobs=2)

        search_gb.fit(X_train, y_train)
                # Log best parameters and best score
        mlflow.log_params(search_gb.best_params_)
        mlflow.log_metric("best_score", search_gb.best_score_)

        # Log the model
        mlflow.sklearn.log_model(search_gb.best_estimator_, model_name)

        # Register the model
        model_uri = f"runs:/{run.info.run_id}/{model_name}"
        mlflow.register_model(model_uri, model_name)
        mlflow.end_run()
