# layer 0: Background Objects
# layer 1: Foreground Objects\
world = [[], [], []]
def add_object(o, depth): # 객체 담기
    world[depth].append(o)

def update(): # 월드에 있는거 몽땅 업데이트
    for layer in world:
        for o in layer:
            o.update()

def render(): # 몽땅 그리기
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('Cannot delete non existing object')