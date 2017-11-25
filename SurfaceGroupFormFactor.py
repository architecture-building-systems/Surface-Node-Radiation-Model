import numpy as np
import pandas as pd

# define polygon coordinates of surface i
# define cartesian coordinates of vertices of polygon i1
ci11 = [0,0,0]
ci12 = [0,1,0]
ci13 = [0,1,1]
ci14 = [0,0,1]
# define cartesian coordinates of vertices of polygon i2
ci21 = [0,1,0]
ci22 = [0,2,0]
ci23 = [0,2,1]
ci24 = [0,1,1]
# total number of polygons in surface 'i'
N = 2

# define polygon coordinates of surface j
# define cartesian coordinates of vertices of polygon j1
cj11 = [1,1,0]
cj12 = [1,2,0]
cj13 = [1,2,1]
cj14 = [1,1,1]
# define cartesian coordinates of vertices of polygon j2
cj21 = [1,1,0]
cj22 = [1,3,0]
cj23 = [1,3,1]
cj24 = [1,2,1]
# total number of polygons in surface 'j'
M = 2

# Functions

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

# Calculations
# find centres of all polygons
midpt_i1 = midpt_polygon(ci11,ci12,ci13,ci14)
midpt_i2 = midpt_polygon(ci21,ci22,ci23,ci24)
midpt_j1 = midpt_polygon(cj11,cj12,cj13,cj14)
midpt_j2 = midpt_polygon(cj21,cj22,cj23,cj24)

# find areas of all polygons
Ai1 = area_polygon(ci11,ci12,ci13,ci14)
Ai2 = area_polygon(ci21,ci22,ci23,ci24)
Aj1 = area_polygon(cj11,cj12,cj13,cj14)
Aj2 = area_polygon(cj21,cj22,cj23,cj24)


# find vector normal to 1234 and 5678
n_i1 = normal_vector(ci11,ci12,ci13)
n_i2 = normal_vector(ci21,ci22,ci23)
n_j1 = normal_vector(cj11,cj12,cj13)
n_j2 = normal_vector(cj21,cj22,cj23)

# find vector of line connecting i and j polygons
r_vector_i1j1 = vector_vertices(midpt_i1,midpt_j1)
r_vector_i1j2 = vector_vertices(midpt_i1,midpt_j2)
r_vector_i2j1 = vector_vertices(midpt_i2,midpt_j1)
r_vector_i2j2 = vector_vertices(midpt_i2,midpt_j2)

# find length of vector r
r_dist_i1j1 = mag_vector(r_vector_i1j1)
r_dist_i1j2 = mag_vector(r_vector_i1j2)
r_dist_i2j1 = mag_vector(r_vector_i2j1)
r_dist_i2j2 = mag_vector(r_vector_i2j2)

# find angle between r and normal of midpt123
theta1_i1j1 = angle_incident(n_i1,r_vector_i1j1)
theta2_i1j1 = angle_incident(n_j1,r_vector_i1j1)
theta1_i1j2 = angle_incident(n_i1,r_vector_i1j2)
theta2_i1j2 = angle_incident(n_j2,r_vector_i1j2)
theta1_i2j1 = angle_incident(n_i2,r_vector_i2j1)
theta2_i2j1 = angle_incident(n_j1,r_vector_i2j1)
theta1_i2j2 = angle_incident(n_i2,r_vector_i2j2)
theta2_i2j2 = angle_incident(n_j2,r_vector_i2j2)


# find Form Factor between 1234 and 5678
ff_i1j1 = form_factor(Ai1,Aj1,theta1_i1j1,theta2_i1j1,r_dist_i1j1)
ff_i1j2 = form_factor(Ai1,Aj2,theta1_i1j2,theta2_i1j2,r_dist_i1j2)
ff_i2j1 = form_factor(Ai2,Aj1,theta1_i2j1,theta2_i2j1,r_dist_i2j1)
ff_i2j2 = form_factor(Ai2,Aj2,theta1_i2j2,theta2_i2j2,r_dist_i2j2)

result = (np.sum([ff_i1j1,ff_i1j2,ff_i2j1,ff_i2j2]))/np.sum([Ai1,Ai2])

print(result)

# Next Step is to automate the calculations based on number of polygons created