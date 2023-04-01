#Given some points in cartesian coordinate, (X, Y) find the number of rectangles that can be created by those points.
#Take into consideration only the rectangles that are parallel with the X, Y axes.

#If for any points (x,y) and (a,b) there exists the points (x,b) and (a,y) with x!= a and y!=b then we can form a 
#rectangle by denoting them as the coordinates of the points of the rectangle. 
#For every such pair we find we increase the counter and return the result divided by 4, the number of points in  a rectangle.
#O(n^2)
def rectangles(pairs):
 
    # Creating set containing elements
    points = set()
 
    # Inserting the pairs in the points set
    for i in range(len(pairs)):
        points.add(f"{pairs[i]}");
 
    res = 0;
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if (pairs[i][0] != pairs[j][0] and pairs[i][1] != pairs[j][1]):
               
                # Searching the pairs in the set
                if (f"{[pairs[i][0], pairs[j][1]]}" in points and f"{[pairs[j][0], pairs[i][1]]}" in points):
 
                    # Increase the counter
                    res += 1
 
    # Return the final result
    return int(res / 4);

N = 6;
pairs = [0] * N
 
# Inserting the pairs
pairs[0] = [1, 1];
pairs[1] = [1, 3];
pairs[2] = [2, 1];
pairs[3] = [2, 3];
pairs[4] = [3, 1];
pairs[5] = [3, 3];
 
print(rectangles(pairs)); # Outputs 3

N2 = 5;
pairs2 = [0] * N2
 
# Inserting the pairs
pairs2[0] = [1, 1];
pairs2[1] = [1, 3];
pairs2[2] = [2, 1];
pairs2[3] = [3, 1];
pairs2[4] = [3, 3];

print(rectangles(pairs2)); # Outputs 1