test = {'name': 'q3',
        'points': 1,
        'suites': [{'cases': [{'code': '''
                                        >>> import sys, os
        		                >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> list_of_words = ["sister", "habit", "underline", "idea", "lake", "sun", "year"]
                                        >>> blockPrint()
                                        >>> list_of_words = exclude_four_letter_words(list_of_words)
                                        >>> assert "sister" in list_of_words and "habit" in list_of_words and "underline" in list_of_words and "idea" not in list_of_words and "lake" not in list_of_words and "sun" in list_of_words and "year" not in list_of_words''',
                               'hidden': False, 'locked': False},
                              {'code': '''
                                        >>> import sys, os
        		                >>> def blockPrint():
		                        ...		sys.stdout = open(os.devnull, 'w')
                                        >>> list_of_words = ["nature", "dragon", "sing", "vote", "low", "market", "folk", "pearl"]
                                        >>> blockPrint()
                                        >>> list_of_words = exclude_four_letter_words(list_of_words)
                                        >>> assert "nature" in list_of_words and "dragon" in list_of_words and "sing" not in list_of_words and "low" in list_of_words and "vote" not in list_of_words and "market" in list_of_words and "folk" not in list_of_words and "pearl" in list_of_words''',
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
