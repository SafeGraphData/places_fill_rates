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
                   "open_hours", "category_tags","Pct with mcc", "open_on", "closed_on", "tracking_closed_since", "geometry_type", "Pct with domains","Pct with website", "Pct with booking links","Pct with aliases"]
columns_to_convert = ["placekey", "parent_placekey", "location_name", "safegraph_brand_ids", "brands", "store_id", "naics_code", \
                      "top_category", "sub_category", "latitude", "longitude", "street_address", "city", "region", "postal_code", "phone_number",\
                      "open_hours", "category_tags", "Pct with mcc","open_on", "closed_on", "tracking_closed_since", "geometry_type", "Pct with domains","Pct with website", "Pct with booking links", "Pct with aliases"]
fill_rates_df = read_from_gsheets("Countries")[columns_to_keep]

for column in columns_to_convert:
    if fill_rates_df[column].dtype == object:
        fill_rates_df[column] = pd.to_numeric(fill_rates_df[column].str.replace(",", "").str.replace("%", ""), errors="coerce")
    fill_rates_df[column] *= 100
    fill_rates_df[column] = fill_rates_df[column].map("{:.0f}%".format)

fill_rates_df.rename(columns={"country": "Country", "iso_country_code": "ISO Country Code",\
                              "Pct with domains": "domains" ,"Pct with website": "website", "Pct with booking links":"booking_link", "Pct with mcc":"mcc", "Pct with aliases":"name_aliases"}, inplace=True)

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
# Keep-alive comment: 2025-04-27 09:23:18.430263
# Keep-alive comment: 2025-04-27 20:23:13.240499
# Keep-alive comment: 2025-04-28 07:23:40.168283
# Keep-alive comment: 2025-04-28 18:24:03.359098
# Keep-alive comment: 2025-04-29 05:23:33.270913
# Keep-alive comment: 2025-04-29 16:24:17.299627
# Keep-alive comment: 2025-04-30 03:23:07.940034
# Keep-alive comment: 2025-04-30 14:23:35.550802
# Keep-alive comment: 2025-05-01 01:23:47.370036
# Keep-alive comment: 2025-05-01 12:23:18.277832
# Keep-alive comment: 2025-05-01 23:22:51.304856
# Keep-alive comment: 2025-05-02 10:23:37.335921
# Keep-alive comment: 2025-05-02 21:22:48.839286
# Keep-alive comment: 2025-05-03 08:23:12.262348
# Keep-alive comment: 2025-05-03 19:23:31.702716
# Keep-alive comment: 2025-05-04 06:23:37.193555
# Keep-alive comment: 2025-05-04 17:22:46.558714
# Keep-alive comment: 2025-05-05 04:23:56.697718
# Keep-alive comment: 2025-05-05 15:23:14.734909
# Keep-alive comment: 2025-05-06 02:24:07.378500
# Keep-alive comment: 2025-05-06 13:23:08.205545
# Keep-alive comment: 2025-05-07 00:23:07.841166
# Keep-alive comment: 2025-05-07 11:23:08.261320
# Keep-alive comment: 2025-05-07 22:23:18.517963
# Keep-alive comment: 2025-05-08 09:23:11.160737
# Keep-alive comment: 2025-05-08 20:23:18.968733
# Keep-alive comment: 2025-05-09 07:23:26.660415
# Keep-alive comment: 2025-05-09 18:23:39.684204
# Keep-alive comment: 2025-05-10 05:23:16.813057
# Keep-alive comment: 2025-05-10 16:23:11.040401
# Keep-alive comment: 2025-05-11 03:23:11.374072
# Keep-alive comment: 2025-05-11 14:23:03.206977
# Keep-alive comment: 2025-05-12 01:23:08.425948
# Keep-alive comment: 2025-05-12 12:23:38.125612
# Keep-alive comment: 2025-05-12 23:23:11.851141
# Keep-alive comment: 2025-05-13 10:24:10.772804
# Keep-alive comment: 2025-05-13 21:23:12.250719
# Keep-alive comment: 2025-05-14 08:23:38.012924
# Keep-alive comment: 2025-05-14 19:23:37.651934
# Keep-alive comment: 2025-05-15 06:23:39.018377
# Keep-alive comment: 2025-05-15 17:24:02.892584
# Keep-alive comment: 2025-05-16 04:23:24.181271
# Keep-alive comment: 2025-05-16 15:22:26.870446
# Keep-alive comment: 2025-05-17 02:22:45.612169
# Keep-alive comment: 2025-05-17 13:23:19.381822
# Keep-alive comment: 2025-05-18 00:22:44.067320
# Keep-alive comment: 2025-05-18 11:23:12.278745
# Keep-alive comment: 2025-05-18 22:23:09.604325
# Keep-alive comment: 2025-05-19 09:23:44.698283
# Keep-alive comment: 2025-05-19 20:22:44.233224
# Keep-alive comment: 2025-05-20 07:23:00.497706
# Keep-alive comment: 2025-05-20 18:24:12.513889
# Keep-alive comment: 2025-05-21 05:22:44.687270
# Keep-alive comment: 2025-05-21 16:22:53.348802
# Keep-alive comment: 2025-05-22 03:22:48.076493
# Keep-alive comment: 2025-05-22 14:22:51.420295
# Keep-alive comment: 2025-05-23 01:22:50.296949
# Keep-alive comment: 2025-05-23 12:22:50.238119
# Keep-alive comment: 2025-05-23 23:22:54.581411
# Keep-alive comment: 2025-05-24 10:22:52.471258
# Keep-alive comment: 2025-05-24 21:22:49.234356
# Keep-alive comment: 2025-05-25 08:22:49.509105
# Keep-alive comment: 2025-05-25 19:22:54.528768
# Keep-alive comment: 2025-05-26 06:22:39.564839
# Keep-alive comment: 2025-05-26 17:22:44.036038
# Keep-alive comment: 2025-05-27 04:22:49.640346
# Keep-alive comment: 2025-05-27 15:22:53.883576
# Keep-alive comment: 2025-05-28 02:23:03.768276
# Keep-alive comment: 2025-05-28 13:22:52.318386
# Keep-alive comment: 2025-05-29 00:22:47.820789
# Keep-alive comment: 2025-05-29 11:22:42.612506
# Keep-alive comment: 2025-05-29 22:22:57.248848
# Keep-alive comment: 2025-05-30 09:22:42.067005
# Keep-alive comment: 2025-05-30 20:22:42.789864
# Keep-alive comment: 2025-05-31 07:22:55.398918
# Keep-alive comment: 2025-05-31 18:22:50.117141
# Keep-alive comment: 2025-06-01 05:22:48.367887
# Keep-alive comment: 2025-06-01 16:23:02.007964
# Keep-alive comment: 2025-06-02 03:23:03.413808
# Keep-alive comment: 2025-06-02 14:22:53.984156

