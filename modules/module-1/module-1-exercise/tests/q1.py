test = {'name': 'q1',
        'points': 1,
        'suites': [{'cases': [{'code': '''
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert quadratic(5, 6, 1) == (-0.2, -1)
                                ''', 'hidden': False, 'locked': False},
                              {'code': '''
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert quadratic(2, -8, -24) == (6, -2)
                                ''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert quadratic(1, -5, 6) == (3, 2)
                              ''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert quadratic(1, -5, -24) == (8, -3)
                              ''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                >>> import sys, os
		                >>> def blockPrint():
		                ...		sys.stdout = open(os.devnull, 'w')
		                >>> def enablePrint():
		                ...		sys.stdout = sys.__stdout__
                                >>> blockPrint()
                                >>> assert quadratic(1, 3, -10) == (2, -5)
                              ''', 'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
