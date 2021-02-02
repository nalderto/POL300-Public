test = {'name': 'q1',
        'points': 1,
        'suites': [{'cases': [{'code': r"""
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert qualifyForMedicare(65)
                                >>> assert not qualifyForMedicare(64)
                                >>> assert qualifyForMedicare(72)
                                >>> assert not qualifyForMedicare(18)
                                >>> enablePrint()
                                """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}