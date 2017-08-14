#! /usr/bin/env python3
'''Convert image.ppm to sound.opus'''

palete = { (233, 83, 32): '0', (255,155,121): '1', (246,120, 77): '2',
           (233,144, 32): '3', (255,196,121): '4', (246,171, 77): '5',
           (187,109, 11): '6', (147, 82,  0): '7', ( 28,101,149): '8',
           ( 92,147,182): '9', ( 56,117,157): 'A', ( 14, 78,120): 'B',
           (  5, 59, 94): 'C', ( 22,162, 95): 'D', ( 92,194,145): 'E',
           ( 54,171,115): 'F', (  8,130, 71): 'G', (  0,103, 53): 'H', }

def grouper(iterable, n):
    '''Collect data into fixed-length chunks'''
    return zip(*[iter(iterable)] * n)

with open('image.ppm', 'rb') as f:
    *header, data = f.read().split(sep=b'\n')

with open('sound.opus', 'wb') as f:
    ds = (palete[d] for d in grouper(data, 3) if not d in ((0, 0, 0), (255, 255, 255)))
    f.write(bytes(int(''.join(dd), base=len(palete)) for dd in grouper(ds, 2)))
