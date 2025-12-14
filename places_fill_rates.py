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
        fill_rates_df[column] = pd.to_numeric(
            fill_rates_df[column].str.replace(",", "").str.replace("%", ""),
            errors="coerce"
        )
    fill_rates_df[column] *= 100  # convert to percent values

    
    fill_rates_df.loc[
        (fill_rates_df[column] > 0) & (fill_rates_df[column] < 0.5),
        column
    ] = -1

    
    fill_rates_df[column] = fill_rates_df[column].map("{:.0f}%".format)

    
    fill_rates_df[column] = fill_rates_df[column].replace("-1%", "<1%")

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
# Keep-alive comment: 2025-07-21 15:22:38.672707
# Keep-alive comment: 2025-07-22 02:23:01.758942
# Keep-alive comment: 2025-07-22 13:23:14.773216
# Keep-alive comment: 2025-07-23 00:22:48.801864
# Keep-alive comment: 2025-07-23 11:22:38.018586
# Keep-alive comment: 2025-07-23 22:22:41.715375
# Keep-alive comment: 2025-07-24 09:22:57.543318
# Keep-alive comment: 2025-07-24 20:22:43.489446
# Keep-alive comment: 2025-07-25 07:22:37.899557
# Keep-alive comment: 2025-07-25 18:22:42.866908
# Keep-alive comment: 2025-07-26 05:22:37.702846
# Keep-alive comment: 2025-07-26 16:22:42.125480
# Keep-alive comment: 2025-07-27 03:22:37.228900
# Keep-alive comment: 2025-07-27 14:22:27.804865
# Keep-alive comment: 2025-07-28 01:22:48.821661
# Keep-alive comment: 2025-07-28 12:22:43.422389
# Keep-alive comment: 2025-07-28 23:22:42.111076
# Keep-alive comment: 2025-07-29 10:22:17.037961
# Keep-alive comment: 2025-07-29 21:22:47.944966
# Keep-alive comment: 2025-07-30 08:22:44.035732
# Keep-alive comment: 2025-07-30 19:22:52.241691
# Keep-alive comment: 2025-07-31 06:22:57.560918
# Keep-alive comment: 2025-07-31 17:22:42.903185
# Keep-alive comment: 2025-08-01 04:22:41.297447
# Keep-alive comment: 2025-08-01 15:22:52.433886
# Keep-alive comment: 2025-08-02 02:22:37.127844
# Keep-alive comment: 2025-08-02 13:22:47.477600
# Keep-alive comment: 2025-08-03 00:22:43.164175
# Keep-alive comment: 2025-08-03 11:22:48.048099
# Keep-alive comment: 2025-08-03 22:22:42.922411
# Keep-alive comment: 2025-08-04 09:22:39.506512
# Keep-alive comment: 2025-08-04 20:22:43.034523
# Keep-alive comment: 2025-08-05 07:22:46.170984
# Keep-alive comment: 2025-08-05 18:22:47.544150
# Keep-alive comment: 2025-08-06 05:22:42.208343
# Keep-alive comment: 2025-08-06 16:24:33.120229
# Keep-alive comment: 2025-08-07 03:22:46.961804
# Keep-alive comment: 2025-08-07 14:22:48.446084
# Keep-alive comment: 2025-08-08 01:22:37.323583
# Keep-alive comment: 2025-08-08 12:22:48.306668
# Keep-alive comment: 2025-08-08 23:22:48.657027
# Keep-alive comment: 2025-08-09 10:22:42.173120
# Keep-alive comment: 2025-08-09 21:23:04.471532
# Keep-alive comment: 2025-08-10 08:22:48.578621
# Keep-alive comment: 2025-08-10 19:22:48.792279
# Keep-alive comment: 2025-08-11 06:22:42.844304
# Keep-alive comment: 2025-08-11 17:22:48.320675
# Keep-alive comment: 2025-08-12 04:22:47.324925
# Keep-alive comment: 2025-08-12 15:22:39.479695
# Keep-alive comment: 2025-08-13 02:22:48.257025
# Keep-alive comment: 2025-08-13 13:22:43.772878
# Keep-alive comment: 2025-08-14 00:22:41.599005
# Keep-alive comment: 2025-08-14 11:22:49.308685
# Keep-alive comment: 2025-08-14 22:22:42.731530
# Keep-alive comment: 2025-08-15 09:22:42.511875
# Keep-alive comment: 2025-08-15 20:22:31.958369
# Keep-alive comment: 2025-08-16 07:22:56.863604
# Keep-alive comment: 2025-08-16 18:22:43.140439
# Keep-alive comment: 2025-08-17 05:22:46.402974
# Keep-alive comment: 2025-08-17 16:22:41.534160
# Keep-alive comment: 2025-08-18 03:22:43.047698
# Keep-alive comment: 2025-08-18 14:22:43.755274
# Keep-alive comment: 2025-08-19 01:22:43.234132
# Keep-alive comment: 2025-08-19 12:22:48.283710
# Keep-alive comment: 2025-08-19 23:23:10.228514
# Keep-alive comment: 2025-08-20 10:22:44.654798
# Keep-alive comment: 2025-08-20 21:22:47.622091
# Keep-alive comment: 2025-08-21 08:22:44.606859
# Keep-alive comment: 2025-08-21 19:22:48.556291
# Keep-alive comment: 2025-08-22 06:22:48.200475
# Keep-alive comment: 2025-08-22 17:22:43.149791
# Keep-alive comment: 2025-08-23 04:22:52.545775
# Keep-alive comment: 2025-08-23 15:22:41.748493
# Keep-alive comment: 2025-08-24 02:22:41.809141
# Keep-alive comment: 2025-08-24 13:22:42.645100
# Keep-alive comment: 2025-08-25 00:22:49.262458
# Keep-alive comment: 2025-08-25 11:22:47.970227
# Keep-alive comment: 2025-08-25 22:22:42.857077
# Keep-alive comment: 2025-08-26 09:22:43.673324
# Keep-alive comment: 2025-08-26 20:22:47.584366
# Keep-alive comment: 2025-08-27 07:22:52.774995
# Keep-alive comment: 2025-08-27 18:22:22.890111
# Keep-alive comment: 2025-08-28 05:22:53.509879
# Keep-alive comment: 2025-08-28 16:22:43.157380
# Keep-alive comment: 2025-08-29 03:22:26.959285
# Keep-alive comment: 2025-08-29 14:22:33.159561
# Keep-alive comment: 2025-08-30 01:22:32.302169
# Keep-alive comment: 2025-08-30 12:22:27.748690
# Keep-alive comment: 2025-08-30 23:22:31.396502
# Keep-alive comment: 2025-08-31 10:22:27.084906
# Keep-alive comment: 2025-08-31 21:22:38.785850
# Keep-alive comment: 2025-09-01 08:22:40.785018
# Keep-alive comment: 2025-09-01 19:22:38.862473
# Keep-alive comment: 2025-09-02 06:22:27.363808
# Keep-alive comment: 2025-09-02 17:22:38.633045
# Keep-alive comment: 2025-09-03 04:22:31.493034
# Keep-alive comment: 2025-09-03 15:22:33.853679
# Keep-alive comment: 2025-09-04 02:22:36.955276
# Keep-alive comment: 2025-09-04 13:22:43.624605
# Keep-alive comment: 2025-09-05 00:22:27.990794
# Keep-alive comment: 2025-09-05 11:22:23.145622
# Keep-alive comment: 2025-09-05 22:22:32.713890
# Keep-alive comment: 2025-09-06 09:22:28.629809
# Keep-alive comment: 2025-09-06 20:22:27.915344
# Keep-alive comment: 2025-09-07 07:22:33.302310
# Keep-alive comment: 2025-09-07 18:22:33.387017
# Keep-alive comment: 2025-09-08 05:22:29.475779
# Keep-alive comment: 2025-09-08 16:22:34.052638
# Keep-alive comment: 2025-09-09 03:22:59.260049
# Keep-alive comment: 2025-09-09 14:22:34.146478

