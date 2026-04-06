import pickle
import numpy as np

def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def load_encoders():
    with open("le_town.pkl", "rb") as f:
        le_town = pickle.load(f)
    with open("le_flat_type.pkl", "rb") as f:
        le_flat_type = pickle.load(f)
    with open("le_flat_model.pkl", "rb") as f:
        le_flat_model = pickle.load(f)
    return le_town, le_flat_type, le_flat_model

def predict_price(town, flat_type, flat_model, storey_range,
                  floor_area, lease_commence_date, remaining_lease, year):
    model = load_model()
    le_town, le_flat_type, le_flat_model = load_encoders()
    
    town_enc = le_town.transform([town])[0]
    flat_type_enc = le_flat_type.transform([flat_type])[0]
    flat_model_enc = le_flat_model.transform([flat_model])[0]
    
    features = np.array([[town_enc, flat_type_enc, storey_range,
                          floor_area, flat_model_enc, lease_commence_date,
                          remaining_lease, year]])
    
    price = model.predict(features)[0]
    return price