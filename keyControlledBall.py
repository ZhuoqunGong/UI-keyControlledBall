import eventBasedAnimation

def keyDemoInitFn(data):
    (data.x, data.y) = (data.width/2, data.height/2)
    data.speed = 10
    data.aboutText = data.windowTitle = "key Controlled Ball (use arrows to move ball)"

def keyDemoKeyFn(event, data):
    if (event.keysym == "Up"):      data.y -= data.speed
    elif (event.keysym == "Down"):  data.y += data.speed
    elif (event.keysym == "Left"):  data.x -= data.speed
    elif (event.keysym == "Right"): data.x += data.speed

def keyDemoDrawFn(canvas, data):
    (cx, cy, r) = (data.x, data.y, 20)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="Blue")

eventBasedAnimation.run(
    initFn=keyDemoInitFn,
    keyFn=keyDemoKeyFn,
    drawFn=keyDemoDrawFn,
    width=500,
    height=500
    )