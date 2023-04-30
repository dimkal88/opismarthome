import time
import paho.mqtt.client as mqtt
from IOPi import IOPi

topic = None
msg = None
messages=[]

def on_message(client, userdata, message):
    if (message.retain == 0): #flag message if 0 is new message
        topic = message.topic #topic of mqtt
        msg = str(message.payload.decode("utf-8")) #message of mqtt
        flag= message.retain
        #print ("on message ",topic,msg)
        messages.append((topic,msg,flag))

bus1 = IOPi(0x20)
bus2 = IOPi(0x21)
bus3 = IOPi(0x22)
bus4 = IOPi(0x23)

#input pins
bus2.set_pin_direction(1, 1)  # set pin 1 as an input
bus2.set_pin_pullup(1, 1)  # enable the internal pull-up resistor on pin 1
bus2.invert_pin(1, 1)  # invert pin 1 so a button press will register as 1
#
bus2.set_pin_direction(2, 1)  # set pin 2 as an input
bus2.set_pin_pullup(2, 1)  # enable the internal pull-up resistor on pin 1
bus2.invert_pin(2, 1)  # invert pin 2 so a button press will register as 1
#
bus2.set_pin_direction(3, 1)  # set pin 3 as an input
bus2.set_pin_pullup(3, 1)  # enable the internal pull-up resistor on pin 3
bus2.invert_pin(3, 1)  # invert pin 3 so a button press will register as 3
#
bus2.set_pin_direction(4, 1)  # set pin 4 as an input
bus2.set_pin_pullup(4, 1)  # enable the internal pull-up resistor on pin 4
bus2.invert_pin(4, 1)  # invert pin 4 so a button press will register as 4
#
bus2.set_pin_direction(5, 1)  # set pin 5 as an input
bus2.set_pin_pullup(5, 1)  # enable the internal pull-up resistor on pin 5
bus2.invert_pin(5, 1)  # invert pin 5 so a button press will register as 5
#
bus2.set_pin_direction(6, 1)  # set pin 6 as an input
bus2.set_pin_pullup(6, 1)  # enable the internal pull-up resistor on pin 6
bus2.invert_pin(6, 1)  # invert pin 6 so a button press will register as 6
#
bus2.set_pin_direction(7, 1)  # set pin 7 as an input
bus2.set_pin_pullup(7, 1)  # enable the internal pull-up resistor on pin 7
bus2.invert_pin(7, 1)  # invert pin 7 so a button press will register as 7
#
bus2.set_pin_direction(8, 1)  # set pin 8 as an input
bus2.set_pin_pullup(8, 1)  # enable the internal pull-up resistor on pin 8
bus2.invert_pin(8, 1)  # invert pin 8 so a button press will register as 8
#
bus2.set_pin_direction(9, 1)  # set pin 9 as an input
bus2.set_pin_pullup(9, 1)  # enable the internal pull-up resistor on pin 9
bus2.invert_pin(9, 1)  # invert pin 9 so a button press will register as 9
#
bus2.set_pin_direction(10, 1)  # set pin 10 as an input
bus2.set_pin_pullup(10, 1)  # enable the internal pull-up resistor on pin 10
bus2.invert_pin(10, 1)  # invert pin 10 so a button press will register as 10
#
bus2.set_pin_direction(11, 1)  # set pin 11 as an input
bus2.set_pin_pullup(11, 1)  # enable the internal pull-up resistor on pin 11
bus2.invert_pin(11, 1)  # invert pin 11 so a button press will register as 11
#
bus2.set_pin_direction(12, 1)  # set pin 12 as an input
bus2.set_pin_pullup(12, 1)  # enable the internal pull-up resistor on pin 12
bus2.invert_pin(12, 1)  # invert pin 10 so a button press will register as 12
#
#
bus2.set_pin_direction(15, 1)  # set pin 13 as an input
bus2.set_pin_pullup(15, 1)  # enable the internal pull-up resistor on pin 13
bus2.invert_pin(15, 1)  # invert pin 14 so a button press will register as 13
#
bus2.set_pin_direction(14, 1)  # set pin 14 as an input
bus2.set_pin_pullup(14, 1)  # enable the internal pull-up resistor on pin 14
bus2.invert_pin(14, 1)  # invert pin 14 so a button press will register as 14
#
bus4.set_pin_direction(1, 1)  # set pin 1 as an input
bus4.set_pin_pullup(1, 1)  # enable the internal pull-up resistor on pin 1
bus4.invert_pin(1, 1)  # invert pin 1 so a button press will register as 1
#
bus4.set_pin_direction(2, 1)  # set pin 2 as an input
bus4.set_pin_pullup(2, 1)  # enable the internal pull-up resistor on pin 1
bus4.invert_pin(2, 1)  # invert pin 2 so a button press will register as 1
#
bus4.set_pin_direction(3, 1)  # set pin 3 as an input
bus4.set_pin_pullup(3, 1)  # enable the internal pull-up resistor on pin 3
bus4.invert_pin(3, 1)  # invert pin 3 so a button press will register as 3
#
bus4.set_pin_direction(4, 1)  # set pin 4 as an input
bus4.set_pin_pullup(4, 1)  # enable the internal pull-up resistor on pin 4
bus4.invert_pin(4, 1)  # invert pin 3 so a button press will register as 4
#
bus4.set_pin_direction(5, 1)  # set pin 5 as an input
bus4.set_pin_pullup(5, 1)  # enable the internal pull-up resistor on pin 5
bus4.invert_pin(5, 1)  # invert pin 3 so a button press will register as 5
#



