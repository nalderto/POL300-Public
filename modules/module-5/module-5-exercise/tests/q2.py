test = {
    "name": "q2",       # name of the test
    "points": 5,        # number of points for the entire suite
    "suites": [         # list of suites, only 1 suite allowed!
        {
            "cases": [                  # list of test cases
                {
                    "code": r"""
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(transcript_text)
                    >>> assert syllables == 8160
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(transcript_text)
                    >>> assert words == 5509
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(transcript_text)
                    >>> assert sentences == 331

                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(transcript_text)
                    >>> assert flesch == 63.09
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(transcript_text)
                    >>> assert concensus == 9.0
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
