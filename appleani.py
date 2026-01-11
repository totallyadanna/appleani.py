import pgzrun

HEIGHT = 500
WIDTH = 800
TITLE = "Apple Animation"

appleimage = Actor("apple.png")
appleimage.pos = (100,100)

def startAnimation():
    animate(appleimage, pos = (100,150), duration = 3)

def draw():
    screen.clear()
    appleimage.draw()

def on_key_down(key):
    if key == keys.SPACE:
        startAnimation()
    

pgzrun.go()
