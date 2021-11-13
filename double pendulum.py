import numpy as np 
import matplotlib.pyplot as plt
import turtle
import time

window_scaling=100
cartesian1=[]
cartesian2=[]
interval=0

#CONSTANTS
g = 9.8 #m/s^2pi

m1 = 30    #kg
m2 = 10 #kg

l1 = 2 #m
l2 = 1 #m

#INITIAL CONDITIONS
THETA_1_0 = np.pi / 4
THETA_2_0 = np.pi / 4

THETA_DOT_1_0 = 0
THETA_DOT_2_0 = 0

THETA_DOUBLE_DOT_1_0 = 0
THETA_DOUBLE_DOT_2_0 = 0



#POLAR TO RECTANGULAR
def get_x1(theta_1):
    return l1 * np.sin(theta_1)

def get_y1(theta_1):
    return -l1 * np.cos(theta_1)

def get_x2(theta_1, theta_2):
    return get_x1(theta_1) + l2 * np.sin(theta_2)

def get_y2(theta_1, theta_2):
    return get_y1(theta_1) - l2 * np.cos(theta_2)

#RANGE REDUCTION
RANGE = 2 * np.pi
def toRange(angle):
    angle = angle % RANGE
    if angle > np.pi:
        angle -= RANGE
    return angle
    


#ODEs
def get_theta_double_dot_1(theta_1, theta_2, theta_double_dot_2, theta_dot_2):
    eq = -((m1 + m2)*g*np.sin(theta_1) + m2*l2*theta_double_dot_2*np.cos(theta_1-theta_2) + m2*l2*(theta_dot_2**2)*np.sin(theta_1 - theta_2)) /  (m1 + m2)
    return eq

def get_theta_double_dot_2(theta_2, theta_1, theta_dot_1, theta_double_dot_1):
    eq = (-(g*np.sin(theta_2) + (l1*theta_double_dot_1*np.cos(theta_1-theta_2))) + (l1 * theta_dot_1*np.sin(theta_1-theta_2)))/l1
    return eq
    
#Get the lists of angles and Cartesian coordinates
def plot(t_0, t_f, dt):
   theta_1=THETA_1_0
   theta_2=THETA_2_0

   theta_dot_1 = THETA_DOT_1_0
   theta_dot_2 = THETA_DOT_2_0

   theta_double_dot_1 = THETA_DOUBLE_DOT_1_0
   theta_double_dot_2 = THETA_DOUBLE_DOT_2_0

   time_data=np.arange(t_0, t_f, dt)

   theta_1_vals = []
   theta_2_vals = []
   
   theta_dot_1_vals = []
   theta_dot_2_vals = []

   theta_double_dot_1_vals = []
   theta_double_dot_2_vals = []

   x1_vals = []
   y1_vals = []

   x2_vals = []
   y2_vals = []

   for time in time_data:
        theta_double_dot_1 = get_theta_double_dot_1(theta_1, theta_2,theta_double_dot_2, theta_dot_2)
        theta_double_dot_1_vals.append(theta_double_dot_1) 
        

        theta_double_dot_2 = get_theta_double_dot_2(theta_2, theta_1, theta_dot_1, theta_double_dot_1)
        theta_double_dot_2_vals.append(theta_double_dot_2) 


        theta_dot_1 += theta_double_dot_1 * dt
        theta_dot_1_vals.append(theta_dot_1)

        theta_dot_2 += theta_double_dot_2 * dt 
        theta_dot_2_vals.append(theta_dot_2)

        theta_1 += (theta_dot_1 * dt % (2 * np.pi))
        #theta_1 = toRange(theta_1)
        theta_1_vals.append(theta_1)
        
        
        theta_2 += (theta_dot_2 * dt) 
        #theta_2 = toRange(theta_2)
        theta_2_vals.append(theta_2)

        x1_vals.append(get_x1(theta_1))
        y1_vals.append(get_y1(theta_1))

        x2_vals.append(get_x2(theta_1, theta_2))
        y2_vals.append(get_y2(theta_1, theta_2))
    
   for i in range(0, len(theta_1_vals)):
        theta_1_vals[i]= toRange(theta_1_vals[i])
        theta_2_vals[i]= toRange(theta_2_vals[i])

   plt.figure(1)
   plt.plot(time_data, theta_1_vals, label="time vs theta1")
   plt.figure(2)
   plt.plot(time_data, theta_2_vals, label="time vs theta2")
   plt.figure(3)
   plt.plot(x1_vals, y1_vals, label="x1 vs y1")
   plt.figure(4)
   plt.plot(x2_vals, y2_vals, label="x2  vs y2")
   plt.show()
   
   cartesian1.append(x1_vals)
   cartesian1.append(y1_vals)

   cartesian2.append(x2_vals)
   cartesian2.append(y2_vals)

   interval=dt

def translate_to_screen(x):
   screen_size=((l1+l2)*window_scaling)
   #translate all coords to positive
   positive=x+((l1+l2)/2)
   #increase resulution
   return positive*window_scaling

def use_turtle():
   dt=interval
   mass_1=turtle.Turtle()
   mass_1.shape('circle')
   mass_1.penup()
   
   mass_2=turtle.Turtle()
   mass_2.shape('circle')
   mass_2.color('blue')
   mass_2.penup()
   

   x1_vals=cartesian1[0]
   y1_vals=cartesian1[1]

   x2_vals=cartesian2[0]
   y2_vals=cartesian2[1]
   
   for x in range(len(x1_vals)):
      mass_1.goto(translate_to_screen(x1_vals[x]), translate_to_screen(y1_vals[x]))
      mass_2.goto(translate_to_screen(x2_vals[x]), translate_to_screen(y2_vals[x]))
      time.sleep(dt)

wn = turtle.Screen()
wn.setup(width=((l1+l2)*window_scaling),height=((l1+l2)*window_scaling))
wn.title("Double Pendulum")
