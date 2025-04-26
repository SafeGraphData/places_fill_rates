import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components



st.set_page_config(
    page_title="Places Summary Statistics - Fill Rates",
    layout="wide"
)
#### Fill Rates ####

columns_to_keep = ["country", "iso_country_code", "placekey", "parent_placekey",\
                   "location_name", "safegraph_brand_ids", "brands", "store_id", "naics_code", "top_category", \
                   "sub_category", "latitude", "longitude", "street_address", "city", "region", "postal_code", "phone_number", \
                   "open_hours", "category_tags","Pct with mcc", "open_on", "closed_on", "tracking_closed_since", "geometry_type", "Pct with domains","Pct with website", "Pct with booking links"]
columns_to_convert = ["placekey", "parent_placekey", "location_name", "safegraph_brand_ids", "brands", "store_id", "naics_code", \
                      "top_category", "sub_category", "latitude", "longitude", "street_address", "city", "region", "postal_code", "phone_number",\
                      "open_hours", "category_tags", "Pct with mcc","open_on", "closed_on", "tracking_closed_since", "geometry_type", "Pct with domains","Pct with website", "Pct with booking links"]
fill_rates_df = read_from_gsheets("Countries")[columns_to_keep]

for column in columns_to_convert:
    if fill_rates_df[column].dtype == object:
        fill_rates_df[column] = pd.to_numeric(fill_rates_df[column].str.replace(",", "").str.replace("%", ""), errors="coerce")
    fill_rates_df[column] *= 100
    fill_rates_df[column] = fill_rates_df[column].map("{:.0f}%".format)

fill_rates_df.rename(columns={"country": "Country", "iso_country_code": "ISO Country Code",\
                              "Pct with domains": "domains" ,"Pct with website": "website", "Pct with booking links":"booking_link", "Pct with mcc":"mcc"}, inplace=True)

fill_rates_df_styled = fill_rates_df.style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)

st.write("Fill Rates")
st.dataframe(fill_rates_df_styled, hide_index=True)


hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-04-25 16:08:24.228143
# Keep-alive comment: 2025-04-25 16:18:18.766662
# Keep-alive comment: 2025-04-26 00:23:53.358311
# Keep-alive comment: 2025-04-26 11:23:48.326565
# Keep-alive comment: 2025-04-26 22:22:47.530006