#output pins
bus1.set_pin_direction(1, 0)  # set pin 1 as an output
bus1.write_pin(1, 0)  # turn off pin 1
#
bus1.set_pin_direction(2, 0)  # set pin 2 as an output
bus1.write_pin(2, 0)  # turn off pin 2
#
bus1.set_pin_direction(3, 0)  # set pin 3 as an output
bus1.write_pin(3, 0)  # turn off pin 3
#
bus1.set_pin_direction(4, 0)  # set pin 4 as an output
bus1.write_pin(4, 0)  # turn off pin 4
#
bus1.set_pin_direction(5, 0)  # set pin 5 as an output
bus1.write_pin(5, 0)  # turn off pin 5
#
bus1.set_pin_direction(6, 0)  # set pin 6 as an output
bus1.write_pin(6, 0)  # turn off pin 6
#
bus1.set_pin_direction(7, 0)  # set pin 7 as an output
bus1.write_pin(7, 0)  # turn off pin 7
#
bus1.set_pin_direction(8, 0)  # set pin 8 as an output
bus1.write_pin(8, 0)  # turn off pin 8
#
bus1.set_pin_direction(9, 0)  # set pin 9 as an output
bus1.write_pin(9, 0)  # turn off pin 9
#
bus1.set_pin_direction(10, 0)  # set pin 10 as an output
bus1.write_pin(10, 0)  # turn off pin 10
#
bus1.set_pin_direction(11, 0)  # set pin 11 as an output
bus1.write_pin(11, 0)  # turn off pin 11
#
bus1.set_pin_direction(12, 0)  # set pin 12 as an output
bus1.write_pin(12, 0)  # turn off pin 12
#
bus1.set_pin_direction(13, 0)  # set pin 13 as an output
bus1.write_pin(13, 0)  # turn off pin 13
#
bus1.set_pin_direction(14, 0)  # set pin 14 as an output
bus1.write_pin(14, 0)  # turn off pin 14
#

bus1.set_pin_direction(15, 0)  # set pin 15 as an output
bus1.write_pin(15, 0)  # turn off pin 15
#
bus1.set_pin_direction(16, 0)  # set pin 16 as an output
bus1.write_pin(16, 0)  # turn off pin 16
#
bus3.set_pin_direction(1, 0)  # set pin 1 as an output
bus3.write_pin(1, 0)  # turn off pin 1
#
bus3.set_pin_direction(2, 0)  # set pin 2 as an output
bus3.write_pin(2, 0)  # turn off pin 2
#
bus3.set_pin_direction(3, 0)  # set pin 3 as an output
bus3.write_pin(3, 0)  # turn off pin 3
#
bus3.set_pin_direction(4, 0)  # set pin 4 as an output
bus3.write_pin(4, 0)  # turn off pin 4
#
bus3.set_pin_direction(5, 0)  # set pin 5 as an output
bus3.write_pin(5, 0)  # turn off pin 5
#
bus3.set_pin_direction(6, 0)  # set pin 6 as an output
bus3.write_pin(6, 0)  # turn off pin 6
#
bus3.set_pin_direction(7, 0)  # set pin 7 as an output
bus3.write_pin(7, 0)  # turn off pin 7
#
bus3.set_pin_direction(8, 0)  # set pin 8 as an output
bus3.write_pin(8, 0)  # turn off pin 8
#
bus3.set_pin_direction(9, 0)  # set pin 9 as an output
bus3.write_pin(9, 0)  # turn off pin 9
#
bus3.set_pin_direction(10, 0)  # set pin 10 as an output
bus3.write_pin(10, 0)  # turn off pin 10
#
bus3.set_pin_direction(11, 0)  # set pin 11 as an output
bus3.write_pin(11, 0)  # turn off pin 11
#
bus3.set_pin_direction(16, 0)  # set pin 11 as an output
bus3.write_pin(16, 0)  # turn off pin 11
#

