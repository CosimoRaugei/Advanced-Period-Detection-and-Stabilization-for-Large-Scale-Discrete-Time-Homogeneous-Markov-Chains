

from matrix_database import matrices_data

# Display available matrices with IDs and descriptions
def display_matrix_descriptions(data):
    print("Available Matrices:")
    for matrix_entry in data["matrices"]:
        print(f"ID: {matrix_entry['id']}")
        print(f"Description: {matrix_entry['description']}")
        print("-" * 40)

# Get matrix by ID
def get_matrix_by_id(data, matrix_id):
    for matrix_entry in data["matrices"]:
        if matrix_entry["id"] == matrix_id:
            return matrix_entry["matrix"]
    return None

# Main function to interact with the user
def main():
    # Display all available matrices
    display_matrix_descriptions(matrices_data)
    
    # Prompt user for ID
    matrix_id = input("Enter the ID of the matrix you want to view: ")
    matrix = get_matrix_by_id(matrices_data, matrix_id)
    
    if matrix:
        print(f"Matrix for ID '{matrix_id}':")
        for row in matrix:
            print(row)
    else:
        print(f"No matrix found for ID '{matrix_id}'.")

if __name__ == "__main__":
    main()
