VIP_box = ((1, 'the seat is taken'), (2, 'the seat is taken'), (3, 'the seat is taken'),
           (4, 'the seat is taken',), (5, 'the seat is taken'), (6, 'the seat is taken'),
           (7, 'the seat is taken'), (8, 'the seat is taken'),
           (9, 'the seat is taken'), (10, 'the seat is taken'))

common_room = {1: 'the seat is taken', 2: 'the place is free', 3: 'the place is free', 4: 'the seat is taken',
               5: 'the place is free', 6: 'the seat is taken', 7: 'the seat is taken', 8: 'the place is free',
               9: 'the place is free', 10: 'the seat is taken', 11: 'the place is free', 12: 'the seat is taken'}

print('the place is free in the VIP_box?', VIP_box)

free_places_common = common_room.get(2, 'the place is free')
print('the place is free in the common rooms?', free_places_common)

