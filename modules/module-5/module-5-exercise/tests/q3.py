test = {
    "name": "q3",       # name of the test
    "points": 1,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> words = get_keywords(transcript_text)
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