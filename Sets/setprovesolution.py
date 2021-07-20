def intersect(set1, set2):
    intersections = set()

    for x in set1:
        for y in set2:
            if x == y:
                intersections.add(x)
    return intersections

def union(set1, set2):
    union = set() # make a set
    for x in set1:
        union.add(x) # sets won't add duplicates
    for y in set2:
        union.add(y) # sets won't add duplicates
    return union

# Tests
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(intersect(s1,s2))  # Should show {4, 5}
print(union(s1,s2)) # Should show {1, 2, 3, 4, 5, 6, 7, 8}

s1 = {5,8,3,4,7}
s2 = {6,15,20,9,10}
print(intersect(s1,s2))  # Should show an empty set
print(union(s1,s2)) # Should show {3, 4, 5, 6, 7, 8, 9, 10, 15, 20}
