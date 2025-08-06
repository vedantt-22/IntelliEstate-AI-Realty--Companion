## 🏡 IntelliEstate – AI Realty Companion

**IntelliEstate** is an AI-powered real estate analysis and prediction platform that helps users explore, understand, and make informed decisions about property investments in India. It provides intelligent tools for price prediction, trend visualization, recommendation, and insights — all powered by machine learning, data analysis, and interactive visualizations.

---

## 🚀 Features

- 🔍 Price Prediction Module – Predict property prices using trained machine learning models.
- 📊 Analytical Dashboard – Explore trends, correlations, and insights through interactive plots and charts.
- 🤝 Recommendation Engine – Suggests properties based on user preferences using similarity-based filtering.
- 🧹 Data Cleaning Pipelines – Handles outliers, missing values, and noisy data efficiently.
- 📈 EDA & Feature Engineering – Visualize univariate, bivariate, and multivariate relationships.
- 🌐 Web Scraping Utilities – Extract raw listings data from real estate portals.
- 🧠 Model Selection & Evaluation – Multiple regression models with evaluation metrics and visual comparison.
- 🧾 Streamlit Frontend – Simple and responsive UI to interact with the platform.

---

## 🛠️ Tech Stack

| Component         | Technology Used                        |
|------------------|----------------------------------------|
| Programming       | Python                                 |
| Web Framework     | Streamlit                              |
| Data Processing   | Pandas, NumPy                          |
| Machine Learning  | Scikit-learn, XGBoost                  |
| Visualization     | Matplotlib, Seaborn, Plotly            |
| Web Scraping      | BeautifulSoup, Selenium                |
| Version Control   | Git & GitHub                           |

---

## 📁 Project Structure

```

IntelliEstate/
│
├── Pages/                        # Streamlit pages
├── Data/
│   ├── Raw Dataset/             # Unprocessed CSV files
│   ├── Data Cleaning/           # Jupyter notebooks for preprocessing
│   ├── EDA/                     # Exploratory Data Analysis
│   ├── Feature Engineering/     # Feature generation & baseline models
│   ├── Price Predictor/         # Model training & selection
│   └── Recommender System/      # Property recommendation system
│
├── pipeline.pkl                 # Trained ML pipeline (tracked via Git LFS)
├── requirements.txt             # Dependencies
├── README.md                    # Project documentation
└── .gitattributes               # Git LFS tracking

````

---

## 🔍 Usage

### 📦 1. Clone the Repository

```bash
git clone https://github.com/vedantt-22/IntelliEstate---AI-Realty-Companion.git
cd IntelliEstate---AI-Realty-Companion
````

### 🐍 2. Set up Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### 🚀 3. Run the App

```bash
streamlit run main.py
```


## 📈 Example Screenshots

<img width="1917" height="905" alt="image" src="https://github.com/user-attachments/assets/c563ecd0-b943-4549-afd5-4320ad3a22ed" />


---

## 📊 Sample Visualizations

🗺️ Sector GeoMap – Visualize price per sqft across locations
🌀 WordCloud – Extract popular keywords from property features.
📈 Area vs Price – See how built-up area affects pricing.
📊 Bedroom Distribution – Understand BHK trends by sector.
📉 Price Distribution – Compare prices across property types.

---
📄 License
This project is licensed under the Vedant Karekar.


