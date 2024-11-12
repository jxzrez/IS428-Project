import streamlit as st
import joblib
import pandas as pd

# Load the model and scalers
model = joblib.load('./JobLib/trained_model2.joblib')
feature_scalers = {
    'closest_mrt_dist': joblib.load('./JobLib/closest_mrt_dist_scaler.joblib'),
    'cbd_dist': joblib.load('./JobLib/cbd_dist_scaler.joblib'),
    'floor_area_sqm': joblib.load('./JobLib/floor_area_sqm_scaler.joblib'),
    'remaining_lease': joblib.load('./JobLib/remaining_lease_scaler.joblib'),
    'year': joblib.load('./JobLib/year_scaler.joblib'),
    'distance_to_closest_school': joblib.load('./JobLib/distance_to_closest_school_scaler.joblib'),
    'distance_to_closest_mall': joblib.load('./JobLib/distance_to_closest_mall_scaler.joblib'),
    'Interest Rate': joblib.load('./JobLib/Interest Rate_scaler.joblib'),
    'Employment Rate': joblib.load('./JobLib/Employment Rate_scaler.joblib'),
    'Population': joblib.load('./JobLib/Population_scaler.joblib')
}

all_flat_model = [
    '2-room', 'Adjoined flat', 'Apartment', 'DBSS', 'Improved', 'Improved-Maisonette',
    'Maisonette', 'Model A', 'Model A-Maisonette', 'Model A2', 'Multi Generation',
    'New Generation', 'Premium Apartment', 'Premium Apartment Loft', 'Premium Maisonette',
    'Simplified', 'Standard', 'Terrace', 'Type S1', 'Type S2'
]

all_town_categories = [
    'ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG',
    'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG',
    'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS',
    'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
    'TOA PAYOH', 'WOODLANDS', 'YISHUN'
]

all_flat_type = [
    '1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION'
]

all_storey_range = [
    '01 TO 03', '01 TO 05', '04 TO 06', '06 TO 10', '07 TO 09', '10 TO 12', '11 TO 15',
    '13 TO 15', '16 TO 18', '16 TO 20', '19 TO 21', '21 TO 25', '22 TO 24', '25 TO 27',
    '26 TO 30', '28 TO 30', '31 TO 33', '31 TO 35', '34 TO 36', '36 TO 40', '37 TO 39',
    '40 TO 42', '43 TO 45', '46 TO 48', '49 TO 51'
]

def predict_price(input_data):
    input_df = pd.DataFrame([input_data])

    town = input_df['town'].item()
    flat_type = input_df['flat_type'].item()
    storey_range = input_df['storey_range'].item()
    flat_model = input_df['flat_model'].item()

    input_df = input_df.drop(columns=['town', 'flat_type', 'storey_range', 'flat_model'])

    for category in all_town_categories:
        input_df[category] = 1 if category == town else 0

    for category in all_flat_type:
        input_df[category] = 1 if category == flat_type else 0

    for category in all_storey_range:
        input_df[category] = 1 if category == storey_range else 0

    for category in all_flat_model:
        input_df[category] = 1 if category == flat_model else 0

    for feature, scaler in feature_scalers.items():
        input_df[feature] = scaler.transform(input_df[[feature]])

    prediction = model.predict(input_df)
    return float(prediction[0])

st.set_page_config(page_title="Price Forecast Tool")

st.title("Price Forecast Tool")
st.markdown("This is a price forecasting tool trained using a machine learning regression model to predict prices beyond the range of the original analysis which stopped at 2023. By entering the various parameters, including economic indicators that can be obtained from the earlier tabs, with a r-square of 0.86 the flat resale price.")

with st.form("predict_form"):
    town = st.selectbox("Town", all_town_categories)
    flat_type = st.selectbox("Flat Type", all_flat_type)
    storey_range = st.selectbox("Storey Range", all_storey_range)
    flat_model = st.selectbox("Flat Model", all_flat_model)
    closest_mrt_dist = st.slider("Closest MRT Distance (m)", 0, 5471, 2500)
    cbd_dist = st.slider("CBD Distance (m)", 0, 22406, 10000)
    floor_area_sqm = st.slider("Floor Area (sqm)", 29.4, 188.5, 110.0)
    remaining_lease = st.slider("Remaining Lease (years)", 0, 99, 50)
    year = st.number_input("Year", min_value=2000, max_value=2100, value=2024)
    distance_to_closest_school = st.slider("Distance to Closest School (km)", 0.0, 3.36, 1.5)
    distance_to_closest_mall = st.slider("Distance to Closest Mall (km)", 0.0, 3.47, 1.6)
    interest_rate = st.slider("Interest Rate (%)", 0.0, 3.2, 1.6)
    employment_rate = st.slider("Employment Rate (%)", 0, 100, 66)
    st.caption("  Singapore's employment rate is 66% as of 2023")
    population = st.number_input("Population", min_value=0, value=5918000)
    st.caption("  Singapore's population is 5.918 million as of 2023")

    submitted = st.form_submit_button("Predict")

    if submitted:
        input_data = {
            'town': town,
            'flat_type': flat_type,
            'storey_range': storey_range,
            'flat_model': flat_model,
            'closest_mrt_dist': closest_mrt_dist,
            'cbd_dist': cbd_dist,
            'floor_area_sqm': floor_area_sqm,
            'remaining_lease': remaining_lease,
            'year': year,
            'distance_to_closest_school': distance_to_closest_school,
            'distance_to_closest_mall': distance_to_closest_mall,
            'Interest Rate': interest_rate,
            'Employment Rate': employment_rate,
            'Population': population
        }

        predicted_value = predict_price(input_data)
        st.success(f'Predicted value: ${predicted_value:.2f}')