import random;

# Create a 10*10 matrix filled with '' for ocean
ocean = [['' for x in range(10)] for y in range(10)]

# put each boat's size in a array
all_ship_size = [6,   4,  4,  3,  3,  3,  2,  2]
all_ship_name = ['a','b','c','d','e','f','g','h']
# Boat is not put:0
# Boat is put:    1
all_ship_put = [0, 0, 0, 0, 0, 0, 0, 0]

# put boats
print("put boats!")
for ship_number in range(8):
    while all_ship_put[ship_number] == 0:
        # generate the ship head
        ship_head_position_x = random.sample(range(10), 1)[0]
        ship_head_position_y = random.sample(range(10), 1)[0]
        while ocean[ship_head_position_x][ship_head_position_y] != '':
            ship_head_position_x = random.sample(range(10), 1)[0]
            ship_head_position_y = random.sample(range(10), 1)[0]

        # make sure the boat tail is ok
        if ship_head_position_y + all_ship_size[ship_number] < 11:
            ship_tail_position_x = ship_head_position_x
            ship_tail_position_y = ship_head_position_y + all_ship_size[ship_number] - 1
        else:
            ship_tail_position_x = ship_head_position_x
            ship_tail_position_y = ship_head_position_y - all_ship_size[ship_number] + 1

        if ocean[ship_tail_position_x][ship_tail_position_y] == '':
            # Occupy the ocean
            if ship_head_position_y + all_ship_size[ship_number] < 11:
                for num in range(0, all_ship_size[ship_number]):
                    ocean[ship_head_position_x][ship_head_position_y + num] = all_ship_name[ship_number]
            else:
                for num in range(0,all_ship_size[ship_number]):
                    ocean[ship_head_position_x][ship_head_position_y - num] = all_ship_name[ship_number]
            all_ship_put[ship_number] = 1
        else:
            all_ship_put[ship_number] = 0

for row in ocean:
    print(row)

print("Boats are ready!")
print("----------------------------------------------")
print("Start bomb!")
ocean = [['' for x in range(10)] for y in range(10)]
for row in ocean:
    print(row)

print("Done!")