# timers for delay
xtime=.55 # time between press time for switches

#rollershutters flags
shflag01=0
shflag02=0
shflag03=0
shflag04=0

# Create client instance and connect to localhost
client = mqtt.Client()
client.connect("127.0.0.1",1883,60)
client.subscribe("#")
client.on_message=on_message

client.loop_start() #start the loop
while True :
    l=len(messages) #flag for messages variable
    if l>0: #are there any
        topic,msg,flag=messages.pop()
        print(topic,msg,flag)
    if (msg=="OFF") and (flag==0):
        if (topic=="light/l01"):
            bus1.write_pin(1, 0)  # turn off pin 1
            print ('mqtt received turn OFF relay 1')  # print a message to the screen
            flag=1
        elif (topic=="light/l02"):
            bus1.write_pin(2, 0)  # turn off pin 2
            print ('mqtt received turn OFF relay 2')  # print a message to the screen
            flag=1
        elif (topic=="light/l03"):
            bus1.write_pin(3, 0)  # turn off pin 3
            print ('mqtt received turn OFF relay 3')  # print a message to the screen
            flag=1
        elif (topic=="light/l04"):
            bus1.write_pin(4, 0)  # turn off pin 4
            print ('mqtt received turn OFF relay 4')  # print a message to the screen
            flag=1
        elif (topic=="light/l05"):
            bus1.write_pin(5, 0)  # turn off pin 5
            print ('mqtt received turn OFF relay 5')  # print a message to the screen
            flag=1
        elif (topic=="light/l06"):
            bus1.write_pin(6, 0)  # turn off pin 6
            print ('mqtt received turn OFF relay 6')  # print a message to the screen
            flag=1
        elif (topic=="light/l07"):
            bus1.write_pin(7, 0)  # turn off pin 7
            print ('mqtt received turn OFF relay 7')  # print a message to the screen
            flag=1
        elif (topic=="light/l08"):
            bus1.write_pin(8, 0)  # turn off pin 8
            print ('mqtt received turn OFF relay 8')  # print a message to the screen
            flag=1
        elif (topic=="light/l09"):
            bus1.write_pin(9, 0)  # turn off pin 9
            print ('mqtt received turn OFF relay 9')  # print a message to the screen
            flag=1
        elif (topic=="light/l10"):
            bus1.write_pin(10, 0)  # turn off pin 10
            print ('mqtt received turn OFF relay 10')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r01"):
            bus1.write_pin(11, 0)  # turn off pin 11
            print ('mqtt received turn OFF relay 11')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r02"):
            bus1.write_pin(12, 0)  # turn off pin 12
            print ('mqtt received turn OFF relay 12')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r03"):
            bus1.write_pin(13, 0)  # turn off pin 13
            print ('mqtt received turn OFF relay 13')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r04"):
            bus1.write_pin(14, 0)  # turn off pin 14
            print ('mqtt received turn OFF relay 14')  # print a message to the screen
            flag=1
        elif (topic=="heater/h01"):
            bus1.write_pin(15, 0)  # turn off pin 15
            print ('mqtt received turn OFF relay 15')  # print a message to the screen
            flag=1
        elif (topic=="heater/h02"):
            bus1.write_pin(16, 0)  # turn off pin 16
            print ('mqtt received turn OFF relay 16')  # print a message to the screen
            flag=1
        elif (topic=="light/l11"):
            bus3.write_pin(1, 0)  # turn off pin 1
            print ('mqtt received turn OFF relay 17')  # print a message to the screen
            flag=1
        elif (topic=="light/l12"):
            bus3.write_pin(2, 0)  # turn off pin 2
            print ('mqtt received turn OFF relay 18')  # print a message to the screen
            flag=1
        elif (topic=="light/l13"):
            bus3.write_pin(3, 0)  # turn off pin 3
            print ('mqtt received turn OFF relay 19')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p01"):
            bus3.write_pin(4, 0)  # turn off pin 4
            print ('mqtt received turn OFF relay 20')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p02"):
            bus3.write_pin(5, 0)  # turn off pin 5
            print ('mqtt received turn OFF relay 21')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p03"):
            bus3.write_pin(6, 0)  # turn off pin 6
            print ('mqtt received turn OFF relay 22')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p04"):
            bus3.write_pin(7, 0)  # turn off pin 7
            print ('mqtt received turn OFF relay 23')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p05"):
            bus3.write_pin(8, 0)  # turn off pin 8
            print ('mqtt received turn OFF relay 24')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p06"):
            bus3.write_pin(9, 0)  # turn off pin 9
            print ('mqtt received turn OFF relay 25')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p07"):
            bus3.write_pin(10, 0)  # turn off pin 10
            print ('mqtt received turn OFF relay 26')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p08"):
            bus3.write_pin(11, 0)  # turn off pin 11
            print ('mqtt received turn OFF relay 27')  # print a message to the screen
            flag=1
        elif (topic=="device/d01"):
            bus3.write_pin(16, 0)  # turn off pin 11
            print ('mqtt received turn OFF relay 28')  # print a message to the screen
            flag=1
    elif (msg=="ON") and (flag==0):
        if (topic=="light/l01"):
            bus1.write_pin(1, 1)  # turn on pin 1
            print ('mqtt received turn ON relay 1')  # print a message to the screen
            flag=1
        elif (topic=="light/l02"):
            bus1.write_pin(2, 1)  # turn on pin 2
            print ('mqtt received turn ON relay 2')  # print a message to the screen
            flag=1
        elif (topic=="light/l03"):
            bus1.write_pin(3, 1)  # turn on pin 3
            print ('mqtt received turn ON relay 3')  # print a message to the screen
            flag=1
        elif (topic=="light/l04"):
            bus1.write_pin(4, 1)  # turn on pin 4
            print ('mqtt received turn ON relay 4')  # print a message to the screen
            flag=1
        elif (topic=="light/l05"):
            bus1.write_pin(5, 1)  # turn on pin 5
            print ('mqtt received turn ON relay 5')  # print a message to the screen
            flag=1
        elif (topic=="light/l06"):
            bus1.write_pin(6, 1)  # turn on pin 6
            print ('mqtt received turn ON relay 6')  # print a message to the screen
            flag=1
        elif (topic=="light/l07"):
            bus1.write_pin(7, 1)  # turn on pin 7
            print ('mqtt received turn ON relay 7')  # print a message to the screen
            flag=1
        elif (topic=="light/l08"):
            bus1.write_pin(8, 1)  # turn on pin 8
            print ('mqtt received turn ON relay 8')  # print a message to the screen
            flag=1
        elif (topic=="light/l09"):
            bus1.write_pin(9, 1)  # turn on pin 9
            print ('mqtt received turn ON relay 9')  # print a message to the screen
            flag=1
        elif (topic=="light/l10"):
            bus1.write_pin(10, 1)  # turn on pin 10
            print ('mqtt received turn ON relay 10')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r01"):
            bus1.write_pin(11, 1)  # turn ON pin 11
            print ('mqtt received turn ON relay 11')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r02"):
            bus1.write_pin(12, 1)  # turn off pin 12
            print ('mqtt received turn ON relay 12')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r03"):
            bus1.write_pin(13, 1)  # turn ON pin 13
            print ('mqtt received turn ON relay 13')  # print a message to the screen
            flag=1
        elif (topic=="rollershutter/r04"):
            bus1.write_pin(14, 1)  # turn off pin 14
            print ('mqtt received turn ON relay 14')  # print a message to the screen
            flag=1
        elif (topic=="heater/h01"):
            bus1.write_pin(15, 1)  # turn ON pin 15
            print ('mqtt received turn ON relay 15')  # print a message to the screen
            flag=1
        elif (topic=="heater/h02"):
            bus1.write_pin(16, 1)  # turn off pin 16
            print ('mqtt received turn ON relay 16')  # print a message to the screen
            flag=1
        elif (topic=="light/l11"):
            bus3.write_pin(1, 1)  # turn on pin 1
            print ('mqtt received turn ON relay 17')  # print a message to the screen
            flag=1
        elif (topic=="light/l12"):
            bus3.write_pin(2, 1)  # turn on pin 2
            print ('mqtt received turn ON relay 18')  # print a message to the screen
            flag=1
        elif (topic=="light/l13"):
            bus3.write_pin(3, 1)  # turn on pin 3
            print ('mqtt received turn ON relay 19')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p01"):
            bus3.write_pin(4, 1)  # turn on pin 4
            print ('mqtt received turn ON relay 20')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p02"):
            bus3.write_pin(5, 1)  # turn on pin 5
            print ('mqtt received turn ON relay 21')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p03"):
            bus3.write_pin(6, 1)  # turn on pin 6
            print ('mqtt received turn ON relay 22')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p04"):
            bus3.write_pin(7, 1)  # turn on pin 7
            print ('mqtt received turn ON relay 23')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p05"):
            bus3.write_pin(8, 1)  # turn on pin 8
            print ('mqtt received turn ON relay 24')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p06"):
            bus3.write_pin(9, 1)  # turn on pin 9
            print ('mqtt received turn ON relay 25')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p07"):
            bus3.write_pin(10, 1)  # turn on pin 10
            print ('mqtt received turn ON relay 26')  # print a message to the screen
            flag=1
        elif (topic=="poweroutlet/p08"):
            bus3.write_pin(11, 1)  # turn ON pin 11
            print ('mqtt received turn ON relay 27')  # print a message to the screen
            flag=1
        elif (topic=="device/d01"):
            bus3.write_pin(16, 1)  # turn ON pin 11
            print ('mqtt received turn ON relay 28')  # print a message to the screen
            flag=1
