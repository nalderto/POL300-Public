test = {'name': 'q3',
        'points': 1,
        'suites': [{'cases': [{'code': '''
                                        >>> roster = ["Sally", "Ruben", "Jim", "Adeline"]
                                        >>> roster = updateRoster(roster)
                                        >>> assert "Sally" in roster and "Ruben" in roster and "Jim" not in roster and "Arya" in roster and "Theo" in roster and "Adeline" in roster
                                        ''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                        >>> roster = ["Melisa", "Axl", "Jim", "David"]
                                        >>> roster = updateRoster(roster)
                                        >>> assert "Melisa" in roster and "Axl" in roster and "Jim" not in roster and "David" in roster and "Theo" in roster and "Arya" in roster
                                        ''',
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
