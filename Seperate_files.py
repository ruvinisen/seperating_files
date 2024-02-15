import pandas as pd
import os

def separate_files(input_file):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    # Group the DataFrame by the first column
    grouped = df.groupby(df.columns[0])

   # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over groups and save each group to a separate file in the output folder
    for name, group in grouped:
        output_file = os.path.join(output_folder, f"{name}_output.csv")
        group.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "datasepe.csv"
    separate_files(input_file)