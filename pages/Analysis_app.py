import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import pickle

# ---------- Page Configuration ---------- #
st.set_page_config(
    page_title='IntelliEstate Analytics Dashboard',
    layout="wide",
    page_icon="🏡"
)

# ---------- Title & Header ---------- #
st.title('IntelliEstate 🏠 Real Estate Analytics Dashboard')
st.markdown("""
<style>
.big-font {
    font-size:22px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ---------- #
view = st.sidebar.radio("Navigation", ["Overview", "Map", "WordCloud", "Price Analysis", "Distribution"])

# ---------- Load Data ---------- #
with st.spinner('Loading data and features...'):
    with open(r'D:\DOCUMENTS\Projects\IntelliEstate - AI Realty Companion\feature_text.pkl', 'rb') as f:
        feature_text = pickle.load(f)

    new_df = pd.read_csv(r'D:\DOCUMENTS\Projects\IntelliEstate - AI Realty Companion\data_viz1.csv')

    if isinstance(feature_text, list):
        feature_text = " ".join(feature_text)



# ---------- KPI Metrics ---------- #
st.header("📌 Key Metrics")
avg_price = new_df['price'].mean()
avg_area = new_df['built_up_area'].mean()
total_properties = new_df.shape[0]
col1, col2, col3 = st.columns(3)

# Comparison values (dummy example)
previous_month_avg_price = avg_price * 0.95  # Example: 5% increase
sector_avg_price = new_df.groupby('sector')['price'].mean().mean()
col1, col2, col3 = st.columns(3)
col1.metric(
    "📦 Avg. Price (Crores)",
    f"₹ {avg_price:,.0f}",
    delta=f"{((avg_price - previous_month_avg_price) / previous_month_avg_price) * 100:.2f}% vs last month",
    delta_color="normal"
)
col2.metric(
    "📊 Avg. Area (sqft)",
    f"{avg_area:.2f}",
    delta=f"{avg_area - new_df['built_up_area'].median():.2f} sqft vs median"
)
col3.metric(
    "🏡 Total Listings",
    total_properties,
    delta=f"{total_properties - new_df['sector'].nunique()} vs unique sectors"
)

# ---------- Views ---------- #
if view == "Map":
    st.header("🗺️ Sector-wise Price Per Sqft Map")
    group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()
    fig_map = px.scatter_mapbox(
        group_df,
        lat="latitude",
        lon="longitude",
        color="price_per_sqft",
        size='built_up_area',
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        mapbox_style="open-street-map",
        hover_name=group_df.index,
        width=1200,
        height=700
    )
    st.plotly_chart(fig_map, use_container_width=True)

elif view == "WordCloud":
    st.header("🌀 Feature Keyword WordCloud")
    sectors = ['Overall'] + sorted(new_df['sector'].dropna().unique().tolist())
    selected_wc_sector = st.selectbox("Select Sector for WordCloud:", sectors)

    if selected_wc_sector == 'Overall':
        wc_text = feature_text
    else:
        sector_df = new_df[new_df['sector'] == selected_wc_sector]
        wc_text = " ".join(sector_df.astype(str).apply(lambda x: ' '.join(x), axis=1))

    stopwords = set(WordCloud().stopwords).union({'sector', 'flat', 'house', 'price', 'area'})
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color='white',
        stopwords=stopwords,
        min_font_size=10
    ).generate(wc_text)

    fig_wc, ax_wc = plt.subplots(figsize=(8, 8))
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig_wc)

elif view == "Price Analysis":
    st.header("📈 Area vs Price by Property Type")
    property_type = st.selectbox('Select Property Type:', ['house', 'flat'])
    filtered_df = new_df[new_df['property_type'] == property_type]
    fig_price_scatter = px.scatter(
        filtered_df,
        x="built_up_area",
        y="price",
        color="bedRoom",
        title=f"Built-up Area vs Price for {property_type.title()}s",
        hover_data=['sector', 'price_per_sqft']
    )
    st.plotly_chart(fig_price_scatter, use_container_width=True)

    st.header("🍰 Bedroom Distribution by Sector")
    sector_options = ['Overall'] + sorted(new_df['sector'].dropna().unique().tolist())
    selector_sector = st.selectbox('Select Sector:', sector_options)

    if selector_sector == 'Overall':
        pie_data = new_df
    else:
        pie_data = new_df[new_df['sector'] == selector_sector]

    fig_bhk_pie = px.pie(
        pie_data,
        names='bedRoom',
        title=f"Bedroom Distribution in {selector_sector}"
    )
    st.plotly_chart(fig_bhk_pie, use_container_width=True)

    st.download_button("Download Sector Data", pie_data.to_csv(index=False), file_name="sector_data.csv")

elif view == "Distribution":
    st.header("🏡 BHK vs Price Comparison")
    temp_df = new_df[new_df['bedRoom'] <= 4]
    fig_box = px.box(
        temp_df,
        x='bedRoom',
        y='price',
        title='Price Range by Bedroom Count (1-4 BHK)'
    )
    st.plotly_chart(fig_box)

    st.header("🔍 Price Distribution for Houses")
    fig_dist, ax_dist = plt.subplots()
    sns.histplot(new_df[new_df['property_type'] == 'house']['price'], kde=True, ax=ax_dist)
    ax_dist.set_title("Price Distribution of Houses")
    st.pyplot(fig_dist)

elif view == "Overview":
    st.header("Welcome to IntelliEstate Dashboard")
    st.markdown("""
    This dashboard provides an analytical overview of real estate data including:
    - 📌 WordClouds for keyword insights
    - 🗺️ Geo-plots for sector performance
    - 📊 Price and Area correlations
    - 🧠 Dynamic sector-level comparisons
    """)

# ---------- Footer ---------- #
st.markdown("""
<hr style="border: 1px solid #f0f0f0;">
<div style='text-align: center;'>
Built with ❤️ using Streamlit | IntelliEstate © 2025
</div>
""", unsafe_allow_html=True)
