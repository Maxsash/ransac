# RANSAC
Implementation of RANSAC algorithm in python 3.
The code in ransac_main.py uses random data everytime it is run. 

This random data is stored in <b>data_x</b> and <b>data_y</b>. (line 58)
The main algorithm uses the properties of triangles to figure out the inliers and outliers.

At the beginning of the file (upto line 16) the various parameters can be changed.

<b>Parameter description:</b>
<ul>
<li>DEBUG_MODE</li> (line 5) 

can be toggled to print results and actions at various points of the code.

<li>data_size</li> (line 8) 

is the number of samples. The more samples you take, the more time will the code take to run.

<li>x_size</li> (line 9) 

is the range for x-cordinate, starting from zero.

<li>y_size</li> (line 10) 

is the range for y-cordinate, starting from zero.

<li>threshold_factor</li>li (line 13) 

defines the threshold for determinig inliers

<li>threshold</li> (line 14) 

since the threshold depends on the size of graph. I have used a simple formula to relate them.

<li>optimized_distance</li> (line 15) 

is used so that points that are too close together are not used since this was giving bad results.

<li>angle_threshold</li> (line 16) 

is used to filter out points too far away from the model line.</ul>
