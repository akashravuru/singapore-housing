import pandas as pd
import numpy as np
import re
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def parse_remaining_lease(lease_str):
    years = 0
    months = 0
    year_match = re.search(r'(\d+) year', lease_str)
    if year_match:
        years = int(year_match.group(1))
    month_match = re.search(r'(\d+) month', lease_str)
    if month_match:
        months = int(month_match.group(1))
    return years + months/12

def parse_storey_range(storey_str):
    top = 0
    low = 0
    top_floor = re.search(r'TO (\d+)', storey_str)
    if top_floor:
        top = int(top_floor.group(1))
    lower_floor = re.search(r'(\d+) TO', storey_str)
    if lower_floor:
        low = int(lower_floor.group(1))
    return (top + low) / 2

@st.cache_resource
def load_model_and_encoders():
    df = pd.read_csv("ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv")
    
    df = df.drop(columns=['block', 'street_name'])
    df['remaining_lease'] = df['remaining_lease'].apply(parse_remaining_lease)
    df['storey_range'] = df['storey_range'].apply(parse_storey_range)
    df['year'] = df['month'].str[:4].astype(int)
    df = df.drop(columns=['month'])
    
    le_town = LabelEncoder()
    le_flat_type = LabelEncoder()
    le_flat_model = LabelEncoder()
    
    df['town'] = le_town.fit_transform(df['town'])
    df['flat_type'] = le_flat_type.fit_transform(df['flat_type'])
    df['flat_model'] = le_flat_model.fit_transform(df['flat_model'])
    
    X = df.drop(columns=['resale_price'])
    y = df['resale_price']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)
    
    return model, le_town, le_flat_type, le_flat_model

def predict_price(town, flat_type, flat_model, storey_range,
                  floor_area, lease_commence_date, remaining_lease, year):
    
    model, le_town, le_flat_type, le_flat_model = load_model_and_encoders()
    
    town_enc = le_town.transform([town])[0]
    flat_type_enc = le_flat_type.transform([flat_type])[0]
    flat_model_enc = le_flat_model.transform([flat_model])[0]
    
    features = np.array([[town_enc, flat_type_enc, storey_range,
                          floor_area, flat_model_enc, lease_commence_date,
                          remaining_lease, year]])
    
    price = model.predict(features)[0]
    return price

def get_unique_values():
    _, le_town, le_flat_type, le_flat_model = load_model_and_encoders()
    return le_town.classes_, le_flat_type.classes_, le_flat_model.classes_