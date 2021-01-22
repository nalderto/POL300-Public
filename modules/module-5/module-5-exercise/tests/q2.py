test = {
    "name": "q2",       # name of the test
    "points": 5,        # number of points for the entire suite
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
                    >>> blockPrint()
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(utils.get_transcript())
                    >>> enablePrint()
                    >>> assert syllables == 8160
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import sys, os
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> blockPrint()
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(utils.get_transcript())
                    >>> enablePrint()
                    >>> assert words == 5509
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import sys, os
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> blockPrint()
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(utils.get_transcript())
                    >>> enablePrint()
                    >>> assert sentences == 331

                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import sys, os
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> blockPrint()
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(utils.get_transcript())
                    >>> enablePrint()
                    >>> assert flesch == 63.09
                    """,
                    "hidden": False,
                    "locked": False,
                },
                {
                    "code": r"""
                    >>> import sys, os
		            >>> def blockPrint():
		            ...		sys.stdout = open(os.devnull, 'w')
		            >>> def enablePrint():
		            ...		sys.stdout = sys.__stdout__
                    >>> blockPrint()
                    >>> syllables, words, sentences, flesch, concensus = get_grade_level(utils.get_transcript())
                    >>> enablePrint()
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
