'''
Authors:
Logan Crossley
John Pischke
Seth Whetten
Dawson Packer 

Description:
This is our test class. This was created so we could make sure everything works correctly.
'''

graphic_parts = [
    '  ___\n /___\\\n \\   /\n  \\ /\n   0\n',
    '     \n /___\\\n \\   /\n  \\ /\n   0\n',
    '     \n  ___\\\n \\   /\n  \\ /\n   0\n',
    '     \n  ___  \n \\   /\n  \\ /\n   0\n',
    '     \n       \n \\   /\n  \\ /\n   0\n',
    '     \n       \n     /\n  \\ /\n   0\n',
    '     \n       \n      \n  \\ /\n   0\n',
    '     \n       \n      \n    /\n   0\n',
    '     \n       \n      \n     \n   x\n',
]
graphic_end = '  /|\\\n  / \\\n\n^^^^^^^'

for item in graphic_parts:
    print(item + graphic_end)