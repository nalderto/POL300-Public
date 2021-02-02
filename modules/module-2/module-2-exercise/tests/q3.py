test = {'name': 'q3',
        'points': 1,
        'suites': [{'cases': [{'code': '''
                                        >>> import sys, os
		                        >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> def enablePrint():
                                        ...		sys.stdout = sys.__stdout__
                                        >>> blockPrint()
                                        >>> roster = ["Sally", "Ruben", "Jim", "Adeline"]
                                        >>> roster = updateRoster(roster)
                                        >>> assert "Sally" in roster and "Ruben" in roster and "Jim" not in roster and "Arya" in roster and "Theo" in roster and "Adeline" in roster
                                        >>> enablePrint()
                                        ''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                        >>> import sys, os
		                        >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> def enablePrint():
                                        ...		sys.stdout = sys.__stdout__
                                        >>> blockPrint()
                                        >>> roster = ["Melisa", "Axl", "Jim", "David"]
                                        >>> roster = updateRoster(roster)
                                        >>> assert "Melisa" in roster and "Axl" in roster and "Jim" not in roster and "David" in roster and "Theo" in roster and "Arya" in roster
                                        >>> enablePrint()
                                        ''',
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
