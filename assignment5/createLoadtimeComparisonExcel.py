import subprocess
import pandas as pd
import re

# Function to run loadFiles.py and capture its output
def run_and_capture(script_name):
    # Run the script and capture the output
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    output = result.stdout

    # Extract load times using regular expression
    pattern = re.compile(r"(.+): (\d+\.\d+) seconds")
    times = pattern.findall(output)

    return times

# Function to create the Excel file
def create_excel(data, excel_filename):
    # Convert data to DataFrame
    df = pd.DataFrame(data, columns=['File', 'Load Time (seconds)'])

    # Write to Excel file without pivoting
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Load Times', index=False)

    # print(f"Excel file '{excel_filename}' has been created.")

# Main execution
if __name__ == "__main__":
    load_times = run_and_capture('loadFiles.py')
    create_excel(load_times, 'MatrixLoadTimes.xlsx')
    print(f"Excel file 'MatrixLoadTimes.xlsx' has been created with the load times.")
