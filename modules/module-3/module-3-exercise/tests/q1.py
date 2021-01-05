test = {
    "name": "q1",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> table = str(get_table())
                    >>> df = pd.read_html(table, header=1, index_col=False)[0]
                    >>> amount= ['$19,285', '$36,150', '$50,650', '$64,846', '$44,314', '$49,204', '$64,756', '$164,829', '$24,143', '$17,425']
                    >>> candidates = [2, 2, 1, 1, 2, 3, 3, 3, 1, 1]
                    >>> average = ['$9,643', '$18,075', '$50,650', '$64,846', '$22,157', '$16,401', '$21,585', '$54,943', '$24,143', '$17,425']
                    >>> for i in range(0, 10):
                    ...     assert df['Year'][i] == str(2018 - (i * 2))
                    ...     assert df['Amount'][i] == amount[i]
                    ...     assert df['Candidates'][i] == candidates[i]
                    ...     assert df['Average'][i] == average[i]
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