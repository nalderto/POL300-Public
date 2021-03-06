test = {
    "name": "q3",       # name of the test
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
                    >>> df = pd.DataFrame({'name': ['Purdue', 'Ohio State', 'Michigan', 'Minnesota', 'Wisconsin', 'Illinois'], 'nickname': ['Boilermakers', 'Buckeyes', 'Wolverines', 'Golden Gophers', 'Badgers', 'Fighting Illini']})
                    >>> blockPrint()
                    >>> new_df = append_df(df[:3], df[3:])
                    >>> enablePrint()
                    >>> assert df.equals(new_df)                    """,
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