import plotly.express as px
import pandas as pd

def plot_data(df, x_column, y_column):
    # Create an interactive plot
    fig = px.scatter(df, x=x_column, y=y_column, title=f'{y_column} vs {x_column}')
    fig.show()

if __name__ == "__main__":
    file_path = 'data.csv'  # Replace with your CSV file path
    df = pd.read_csv(file_path)
    plot_data(df, 'column1', 'column2')  # Replace with your column names