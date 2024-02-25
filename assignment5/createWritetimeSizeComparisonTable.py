import subprocess
import os
import pandas as pd
import re

# Function to run generate.py and capture output
def run_generate_script(script_name):
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.stderr:
        print("Error running script:", result.stderr)
    return result.stdout

# Function to parse output and get file sizes
def parse_output_and_get_file_sizes(output):
    pattern = re.compile(r"(.+): (\d+\.\d+) seconds")
    matches = pattern.findall(output)

    data = []

    for match in matches:
        filename, time_taken = match
        # Check if the filename refers to an HDF5 dataset
        if '.hdf5/' in filename:
            # Extract the HDF5 filename before the first '/'
            hdf5_filename = filename.split('/')[0]
            # Ensure we only get the file size once per HDF5 file
            if not any(hdf5_filename in row[0] for row in data):
                try:
                    file_size = os.path.getsize(hdf5_filename)
                except FileNotFoundError:
                    print(f"File {hdf5_filename} not found.")
                    file_size = None
                data.append([hdf5_filename, float(time_taken), file_size])
        else:
            # Handle regular file
            try:
                file_size = os.path.getsize(filename)
            except FileNotFoundError:
                print(f"File {filename} not found.")
                file_size = None
            data.append([filename, float(time_taken), file_size])

    return data


# Function to create an Excel file from the data
def create_excel(data, filename='MatrixGenerationTimesAndSizes.xlsx'):
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Filename', 'CPU Time (seconds)', 'File Size (bytes)'])
    
    # Write DataFrame to an Excel file
    df.to_excel(filename, index=False)
    print(f"Excel file '{filename}' has been created.")

if __name__ == "__main__":
    # Run the script and capture the output
    output = run_generate_script('generate.py')
    
    # Parse the output and get file sizes
    data = parse_output_and_get_file_sizes(output)
    
    # Create Excel file
    create_excel(data)
