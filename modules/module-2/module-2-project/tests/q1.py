test = {'name': 'q1',
        'points': 1,
        'suites': [{'cases': [{'code': """
                                        >>> import sys, os
        		                >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
		                        >>> def enablePrint():
		                        ...		sys.stdout = sys.__stdout__
                                        >>> import requests, csv 
                                        >>> response = requests.get("https://www.brookings.edu/wp-content/uploads/2017/01/vitalstats_ch3_tbl1.csv").content.decode("ascii") 
                                        >>> reader = list(csv.DictReader(response.splitlines())) 
                                        >>> blockPrint()
                                        >>> assert find_min_2018_dollars(reader) == {"Year": "1990", "Chamber": "House", "NominalDollars": "423245", "2018Dollars": "813158"}
                                        >>> enablePrint()
                                        """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}

