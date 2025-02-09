# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************


# COMMENT --------------------------------------------------
# Not optimal
def set_color(ctrl_list=None, color=None):

    for ctrl_name in ctrl_list:
        try:
            mc.setAttr(ctrl_name + 'Shape.overrideEnabled', 1)
        except:
            pass

        
        if color == 1:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 4)
        elif color == 2:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 13)
        elif color == 3:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 25)
        elif color == 4:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 17)
        elif color == 5:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 17)
        elif color == 6:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 15)
        elif color == 7:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 6)
        elif color == 8:
            mc.setAttr(ctrl_name + 'Shape.overrideColor', 16)
        else:
            pass


# EXAMPLE
# set_color(['circle','circle1'], 8)
