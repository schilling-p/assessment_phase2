input = {1 : 0, 2 : 1, 3 : 0,
        4 : 0, 5 : 1, 6 : 0,
        7 : 0, 8 : 1, 9 : 0}
 
lookup = {
   1 : [2,5,4], 2 : [1,3,4,5,6], 3 : [2,5,6],
   4 : [1,2,5,7,8], 5 : [1,2,3,4,6,7,8,9], 6 : [2,3,5,8,9],
   7 : [4,5,8], 8 : [4,5,6,7,9], 9 : [5,6,8]
   }
 
heatmap = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : []}
 
for key in input:
   for i in lookup[key]:
       heatmap[key].append(input[i])
 
output = {}
for cell, value in heatmap.items():
   output[cell] = sum(value)
 
output_string = """
{} {} {}
{} {} {}
{} {} {}
""".format(*output.values())
print(output_string)
 
