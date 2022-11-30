input = {
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

heatmap = {
    1 : [], 2 : [], 3 : [], 4 : [],
    5 : [], 6 : [], 7 : [], 8 : [],
    9 : [], 10: [], 11: [], 12: [],
    13: [], 14: [], 15: [], 16: []
    }
 
for key in input:
   for i in lookup[key]:
       heatmap[key].append(input[i])
 
output = {}
for cell, value in heatmap.items():
    output[cell] = sum(value)

# Exercise 3:
# if number of neighbors (heat) = 3 -> 1
# if number of neighbors (heat) = 2 -> check input for inhabitants
# else -> inhabitant dies
for cell, number_of_neighbors in output.items():
    if number_of_neighbors == 3:
        output[cell] = 1
    elif number_of_neighbors == 2 or number_of_neighbors == 3:
        output[cell] = input[cell]
    else:
        output[cell] = 0

 
output_string = """
{} {} {} {}
{} {} {} {}
{} {} {} {}
{} {} {} {}
""".format(*output.values())
print(output_string)
 
