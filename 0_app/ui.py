import os
import sys
import webbrowser

import maya.cmds as cmds
from Qt import QtWidgets, QtGui, QtCore, QtCompat


sys.path.append("C:/Users/Zakkyo/Desktop/class/advanced/0_app")

import autorig

#*************************************************************
# VARIABLES
TITLE = os.path.splitext(os.path.basename(__file__))[0]
CURRENT_PATH = os.path.dirname(__file__)
IMG_PATH = CURRENT_PATH + "/img/{}.png"

#*************************************************************
#CLASS
class ARig:

    def __init__(self):
        path_ui = CURRENT_PATH + "/" + TITLE + ".ui"
        self.wgRig = QtCompat.loadUI(path_ui)

        #self.wgRig.mainImmage.
        self.wgRig.show()

        #SIGNAL
        self.wgRig.btnCreateLoc.clicked.connect(self.press_btnCreateLoc)
        self.wgRig.btnBuildSkeleton.clicked.connect(self.press_btnBuildSkeleton)
        self.wgRig.btnSelectSkinJoint.clicked.connect(self.press_btnSelectSkinJoint)
        #*************************************************************
        #PRESS
        def press_btnCreateLoc(self):
            autorig.create_pos_locator()

        def press_btnBuildSkeleton(self):
            autorig.auto_rigger()

        def btnSelectSkinJoint(self):
            autorig.select_skin_jnt()


#*************************************************************
#START UI
if __name__ == "__main__":
    app = QtWidgets.QApplications(sys.argv)
    aRig()
    app.exec_()