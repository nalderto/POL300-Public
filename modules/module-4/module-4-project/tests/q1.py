test = {
    "name": "q1",       # name of the test
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
                    >>> state = get_state()
                    >>> chamber = get_chamber()
                    >>> state = state.title()
                    >>> chamber = chamber.title().replace(" Of ", " of ")
                    >>> answer_df = pd.read_csv("https://raw.githubusercontent.com/nalderto/POL300-Public/master/All-Campaign-Contributions.csv")
                    >>> answer_df = answer_df[(answer_df['State'] == state) & (answer_df['Chamber'] == chamber)].reset_index(drop=True).sort_index(axis=1)
                    >>> filename = state.replace(" ", "-") + "-" + chamber.replace(" ", "-") + "-Campaign-Contributions.csv"
                    >>> blockPrint()
                    >>> collectCampaignContributions()
                    >>> enablePrint()
                    >>> test_df = pd.read_csv(filename).reset_index(drop=True).sort_index(axis=1)
                    >>> assert test_df.equals(answer_df)
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
