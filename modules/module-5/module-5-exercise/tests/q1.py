test = {
    "name": "q1",       # name of the test
    "points": 2,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> polarity, subjectivity = get_sentiment(transcript_text)
                    >>> assert polarity == 0.15544314121712638
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> polarity, subjectivity = get_sentiment(transcript_text)
                    >>> assert subjectivity == 0.46102034711905604
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