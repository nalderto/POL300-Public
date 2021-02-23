test = {
    "name": "q1",       # name of the test
    "points": 16,        # number of points for the entire suite
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
                    >>> df = get_sots()
                    >>> assert 'State' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Governor' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Polarity' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Subjectivity' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Syllables' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Words' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'FleschKincaid' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Gunning' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'ARI' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'ColemanLiau' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'RCS' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Keyword1' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Keyword2' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Keyword3' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Keyword4' in df.columns
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
                    >>> df = get_sots()
                    >>> assert 'Keyword5' in df.columns
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
