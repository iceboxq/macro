import pywinmacro as pw
import time

def aa():
    position = pw.get_mouse_position()
    print("Mouse Position is " + str(position))
    print("Color in hex is " + str(pw.get_color(position)))
