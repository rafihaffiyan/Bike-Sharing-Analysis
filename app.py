import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import altair as alt


day_df = pd.read_csv("day_bikesharing.csv")
hour_df = pd.read_csv("hour_bikesharing.csv")

st.header("Proyek Analisis Data dengan Python Dicoding :sparkles:")
st.write("Rafi Haffiyan")
st.write("haffiyanrafi@gmail.com")

st.subheader("Analisis Penggunaan Sepeda pada Rental Sepeda")
image_url = "https://media.wired.com/photos/59328fcc5c4fbd732b5538f4/master/w_2560%2Cc_limit/bike-share-660.jpg"  
st.image(image_url, use_column_width=True)
st.write("")
hourly_count = hour_df.groupby('hour')['count'].sum().reset_index()

chart = alt.Chart(hourly_count).mark_bar().encode(
    x='hour',
    y='count',
    tooltip=['hour', 'count']
).properties(
    title='Jumlah Sewa Sepeda Setiap Jam',
    width=500,
    height=300
)
st.altair_chart(chart, use_container_width=True)

counts = day_df.groupby('workingday')['count'].sum()
comparison_table = pd.DataFrame({'Total Sewa Sepeda': counts.values},
                                index=['Weekend', 'Weekday']).reset_index()

chart = alt.Chart(comparison_table).mark_bar().encode(
    x=alt.X('index', title='Kategori', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Total Sewa Sepeda', title='Total Sewa Sepeda'),
    tooltip=['index', 'Total Sewa Sepeda']
).properties(
    title='Perbandingan Jumlah Sewa Sepeda\nAntara Weekend dan Weekday'
)
st.altair_chart(chart, use_container_width=True)

counts_season = day_df.groupby('season')['count'].sum()
season_counts = pd.DataFrame({'Musim': counts_season.index, 'Jumlah Sewa Sepeda': counts_season.values})
chart_season = alt.Chart(season_counts).mark_bar().encode(
    x=alt.X('Musim:N', title='Musim'),
    y=alt.Y('Jumlah Sewa Sepeda:Q', title='Jumlah Sewa Sepeda'),
    tooltip=['Musim', 'Jumlah Sewa Sepeda']
).properties(
    title='Jumlah Sewa Sepeda Berdasarkan Musim'
)

counts_weather = day_df.groupby('weather')['count'].sum()
weather_counts = pd.DataFrame({'Cuaca': counts_weather.index, 'Jumlah Sewa Sepeda': counts_weather.values})

chart_weather = alt.Chart(weather_counts).mark_bar().encode(
    x=alt.X('Cuaca:N', title='Cuaca'),
    y=alt.Y('Jumlah Sewa Sepeda:Q', title='Jumlah Sewa Sepeda'),
    tooltip=['Cuaca', 'Jumlah Sewa Sepeda']
).properties(
    title='Jumlah Sewa Sepeda Berdasarkan Cuaca'
)
combined_chart = alt.hconcat(chart_season, chart_weather)
st.altair_chart(combined_chart, use_container_width=True)

casual_count = day_df['casual'].sum()
registered_count = day_df['registered'].sum()

data = pd.DataFrame({'Tipe Pengguna': ['Casual', 'Registered'],
                     'Jumlah Pengguna Sepeda': [casual_count, registered_count]})

chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('Tipe Pengguna', axis=alt.Axis(labelAngle=0)),
    y='Jumlah Pengguna Sepeda',
    tooltip=['Tipe Pengguna', 'Jumlah Pengguna Sepeda']
).properties(
    title='Jumlah Pengguna Sepeda Casual vs Registered'
)

st.altair_chart(chart, use_container_width=True)


total_rentals = day_df['count'].sum()
total_casual_rentals = casual_count
total_registered_rentals = registered_count
max_rentals = day_df['count'].max()
average_rentals = day_df['count'].mean()

st.sidebar.subheader("Bike Rental Summary")
st.sidebar.write("Total Count of Bike Rentals:")
st.sidebar.write(f"{total_rentals:,}")
st.sidebar.write("Maximum Bike Rentals in a Day:")
st.sidebar.write(f"{max_rentals:,}")
st.sidebar.write("Average Bike Rentals per Day:")
st.sidebar.write(f"{average_rentals:.2f}")
