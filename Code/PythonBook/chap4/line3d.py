from pylab import *
from mpl_toolkits.mplot3d import Axes3D
ax = Axes3D(figure())

phi = linspace(0, 2*pi, 400)
x = cos(phi)
y = sin(phi)	
z = 0

ax.plot(x, y, z, label = 'x')	# circle

z = sin(4*phi)  # modulated in z plane
ax.plot(x, y, z, label = 'x')  

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

show()


