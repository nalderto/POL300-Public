test = {'name': 'q2',
        'points': 1,
        'suites': [{'cases': [{'code': 'import requests, csv >>> response = requests.get("https://www.brookings.edu/wp-content/uploads/2017/01/vitalstats_ch3_tbl1.csv").content.decode("ascii") >>> reader = list(csv.DictReader(response.splitlines())) >>> assert int(find_max_house(reader)) == 2012',
                               'hidden': False, 'locked': False}],
                    'scored': True,
                    'setup': '',
                    'teardown': '',
                    'type': 'doctest'}]}
