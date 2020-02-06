import matplotlib.pyplot as plt
import numpy, math, random

#debug mode toggle
DEBUG_MODE = False 

#define the number of sample points and graph size
data_size = 100
x_size = 100
y_size = 100

#define threshold and distance
threshold_factor = 0.6
threshold = max(threshold_factor*x_size, threshold_factor*y_size)
optimized_distance = 15
angle_threshold = 90

#initialize x and y coordinates for data set
data_x = []
data_y = []

#initialize inlier and outlier arrays
inlier_x = []
inlier_y = []
outlier_x = []
outlier_y = []

#initialize coordinates for solution line
x = numpy.linspace(0, x_size, x_size*10)
y = numpy.linspace(0, y_size, y_size*10)

#the number of inliers in the best line | initialize
best_inliers = 0

def area_triangle(a_x, a_y, b_x, b_y, c_x, c_y):
  M = [[a_x, a_y, 1], [b_x, b_y, 1], [c_x, c_y, 1]]
  return numpy.absolute(0.5*numpy.linalg.det(M))

def distance(a_x, a_y, b_x, b_y):
  return math.sqrt(math.pow((a_x-b_x), 2) + math.pow((a_y-b_y), 2))

def check_angle(a_x, a_y, b_x, b_y, c_x, c_y, area_s):
  a = distance(a_x, a_y, b_x, b_y)
  b = distance(b_x, b_y, c_x, c_y)
  c = distance(c_x, c_y, a_x, a_y)
  try:
    h = (2*area)/a
    angle_b = math.asin(h/c)
    angle_c = math.asin(h/b)
  except:
    return True
  else:
    if angle_b > angle_threshold or angle_c > angle_threshold or (180-angle_b-angle_c) > angle_threshold:
      return True
    else:
      return False

#putting random values in the arrays
for i in range (data_size):
  x_value = random.randint(1,x_size)
  y_value = random.randint(1,y_size)
  data_x.append(x_value)
  data_y.append(y_value)

#seleting two points and checking area against other points
for i in range (data_size - 1):
  first_x = data_x[i]
  first_y = data_y[i]
  for j in range (data_size - i):
    if (i != j):
      second_x = data_x[j+i]
      second_y = data_y[j+i]
      if distance(first_x, first_y, second_x, second_y) < (optimized_distance):
        if(DEBUG_MODE):
          print('\n[NEW] Skipping..distance less than threshold. Distance =' + str(int(distance(first_x, first_y, second_x, second_y))) + '\nx1:' + str(first_x) +'\ny1:' + str(first_y) +'\nx2:' + str(second_x) +'\ny2:' + str(second_y))
        continue
      else:
        if(DEBUG_MODE):
          print('\n[NEW] Operating on: ' + '\nx1:' + str(first_x) +'\ny1:' + str(first_y) +'\nx2:' + str(second_x) +'\ny2:' + str(second_y))
        inlier_count = 0
        for k in range (data_size):
          if (k != i) and (k != j):
            area = area_triangle(first_x, first_y, second_x, second_y, data_x[k], data_y[k])
            if area < threshold and check_angle(first_x, first_y, second_x, second_y, data_x[k], data_y[k], area):
              inlier_count = inlier_count + 1
              if(DEBUG_MODE):
                print('\nInlier count changed to : ' + str(inlier_count))
            else:
              continue
          else:
            continue
        if (inlier_count >= best_inliers):
          if(DEBUG_MODE):
            print('\nupdating the best count from ' + str(best_inliers) + ' to ' + str(inlier_count))
          best_inliers = inlier_count
          final_first_x = first_x
          final_first_y = first_y
          final_second_x = second_x
          final_second_y = second_y
          if(DEBUG_MODE):
            print('\nBest pair set as' + '\nx1:' + str(first_x) +'\ny1:' + str(first_y) +'\nx2:' + str(second_x) +'\ny2:' + str(second_y))
        else:
          if(DEBUG_MODE):
            print('\nMaking no changes')
            print('\ncurrent inlier count :' + str(inlier_count) + ' | current best :' + str(best_inliers))
          continue
    else:
      continue

point1 = [final_first_x, final_second_x]
point2 = [final_first_y, final_second_y]

if(DEBUG_MODE):
  print('\n Final points at :')
  print(point1)
  print(point2)

#separating inliers and outliers
for k in range (data_size):
  if (data_x[k]!=final_first_x) and (data_x[k]!=final_second_x):
    area = area_triangle(final_first_x, final_first_y, final_second_x, final_second_y, data_x[k], data_y[k])
    if area < threshold and check_angle(first_x, first_y, second_x, second_y, data_x[k], data_y[k], area):
      if(DEBUG_MODE):
        print('\n inlier at :' + str(data_x[k]) + ',' + str(data_y[k]))
      inlier_x.append(data_x[k])
      inlier_y.append(data_y[k])
    else:
      if(DEBUG_MODE):
        print('\n oulier at :' + str(data_x[k]) + ',' + str(data_y[k]))
      outlier_x.append(data_x[k])
      outlier_y.append(data_y[k])
      continue
  else:
    continue

#calculating the line equation (y = mx + c)
slope = (final_first_y-final_second_y)/(final_first_x-final_second_x)
constant = final_first_y - (slope*final_first_x)
line = (slope*x) + constant

#plot the graph
if(DEBUG_MODE):
  print (data_x)
  print (data_y)
plt.xlim(0, x_size)
plt.ylim(0, y_size)
plt.plot(point1, point2, marker='o', c='green')
plt.plot(x,line, c='green')
plt.scatter(inlier_x,inlier_y, c='green')
plt.scatter(outlier_x, outlier_y, c='blue')
plt.show()
