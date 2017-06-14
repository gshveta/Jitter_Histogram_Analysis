'''
scipy.lineargrass library to plot a curve using points
if - and + or + and -
store samples
plot a curve using +-10 samples from those points using the lib
find the point at which this line crosses zero
'''


from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy import stats


x,y  = np.loadtxt("BCReset.csv", unpack = True, delimiter = ',')  # numpy array. Like an array (different from list
x_list = list(x)
y_list = list(y)
style.use('ggplot')
plt.plot(x,y)

plt.title('f1 plot')
plt.xlabel('x axis')
plt.ylabel('y axis')

#plt.show()
# code to detect zero crossings
list_zc = []
zplus= []  #list of all y points defining  intercepts
zminus = []
zero_cross = []  #list of all actual zero crossings(x intercepts)
#for i in range(0,len(np.nditer(y, op_flags=['readwrite']))):
for i in range (1, len(y_list)):
  #  print y[i]
    if ((y[i-1] <0) & (y[i] >0)) | ((y[i-1] >0) & (y[i] <0)) :
        #zminus.append(y[i-1])
        #zplus.append(y[i])
       # slope = (y[i]-y[i-1])/(x[i]-x[i-1])
        zminus = [y[i-5],y[i-4],y[i-3],y[i-2],y[i-1]]
        zplus = [y[i],y[i+1],y[i+2],y[i+3],y[i+4]]
        slope, intercept, r, p, std_error = stats.linregress(zminus, zplus)
        zero_cross.append(intercept)
        #slope, intercept, r,p,std_error = stats.linregress(y[i-1],y[i])
        #zero_cross.append(intercept)

#slope, intercept, r,p,std_error = stats.linregress(zminus, zplus)
#zero_cross.append(intercept)
print zero_cross
print len(zero_cross)
'''
#find the cycle-cycle difference
diff =[]
for i in range(2,len(zero_cross)):
    diff.append(zero_cross[i]-zero_cross[i-2])
for i in range(0,len(diff)):   # difference should be positive only
    if diff[i] < 0:
        diff[i] = diff[i]* -1
print diff
'''
cyc_duration = []
for i in range(2,len(zero_cross),2):
    cyc_duration.append(zero_cross[i] - zero_cross[i-2])
for i in range(0, len(cyc_duration)-1):
    if cyc_duration[i] < 0:
        cyc_duration[i] = cyc_duration[i] * -1

diff = []
for i in range(0, len(cyc_duration)-1):
    diff.append(cyc_duration[i+1]-cyc_duration[i])
print diff
print len(diff)

# to plot the histogram
plt.hist(diff)
plt.title("Jitter Histogram")
plt.show()
median_val = np.median(diff)
mean_val = np.mean(diff)
std_dev_value = np.std(diff)
print median_val
print mean_val
print std_dev_value


#f2 = interp1d(zminus, zplus, kind='cubic')
#plt.plot(f2)
#plt.show()
#print zero_cross
#print zplus
#print len(z)

# to obtain the exact x-coordinate of zero crossings

# to obtain the cycle duration

'''diff = []
for i in range(2,len(list_zc)):
    diff.append(list_zc[i]-list_zc[i-2])
print diff
'''
