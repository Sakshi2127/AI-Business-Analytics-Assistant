# 🤖 AI Business Analytics Assistant

An interactive business analytics dashboard built using **Python, Streamlit, Pandas, Plotly, and Google Gemini AI**. This project helps users explore sales performance, analyze business trends, and ask questions about sales data using an AI-powered assistant.

## 🚀 Live Demo

**Live App:** [Open AI Business Analytics Assistant](https://ai-business-analytics-assistant-faapppplorz22v2r7tymhgbz.streamlit.app/)

> Replace `YOUR_STREAMLIT_APP_URL` with your deployed Streamlit app link.

## 📌 Project Overview

The AI Business Analytics Assistant combines data visualization and generative AI to make sales data easier to understand. It provides an interactive dashboard for exploring business performance and an AI assistant for asking questions about the dataset.

The project uses a **synthetic e-commerce sales dataset** for demonstration purposes.

## ✨ Features

- 📊 Interactive sales analytics dashboard
- 💰 Key business metrics, including revenue and profit
- 📈 Revenue analysis by product category and region
- 📅 Monthly sales trend visualization
- 🔎 Interactive filters for exploring the data
- 📋 Sales dataset preview
- 🤖 Gemini-powered AI assistant for asking questions about sales data
- 🌐 Web-based interface built with Streamlit

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data processing and analysis |
| Streamlit | Interactive web application |
| Plotly | Interactive charts and visualizations |
| Google Gemini API | AI-powered question answering |
| python-dotenv | Local environment variable management |

## 📂 Project Structure

```text
AI-Business-Analytics-Assistant/
│
├── app.py
├── generate_data.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── data/
    └── sales_data.csv
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Business-Analytics-Assistant
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a `.env` file in the project root directory:

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own Gemini API key. Never upload your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 Dataset

The project uses a synthetic e-commerce sales dataset containing fields such as:

- Order ID and order date
- Customer ID
- Product and category
- Region
- Quantity and unit price
- Revenue, cost, and profit
- Payment method

The dataset is intended for learning, demonstration, and experimentation. It does not represent actual company sales.

## 🎯 Project Objectives

- Understand business performance through data visualization.
- Identify sales trends across categories and regions.
- Explore key revenue and profit metrics.
- Make sales data easier to query using an AI assistant.
- Apply Python, data analytics, visualization, and generative AI in one project.

## 🔮 Future Enhancements

- Add sales forecasting and trend prediction.
- Introduce more advanced business KPIs.
- Improve AI-generated insights and recommendations.
- Add data upload functionality for custom datasets.
- Enhance dashboard filtering and reporting capabilities.

## 👩‍💻 Author

**Sakshi Phadtare**

MCA Student | Aspiring Data Analyst

**Skills demonstrated:** Python, Pandas, Data Visualization, Streamlit, SQL and Generative AI.

---

⭐ If you find this project interesting, feel free to explore the repository and live demo.# AI-Business-Analytics-Assistant
