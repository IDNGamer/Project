
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Buat tanah
for z in range(20):
    for x in range(20):
        block = Button(
            parent=scene,
            model='cube',
            color=color.green,
            texture='white_cube',
            position=(x,0,z),
            origin_y=0.5,
            scale=1
        )

        # Tambah event saat blok diklik
        def input(key):
            if key == 'left mouse down' and mouse.hovered_entity == block:
                destroy(mouse.hovered_entity)
            if key == 'right mouse down' and mouse.hovered_entity:
                new_block = Button(
                    parent=scene,
                    model='cube',
                    color=color.gray,
                    texture='white_cube',
                    position=mouse.hovered_entity.position + mouse.normal,
                    origin_y=0.5,
                    scale=1
                )

# Pemain (kamera + kontrol)
player = FirstPersonController()
player.gravity = 0  # Nonaktifkan gravitasi agar mirip Minecraft creative mode

app.run()
