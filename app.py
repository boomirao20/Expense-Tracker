import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import date
from sklearn.linear_model import LinearRegression
from io import BytesIO

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="AI Expense Tracker",
    page_icon="💰",
    layout="wide"
)

# -------------------------------------------------
# DATABASE
# -------------------------------------------------

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
category TEXT,
amount REAL
)
""")

conn.commit()

# -------------------------------------------------
# DARK MODE TOGGLE
# -------------------------------------------------

theme = st.sidebar.radio("Theme", ["Light Mode", "Dark Mode"])

if theme == "Dark Mode":

    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }

    h1,h2,h3,h4,h5,h6,p,label,span {
        color:white !important;
    }

    section[data-testid="stSidebar"] {
        background-color:#111827;
    }

    div[data-testid="stMetric"]{
        background-color:#1f2937;
        padding:15px;
        border-radius:10px;
    }

    .stButton>button{
        background-color:#22c55e;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("💰 Expense Tracker")

menu = st.sidebar.radio(
    "Navigation",
    ["Add Expense","Dashboard","Analytics"]
)

# =================================================
# ADD EXPENSE
# =================================================

if menu == "Add Expense":

    st.header("Add Expense")

    col1,col2,col3 = st.columns(3)

    expense_date = col1.date_input("Date",date.today())

    category = col2.selectbox(
        "Category",
        ["🍔 Food","🚗 Travel","🛍 Shopping","💡 Bills","📦 Other"]
    )

    amount = col3.number_input("Amount",min_value=0)

    if st.button("Add Expense"):

        cursor.execute(
            "INSERT INTO expenses(date,category,amount) VALUES(?,?,?)",
            (expense_date,category,amount)
        )

        conn.commit()

        st.success("Expense Added!")

# =================================================
# DASHBOARD
# =================================================

elif menu == "Dashboard":

    df = pd.read_sql("SELECT * FROM expenses",conn)

    if df.empty:

        st.info("No expenses yet")

    else:

        st.header("Expense Dashboard")

        df["date"] = pd.to_datetime(df["date"])

        # DATE FILTER
        start_date = st.sidebar.date_input("Start Date",df["date"].min())
        end_date = st.sidebar.date_input("End Date",df["date"].max())

        df = df[(df["date"]>=str(start_date))&(df["date"]<=str(end_date))]

        # KPI CARDS
        total = df["amount"].sum()
        avg = df["amount"].mean()
        entries = len(df)

        col1,col2,col3 = st.columns(3)

        col1.metric("💰 Total Spending",f"₹{total}")
        col2.metric("📊 Average Expense",f"₹{round(avg,2)}")
        col3.metric("🧾 Entries",entries)

        st.divider()

        st.dataframe(df,use_container_width=True)

        # DELETE
        st.subheader("Delete Expense")

        delete_id = st.number_input("Expense ID",min_value=1)

        if st.button("Delete"):

            cursor.execute("DELETE FROM expenses WHERE id=?",(delete_id,))
            conn.commit()

            st.warning("Expense Deleted")

        # DOWNLOAD CSV
        st.subheader("Download Report")

        csv = df.to_csv(index=False)

        st.download_button(
            "Download CSV",
            csv,
            "expense_report.csv",
            "text/csv"
        )

        # DOWNLOAD EXCEL
        excel_buffer = BytesIO()

        df.to_excel(excel_buffer,index=False,engine="openpyxl")

        excel_data = excel_buffer.getvalue()

        st.download_button(
            label="Download Excel",
            data=excel_data,
            file_name="expense_report.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # -------------------------------------------------
        # MONTHLY BUDGET TRACKER
        # -------------------------------------------------

        st.divider()

        st.subheader("💼 Monthly Budget Tracker")

        budget = st.number_input(
            "Enter Monthly Budget",
            min_value=0,
            value=10000
        )

        spent = df["amount"].sum()

        remaining = budget - spent

        st.metric("Budget Remaining",f"₹{remaining}")

        if spent > budget:
            st.error("⚠ You exceeded your monthly budget!")
        else:
            st.success("✔ You are within your budget.")

# =================================================
# ANALYTICS
# =================================================

elif menu == "Analytics":

    st.header("Expense Analytics")

    df = pd.read_sql("SELECT * FROM expenses",conn)

    if df.empty:

        st.info("No data available")

    else:

        df["date"] = pd.to_datetime(df["date"])

        category_data = df.groupby("category")["amount"].sum().reset_index()

        col1,col2 = st.columns(2)

        # PIE CHART
        with col1:

            fig = px.pie(
                category_data,
                values="amount",
                names="category",
                title="Expense Distribution",
                hole=0.4
            )

            st.plotly_chart(fig,use_container_width=True)

        # BAR CHART
        with col2:

            fig2 = px.bar(
                category_data,
                x="category",
                y="amount",
                title="Category Spending",
                color="category"
            )

            st.plotly_chart(fig2,use_container_width=True)

        # MONTHLY REPORT

        df["month"] = df["date"].dt.strftime("%b %Y")

        monthly_data = df.groupby("month")["amount"].sum().reset_index()

        fig3 = px.line(
            monthly_data,
            x="month",
            y="amount",
            markers=True,
            title="Monthly Expense Trend"
        )

        st.plotly_chart(fig3,use_container_width=True)

        # -------------------------------------------------
        # AI PREDICTION
        # -------------------------------------------------

        monthly_data["month_num"] = np.arange(len(monthly_data))

        X = monthly_data[["month_num"]]
        y = monthly_data["amount"]

        model = LinearRegression()

        model.fit(X,y)

        next_month = np.array([[len(monthly_data)]])

        prediction = model.predict(next_month)

        predicted = round(prediction[0],2)

        st.subheader("🤖 AI Prediction")

        st.success(f"Predicted Next Month Expense: ₹{predicted}")

        # -------------------------------------------------
        # AI SPENDING INSIGHTS
        # -------------------------------------------------

        st.divider()

        st.subheader("🧠 AI Spending Insights")

        total_spending = df["amount"].sum()

        top_category = category_data.loc[
            category_data["amount"].idxmax(),"category"
        ]

        top_amount = category_data["amount"].max()

        percentage = (top_amount/total_spending)*100

        avg_expense = df["amount"].mean()

        st.info(f"You spent the most on **{top_category} (₹{top_amount})**.")

        st.info(
            f"**{top_category} accounts for {percentage:.2f}% of your spending.**"
        )

        st.info(
            f"Your **average expense** is **₹{avg_expense:.2f}**."
        )

        if percentage > 50:

            st.warning(
                f"⚠ You are spending a large portion on {top_category}. Consider reducing it."
            )