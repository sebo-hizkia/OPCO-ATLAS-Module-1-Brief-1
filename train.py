from modules.preprocess import preprocessing, split
from modules.evaluate import evaluate_performance
from modules.print_draw import print_data, draw_loss
from models.models import create_nn_model, train_model, model_predict
import pandas as pd
import joblib
from os.path import join as join
import mlflow

# Chargement des datasets
df_old = pd.read_csv(join('data', 'df_old.csv'))
#df_new = pd.read_csv(join('data', 'df_new.csv'))

# Charger le préprocesseur
preprocessor_loaded = joblib.load(join('models','preprocessor.pkl'))

# preprocesser les data
X, y, _ = preprocessing(df_old)
# X, y, _ = preprocessing(df_new)

# split data in train and test dataset
# X_train, X_test, y_train, y_test = split(X, y)

with mlflow.start_run():
    # # create a new model
    # model = create_nn_model(X_train.shape[1])

    # charger l'ancien modèle
    #model = mlflow.sklearn.load_model("runs:/93186a080ca54349b621686e8a7d3fcb/model")

    # re-entraîner le modèle avec les ancinnes données
    #model, hist = train_model(model, X_train, y_train, X_val=X_test, y_val=y_test)
    # draw_loss(hist)

    # charger le nouveau modèle
    model = mlflow.sklearn.load_model("runs:/25d1bb0e97a644f9815ac0ab49c1d61f/new_model")

    # entrainer le modèle sur les nouvelles données
    # model, hist = train_model(model, X_train, y_train, X_val=X_test, y_val=y_test)

    # predire sur les valeurs de train
    # y_pred = model_predict(model, X_test)

    # predire les valeurs sur l'ancien jeu de donées
    y_pred = model_predict(model, X)

    # mesurer les performances MSE, MAE et R²
    perf = evaluate_performance(y, y_pred)
    # perf = evaluate_performance(y, y_pred)

    # tracer les performances
    mlflow.log_metric("MSE", perf["MSE"])
    mlflow.log_metric("MAE", perf["MAE"])
    mlflow.log_metric("R²", perf["R²"])
    mlflow.sklearn.log_model(model, "new_model") # sauvegarder dans mlflow
    #mlflow.sklearn.save_model(model, "model") # sauvegarder localement

    print_data(perf)






