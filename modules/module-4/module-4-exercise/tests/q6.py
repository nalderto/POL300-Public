test = {
    "name": "q6",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
                    >>> export_big_iris(iris)
                    >>> new_iris = pd.read_csv('big.csv').sort_index(axis=1)
                    >>> proper_rows = pd.DataFrame({'sepal_length': [7.2, 7.7, 7.9], 'sepal_width': [3.6, 3.8, 3.8], 'petal_length': [6.1, 6.7, 6.4], 'petal_width': [2.5, 2.2, 2.0], 'species': ['virginica'] * 3}).sort_index(axis=1)
                    >>> assert new_iris.equals(proper_rows)
                    """,
                    "hidden": False,
                    "locked": False,
                }, 
            ],
            "scored": False,            # ignored by Otter
            "setup": "",                # ignored by Otter
            "teardown": "",             # ignored by Otter
            "type": "doctest"           # the type of test; only "doctest" allowed
        },
    ]
}