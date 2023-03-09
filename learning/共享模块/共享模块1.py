import nester
from nester import split_line

cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast, 0)

split_line()
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

nester.print_lol(movies, True, 0)
