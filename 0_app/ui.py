import os

import maya.cmds as cmds


import sys
sys.path.append("C:/Users/Zakkyo/Desktop/class/w8")

import autorig

def arm_auto_rigger():
    
    ui_title = "auto_rigger"

    if cmds.window(ui_title, exists=True):
        print("CLOSE duplicate window")
        cmds.deleteUI(ui_title)

    window = cmds.window(ui_title, title="Auto Rigger",width=300)

    cmds.columnLayout(adjustableColumn=True)

    cmds.rowLayout(numberOfColumns=1)

    cmds.text(label="Auto Rigger", width=300, height=30)
    
    cmds.setParent("..")
    cmds.rowLayout(numberOfColumns=1)

    cmds.button(label="CreatePosLocator",
                annotation="Create locator to position on shoulder/elb/wrist",
                width= 300, command = "autorig.create_pos_locator()")
    
    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1)

    cmds.text(label="", width=300, height=30)

    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1)

    cmds.button(label="SetupRig",
                annotation="Create Joint chain on the  position of shoulder/elb/wrist locator",
                width= 300, command = "autorig.auto_rigger()")

    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1)

    cmds.text(label="click the select skin jnt" , width=300, height=30)

    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1)

    cmds.button(label="Select Skin Joint",
                annotation="Select the joint to skin",
                width= 300, command = "autorig.select_skin_jnt()")

    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=1)

    cmds.text(label="now add select the mesh you want to skin", width=300, height=30)

    cmds.showWindow(window)


class baseUi