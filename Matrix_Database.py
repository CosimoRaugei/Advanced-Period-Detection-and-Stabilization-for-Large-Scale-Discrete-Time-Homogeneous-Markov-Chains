# Dictionary of matrices
matrices_data = {
    "matrices": [
        {
            "id": "matrix_1",
            "description": "Transition matrix for Markov chain example A.",
            "matrix": [
                [0.5, 0.5],
                [0.2, 0.8]
            ]
        },
        {
            "id": "matrix_2",
            "description": "Stochastic matrix for random walk on a graph.",
            "matrix": [
                [0.4, 0.6, 0.0],
                [0.3, 0.5, 0.2],
                [0.0, 0.7, 0.3]
            ]
        }
    ]
}

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
    # Use the predefined dictionary instead of loading from a file
    data = matrices_data
    
    # Display all available matrices
    display_matrix_descriptions(data)
    
    # Prompt user for ID
    matrix_id = input("Enter the ID of the matrix you want to view: ")
    matrix = get_matrix_by_id(data, matrix_id)
    
    if matrix:
        print(f"Matrix for ID '{matrix_id}':")
        for row in matrix:
            print(row)
    else:
        print(f"No matrix found for ID '{matrix_id}'.")

if __name__ == "__main__":
    main()