#

# lights code
    if (bus2.read_pin(1) == 1) and (bus1.read_pin(1) == 0):  # check to see if the button is pressed
        print ('button 1 pressed turn ON switch 1')  # print a message to the screen
        #bus1.write_pin(1, 1)  # turn on pin 1
        client.publish("light/l01", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(1) == 1) and (bus1.read_pin(1) == 1):
        print ('button 1 pressed turn OFF switch 1')  # print a message to the screen
        #bus1.write_pin(1, 0)  # turn off pin 1
        client.publish("light/l01", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(2) == 1) and (bus1.read_pin(2) == 0):  # check to see if the button is pressed
        print ('button 2 pressed turn ON switch 2')  # print a message to the screen
        client.publish("light/l02", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(2) == 1) and (bus1.read_pin(2) == 1):
        print ('button 2 pressed turn OFF switch 2')  # print a message to the screen
        client.publish("light/l02", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(3) == 1) and (bus1.read_pin(3) == 0):  # check to see if the button is pressed
        print ('button 3 pressed turn ON switch 3')  # print a message to the screen
        client.publish("light/l03", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(3) == 1) and (bus1.read_pin(3) == 1):
        print ('button 3 pressed turn OFF switch 3')  # print a message to the screen
        client.publish("light/l03", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(4) == 1) and (bus1.read_pin(4) == 0):  # check to see if the button is pressed
        print ('button 4 pressed turn ON switch 4')  # print a message to the screen
        client.publish("light/l04", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(4) == 1) and (bus1.read_pin(4) == 1):
        print ('button 4 pressed turn OFF switch 4')  # print a message to the screen
        client.publish("light/l04", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(5) == 1) and (bus1.read_pin(5) == 0):  # check to see if the button is pressed
        print ('button 5 pressed turn ON switch 5')  # print a message to the screen
        client.publish("light/l05", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(5) == 1) and (bus1.read_pin(5) == 1):
        print ('button 5 pressed turn OFF switch 2')  # print a message to the screen
        client.publish("light/l05", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(6) == 1) and (bus1.read_pin(6) == 0):  # check to see if the button is pressed
        print ('button 6 pressed turn ON switch 6')  # print a message to the screen
        client.publish("light/l06", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(6) == 1) and (bus1.read_pin(6) == 1):
        print ('button 6 pressed turn OFF switch 6')  # print a message to the screen
        client.publish("light/l06", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(7) == 1) and (bus1.read_pin(7) == 0):  # check to see if the button is pressed
        print ('button 7 pressed turn ON switch 7')  # print a message to the screen
        client.publish("light/l07", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(7) == 1) and (bus1.read_pin(7) == 1):
        print ('button 7 pressed turn OFF switch 7')  # print a message to the screen
        client.publish("light/l07", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(8) == 1) and (bus1.read_pin(8) == 0):  # check to see if the button is pressed
        print ('button 8 pressed turn ON switch 8')  # print a message to the screen
        client.publish("light/l08", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(8) == 1) and (bus1.read_pin(8) == 1):
        print ('button 8 pressed turn OFF switch 8')  # print a message to the screen
        client.publish("light/l08", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(9) == 1) and (bus1.read_pin(9) == 0):  # check to see if the button is pressed
        print ('button 9 pressed turn ON switch 9')  # print a message to the screen
        client.publish("light/l09", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(9) == 1) and (bus1.read_pin(9) == 1):
        print ('button 9 pressed turn OFF switch 9')  # print a message to the screen
        client.publish("light/l09", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus2.read_pin(10) == 1) and (bus1.read_pin(10) == 0):  # check to see if the button is pressed
        print ('button 10 pressed turn ON switch 10')  # print a message to the screen
        client.publish("light/l10", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus2.read_pin(10) == 1) and (bus1.read_pin(10) == 1):
        print ('button 10 pressed turn OFF switch 10')  # print a message to the screen
        client.publish("light/l10", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus4.read_pin(1) == 1) and (bus3.read_pin(1) == 0):  # check to see if the button is pressed
        print ('button 15 pressed turn ON relay 17')  # print a message to the screen
        client.publish("light/l11", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus4.read_pin(1) == 1) and (bus3.read_pin(1) == 1):
        print ('button 15 pressed turn OFF relay 17')  # print a message to the screen
        client.publish("light/l11", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
    if (bus4.read_pin(2) == 1) and (bus3.read_pin(2) == 0):  # check to see if the button is pressed
        print ('button 16 pressed turn ON relay 18')  # print a message to the screen
        client.publish("light/l12", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
    elif (bus4.read_pin(2) == 1) and (bus3.read_pin(2) == 1):
        print ('button 16 pressed turn OFF relay 18')  # print a message to the screen
        client.publish("light/l12", "OFF")
        time.sleep(xtime) # sleep xtime before checking the pin again
#
#contact buttons
    if (bus4.read_pin(4) == 1):  # check to see if the button is pressed
        print ('button 17 pressed')  # print a message to the screen
        client.publish("contact/c01", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
        client.publish("contact/c01", "OFF")
    if (bus4.read_pin(5) == 1):  # check to see if the button is pressed
        print ('button 18 pressed')  # print a message to the screen
        client.publish("contact/c02", "ON")
        time.sleep(xtime) # sleep xtime before checking the pin again
        client.publish("contact/c02", "OFF")
#

# rollershutter code
    if (bus2.read_pin(11) == 1) and (shflag01==0):  # check to see if the button is pressed
        print ('button 11 pressed turn ON relay 11')  # print a message to the screen
        client.publish("rollershutter/r01", "ON")
        shflag01=1
    elif (bus2.read_pin(11) == 0) and (shflag01==1):
        print ('button 10 unleased turn OFF relay 11')  # print a message to the screen
        client.publish("rollershutter/r01", "OFF")
        shflag01=0
#
    if (bus2.read_pin(12) == 1) and (shflag02==0):  # check to see if the button is pressed
        print ('button 12 pressed turn ON relay 12')  # print a message to the screen
        client.publish("rollershutter/r02", "ON")
        shflag02=1
    elif (bus2.read_pin(12) == 0) and (shflag02==1):
        print ('button 12 unleased turn OFF relay 12')  # print a message to the screen
        client.publish("rollershutter/r02", "OFF")
        shflag02=0
#
    if (bus2.read_pin(15) == 1) and (shflag03==0):  # check to see if the button is pressed
        print ('button 13 pressed turn ON relay 13')  # print a message to the screen
        client.publish("rollershutter/r03", "ON")
        shflag03=1
    elif (bus2.read_pin(15) == 0) and (shflag03==1):
        print ('button 10 unleased turn OFF relay 11')  # print a message to the screen
        client.publish("rollershutter/r03", "OFF")
        shflag03=0
#
    if (bus2.read_pin(14) == 1) and (shflag04==0):  # check to see if the button is pressed
        print ('button 14 pressed turn ON relay 14')  # print a message to the screen
        client.publish("rollershutter/r04", "ON")
        shflag04=1
    elif (bus2.read_pin(14) == 0) and (shflag04==1):
        print ('button 14 unleased turn OFF relay 14')  # print a message to the screen
        client.publish("rollershutter/r04", "OFF")
        shflag04=0
#
client.loop_stop() #stop the loop
