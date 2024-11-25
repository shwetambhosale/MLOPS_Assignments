import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
def load_data(file_path):
    """Loads the agricultural dataset from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        st.success("Data loaded successfully.")
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Plotting Average Yield per Crop
def plot_avg_yield(data, crops):
    """Plots the average yield for each crop."""
    avg_yield = {crop: data[crop].mean() for crop in crops}
    
    # Remove 'Kg per ha' and add ' after crop'
    crops_cleaned = [crop.replace(" YIELD (Kg per ha)", "") + " Yield" for crop in crops]
    
    # Plotting
    fig, ax = plt.subplots()
    ax.bar(crops_cleaned, avg_yield.values(), color='skyblue')
    ax.set_xlabel('Crops')
    ax.set_ylabel('Average Yield')
    ax.set_title('Average Yield per Crop')
    st.pyplot(fig)

# Plotting Total Production by Year for Rice
def plot_production_by_year(data, crop_column, year_column="Year"):
    """Plots total production by year for a given crop."""
    yearly_production = data.groupby(year_column)[crop_column].sum()
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(yearly_production.index, yearly_production.values, marker='o', linestyle='-', color='green')
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Production (1000 tons)')
    ax.set_title(f'Total Production by Year for {crop_column}')
    st.pyplot(fig)

# Plotting Distribution of Yield for a Specific Crop
def plot_yield_distribution(data, crop_column):
    """Plots the distribution of yield for a given crop."""
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data[crop_column], bins=30, color='orange', edgecolor='black')
    ax.set_xlabel('Yield (Kg per ha)')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Distribution of {crop_column}')
    st.pyplot(fig)

# Show Project Summary
def show_project_summary():
    """Displays a summary of the project."""
    st.subheader("Project Summary")
    st.write("""
        **Dataset Overview**:
        - The dataset contains agricultural data for 20 major crops, including cereals, pulses, oilseeds, cotton, sugarcane, and fruits/vegetables.
        - Key variables include crop area, production, and yield, calculated on a district-level scale for multiple years.
        - Yield is calculated using the formula: **Yield = Production / Area**.
        - The dataset also includes data on **High Yielding Varieties (HYVs)** for major cereal crops.
        
        **Key Insights**:
        - The dataset provides insights into **crop productivity** over time and geographical regions.
        - Understanding trends in crop yield and production can guide **policy planning** for improving agricultural practices.
        - Analysis of **High Yielding Varieties (HYVs)** shows the adoption rates and their effect on crop productivity.
        
        **Project Objectives**:
        - The goal is to analyze **crop yield, production, and area** data to identify trends, patterns, and anomalies.
        - The project aims to provide **visualizations** that offer actionable insights into agricultural productivity.
        - It will also focus on exploring the **adoption of high-yielding varieties** across regions.
    """)

# Main function to display Streamlit content
def main():
    # Title of the Streamlit app
    st.set_page_config(page_title="Agricultural Data Dashboard", layout="wide")
    
    # Sidebar for filter options
    st.sidebar.header("Dashboard Filters")
    file_path = st.sidebar.text_input('Enter the file path', 'ICRISAT-District Level Data.csv')
    
    # Sidebar: Show Project Summary
    if st.sidebar.checkbox('Show Project Summary'):
        show_project_summary()
    
    # Load the dataset
    data = load_data(file_path)
    if data is None:
        return
    
    # Show summary statistics
    if st.sidebar.checkbox('Show Summary Statistics'):
        st.write(data.describe())
    
    # Sidebar: Crop Selection for Yield Plot
    crops = ["RICE YIELD (Kg per ha)", "WHEAT YIELD (Kg per ha)", "SORGHUM YIELD (Kg per ha)"]
    selected_crop = st.sidebar.selectbox("Select Crop for Yield Analysis", crops)
    
    # Sidebar: Show Raw Data
    if st.sidebar.checkbox('Show Raw Data'):
        st.write(data)

    # Display the main dashboard section
    st.title("Agricultural Data Visualization Dashboard")
    st.write("This dashboard provides insights into agricultural data for different crops.")

    # Left Column: Average Yield per Crop
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("Average Yield per Crop")
        plot_avg_yield(data, crops)
    
    # Right Column: Summary or Other Widgets
    with col2:
        st.subheader("Crop Statistics")
        st.write(f"**Selected Crop**: {selected_crop}")
        st.write(f"**Average Yield**: {data[selected_crop].mean():.2f} Kg per ha")

    # Show production by year for Rice (with interactivity)
    st.subheader("Rice Production by Year")
    plot_production_by_year(data, "RICE PRODUCTION (1000 tons)")
    
    # Histogram of Yield Distribution
    st.subheader(f"Distribution of {selected_crop}")
    plot_yield_distribution(data, selected_crop)
    
    # Add interactive graphs if required (e.g., Plotly, Altair)

if __name__ == "__main__":
    main()
