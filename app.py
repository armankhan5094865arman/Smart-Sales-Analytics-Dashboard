"""
Smart Sales Analytic Dashboard Code in Python :

"""

# Importing of Labraries :
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Backgroung color :
st.markdown(
    """
<style>
.stApp {
    background-color: lightgray;
}
</style>
""",
    unsafe_allow_html=True,
)

# Side Menu code :
st.sidebar.title("Menu")
st.sidebar.write("Home")
st.sidebar.write("Contact")
st.sidebar.write("About")
st.sidebar.write("Skills")
st.sidebar.write("certifications")
st.sidebar.write("Company")
st.sidebar.write("Technologies")
st.sidebar.write("Tools")
st.sidebar.write("Setting")

# Body of the App
st.title("Smart Sales Analytics Dashboard")
st.subheader("Welcome to the smart sales analytics dashboard!")
st.write("Upload your sales data and analyze your business performace.")

uploaded_file = st.file_uploader("upload your sales csv file here", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    # Subheadig
    st.subheader("Original Data :")

    st.dataframe(data)
    data = data.drop_duplicates()
    data = data.dropna()
    data["Date"] = pd.to_datetime(data["Date"])
    data["Quantity"] = pd.to_numeric(data["Quantity"])
    data["Price"] = pd.to_numeric(data["Price"])
    # Subheading
    st.subheader("Cleaned Data :")

    st.dataframe(data)

    data["Total_sale"] = data["Quantity"] * data["Price"]
    Total_sales = data["Total_sale"].sum()
    total_quantity = data["Quantity"].sum()
    average_sale = data["Total_sale"].mean()
    best_product = data.groupby("Product")["Total_sale"].sum().idxmax()
    st.subheader("Sales Overview :")

    # Making or Rows :

    col1, col2 = st.columns(2)
    col1.metric("Total Sales ", f"Rs:{float(Total_sales)}")
    col2.metric("Total Quantity ", f"{float(total_quantity)}")
    col3, col4 = st.columns(2)
    col3.metric("Average Sale ", f"Rs:{float(average_sale)}")
    col4.metric("Best Product ", best_product)

    # subheader
    st.subheader("Sales by category :")

    category_sales = (
        (data.groupby("Category")["Total_sale"]).sum().sort_values(ascending=False)
    )
    st.subheader("Monthly Sales")
    data["Month"] = data["Date"].dt.to_period("M").astype(str)
    monthly_sales = data.groupby("Month")["Total_sale"].sum()
    st.bar_chart(monthly_sales)
    st.bar_chart(category_sales)
    st.subheader("Top Products")
    top_products = (
        data.groupby("Product")["Total_sale"].sum().sort_values(ascending=False).head()
    )
    st.bar_chart(top_products)  # call for bar graph .
