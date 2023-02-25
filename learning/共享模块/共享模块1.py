import nester
from nester import split_line

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.is_list(cast, 0)

split_line(20, '')
movies = [
    'The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91,
    [
        'Graham CHapman',
        [
            'Michael Palin', 'John Cleese', 'Terry Gilliam', ' Eric Idle',
            'Terry Jones'
        ]
    ]
]

nester.is_list(movies, True, 0)
