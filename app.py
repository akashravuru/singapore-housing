from singapore_functions import *
import streamlit as st

# Load encoders to get unique values for dropdowns
_, le_flat_type, le_flat_model = load_encoders()
le_town_enc, _, _ = load_encoders()

st.title("Singapore HDB Resale Price Predictor")
st.subheader("Enter flat details to get a price estimate")

town = st.selectbox("Town", sorted(le_town_enc.classes_))
flat_type = st.selectbox("Flat Type", sorted(le_flat_type.classes_))
flat_model = st.selectbox("Flat Model", sorted(le_flat_model.classes_))
storey_range = st.slider("Floor Level", 1, 50, 10)
floor_area = st.number_input("Floor Area (sqm)", min_value=30, max_value=300, value=90)
lease_commence_date = st.number_input("Lease Commence Year", min_value=1960, max_value=2023, value=1990)
remaining_lease = st.number_input("Remaining Lease (years)", min_value=1.0, max_value=99.0, value=70.0)
year = st.number_input("Transaction Year", min_value=2017, max_value=2024, value=2023)

if st.button("Predict Price"):
    price = predict_price(town, flat_type, flat_model, storey_range,
                          floor_area, lease_commence_date, remaining_lease, year)
    st.success(f"Estimated Resale Price: ${price:,.0f}")