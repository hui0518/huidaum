GlowScript 2.7 VPython
# object 생성
white = sphere(pos = vector(-10, 1.25, 0), radius = 1, color = color.white)
floor = box(length = 30, height = 0.5, width = 3, color = color.green)

#버튼이벤트
ev = scene.waitfor('click keydown')
dt = 0.01

#
#튕길때 땅을 기어가는 오류로 인해 한번 튕길때마다 for문을 이용하여 구현.
#
white.velocity = vector(10,10,0)
while True :
    rate(100)
    e = 0.7
    white.pos = white.pos + white.velocity * dt
    white.velocity.y = white.velocity.y + -9.8 * dt
    if white.pos.y <= 1.25 :
        white.velocity.y = -white.velocity.y * e
        break
    

for i in range(100):
    rate(100)
    e = 0.7
    white.pos = white.pos + white.velocity * dt
    white.velocity.y = white.velocity.y + -9.8 * dt
    

        
while True :
    rate(100)
    e = 0.7
    white.pos = white.pos + white.velocity * dt
    white.velocity.y = white.velocity.y + -9.8 * dt
    if white.pos.y <= 1.25 :
        white.velocity.y = -white.velocity.y * e
        break
    
for i in range(100):
    rate(100)
    e = 0.7
    white.pos = white.pos + white.velocity * dt
    white.velocity.y = white.velocity.y + -9.8 * dt
    

        
while True :
    rate(100)
    e = 0.7
    white.pos = white.pos + white.velocity * dt
    white.velocity.y = white.velocity.y + -9.8 * dt
    if white.pos.y <= 0.75 :
        white.velocity.y = -white.velocity.y * e
        break
