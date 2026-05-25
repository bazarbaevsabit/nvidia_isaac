import numpy as np

from isaacsim import SimulationApp
simulation_app = SimulationApp({"headless": False})  # start the simulation app, with GUI open

from isaacsim.core.api import World
from isaacsim.core.api.objects import VisualCuboid
from isaacsim.sensors.camera import Camera
import matplotlib.pyplot as plt
import numpy as np
import isaacsim.core.utils.numpy.rotations as rot_utils

my_world = World(stage_units_in_meters=1.0)
my_world.scene.add_default_ground_plane()  # add ground plane
print(11)
visual_cube = VisualCuboid(
    prim_path="/visual_cube",
    name="visual_cube",
    # Поставили куб на 2 метра впереди камеры (по оси X) и на высоту 1.0 метр
    position=np.array([2.0, 0.0, 1.0]), 
    size=0.3,
    color=np.array([255, 255, 0]),
)


print(22)
camera = Camera(
    prim_path="/World/camera",
    # Опустили камеру на высоту 1.5 метра и отодвинули назад на -3.0 метра по оси X
    position=np.array([-3.0, 0.0, 1.5]),
    frequency=20,
    resolution=(256, 256),
    # Повернули на 15 градусов вниз, чтобы она смотрела на куб перед собой
    orientation=rot_utils.euler_angles_to_quats(np.array([0, 15, 0]), degrees=True),
)

my_world.reset()
camera.initialize()
for _ in range(10):
    my_world.step(render=True)
print(33)
plt.imsave("camera_frame.png", camera.get_rgb())
print(44)
print("Кадр успешно сохранен в файл camera_frame.png")
print(55)

print("Симуляция завершена. Окно удерживается открытым. Нажмите Ctrl+C в терминале для выхода.")
while simulation_app.is_running():
    my_world.step(render=True)
simulation_app.close()
