# Double Pendulum
A derivation of the differential equations for the double pendulum alongside a Python program to generate a numerical solution.  
Available as an ```ipynb``` file.

I have added a turtle implementation to the program made by srivatsa-kundurthy, and it is a .py file.
You can use the shell to change gravity, masses, length of the rigid rods, initial angles, initial angular velocities, and initial angular accelerations. The names of the variables are under the #initial conditions section of the program
This program generates a table of values and stores them in a list when you call the plot function, and it plots them using matplotlib
To call the plot function, input an initial time and a final time, and an interval(the smaller the interval, the smoother the plot and turtle will be, it will take longer to compute)
For example, plot(1, 30, 0.1) will plot the motion of the pendulum from 1 second to 30 seconds, by computing the position for each tenth of a second.
To view a simulation of the pendulum with time as seconds, call the command use_turtle() in the shell, and it will play the simulation, based on the table of values computed earlier.
Window scaling will change the size of the turtle window
