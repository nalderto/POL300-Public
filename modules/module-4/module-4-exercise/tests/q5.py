test = {
    "name": "q5",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import sys, os
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> import pandas as pd
                    >>> iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
                    >>> blockPrint()
                    >>> mean, minimum, maximum = petal_area_stats(iris)
                    >>> enablePrint()
                    >>> assert round(mean, 6) == 5.794067
                    >>> assert round(minimum, 2) == 0.11
                    >>> assert maximum == 15.87
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