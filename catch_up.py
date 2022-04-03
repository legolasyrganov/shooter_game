from pygame import *
#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
#задай фон сцены
background = transform.scale(image.load("background.png"),    (700, 500))
sprite1 = transform.scale(image.load('sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load('sprite2.png'), (100, 100))

x1 = 100
y1 = 200

x2 = 200
y2 = 200


clock = time.Clock()
FPS = 60


game = True
while game:
    window.blit(background,(0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    key_pressed = key.get_pressed()
    if key_pressed[K_UP]:
        y1-=10
    if key_pressed[K_DOWN]:
        y1+=10
    if key_pressed[K_LEFT]:
        x1-=10
    if key_pressed[K_RIGHT]:
        x1+=10

    if key_pressed[K_w]:
        y2-=10
    if key_pressed[K_s]:
        y2+=10
    if key_pressed[K_a]:
        x2-=10
    if key_pressed[K_d]:
        x2+=10
        



    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False




    display.update()
    clock.tick(FPS)


#создай 2 спрайта и размести их на сцене

