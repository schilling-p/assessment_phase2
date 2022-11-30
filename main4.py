game_input = {
    1 : 0, 2 : 1, 3 : 0, 4 : 0,
    5 : 0, 6 : 1, 7 : 0, 8 : 0, 
    9 : 0, 10: 1, 11: 0, 12: 0,
    13: 0, 14: 0, 15: 0, 16: 0
    }
 
lookup = {
    1 : [2,5,6], 2 : [1,3,5,6,7], 3 : [2,4,6,7,8], 4 : [3,7,8], 5 : [1,2,6,9,10], 
    6 : [1,2,3,5,7,9,10,11], 7 : [2,3,4,6,8,10,11,12], 8 : [4,3,7,11,12], 9 : [5,6,10,13,14],
    10: [5,6,7,9,11,13,14,15], 11: [6,7,8,10,12,14,15,16], 12: [8,7,11,15,16],
    13: [9,10,14], 14: [9,10,11,13,15], 15: [10,11,12,14,16], 16: [11,12,15]
   }

def build_heatmap(input_dict, lookup_dict):
    """return a heatmap describing the number of neighbors"""
    heatmap = {
    1 : [], 2 : [], 3 : [], 4 : [],
    5 : [], 6 : [], 7 : [], 8 : [],
    9 : [], 10: [], 11: [], 12: [],
    13: [], 14: [], 15: [], 16: []
    }
    for key in input_dict:
        for i in lookup_dict[key]:
            heatmap[key].append(input_dict[i])
    return heatmap


def iteration(input_dict, heatmap_dict):
    """iterate once through the game of life"""
    output_dict = {}
    for cell, value in heatmap_dict.items():
        output_dict[cell] = sum(value)
    for cell, number_of_neighbors in output_dict.items():
        if number_of_neighbors == 3 and input_dict[cell] == 0:
            output_dict[cell] = 1
        elif number_of_neighbors == 2 or number_of_neighbors == 3:
            output_dict[cell] = input_dict[cell]
        else:
            output_dict[cell] = 0
    return output_dict

def print_next_iteration():
    """combines a dictionary and a string to print out the next iteration"""
    output = iteration(game_input, build_heatmap(game_input, lookup))
    output_string = """
    {} {} {} {}
    {} {} {} {}
    {} {} {} {}
    {} {} {} {}
    """.format(*output.values())
    print(output_string)

# the game of life:
input_string = """
{} {} {} {}
{} {} {} {}
{} {} {} {}
{} {} {} {}
""".format(*game_input.values())

print(input_string)

answer = int(input("How many times do you want to play?: "))

for i in range(0, answer):
    print_next_iteration()


