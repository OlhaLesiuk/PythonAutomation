casino_blacklist = {'John Dow', 'Jack Sparrow', 'John Wick',
                    'Johny Deep', 'Jessica Bowl', 'Orlando Bloom'}
poker_blacklist = {'John Dow', 'John Wick', 'Jack Sparrow', 'Orlando Bloom',
                   'Kate Wet', 'Sarah Parker'}
alcohol_blacklist = {'Sarah Parker', 'John Wick', 'Jack Sparrow', 'Kim Kardashian',
                     'Kris Jenner', 'Rob Stewart'}

common_names = casino_blacklist & poker_blacklist & alcohol_blacklist
print('Common names:', common_names)
