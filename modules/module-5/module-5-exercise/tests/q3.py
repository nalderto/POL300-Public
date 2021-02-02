test = {
    "name": "q3",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> import sys, os, utils
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> blockPrint()
                    >>> words = get_keywords(utils.get_transcript())
                    >>> enablePrint()
                    >>> answer = ['americans', 'new', 'thanks', 'america', 'family', 'tonight', 'free', 'forcing', 'works', 'year']
                    >>> assert words == answer
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