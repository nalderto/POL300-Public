test = {'name': 'q2',
        'points': 1,
        'suites': [{'cases': [{'code': r"""
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert isEven(0)
                                >>> assert isEven(64)
                                >>> assert isEven(754)
                                >>> assert not isEven(33)
                                >>> assert not isEven(79)
                                >>> assert not isEven(1)
                                >>> enablePrint()
                                """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
