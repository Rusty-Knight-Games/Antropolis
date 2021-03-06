import time
import random

import glfw
from OpenGL.GL import *

import ant
import block
import globals
import util

if __name__ == "__main__":
    if not glfw.init():
        print("Failed to load GLFW")

    window = glfw.create_window(640, 480, "Antropolis", None, None)
    if not window:
        glfw.terminate()

    glfw.make_context_current(window)

    ant_list = []
    # Make some default ants
    for i in range(1):
        ant_list.append(ant.Ant(f"ant {i}", random.randint(0, 6)))
    globals.ant_list = ant_list

    # TODO: Add the blocks to the map matrix
    for i in [(-0.32, -0.32),
              (-0.16, 0.18),
              (0.02, 0.18),
              (0.20, 0.18),
              (0.20, 0.02),
              (0.20, -0.32)]:
        ant_list.append(block.Block(i[0], i[1]))

    glViewport(0, 0, 640, 480)
    glShadeModel(GL_SMOOTH)

    glColor3f(0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    # TODO: It's supposed to be 3D
    # glOrtho(0.0, 640, 480, 0.0, -100.0, 100.0)
    glMatrixMode(GL_MODELVIEW)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glClearColor(0.25, 0.25, 0.25, 0)

        curr_time = time.time()
        for i in ant_list:
            # print(i)
            new_time = time.time()
            i.update(curr_time - new_time)
            curr_time = new_time

            i.render()

        util.draw_grid(640 // 16, 480 // 16)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()
