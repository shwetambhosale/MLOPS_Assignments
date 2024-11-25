# MLOPs Assignment

## Overview

This repository contains the code for the MLOPs Assignment, which involves working with agricultural data to provide insightful visualizations and analytics. The project focuses on analyzing crop yield, production, and area data using various data science and machine learning techniques.

The data used in the project is from the ICRISAT-District Level Dataset, which includes agricultural statistics for various crops, including cereals, pulses, oilseeds, cotton, sugarcane, fruits, and vegetables.

## Project Components

### 1. **Data**
The dataset used for this project is `ICRISAT-District Level Data.csv`, which contains annual data on area, yield, and production for multiple crops. This dataset is analyzed and visualized in the project.

### 2. **Streamlit Dashboard**
The project includes a **Streamlit dashboard** that allows users to interact with the agricultural data. Users can visualize:
- Average Yield per Crop
- Total Production by Year for different crops
- Distribution of Yield for selected crops
- Statistical summary of the dataset

### 3. **Machine Learning and Data Processing**
The project demonstrates the use of basic data processing and visualization techniques using `Pandas`, `Matplotlib`, and `Seaborn` to understand crop production patterns and trends.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gaurikarkhile001/MLOPs-Assignment.git
   cd MLOPs-Assignment
   ```

2. **Install the required packages:**
   You can install the required Python packages using `pip`. It is recommended to create a virtual environment first:
   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, you can install the individual libraries:
   ```bash
   pip install pandas streamlit matplotlib seaborn
   ```

3. **Run the Streamlit app:**
   To launch the app, run the following command:
   ```bash
   streamlit run app.py
   ```

   This will open the Streamlit dashboard in your default web browser.

## Features

- **Data Summary:** Provides statistical insights into the dataset.
- **Crop Yield Analysis:** Displays the average yield per crop.
- **Total Production Analysis:** Plots total production by year for different crops.
- **Yield Distribution:** Shows a histogram of the yield distribution for selected crops.
- **Interactive Dashboard:** Allows the user to interact with different filters and visualize the data.

## Contributions

Feel free to fork this repository and contribute by submitting issues, suggestions, or pull requests to improve the project.


## Acknowledgements

- [ICRISAT](https://www.icrisat.org/) for providing the dataset.
- [Streamlit](https://streamlit.io/) for making interactive data applications easy to build.
- [Pandas](https://pandas.pydata.org/), [Matplotlib](https://matplotlib.org/), and [Seaborn](https://seaborn.pydata.org/) for data analysis and visualization.

```

### Instructions to Use:
1. Replace the placeholder with any additional information specific to your project.
2. Ensure you have a `requirements.txt` file if you want to list all dependencies. You can generate it by running:
   ```bash
   pip freeze > requirements.txt
   ```
3. The `README.md` provides a description of your project, how to set it up, and how to run it. Make sure it's in the root of your repository.

Let me know if you'd like me to customize it further!
