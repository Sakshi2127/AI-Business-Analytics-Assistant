
from pathlib import Path
import os

import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from google import genai


# =========================================================
# 1. PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AI Business Analytics Assistant",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).parent
DATA_PATH = BASE_DIR / "data" / "sales_data.csv"

load_dotenv(BASE_DIR / ".env")
API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

GREEN = "#168568"
DARK_GREEN = "#123F35"
FOREST = "#145A46"
MINT = "#DCEFE0"
CREAM = "#F8F8EF"
TEXT = "#173F43"

PALETTE = [
    "#145A46",
    "#23866B",
    "#55A982",
    "#91C49A",
    "#D2DF9B",
]


# =========================================================
# 2. PREMIUM GREEN + CREAM THEME
# =========================================================

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #F8F8EF, #EDF5E9);
        color: #173F43;
    }

    [data-testid="stHeader"] {
        background: rgba(248, 248, 239, 0.95);
    }

    h1, h2, h3 {
        color: #123F35 !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #123F35, #092E26);
    }

    [data-testid="stSidebar"] * {
        color: #F4F7ED;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #F8F8EF;
        border-color: #82B98B;
        border-radius: 9px;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background-color: #23866B;
        color: white;
        border: 1px solid #55A982;
        border-radius: 7px;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: white;
    }

    [data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.9);
        border: 1px solid #D8E8DA;
        border-radius: 16px;
        padding: 20px 18px;
        box-shadow: 0 4px 16px rgba(18, 63, 53, 0.06);
    }

    [data-testid="stMetricLabel"] {
        color: #426A5F;
    }

    [data-testid="stMetricValue"] {
        color: #123F35;
        font-weight: 700;
    }

    div[data-testid="stPlotlyChart"],
    div[data-testid="stDataFrame"] {
        background: rgba(255, 255, 255, 0.65);
        border: 1px solid #D8E8DA;
        border-radius: 14px;
        padding: 7px;
    }

    div[data-testid="stChatMessage"] {
        background: #F8FBF5;
        border: 1px solid #D3E5D5;
        border-radius: 14px;
        padding: 14px;
        color: #173F43;
    }

    [data-testid="stChatInput"] {
        background: #F8F8EF;
        border: 1px solid #82B98B;
        border-radius: 14px;
    }

    [data-testid="stChatInput"] textarea {
        color: #123F35;
    }

    [data-testid="stDownloadButton"] button,
    [data-testid="stButton"] button {
        background: #168568;
        color: white;
        border: 1px solid #168568;
        border-radius: 9px;
        font-weight: 600;
    }

    [data-testid="stDownloadButton"] button:hover,
    [data-testid="stButton"] button:hover {
        background: #123F35;
        color: white;
    }

    hr {
        border-color: #D8E8DA;
    }

    .hero {
        background: linear-gradient(120deg, #123F35, #23866B);
        padding: 25px 28px;
        border-radius: 18px;
        margin-bottom: 22px;
    }

    .hero h1 {
        color: #FFFFFF !important;
        margin: 0;
    }

    .hero p {
        color: #E4F2E8;
        margin: 8px 0 0 0;
    }

    .section-note {
        color: #68877A;
        font-size: 14px;
    }

    
    /* Sidebar dropdowns and selected filter chips */
    [data-testid="stSidebar"] [data-baseweb="select"] [data-baseweb="tag"] {
        background: #23866B !important;
        border: 1px solid #91C49A !important;
        border-radius: 7px !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #F8F8EF !important;
        border-color: #82B98B !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] input {
        color: #123F35 !important;
    }

    [data-testid="stSidebar"] [data-baseweb="select"] svg {
        fill: #145A46 !important;
    }

    [data-testid="stSidebar"] [role="option"] {
        background-color: #F8F8EF !important;
        color: #123F35 !important;
    }

    [data-testid="stSidebar"] [role="option"]:hover {
        background-color: #DCEFE0 !important;
    }

    
    /* Chat question and answer text visibility */
    [data-testid="stChatMessage"] {
        background-color: #F8F8EF !important;
        color: #123F35 !important;
    }

    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] div,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] strong,
    [data-testid="stChatMessage"] span {
        color: #123F35 !important;
    }

    /* Text typed in the chatbot input */
    [data-testid="stChatInput"] textarea {
        color: #123F35 !important;
        -webkit-text-fill-color: #123F35 !important;
        background-color: #F8F8EF !important;
        caret-color: #168568 !important;
    }

    [data-testid="stChatInput"] textarea::placeholder {
        color: #68877A !important;
        -webkit-text-fill-color: #68877A !important;
        opacity: 1 !important;
    }

    
    /* Premium green selected filter chips */
    [data-testid="stSidebar"] [data-baseweb="tag"] {
        background-color: #23866B !important;
        border: 1px solid #91C49A !important;
        border-radius: 7px !important;
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: #FFFFFF !important;
    }

    /* Filter chip close/remove icon */
    [data-testid="stSidebar"] [data-baseweb="tag"] svg {
        fill: #FFFFFF !important;
        color: #FFFFFF !important;
    }

    /* Dropdown box */
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        background-color: #F8F8EF !important;
        border-color: #82B98B !important;
        border-radius: 9px !important;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    data["order_date"] = pd.to_datetime(
        data["order_date"], errors="coerce"
    )
    return data


