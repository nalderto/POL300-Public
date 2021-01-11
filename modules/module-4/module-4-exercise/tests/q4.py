test = {
    "name": "q4",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> data = pd.read_csv("https://www.brookings.edu/wp-content/uploads/2017/01/vitalstats_ch8_tbl3.csv")
                    >>> new_df = return_specific_data(data)
                    >>> for i in range(34, 73):
                    ... assert data.PctPartyUnityVotes[i] == new_df[i]
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