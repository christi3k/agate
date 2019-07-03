import datetime
import agate
from typing import List, Sequence

# agate.Config
config: str = agate.get_option('default_locale')

# set up a sample table for various testing
column_names: List = [
    'boolean',
    'date',
    'date_time',
    'number',
    'text', 
    'time_delta'
    ]

column_types: List = [
        agate.Boolean(),
        agate.Date(),
        agate.DateTime(),
        agate.Number(),
        agate.Text(), 
        agate.TimeDelta()
        ]

rows = [
    (True, '12-03-2019', '12-03-2019 00:00', 34, 'test 1 2 3', datetime.timedelta(hours=4, minutes=10)),
    (False, '10-23-2019', '10-23-2019 03:00', 13, 'robert smith', datetime.timedelta(hours=1, minutes=15))
]

table: agate.Table = agate.Table(rows, column_names, column_types)

# reveal_type(table)

#################################################
# agate.Columns (including agate.MappedSequence)
#################################################
columns: agate.MappedSequence = table.columns
# reveal_type(columns)
#################################################

#################################################
# agate.Table.from_csv
#################################################
from_csv: agate.Table = agate.Table.from_csv('test.csv')
reveal_type(from_csv)
#################################################
