import pickle
import pandas as pd

#import the ml model
with open('model/model.pkl', 'rb') as f:         #rb -> read binary mode
    model = pickle.load(f)

#created by MLFlow automatically (for now hardcoded)
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])              #[send as rows]

    output = model.predict(input_df)[0]

    return output