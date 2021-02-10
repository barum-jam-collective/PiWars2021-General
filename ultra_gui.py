# Python GUI for Servo control
# Specifically written for and in lieu of PiBorg's vesion for the UltraBorg Servo and Sensor Board
# 10 Feb 2021

#import libraries
import UltraBorg3 as UltraBorg
from guizero import App, Box, Slider, Text, TextBox, PushButton

# Start the UltraBorg
global UB
UB = UltraBorg.UltraBorg()
UB.Init()

def set_initial_servo_positions():
    # To read the saved servo positiona and set the slider start position?
    slider1_value = UB.GetServoPosition1()
    slider2_value = UB.GetServoPosition2()
    slider3_value = UB.GetServoPosition3()
    slider4_value = UB.GetServoPosition4()    
    
    UB.SetServoPosition1(float(slider1_value) / 100.0)
    UB.SetServoPosition2(float(slider1_value) / 100.0)
    UB.SetServoPosition3(float(slider1_value) / 100.0)
    UB.SetServoPosition4(float(slider1_value) / 100.0)
    
    # Print the servo positions to the sccreen
    print("Servo 1 = ",slider1_value)
    print("Servo 2 = ",slider2_value)
    print("Servo 3 = ",slider3_value)
    print("Servo 4 = ",slider4_value)

def slider1_changed(slider1_value):
    global UB 
    textbox1.value = UB.GetServoPosition1() #retrieves the servo position and displays it in the box below the slider
    UB.SetServoPosition1(float(slider1_value) / 90)
    
def slider2_changed(slider2_value):
    global UB
    textbox2.value = UB.GetServoPosition2() #retrieves the servo position and displays it in the box below the slider
    UB.SetServoPosition2(float(slider2_value) / 90)
    
def slider3_changed(slider3_value):
    global UB
    textbox3.value = UB.GetServoPosition3() #retrieves the servo position and displays it in the box below the slider
    UB.SetServoPosition3(float(slider3_value) / 90)

def slider4_changed(slider4_value):
    global UB
    textbox4.value = UB.GetServoPosition4() #retrieves the servo position and displays it in the box below the slider
    UB.SetServoPosition4(float(slider4_value) / 90)

# Reset the servos
def reset_servo1():
    UB.SetServoPosition1(float(0) / 90)
    textbox1.value = UB.GetServoPosition1()
    slider1.value="0"
    
def reset_servo2():
    UB.SetServoPosition1(float(0) / 90)
    textbox2.value = UB.GetServoPosition2()
    slider2.value="0"
    
def reset_servo3():
    UB.SetServoPosition3(float(0) / 90)
    textbox1.value = UB.GetServoPosition3()
    slider3.value="0"
    
def reset_servo4():
    UB.SetServoPosition4(float(0) / 90)
    textbox1.value = UB.GetServoPosition4()
    slider4.value="0"

app = App(title="Servo Control") # Window Title 
message = Text(app, text="UltraBorg Servo Control - Move the sliders to control servos") # Text to display inside window

set_initial_servo_positions() # Not sure if this is working

#create the sliders in the window and link to control functions
slider1 = Slider(app, command=slider1_changed, start=-90, end=90, width='fill')
textbox1 = TextBox(app)
button = PushButton(app, text="Reset",  command=reset_servo1)
 
slider2= Slider(app, command=slider2_changed, start=-90, end=90, width='fill')
textbox2 = TextBox(app)
button = PushButton(app, text="Reset",  command=reset_servo2)

slider3= Slider(app, command=slider3_changed, start=-90, end=90, width='fill')
textbox3 = TextBox(app)
button = PushButton(app, text="Reset",  command=reset_servo3)

slider4= Slider(app, command=slider4_changed, start=-90, end=90, width='fill')
textbox4 = TextBox(app)
button = PushButton(app, text="Reset",  command=reset_servo4)

#display everything
app.display()
