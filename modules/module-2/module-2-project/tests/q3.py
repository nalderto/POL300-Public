test = {'name': 'q3',
        'points': 1,
        'suites': [{'cases': [{'code': """
                                        >>> import requests, csv 
                                        >>> import sys, os
		                        >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> def enablePrint():
                                        ...		sys.stdout = sys.__stdout__
                                        >>> blockPrint()
                                        >>> response = requests.get("https://www.brookings.edu/wp-content/uploads/2017/01/vitalstats_ch3_tbl1.csv").content.decode("ascii") 
                                        >>> reader = list(csv.DictReader(response.splitlines())) 
                                        >>> assert find_bigger_spender(reader) == ("Senate", 8861261.059823528, 7554219.041499998)
                                        >>> enablePrint()
                                        """,
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}