#def setup():
 #   size (720,1080)
#def draw():
 #   background(0,0,0)
  #  for i in range(0,720,200):
   #    ellipse(i,i,5,5)
stars_x = [50, 100, 150,200,250,300,350,400,450,500,550,600,700]
stars_y = [200, 250, 300,350,400,450,500,550,600,650,700]

def setup():
    size(640, 480)


def draw():
    stars_x_choose =int(random(1,11))
    stars_y_choose =int(random(1,11))
    background(0)
    # draw stars
    
    ellipse(stars_x[stars_x_choose], stars_y[stars_y_choose], 5, 5)
    ellipse(stars_x[stars_x_choose], stars_y[stars_y_choose], 5, 5)
    ellipse(stars_x[stars_x_choose], stars_y[stars_y_choose], 5, 5)
