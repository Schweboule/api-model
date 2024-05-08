import panda as pd
import sklearn
import joblib

def ingest_data(file_path:str) -> pd.DataFrame:
    return pd.read_excel(file_path)

def clean_data(df : pd.DataFrame) -> pd.DataFrame:
    #suppression des lignes avec des valeurs manquantes
    #remplacer les valeurs non numériques par des valeurs numériques
    return df
def train_model (df : pd.DataFrame) -> ClassifierMixin:
    #instantiate model
    model = KNeighborsClassifier()
    
    #split data
    y=df['survive']
    X = df.drop('survived', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)
    
    #• train model
    model.fit(X_train, y_train)
    