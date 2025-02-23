# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

class Cube:
    def __init__(self, name):
        self.name  = name
        self.translate = [0, 0, 0]
        self.rotate    = [0, 0, 0]
        self.scale     = [0, 0, 0]
        self.color     = [0, 0, 0]
    
    def print_status(self):
        print("{} : {} : {} : {} : {}".format(self.name, self.translate, self.rotate , self.scale , self.color))


    def update_transform(self, ttype, value = [0, 0 ,0]):
        
        if len(value) < 3:
            sublime.error_message("value missing")
            return

        match ttype:
            case "translate":
                self.translate = value

            case "rotate":
                self.rotate = value

            case "scale":
                self.scale = value

            case _:
                sublime.error_message("transform type insert isn't valid")


class AdvancedCube(Cube):
    def __init__(self, name, translate, rotate, scale):
        self.name      = name
        self.translate = translate
        self.rotate    = rotate
        self.scale     = scale

    def print_status():
        print("{} : {} : {} : {} : {}".format(self.name, self.translate, self.rotate , self.scale , self.color))


cube1 = Cube("blue")

cube1.print_status()

cube1.update_transform("rotate", [0, 4, 3])

cube1.print_status()