import numpy as np
import pandas as pd

# define cartesian coordinates of vertices of polygon 1
c1 = [0,0,0]
c2 = [0,1,0]
c3 = [0,1,1]
c4 = [0,0,1]

# define cartesian coordinates of vertices of polygon 2
c5 = [1,1,0]
c6 = [1,2,0]
c7 = [1,2,1]
c8 = [1,1,1]

def length_vertices(a,b): # displacement between to vertices
    return np.sqrt(np.sum(np.square([x - y for x, y in zip(a,b)])))

def vector_vertices(a,b): # vector of edge connecting 2 vertices
    return [b[0] - a[0], b[1] - a[1], b[2] - a[2]]

def area_polygon(a,b,c,d):
    return length_vertices(a,b)*length_vertices(b,c)

def midpt_polygon(a,b,c,d): # identify centre of polygon
    abcd = [a,b,c,d]
    n_vertices = 4
    return [x/n_vertices for x in (sum(values) for values in zip(*abcd))]

def normal_vector(a,b,c): # vector normal to surface defined by points a,b,c
    ab = vector_vertices(a,b)
    bc = vector_vertices(b,c)
    return [ab[1]*bc[2]-ab[2]*bc[1],ab[0]*bc[2]-ab[2]*bc[0],ab[0]*bc[1]-ab[1]*bc[0]]

def mag_vector(x): # magnitude of vector
    return np.sqrt(np.sum(np.square(x)))

def angle_incident(vector1,vector2): #angle between 2 vectors
    return np.arccos(sum([a*b for a,b in zip(vector1,vector2)])/(mag_vector(vector1)* mag_vector(vector2)))

def form_factor(A1,A2,theta1,theta2,r):
    return np.cos(theta1)*np.cos(theta2)*A2/(3.14*np.square(r))

# find centre of 1234 and 5678
midpt_1234 = midpt_polygon(c1,c2,c3,c4)
midpt_5678 = midpt_polygon(c5,c6,c7,c8)

# find areas of polygons
A1 = area_polygon(c1,c2,c3,c4)
A2 = area_polygon(c5,c6,c7,c8)

# find vector normal to 1234 and 5678
n_1234 = normal_vector(c1,c2,c3)
n_5678 = normal_vector(c5,c6,c7)

# find vector of line connecting mpt1234 and mpt5678
r_vector = vector_vertices(midpt_1234,midpt_5678)

# find length of vector r
r_dist = mag_vector(r_vector)

# find angle between r and normal of midpt123
theta1 = angle_incident(n_1234,r_vector)
theta2 = angle_incident(n_5678,r_vector)

# find Form Factor between 1234 and 5678
result = form_factor(A1,A2,theta1,theta2,r_dist)

print(result)