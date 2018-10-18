#Ralph Mehitang
#Joseph Anderson
#Cosc 490  
from mpl_toolkits.mplot3d import Axes3D as ax
import matplotlib.pyplot as plt
import numpy as np
import csv
import gudhi 

x = [] #name of counties
y = [] #min upload speed
z = [] #max upload speed
w = []  #average upload speed


#plt.figure(num=None, figsize=(10,15))
with open('Maryland_Broadband_Speed_Test__County_Upload.csv','r', newline='') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    #stores each row of values into respective arrays
    for row in plots:
       x.append(str(row[0]))   #name of counties
       y.append(float(row[1])) #min
       z.append(float(row[2])) #max
       w.append(float(row[3])) #avg
 

#plt.xticks(x, labels, rotation='vertical')
#for the purpose of the 2d graphs we will focus only on the max upload speeds
plt.xlabel('Name of Counties')
plt.xticks(range(0,len(x)),x,rotation='vertical')
plt.ylabel('Max upload speed number')
plt.title('I hate datasets scatter plt')
plt.tight_layout()
plt.scatter(x,z, alpha=0.5, color='red') #creation of scatter plot
plt.show ()

plt.xticks(range(0,len(x)),x,rotation='vertical')
#plt.plot(range(0,len(x)),w, label='Which county has the fastest speed?')
plt.plot(x,w)
plt.title('I hate datasets line graph')
plt.xlabel('County Name')
plt.ylabel('Average Upload number')
plt.tight_layout(pad=0.5)
plt.show()


################### 3d graph implementation 
#creating graph based on min, max, avg

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
#ax.scatter(y,z,w,color='blue',marker='o')
for (k,v) in enumerate(y):
	ax.scatter(y[k], z[k], w[k], marker='o')
	#ax.legend([x[k]])
ax.legend(x)
ax.set_title('I hate datasets in 3d')
ax.set_xlabel('min')
ax.set_ylabel('Max')
ax.set_zlabel('Avg')
plt.show()

############## hw 3 portion

distance_matrix = gudhi.read_lower_triangular_matrix_from_csv_file(csv_file='Maryland_Broadband_Speed_Test__County_Upload.csv')
rips_complex = gudhi.RipsComplex(distance_matrix=distance_matrix, max_edge_length=12.0)
simplex_tree = rips_complex.create_simplex_tree(max_dimension=1)
result_str = 'Rips complex is of dimension ' + repr(simplex_tree.dimension()) + ' - ' + \
    repr(simplex_tree.num_simplices()) + ' simplices - ' + \
    repr(simplex_tree.num_vertices()) + ' vertices.'
print(result_str)
fmt = '%s -> %.2f'
for filtered_value in simplex_tree.get_filtration():
    print(fmt % tuple(filtered_value))


