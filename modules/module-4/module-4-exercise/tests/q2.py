test = {
    "name": "q2",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import pandas as pd
                    >>> df = pd.DataFrame({'name': ['Purdue', 'Ohio State', 'Michigan'], 'nickname': ['Boilermakers', 'Buckeyes', 'Wolverines']})
                    >>> new_df = add_founded_year(df)
                    >>> assert new_df['name'].equals(df['name'])
                    >>> assert new_df['nickname'].equals(df['nickname'])
                    >>> assert new_df['founded'].equals(pd.Series([1869, 1870, 1817]))
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