import pandas as pd

def separate_files(input_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Group the DataFrame by the first and second columns
    grouped = df.groupby([df.columns[0], df.columns[1]])

    # Iterate over groups and save each group to a separate file
    for (column1_value, column2_value), group in grouped:
        output_file = f"{column1_value}_{column2_value}_output.csv"
        group.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "datasepe.csv"
    separate_files(input_file)