#space_invaders
import time
import turtle as trtl
wn = trtl.Screen()
trtl.addshape("ship.gif")
import random as rand
colors = ["red","orange","yellow","green","blue","purple"]
numbers = [0,1,2,3,4,5,6,7,8]
invadername = ["invader1","invader2","invader3","invader4","invader5","invader6","invader7","invader8","invader9"]
invaderplace = []
place = 4
mag = ["bullet0"]
magnumber = 0
bulletnumber = 0
bullets = []
bulletcounter = 0
win_condition = 27
winloss = trtl.Turtle(visible=False)
winloss.penup()
winloss.speed(0)
winloss.goto(-150,0)
#create arena
box = trtl.Turtle()
box.pensize(4)
box.penup()
box.hideturtle()
box.speed(0)
box.goto(-225,250)
box.pendown()
box.goto(225,250)
box.goto(225,-250)
box.goto(-225,-250)
box.goto(-225,250)
amount_of_lines = [0,1,2,3,4,5,6,7,8]
random_colors = ["black"]
player = trtl.Turtle()

player.shape("ship.gif")
player.penup()
player.speed(0)
player.left(90)
player.goto(0,-230)
trtl.addshape("space_invader1.gif")
trtl.addshape("space_invader2.gif")
trtl.addshape("space_invader3.gif")
invader_shapes = ["space_invader1.gif","space_invader2.gif","space_invader3.gif"]
invader_line1 = ["invader1_line1","invader2_line1","invader3_line1"]
invader_line2 = ["invader1_line2","invader2_line2","invader3_line2"]
invader_line3 = ["invader1_line3","invader2_line3","invader3_line3"]
invader_line4 = ["invader1_line4","invader2_line4","invader3_line4"]
invader_line5 = ["invader1_line5","invader2_line5","invader3_line5"]
invader_line6 = ["invader1_line6","invader2_line6","invader3_line6"]
invader_line7 = ["invader1_line7","invader2_line7","invader3_line7"]
invader_line8 = ["invader1_line8","invader2_line8","invader3_line8"]
invader_line9 = ["invader1_line9","invader2_line9","invader3_line9"]
invaderxcors = []
invaderycors = []
turtles_line = [2,1,0]
amount_of_turtles = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
possible_places11 = [0,1,2,3]
possible_places12 = [4,5,6,7]
possible_places13 = [8,9,10,11]
possible_places21 = [0,1,2,3]
possible_places22 = [4,5,6,7]
possible_places23 = [8,9,10,11]
possible_places31 = [0,1,2,3]
possible_places32 = [4,5,6,7]
possible_places33 = [8,9,10,11]
possible_places41 = [0,1,2,3]
possible_places42 = [4,5,6,7]
possible_places43 = [8,9,10,11]
possible_places51 = [0,1,2,3]
possible_places52 = [4,5,6,7]
possible_places53 = [8,9,10,11]
possible_places61 = [0,1,2,3]
possible_places62 = [4,5,6,7]
possible_places63 = [8,9,10,11]
possible_places71 = [0,1,2,3]
possible_places72 = [4,5,6,7]
possible_places73 = [8,9,10,11]
possible_places81 = [0,1,2,3]
possible_places82 = [4,5,6,7]
possible_places83 = [8,9,10,11]
possible_places91 = [0,1,2,3]
possible_places92 = [4,5,6,7]
possible_places93 = [8,9,10,11]
possible_line_places1 = [possible_places11, possible_places12, possible_places13]
possible_line_places2 = [possible_places21, possible_places22, possible_places23]
possible_line_places3 = [possible_places31, possible_places32, possible_places33]
possible_line_places4 = [possible_places41, possible_places42, possible_places43]
possible_line_places5 = [possible_places51, possible_places52, possible_places53]
possible_line_places6 = [possible_places61, possible_places62, possible_places63]
possible_line_places7 = [possible_places71, possible_places72, possible_places73]
possible_line_places8 = [possible_places81, possible_places82, possible_places83]
possible_line_places9 = [possible_places91, possible_places92, possible_places93]

line_cowords = [230, 200, 170, 140, 110, 80, 50, 20, -10, -40, -70, -100]

line_place = 0
x = -200

for j in turtles_line:
    x = -200
    for i in amount_of_lines:
        rand_line1 = rand.choice(possible_line_places1[j])
        i = trtl.Turtle(visible = False,shape = rand.choice(invader_shapes))
        i.right(90)
        i.speed(0)
        i.penup()
        i.goto(x,line_cowords[rand_line1])
        i.color(rand.choice(random_colors))
        i.showturtle()
        invaderplace.append(i)
        x += 50




def end_screen():
    global magnumber
    magnumber += 1
    player.hideturtle()
    for i in amount_of_turtles:
        invaderplace[i].hideturtle()
    winloss.color("red")
    winloss.write("YOU'VE BEEN DEFEATED", font=("Arial", 20, "bold"))
def movement():
    global magnumber

    for i in amount_of_turtles:
        newy = invaderplace[i].ycor()
        newx = invaderplace[i].xcor()
        newy -= 15
        invaderplace[i].goto(newx,newy)
        if (newy <= -215):
            end_screen()






def initiate():
    global place
    shoot(place)
def shoot(a):
    global mag
    global magnumber
    global bullets
    global bulletnumber
    global win_condition
    check = 0
    bullet = mag[magnumber]
    mag.pop()
    if (magnumber == 0):
        magnumber -= 1
        if (a == 0):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(-200, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 1):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(-150, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 2):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(-100, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 3):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(-50, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 4):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(0, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 5):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(50, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 6):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(100, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 7):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(150, -220)
            bullet.showturtle()
            bullets.append(bullet)
        if (a == 8):
            
            bullet = trtl.Turtle("square",1,False)
            bullet.turtlesize(.3)
            bullet.penup()
            bullet.speed(0)
            bullet.goto(200, -220)
            bullet.showturtle()
            bullets.append(bullet)
        x = bullet.xcor()
        y = bullet.ycor()
        while(y < 300):
            y += 15
            bullet.goto(x,y)
            bullet.color(rand.choice(colors))
            if (y == 260):
                bullet.hideturtle()
                bulletnumber += 1
                magnumber = 0
                mag.append("bullet"+str(bulletnumber)) 
                break
            else:
                for i in amount_of_turtles:
                    if (x == invaderplace[i].xcor()):
                        if (y == invaderplace[i].ycor()):
                            bullet.hideturtle()
                            bulletnumber += 1
                            magnumber = 0
                            mag.append("bullet"+str(bulletnumber))
                            invaderplace[i].hideturtle()
                            amount_of_turtles.remove(i)
                            check += 1
                            win_condition -= 1
                            if (win_condition == 0):
                                winloss.color("green")
                                winloss.write("YOU'VE WON", font=("Arial", 20, "bold"))
                            break
            if (check == 1):
                break
            wn.update()
        movement()











#player movement
def left():
    global place
    
    x = player.xcor()
    if (x > -200):
        x -= 50
        player.goto(x,-230)
        place -= 1
def right():
    global place
    
    x = player.xcor()
    if (x < 200):
        x += 50
        player.goto(x,-230)
        place += 1


wn.onkeypress(right, "d")
wn.onkeypress(left, "a")
wn.onkeypress(initiate, "w")




wn.listen()
wn.mainloop()