st.markdown("""
<div class="hero">
    <h1>📊 AI Business Analytics Assistant</h1>
    <p>Explore sales, track performance and get AI-powered insights.</p>
</div>
""", unsafe_allow_html=True)

try:
    df = load_data()
except FileNotFoundError:
    st.error(
        "Dataset not found. Check that data/sales_data.csv "
        "exists inside your project folder."
    )
    st.stop()
except Exception as error:
    st.error(f"Could not load the dataset: {error}")
    st.stop()

required_columns = {
    "order_id", "order_date", "category", "region",
    "revenue", "profit", "quantity", "cost", "unit_price"
}

missing_columns = required_columns.difference(df.columns)

if missing_columns:
    st.error(f"Dataset is missing these columns: {sorted(missing_columns)}")
    st.stop()


# =========================================================
# 4. SIDEBAR FILTERS
# =========================================================

st.sidebar.title("🌿 Analytics Filters")
st.sidebar.caption("Customize your dashboard")

all_categories = sorted(df["category"].dropna().unique().tolist())
all_regions = sorted(df["region"].dropna().unique().tolist())

categories = st.sidebar.multiselect(
    "Select category",
    options=all_categories,
    default=all_categories,
)

regions = st.sidebar.multiselect(
    "Select region",
    options=all_regions,
    default=all_regions,
)

if st.sidebar.button("↻ Reset filters", width="stretch"):
    st.rerun()

filtered = df[
    df["category"].isin(categories)
    & df["region"].isin(regions)
].copy()


# =========================================================
# 5. KPI CARDS
# =========================================================

st.subheader("Business Overview")

revenue = float(filtered["revenue"].sum())
profit = float(filtered["profit"].sum())
orders = int(filtered["order_id"].nunique())
avg_order = revenue / orders if orders else 0

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"₹{revenue:,.0f}")
col2.metric("📈 Total Profit", f"₹{profit:,.0f}")
col3.metric("🛒 Total Orders", f"{orders:,}")
col4.metric("🧾 Average Order Value", f"₹{avg_order:,.0f}")

st.divider()


# =========================================================
# 6. REVENUE BY CATEGORY
# =========================================================

st.subheader("📊 Revenue by Category")

