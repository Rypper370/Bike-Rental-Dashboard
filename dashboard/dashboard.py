import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_daily_trend(df):
    daily = df.groupby('dteday').agg({
        'cnt': 'sum'
    }).reset_index()
    daily.columns = ['dteday', 'Total Rentals']
    return daily

def create_season(df):
    # Membuat salinan dataframe untuk menghindari perubahan pada df asli
    df_season = df.copy()
    season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    df_season['season'] = df_season['season'].map(season_labels)
    df_season['season'] = pd.Categorical(df_season['season'], categories=["Spring", "Summer", "Fall", "Winter"], ordered=True)
    season_trend = df_season.groupby(['season']).agg({
        "cnt": "sum"
    }).reset_index()
    return season_trend

def create_workingday_season(df):
    df_workingday = df.copy()
    season_labels = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    df_workingday['season'] = df_workingday['season'].map(season_labels)
    df_workingday['season'] = pd.Categorical(df_workingday['season'], categories=["Spring", "Summer", "Fall", "Winter"], ordered=True)
    workingday_season = df_workingday.groupby(["workingday", "season"]).agg({
        "cnt": ["min", "max", "mean"]
    })
    workingday_season.columns = ['min_cnt', 'max_cnt', 'mean_cnt']
    workingday_season = workingday_season.reset_index()
    return workingday_season

#load data
day_df = pd.read_csv("day.csv")
datetime_column = ["dteday"]
day_df.sort_values(by="dteday", inplace=True)
day_df.reset_index(inplace=True)

for column in datetime_column:
    day_df[column] = pd.to_datetime(day_df[column])

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df["dteday"] >= str(start_date)) & 
                (day_df["dteday"] <= str(end_date))]

#Menyiapkan berbagai dataframe
daily_trend = create_daily_trend(main_df)
season_trend = create_season(main_df)
workingday_season = create_workingday_season(main_df)

st.header("Bike Rental Dashboard")

#membuat daily bike rental
st.subheader("Daily Bike Rental")
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_rides = main_df["cnt"].sum()
    st.metric("Total Rides", f"{total_rides:,}")
with col2:
    avg_rides = main_df["cnt"].mean()
    st.metric("Average Daily Rides", f"{avg_rides:.2f}")
with col3:
    max_rides = main_df["cnt"].max()
    st.metric("Max Daily Rides", f"{max_rides:,}")
with col4:
    days_count = main_df.shape[0]
    st.metric("Days Analyzed", f"{days_count}")

fig, ax = plt.subplots(figsize=(12, 6))

#Visualisasi daily bike rental
ax.plot(
    daily_trend["dteday"],
    daily_trend["Total Rentals"],
    marker='o', 
    linewidth=2,
    color="#72BCD4"
)
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
fig.tight_layout()
st.pyplot(fig)


# Visualisasi tren musim
st.subheader("Bike Rentals Based on Season")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(
    x='season', 
    y='cnt', 
    data=season_trend,
    palette=["#00FF00", "#FFFF00", "#FFA500", "#00B5E2"]
)
ax.grid(axis='y', linestyle='--', alpha=0.7)
ax.tick_params(axis='x', labelsize=12)
ax.set_xlabel(None)
ax.set_ylabel(None)
fig.tight_layout()
st.pyplot(fig)


# Visualisasi perbandingan jumlah penyewaan di hari kerja dan hari libur di setiap musim
st.subheader("Comparison of Weekday and Holiday Rentals in Each Season")
fig, ax = plt.subplots(figsize=(12, 6))
workingday_labels = {0: 'Weekend', 1: 'Working day'}
colors = ['#4682B4', '#CD853F'] 
sns.barplot(
    data=workingday_season,
    x='season',
    y='mean_cnt',
    hue='workingday',
    palette=colors,
    ax=ax
)
ax.set_ylim(0, 6000)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, [workingday_labels[int(label)] for label in labels], title='Information')
st.pyplot(fig)