# Keep-alive comment: 2025-06-03 01:22:44.667068
# Keep-alive comment: 2025-06-03 12:22:58.563292
# Keep-alive comment: 2025-06-03 23:22:53.437568
# Keep-alive comment: 2025-06-04 10:22:53.944105
# Keep-alive comment: 2025-06-04 21:22:32.431937
# Keep-alive comment: 2025-06-05 08:22:56.486693
# Keep-alive comment: 2025-06-05 19:22:46.077053
# Keep-alive comment: 2025-06-06 06:22:44.231673
# Keep-alive comment: 2025-06-06 17:22:27.526301
# Keep-alive comment: 2025-06-07 04:22:29.461144
# Keep-alive comment: 2025-06-07 15:22:38.668374
# Keep-alive comment: 2025-06-08 02:22:43.988415
# Keep-alive comment: 2025-06-08 13:22:45.437779
# Keep-alive comment: 2025-06-09 00:22:28.143045
# Keep-alive comment: 2025-06-09 11:22:42.575658
# Keep-alive comment: 2025-06-09 22:22:50.724382
# Keep-alive comment: 2025-06-10 09:22:53.948456
# Keep-alive comment: 2025-06-10 20:22:47.249496
# Keep-alive comment: 2025-06-11 07:22:48.314969
# Keep-alive comment: 2025-06-11 18:24:35.192694
# Keep-alive comment: 2025-06-12 05:22:45.412220
# Keep-alive comment: 2025-06-12 16:22:48.752804
# Keep-alive comment: 2025-06-13 03:22:49.785968
# Keep-alive comment: 2025-06-13 14:22:38.907060
# Keep-alive comment: 2025-06-14 01:22:58.873017
# Keep-alive comment: 2025-06-14 12:22:46.190469
# Keep-alive comment: 2025-06-14 23:22:37.555100
# Keep-alive comment: 2025-06-15 10:22:23.271364
# Keep-alive comment: 2025-06-15 21:22:58.043840
# Keep-alive comment: 2025-06-16 08:22:54.629156
# Keep-alive comment: 2025-06-16 19:22:38.565065
# Keep-alive comment: 2025-06-17 06:23:15.453717
# Keep-alive comment: 2025-06-17 17:22:43.347410
# Keep-alive comment: 2025-06-18 04:22:49.997952
# Keep-alive comment: 2025-06-18 15:22:47.447337
# Keep-alive comment: 2025-06-19 02:22:47.453885
# Keep-alive comment: 2025-06-19 13:22:46.581579
# Keep-alive comment: 2025-06-20 00:22:43.933776
# Keep-alive comment: 2025-06-20 11:23:33.237496
# Keep-alive comment: 2025-06-20 22:22:52.820489
# Keep-alive comment: 2025-06-21 09:22:38.439316
# Keep-alive comment: 2025-06-21 20:22:50.323210
# Keep-alive comment: 2025-06-22 07:22:43.325863
# Keep-alive comment: 2025-06-22 18:22:33.899293
# Keep-alive comment: 2025-06-23 05:22:50.337012
# Keep-alive comment: 2025-06-23 16:22:43.443879
# Keep-alive comment: 2025-06-24 03:22:49.907718
# Keep-alive comment: 2025-06-24 14:22:28.918711
# Keep-alive comment: 2025-06-25 01:22:23.647002
# Keep-alive comment: 2025-06-25 12:22:45.113827
# Keep-alive comment: 2025-06-25 23:22:48.151819
# Keep-alive comment: 2025-06-26 10:22:55.643435
# Keep-alive comment: 2025-06-26 21:24:19.633044
# Keep-alive comment: 2025-06-27 08:22:48.531820
# Keep-alive comment: 2025-06-27 19:22:45.605309
# Keep-alive comment: 2025-06-28 06:22:52.902709
# Keep-alive comment: 2025-06-28 17:22:43.079208
# Keep-alive comment: 2025-06-29 04:22:31.958090
# Keep-alive comment: 2025-06-29 15:22:22.860716
# Keep-alive comment: 2025-06-30 02:22:44.177878
# Keep-alive comment: 2025-06-30 13:22:25.222040
# Keep-alive comment: 2025-07-01 00:24:30.107760
# Keep-alive comment: 2025-07-01 11:22:45.072749
# Keep-alive comment: 2025-07-01 22:22:49.545463
# Keep-alive comment: 2025-07-02 09:22:43.155249
# Keep-alive comment: 2025-07-02 20:24:32.045489
# Keep-alive comment: 2025-07-03 07:22:58.025855
# Keep-alive comment: 2025-07-03 18:22:22.978078
# Keep-alive comment: 2025-07-04 05:22:46.722388
# Keep-alive comment: 2025-07-04 16:22:42.923615
# Keep-alive comment: 2025-07-05 03:22:41.842564
# Keep-alive comment: 2025-07-05 14:22:47.056155
# Keep-alive comment: 2025-07-06 01:22:44.262282
# Keep-alive comment: 2025-07-06 12:22:41.675276
# Keep-alive comment: 2025-07-06 23:22:42.885806
# Keep-alive comment: 2025-07-07 10:22:43.220718
# Keep-alive comment: 2025-07-07 21:22:41.756827
# Keep-alive comment: 2025-07-08 08:22:46.986312
# Keep-alive comment: 2025-07-08 19:22:42.476032
# Keep-alive comment: 2025-07-09 06:22:53.760304
# Keep-alive comment: 2025-07-09 17:23:26.922197
# Keep-alive comment: 2025-07-10 04:22:42.357415
# Keep-alive comment: 2025-07-10 15:22:47.583104
# Keep-alive comment: 2025-07-11 02:22:41.268927
# Keep-alive comment: 2025-07-11 13:22:42.156458
# Keep-alive comment: 2025-07-12 00:22:28.546828
# Keep-alive comment: 2025-07-12 11:22:46.718765
# Keep-alive comment: 2025-07-12 22:22:42.836969
# Keep-alive comment: 2025-07-13 09:22:42.675565
# Keep-alive comment: 2025-07-13 20:22:27.084495
# Keep-alive comment: 2025-07-14 07:22:39.225721
# Keep-alive comment: 2025-07-14 18:23:02.279685
# Keep-alive comment: 2025-07-15 05:22:52.970912
# Keep-alive comment: 2025-07-15 16:22:47.251321
# Keep-alive comment: 2025-07-16 03:22:46.987523
# Keep-alive comment: 2025-07-16 14:22:47.525160
# Keep-alive comment: 2025-07-17 01:22:42.461761
# Keep-alive comment: 2025-07-17 12:22:48.618589
# Keep-alive comment: 2025-07-17 23:22:40.947114
# Keep-alive comment: 2025-07-18 10:23:02.300623
# Keep-alive comment: 2025-07-18 21:22:41.988637
# Keep-alive comment: 2025-07-19 08:23:22.711045
# Keep-alive comment: 2025-07-19 19:22:27.656700
# Keep-alive comment: 2025-07-20 06:22:52.027544
# Keep-alive comment: 2025-07-20 17:22:58.100560
# Keep-alive comment: 2025-07-21 04:22:52.478739