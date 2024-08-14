import base64

def csv_to_base64(file_path):
    # Read the CSV file
    with open(file_path, 'rb') as csv_file:
        # Read the content of the file
        csv_content = csv_file.read()
    
    # Encode the content in base64
    base64_encoded = base64.b64encode(csv_content)
    
    # Convert to a string for output
    base64_string = base64_encoded.decode('utf-8')
    
    return base64_string

# Example usage
file_path = './new_results_found_2024-07-14.csv'
base64_string = csv_to_base64(file_path)
print(base64_string)