test = {'name': 'q5',
        'points': 1,
        'suites': [{'cases': [
                              {'code': r"""
                                        >>> import sys, os
		                        >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> def enablePrint():
                                        ...		sys.stdout = sys.__stdout__
                                        >>> blockPrint()
                                        >>> assert summation(2, 4) == 5
                                        >>> assert summation(3, 7) == 18
                                        >>> assert summation(6, 1) == 0
                                        >>> assert summation(22, 20) == 0
                                        >>> assert summation(43, 73) == 1725
                                        >>> assert summation(33, 42) == 333
                                        >>> assert summation(11, 25) == 245
                                        >>> enablePrint()
                                        """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
