# Show zero velocity curves for the restricted, circular three-body problem. 
# The center of the grid is the COM.
# This is a quick and dirty script.  Feel free to alter it as you see fit.
#
# Here are a few ways to play with the Jacobi integral. 
# Change the scaling to empahsize different zero-velocity surfaces.
#
#CJ=[3.7,3.9]
#CJ=[3.197,3.552,3.805]
#
CJ=range(25,40)
for i in xrange(len(CJ)):CJ[i]/=10.
#
# Now put in the parameters for the problem.
# It is common to use a scaled distance, with the
# semi-major axis a=1 (in plotting units). 
# You can do what you like, but I am setting the
# gravitational constant G=1.  If you then use the scaling
# 1 Msun = 1 and 1 AU = 1, then 1 yr = 2pi in the equivalent units.
#
# m1 is the primary, and m2 is the secondary separated from m1 by a.  
# The tertiary for all intents and purposes is massless. 
# N is the number of grid points on an NXN grid. 
# SIZE is the full width of the plotting area.
#
a=1.0
m1_plus_m2=1.0
m2=0.2
N=512
SIZE=3.0*a
#
# You should not need to edit the following, but take a look at what it does.
# You will need to adjust the plots as needed.
#
#
import math
m1=1.0-m2
n=math.sqrt((m1+m2)/a**3)

d1=m2/(m1+m2)*a
d2=m1/(m1+m2)*a

dx=SIZE/float(N)

x=[]
y=[]
V=[]
#
# set up the grid
#
for i in xrange(N):
  x.append(dx*i+dx*0.5-SIZE/2.0)
  y.append(dx*i+dx*0.5-SIZE/2.0)
  V.append([])
  for j in xrange(N):
    V[i].append(0.0)
#
# populate V 
#
for i in xrange(N):
  for j in xrange(N):
    r1=math.sqrt((x[i]+d1)**2+y[j]**2)
    r2=math.sqrt((x[i]-d2)**2+y[j]**2)
    V[j][i]=(n**2*(x[i]**2+y[j]**2)+2.0*(m1/r1+m2/r2))
    
#
# Plot!
#
import pylab as P

P.figure()
P.title('Zero-Velocity Surfaces (Rotating Frame)\n Restricted, Circular Three-Body Problem')
P.xlabel('X Position (scaled units)')
P.ylabel('Y Position (scaled units)')
P.xlim(-SIZE/2.,SIZE/2.)
P.ylim(-SIZE/2.,SIZE/2.)
cb=P.contourf(x,y,V,levels=CJ,extend='max')
P.scatter([-d1,d2],[0,0])
label=["M1","M2"]
for i,x in enumerate([-d1,d2]):
   P.text(x+10*dx,-10*dx,label[i])
P.colorbar(cb)
P.show()


