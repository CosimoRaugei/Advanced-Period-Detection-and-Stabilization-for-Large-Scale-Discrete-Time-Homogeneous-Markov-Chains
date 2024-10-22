# File matrix_database.py
# Dictionary of matrices

# instructions for format of the dictionary
# id = 
# quick description :
# square stochastic matrix: 

matrices_data = {
    "matrices": [
        {
            "id": "1",
            "description": "Simple cycle stochastic matrix of size 1.",
            "matrix": [[1.0]]
        },
        {
            "id": "2",
            "description": "Simple cycle stochastic matrix of size 2.",
            "matrix": [
                [0.0, 1.0],
                [1.0, 0.0]
            ]
        },
        {
            "id": "3",
            "description": "Simple cycle stochastic matrix of size 3.",
            "matrix": [
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0]
            ]
        },
        {
            "id": "4",
            "description": "Simple cycle stochastic matrix of size 4.",
            "matrix": [
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0, 0.0]
            ]
        },
        {
            "id": "5",
            "description": "Simple cycle stochastic matrix of size 5.",
            "matrix": [
                [0.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0, 0.0, 0.0]
            ]
        },
        {
            "id": "6",
            "description": "Simple cycle stochastic matrix of size 6.",
            "matrix": [
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            ]
        },
        {
            "id": "7",
            "description": "Simple cycle stochastic matrix of size 7.",
            "matrix": [
                [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
                [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            ]
        },
        {
            "id": "8",
            "description": "Period 3 size 5.",
            "matrix": [
                [0 ,    0.5 ,  0 ,    0.5 ,  0],
                [0  ,   0  ,   1  ,   0    , 0],
                [0.5 ,  0  ,   0   ,  0.5 ,  0],
                [0   ,  0   ,  0.5 ,  0  ,   0.5],
                [0.5 ,  0  ,   0.5 ,  0   , 0]
            ]
        },
        
    ]
}
