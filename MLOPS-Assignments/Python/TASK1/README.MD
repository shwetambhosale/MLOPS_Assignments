

# Titanic Dataset Exploratory Data Analysis (EDA)

This project provides a Python class, `TitanicEDA`, that performs basic exploratory data analysis (EDA) on the Titanic dataset. It includes functionality to load data, generate summary statistics, and visualize the distribution of survival rates based on features such as `Pclass`, `Sex`, and `Age`. 

## Features
- **Data Loading**: Load the Titanic dataset from a CSV file.
- **Summary Statistics**: Display descriptive statistics of the dataset.
- **Visualization**: 
  - Distribution of survival rates based on `Pclass`, `Sex`, and `Age`.
  - Save visualizations as image files using Matplotlib.

## Requirements
- Python 3.7 or higher
- Pandas
- Matplotlib

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
```markdown
2. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

3. Place your Titanic dataset CSV file in the project directory. Name it `titanic.csv` or update the script to match your file's name.

## How to Use
1. Import the `TitanicEDA` class:
   ```python
   from titanic_eda import TitanicEDA
   ```

2. Create an instance of the class and load the dataset:
   ```python
   eda = TitanicEDA('titanic.csv')
   eda.load_data()
   ```

3. Generate summary statistics:
   ```python
   eda.summary_statistics()
   ```

4. Create visualizations:
   - Distribution of survival rates by passenger class (`Pclass`):
     ```python
     eda.visualize_survival_by_pclass()
     ```
   - Distribution of survival rates by gender (`Sex`):
     ```python
     eda.visualize_survival_by_sex()
     ```
   - Distribution of survival rates by age:
     ```python
     eda.visualize_survival_by_age()
     ```

5. Visualizations will be saved as image files in the project directory.

## File Structure
```
.
├── titanic.csv                 # Titanic dataset (replace with your own file)
├── TitanicEDA.ipynb            # Python script containing the TitanicEDA class
├── README.md                   # Project documentation
├── survival_by_pclass.png      # Sample output image (distribution by Pclass)
├── survival_by_sex.png         # Sample output image (distribution by Sex)
├── survival_by_age.png         # Sample output image (distribution by Age)
```





```