category_sales = (
    filtered.groupby("category", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

fig_category = px.bar(
    category_sales,
    x="category",
    y="revenue",
    color="category",
    color_discrete_sequence=PALETTE,
    title="Category-wise Revenue",
    template="plotly_white",
    text_auto=".2s",
)

fig_category.update_traces(
    marker_line_color=CREAM,
    marker_line_width=1,
    textposition="outside",
    cliponaxis=False,
    hovertemplate="%{x}<br>Revenue: ₹%{y:,.0f}<extra></extra>",
)

fig_category.update_layout(
    paper_bgcolor=CREAM,
    plot_bgcolor=CREAM,
    font=dict(color=TEXT, size=12),
    title_font=dict(color=DARK_GREEN, size=18),
    showlegend=False,
    margin=dict(l=20, r=25, t=65, b=35),
    xaxis=dict(title="Category", showgrid=False),
    yaxis=dict(title="Revenue (₹)", gridcolor="#DCE9DC"),
)

st.plotly_chart(
    fig_category,
    width="stretch",
    theme=None,
)


# =========================================================
# 7. REVENUE BY REGION
# =========================================================

st.subheader("🌍 Revenue by Region")

region_sales = (
    filtered.groupby("region", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

fig_region = px.pie(
    region_sales,
    names="region",
    values="revenue",
    title="Regional Revenue Share",
    hole=0.48,
    color="region",
    color_discrete_sequence=PALETTE,
    template="plotly_white",
)

fig_region.update_traces(
    textposition="inside",
    textinfo="label+percent",
    marker=dict(line=dict(color=CREAM, width=3)),
    hovertemplate=(
        "<b>%{label}</b><br>"
        "Revenue: ₹%{value:,.0f}<br>"
        "Share: %{percent}<extra></extra>"
    ),
)

fig_region.update_layout(
    paper_bgcolor=CREAM,
    plot_bgcolor=CREAM,
    font=dict(color=TEXT, size=12),
    title_font=dict(color=DARK_GREEN, size=18),
    margin=dict(l=20, r=20, t=65, b=25),
    legend=dict(font=dict(color=TEXT)),
)

st.plotly_chart(
    fig_region,
    width="stretch",
    theme=None,
)


# =========================================================
# 8. MONTHLY REVENUE TREND
# =========================================================

st.subheader("📈 Monthly Revenue Trend")

monthly = (
    filtered.dropna(subset=["order_date"])
    .set_index("order_date")
    .resample("MS")["revenue"]
    .sum()
    .reset_index()
)

fig_monthly = px.line(
    monthly,
    x="order_date",
    y="revenue",
    markers=True,
    title="Monthly Revenue",
    template="plotly_white",
)

fig_monthly.update_traces(
    line=dict(color=GREEN, width=3),
    marker=dict(
        color=GREEN,
        size=8,
        line=dict(color=CREAM, width=2),
    ),
    fill="tozeroy",
    fillcolor="rgba(22,133,104,0.12)",
    hovertemplate=(
        "<b>%{x|%b %Y}</b><br>"
        "Revenue: ₹%{y:,.0f}<extra></extra>"
    ),
)

fig_monthly.update_layout(
    paper_bgcolor=CREAM,
    plot_bgcolor=CREAM,
    font=dict(color=TEXT, size=12),
    title_font=dict(color=DARK_GREEN, size=18),
    margin=dict(l=20, r=25, t=65, b=35),
    xaxis=dict(title="Month", showgrid=False),
    yaxis=dict(title="Revenue (₹)", gridcolor="#DCE9DC"),
    hovermode="x unified",
)

st.plotly_chart(
    fig_monthly,
    width="stretch",
    theme=None,
)


# =========================================================
# 9. FULL SALES DATA TABLE
# =========================================================

st.divider()
st.subheader("📋 Sales Data")
st.caption("Explore the filtered records or download them as a CSV file.")


styled_data = (
    filtered.style
    .set_properties(**{
        "background-color": "#F8F8EF",
        "color": "#173F43",
        "border-color": "#D8E8DA",
    })
    .set_table_styles([
        {
            "selector": "th",
            "props": [
                ("background-color", "#145A46"),
                ("color", "#FFFFFF"),
                ("font-weight", "bold"),
                ("border-color", "#D8E8DA"),
            ],
        },
        {
            "selector": "td",
            "props": [
                ("border-color", "#D8E8DA"),
            ],
        },
    ])
)

st.dataframe(
    styled_data,
    width="stretch",
    hide_index=True,
    column_config={
        "order_date": st.column_config.DateColumn(
            "Order Date",
            format="DD MMM YYYY",
        ),
        "revenue": st.column_config.NumberColumn(
            "Revenue",
            format="₹ %.2f",
        ),
        "profit": st.column_config.NumberColumn(
            "Profit",
            format="₹ %.2f",
        ),
        "cost": st.column_config.NumberColumn(
            "Cost",
            format="₹ %.2f",
        ),
        "unit_price": st.column_config.NumberColumn(
            "Unit Price",
            format="₹ %.2f",
        ),
    },
)


# =========================================================
# 10. AI ASSISTANT — LAST SECTION
# =========================================================

st.divider()

st.markdown("""
<div class="hero">
    <h1>🤖 Ask Your Business Data</h1>
    <p>
        Ask questions about revenue, profit, categories, regions
        and business recommendations.
    </p>
</div>
""", unsafe_allow_html=True)


# Calculate exact summaries using Python

category_summary = (
    filtered.groupby("category")[["revenue", "profit", "quantity"]]
    .sum()
    .sort_values("revenue", ascending=False)
)

region_summary = (
    filtered.groupby("region")[["revenue", "profit", "quantity"]]
    .sum()
    .sort_values("revenue", ascending=False)
)


def get_top(summary, column):
    if summary.empty:
        return None, 0.0

    name = summary[column].idxmax()
    return str(name), float(summary.loc[name, column])


top_category_revenue = get_top(category_summary, "revenue")
top_category_profit = get_top(category_summary, "profit")
top_region_revenue = get_top(region_summary, "revenue")
top_region_profit = get_top(region_summary, "profit")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.button("🗑️ Clear chat history"):
    st.session_state.chat_history = []
    st.rerun()


# Show previous chat messages

for message in st.session_state.chat_history:
    content = message.get("content", "")

    if content.strip():
        with st.chat_message(message["role"]):
            st.markdown(
                content,
                unsafe_allow_html=False,
            )



question = st.chat_input(
    "Ask: Which category has the highest revenue?"
)


if question:
    st.session_state.chat_history.append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.markdown(question)

    q = question.lower().replace("-", " ")
    answer = None

    asks_highest = any(
        word in q for word in ["highest", "maximum", "max", "top", "most"]
    )
    asks_category = "categor" in q or "product" in q
    asks_region = "region" in q
    asks_profit = "profit" in q
    asks_revenue = any(
        word in q for word in ["revenue", "sales", "earning", "income"]
    )

    # Handle exact numerical questions in Python first

    if filtered.empty:
        answer = (
            "No data is available for the selected filters. "
            "Please select at least one category and region."
        )

    elif asks_highest and asks_category and asks_profit:
        name, value = top_category_profit
        answer = f"**Highest-profit category: {name}**\n\nProfit: ₹{value:,.2f}"

    elif asks_highest and asks_category and asks_revenue:
        name, value = top_category_revenue
        answer = f"**Highest-revenue category: {name}**\n\nRevenue: ₹{value:,.2f}"

    elif asks_highest and asks_region and asks_profit:
        name, value = top_region_profit
        answer = f"**Highest-profit region: {name}**\n\nProfit: ₹{value:,.2f}"

    elif asks_highest and asks_region and asks_revenue:
        name, value = top_region_revenue
        answer = f"**Highest-revenue region: {name}**\n\nRevenue: ₹{value:,.2f}"

    elif "average" in q and "order" in q:
        answer = f"**Average order value: ₹{avg_order:,.2f}**"

    elif "total profit" in q:
        answer = f"**Total profit: ₹{profit:,.2f}**"

    elif "total revenue" in q or "total sales" in q:
        answer = f"**Total revenue: ₹{revenue:,.2f}**"

    elif "total orders" in q or "how many orders" in q or "number of orders" in q:
        answer = f"**Total orders: {orders:,}**"

    # Use Gemini for broader questions and recommendations

    if answer is None:
        if not API_KEY:
            answer = (
                "Gemini API key not found. Check that your root project "
                "folder contains a .env file with GEMINI_API_KEY set."
            )

        else:
            context = f"""
You are an AI business analytics assistant.

Answer the user's question using only the dataset summaries below.
Do not invent figures or claim that suggestions are proven results.
If the requested information is not present, say so.
Keep the answer clear, practical and easy to understand.

FILTERED DATA SUMMARY
Total revenue: ₹{revenue:,.2f}
Total profit: ₹{profit:,.2f}
Total orders: {orders}
Average order value: ₹{avg_order:,.2f}

Category summary (revenue, profit, quantity):
{category_summary.round(2).to_string()}

Region summary (revenue, profit, quantity):
{region_summary.round(2).to_string()}

Monthly revenue:
{monthly.to_string(index=False)}

User question:
{question}
"""

            try:
                with st.spinner("AI is analyzing your business data..."):
                    client = genai.Client(api_key=API_KEY)

                    try:
                        response = client.models.generate_content(
                            model="gemini-flash-latest",
                            contents=context,
                        )
                        answer = response.text or (
                            "I couldn't generate an answer. Please try again."
                        )
                    finally:
                        client.close()

            except Exception as error:
                answer = (
                    "Gemini could not respond. Please check your API key, "
                    "internet connection, API quota and model availability."
                )
                st.error(f"Technical details: {error}")

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": answer}
    )