# Keep-alive comment: 2025-09-10 01:22:26.940572
# Keep-alive comment: 2025-09-10 12:22:38.853311
# Keep-alive comment: 2025-09-10 23:22:27.962869
# Keep-alive comment: 2025-09-11 10:22:30.364839
# Keep-alive comment: 2025-09-11 21:22:28.240547
# Keep-alive comment: 2025-09-12 08:22:42.804412
# Keep-alive comment: 2025-09-12 19:22:33.251689
# Keep-alive comment: 2025-09-13 06:22:22.037792
# Keep-alive comment: 2025-09-13 17:22:28.404175
# Keep-alive comment: 2025-09-14 04:22:18.463379
# Keep-alive comment: 2025-09-14 15:22:29.525009
# Keep-alive comment: 2025-09-15 02:22:27.369558
# Keep-alive comment: 2025-09-15 13:22:29.525716
# Keep-alive comment: 2025-09-16 00:22:28.272188
# Keep-alive comment: 2025-09-16 11:22:33.492917
# Keep-alive comment: 2025-09-16 22:22:27.280761
# Keep-alive comment: 2025-09-17 09:22:29.570419
# Keep-alive comment: 2025-09-17 20:22:38.726140
# Keep-alive comment: 2025-09-18 07:22:35.172175
# Keep-alive comment: 2025-09-18 18:22:34.617681
# Keep-alive comment: 2025-09-19 05:22:28.961728
# Keep-alive comment: 2025-09-19 16:23:03.310116
# Keep-alive comment: 2025-09-20 03:22:33.223534
# Keep-alive comment: 2025-09-20 14:22:34.189627
# Keep-alive comment: 2025-09-21 01:22:33.392573
# Keep-alive comment: 2025-09-21 12:22:33.285261
# Keep-alive comment: 2025-09-21 23:22:28.633297
# Keep-alive comment: 2025-09-22 10:22:31.289299
# Keep-alive comment: 2025-09-22 21:22:28.039385
# Keep-alive comment: 2025-09-23 08:22:30.253438
# Keep-alive comment: 2025-09-23 19:22:35.175335
# Keep-alive comment: 2025-09-24 06:22:29.043245
# Keep-alive comment: 2025-09-24 17:22:33.399030
# Keep-alive comment: 2025-09-25 04:24:46.879624
# Keep-alive comment: 2025-09-25 15:22:38.528642
# Keep-alive comment: 2025-09-26 02:22:34.405557
# Keep-alive comment: 2025-09-26 13:22:38.132846
# Keep-alive comment: 2025-09-26 19:31:05.415865
# Keep-alive comment: 2025-09-27 05:31:10.897376
# Keep-alive comment: 2025-09-27 15:31:05.797593
# Keep-alive comment: 2025-09-28 01:31:10.100193
# Keep-alive comment: 2025-09-28 11:31:10.872816
# Keep-alive comment: 2025-09-28 21:31:09.737537
# Keep-alive comment: 2025-09-29 07:31:16.498543
# Keep-alive comment: 2025-09-29 17:31:25.944429
# Keep-alive comment: 2025-09-30 03:31:04.600345
# Keep-alive comment: 2025-09-30 13:31:11.007895
# Keep-alive comment: 2025-09-30 23:31:29.809722
# Keep-alive comment: 2025-10-01 09:31:36.297815
# Keep-alive comment: 2025-10-01 19:31:10.626978
# Keep-alive comment: 2025-10-02 05:31:39.053840
# Keep-alive comment: 2025-10-02 15:31:36.399482
# Keep-alive comment: 2025-10-03 01:31:10.040932
# Keep-alive comment: 2025-10-03 11:31:31.062665
# Keep-alive comment: 2025-10-03 21:31:04.990094
# Keep-alive comment: 2025-10-04 07:31:05.037803
# Keep-alive comment: 2025-10-04 17:31:15.162319
# Keep-alive comment: 2025-10-05 03:31:09.911378
# Keep-alive comment: 2025-10-05 13:31:15.117682
# Keep-alive comment: 2025-10-05 23:31:35.176601
# Keep-alive comment: 2025-10-06 09:31:41.130092
# Keep-alive comment: 2025-10-06 19:31:12.480121
# Keep-alive comment: 2025-10-07 05:31:12.478021
# Keep-alive comment: 2025-10-07 15:31:33.435183
# Keep-alive comment: 2025-10-08 01:31:10.623957
# Keep-alive comment: 2025-10-08 11:31:11.858112
# Keep-alive comment: 2025-10-08 21:31:11.302119
# Keep-alive comment: 2025-10-09 07:31:13.773144
# Keep-alive comment: 2025-10-09 17:31:13.524841
# Keep-alive comment: 2025-10-10 03:31:01.034962
# Keep-alive comment: 2025-10-10 13:30:52.254436
# Keep-alive comment: 2025-10-10 23:31:05.208378
# Keep-alive comment: 2025-10-11 09:31:11.334904
# Keep-alive comment: 2025-10-11 19:31:04.903661
# Keep-alive comment: 2025-10-12 05:31:08.556434
# Keep-alive comment: 2025-10-12 15:31:12.597980
# Keep-alive comment: 2025-10-13 01:31:07.038297
# Keep-alive comment: 2025-10-13 11:31:38.464298
# Keep-alive comment: 2025-10-13 21:31:01.070027
# Keep-alive comment: 2025-10-14 07:31:05.404441
# Keep-alive comment: 2025-10-14 17:31:08.081362
# Keep-alive comment: 2025-10-15 03:31:05.583769
# Keep-alive comment: 2025-10-15 13:31:07.631931
# Keep-alive comment: 2025-10-15 23:31:10.860162
# Keep-alive comment: 2025-10-16 09:31:06.944894
# Keep-alive comment: 2025-10-16 19:31:13.030298
# Keep-alive comment: 2025-10-17 05:31:11.784477
# Keep-alive comment: 2025-10-17 15:31:28.107738
# Keep-alive comment: 2025-10-18 01:31:06.728226
# Keep-alive comment: 2025-10-18 11:31:31.520859
# Keep-alive comment: 2025-10-18 21:31:41.268735
# Keep-alive comment: 2025-10-19 07:31:01.384867
# Keep-alive comment: 2025-10-19 17:31:36.103615
# Keep-alive comment: 2025-10-20 03:31:33.624584
# Keep-alive comment: 2025-10-20 13:31:12.141979
# Keep-alive comment: 2025-10-20 23:31:06.569518
# Keep-alive comment: 2025-10-21 09:31:12.367299
# Keep-alive comment: 2025-10-21 19:33:12.972327
# Keep-alive comment: 2025-10-22 05:31:07.405136
# Keep-alive comment: 2025-10-22 15:32:12.722505
# Keep-alive comment: 2025-10-23 01:31:06.231078
# Keep-alive comment: 2025-10-23 11:31:18.834109
# Keep-alive comment: 2025-10-23 21:31:07.771228
# Keep-alive comment: 2025-10-24 07:32:27.694149
# Keep-alive comment: 2025-10-24 17:31:17.274183
# Keep-alive comment: 2025-10-25 03:31:11.624695
# Keep-alive comment: 2025-10-25 13:31:35.431544
# Keep-alive comment: 2025-10-25 23:31:07.542034
# Keep-alive comment: 2025-10-26 09:31:00.721007
# Keep-alive comment: 2025-10-26 19:31:37.595558
# Keep-alive comment: 2025-10-27 05:31:18.172162
# Keep-alive comment: 2025-10-27 15:31:32.963684
# Keep-alive comment: 2025-10-28 01:31:10.495850
# Keep-alive comment: 2025-10-28 11:31:12.795005
# Keep-alive comment: 2025-10-28 21:31:01.352541
# Keep-alive comment: 2025-10-29 07:31:08.119371
# Keep-alive comment: 2025-10-29 17:31:16.998887
# Keep-alive comment: 2025-10-30 03:31:06.807647
# Keep-alive comment: 2025-10-30 13:31:38.372503
# Keep-alive comment: 2025-10-30 23:31:13.128830
# Keep-alive comment: 2025-10-31 09:32:27.167130
# Keep-alive comment: 2025-10-31 19:31:02.501899
# Keep-alive comment: 2025-11-01 05:31:11.215632
# Keep-alive comment: 2025-11-01 15:31:00.243958
# Keep-alive comment: 2025-11-02 01:31:12.085577
# Keep-alive comment: 2025-11-02 11:31:13.518023
# Keep-alive comment: 2025-11-02 21:31:27.270839
# Keep-alive comment: 2025-11-03 07:31:07.909985
# Keep-alive comment: 2025-11-03 17:31:11.424110
# Keep-alive comment: 2025-11-04 03:31:11.849939
# Keep-alive comment: 2025-11-04 13:31:39.197250
# Keep-alive comment: 2025-11-04 23:31:31.679707
# Keep-alive comment: 2025-11-05 09:31:42.695194
# Keep-alive comment: 2025-11-05 19:31:11.936238
# Keep-alive comment: 2025-11-06 05:31:37.261176
# Keep-alive comment: 2025-11-06 15:31:25.276979
# Keep-alive comment: 2025-11-07 01:31:10.163039
# Keep-alive comment: 2025-11-07 11:31:14.716532
# Keep-alive comment: 2025-11-07 21:31:13.770763
# Keep-alive comment: 2025-11-08 07:31:01.532110
# Keep-alive comment: 2025-11-08 17:31:17.590916
# Keep-alive comment: 2025-11-09 03:31:51.476538
# Keep-alive comment: 2025-11-09 13:31:12.651150
# Keep-alive comment: 2025-11-09 23:31:02.841970
# Keep-alive comment: 2025-11-10 09:31:07.797992
# Keep-alive comment: 2025-11-10 19:31:23.913973
# Keep-alive comment: 2025-11-11 05:31:09.071619
# Keep-alive comment: 2025-11-11 15:31:06.362077
# Keep-alive comment: 2025-11-12 01:31:14.269822
# Keep-alive comment: 2025-11-12 11:31:15.882453
# Keep-alive comment: 2025-11-12 21:31:32.708508
# Keep-alive comment: 2025-11-13 07:30:56.286839
# Keep-alive comment: 2025-11-13 17:31:08.314189
# Keep-alive comment: 2025-11-14 03:31:14.818561
# Keep-alive comment: 2025-11-14 13:31:35.850360
# Keep-alive comment: 2025-11-14 23:31:07.510617
# Keep-alive comment: 2025-11-15 09:31:11.479781
# Keep-alive comment: 2025-11-15 19:31:16.716272
# Keep-alive comment: 2025-11-16 05:31:08.137553
# Keep-alive comment: 2025-11-16 15:31:12.824202
# Keep-alive comment: 2025-11-17 01:31:02.686906
# Keep-alive comment: 2025-11-17 11:31:36.448145
# Keep-alive comment: 2025-11-17 21:31:03.893559
# Keep-alive comment: 2025-11-18 07:31:06.837677
# Keep-alive comment: 2025-11-18 17:31:07.687146
# Keep-alive comment: 2025-11-19 03:31:10.923589
# Keep-alive comment: 2025-11-19 13:31:03.331442
# Keep-alive comment: 2025-11-19 23:31:05.344901
# Keep-alive comment: 2025-11-20 09:31:12.970544
# Keep-alive comment: 2025-11-20 19:33:02.482639
# Keep-alive comment: 2025-11-21 05:31:08.586396
# Keep-alive comment: 2025-11-21 15:31:12.834070
# Keep-alive comment: 2025-11-22 01:31:16.915427
# Keep-alive comment: 2025-11-22 11:31:02.092536
# Keep-alive comment: 2025-11-22 21:31:12.370987
# Keep-alive comment: 2025-11-23 07:31:13.232893
# Keep-alive comment: 2025-11-23 17:31:16.264550
# Keep-alive comment: 2025-11-24 03:31:06.837030
# Keep-alive comment: 2025-11-24 13:31:02.940843
# Keep-alive comment: 2025-11-24 23:31:13.142226
# Keep-alive comment: 2025-11-25 09:31:34.955367
# Keep-alive comment: 2025-11-25 19:31:08.857162
# Keep-alive comment: 2025-11-26 05:31:19.434622
# Keep-alive comment: 2025-11-26 15:31:18.265871
# Keep-alive comment: 2025-11-27 01:31:12.665274
# Keep-alive comment: 2025-11-27 11:31:09.279060
# Keep-alive comment: 2025-11-27 21:31:03.149077
# Keep-alive comment: 2025-11-28 07:31:01.704244
# Keep-alive comment: 2025-11-28 17:31:13.463920
# Keep-alive comment: 2025-11-29 03:31:07.768339
# Keep-alive comment: 2025-11-29 13:31:17.967784
# Keep-alive comment: 2025-11-29 23:31:07.577092
# Keep-alive comment: 2025-11-30 09:31:09.657412
# Keep-alive comment: 2025-11-30 19:30:57.952806
# Keep-alive comment: 2025-12-01 05:30:57.648275
# Keep-alive comment: 2025-12-01 15:31:04.234588
# Keep-alive comment: 2025-12-02 01:30:47.678380
# Keep-alive comment: 2025-12-02 11:31:09.982925
# Keep-alive comment: 2025-12-02 21:31:12.529988
# Keep-alive comment: 2025-12-03 07:31:09.696066
# Keep-alive comment: 2025-12-03 17:31:17.260626
# Keep-alive comment: 2025-12-04 03:31:07.227610
# Keep-alive comment: 2025-12-04 13:31:04.898197
# Keep-alive comment: 2025-12-04 23:31:07.171421
# Keep-alive comment: 2025-12-05 09:31:07.275581
# Keep-alive comment: 2025-12-05 19:31:02.096883
# Keep-alive comment: 2025-12-06 05:31:07.860381
# Keep-alive comment: 2025-12-06 15:30:54.655427
# Keep-alive comment: 2025-12-07 01:31:03.861585
# Keep-alive comment: 2025-12-07 11:31:07.388099
# Keep-alive comment: 2025-12-07 21:31:03.719701
# Keep-alive comment: 2025-12-08 07:31:17.031974
# Keep-alive comment: 2025-12-08 17:31:02.729762
# Keep-alive comment: 2025-12-09 03:31:07.198203
# Keep-alive comment: 2025-12-09 13:31:05.858087
# Keep-alive comment: 2025-12-09 23:31:07.640024
# Keep-alive comment: 2025-12-10 09:31:09.071888
# Keep-alive comment: 2025-12-10 19:31:13.522223
# Keep-alive comment: 2025-12-11 05:30:48.237740
# Keep-alive comment: 2025-12-11 15:31:10.076171
# Keep-alive comment: 2025-12-12 01:31:07.219121
# Keep-alive comment: 2025-12-12 11:30:53.663946
# Keep-alive comment: 2025-12-12 21:31:12.922291
# Keep-alive comment: 2025-12-13 07:31:06.700826
# Keep-alive comment: 2025-12-13 17:31:08.510343
# Keep-alive comment: 2025-12-14 03:31:10.742447
# Keep-alive comment: 2025-12-14 13:31:06.367274