test = {'name': 'q4',
        'points': 1,
        'suites': [{'cases': [{'code': r"""
                                        >>> import sys, os
		                        >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> def enablePrint():
                                        ...		sys.stdout = sys.__stdout__
                                        >>> blockPrint()
                                        >>> car = {"color": "red", "year": 2001, "model": "S90", "insurance": "Allstate"}
                                        >>> car = updateListing(car)
                                        >>> assert car["color"] == "white"
                                        >>> assert car["year"] == 1997
                                        >>> assert car["make"] == "Volvo"
                                        >>> assert car["model"] == "S90"
                                        >>> assert "insurance" not in car.values()
                                        >>> enablePrint()
                                        """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
