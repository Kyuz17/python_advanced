"""import maya.cmds as cmds
import maya.mel as mel


def create_move_locator(tx, ty, tz, naming):
    locator = cmds.spaceLocator(n = naming)[0]
    cmds.setAttr(locator + ".translateX", tx)
    cmds.setAttr(locator + ".translateY", ty)
    cmds.setAttr(locator + ".translateZ", tz)

def create_pos_locator():
    create_move_locator( 0, 10, 0, naming = "should_pos_loc" )
    create_move_locator( 3, 7, 0, naming = "elbow_pos_loc" )
    create_move_locator( 5, 5, 0, naming = "wrist_pos_loc" )
    cmds.group( em=True, name='loc_scale_grp' )
    position_locators = cmds.ls("*pos_loc",type = "transform")
    for locator in position_locators:
        cmds.parent(locator ,"loc_scale_grp" , a = True)

def right_side_jnt():
    position_locators = cmds.ls("*pos_loc",type = "transform")
    for locator in position_locators:
        loc_tx = cmds.getAttr(locator + ".translateX") * (-1)
        loc_ty = cmds.getAttr(locator + ".translateY") * (-1)
        loc_tz = cmds.getAttr(locator + ".translateZ") * (-1)
        l_loc_name = locator.replace("l_", "r_")
        create_move_locator(loc_tx, loc_ty, loc_tz, l_loc_name)


def orientJoint(extention):
    cmds.select("*_" + str(extention))
    mel.eval("joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso")
    cmds.select("*wrist_" + str(extention))
    mel.eval("joint -e  -oj none -ch -zso")

def create_circle_x_axis(naming):
    ctrl = cmds.circle(n = naming)[0]
    cmds.setAttr(ctrl + ".rotateY", 90)
    cmds.makeIdentity(ctrl, apply=True, t=True, r=True, s=True)
    return ctrl

def parent_groups(naming):   
    cmds.parent("wrist_" + str(naming) + "_grp" , "elbow_" + str(naming) + "_ctrl")
    cmds.parent("elbow_" + str(naming) + "_grp" , "should_" + str(naming) + "_ctrl")

def group_offset(obj):
    ikfk = cmds.ls("ikfk_ctrl")[0]
    grp_name = ikfk.replace("ctrl", "grp")
    off_name = ikfk.replace("ctrl", "off")
    off_grp = cmds.group( em=True, name = off_name)
    grp_grp = cmds.group( em=True, name = grp_name)
    cmds.parentConstraint(ikfk, off_grp, maintainOffset = False)
    cmds.parentConstraint(ikfk, grp_grp, maintainOffset = False)
    cmds.delete(str(off_grp) + "_parent*")
    cmds.delete(str(grp_grp) + "_parent*")
    cmds.parent(ikfk, off_grp)
    cmds.parent(off_grp, grp_grp)

def lock_translate(obj):
    cmds.setAttr(obj + '.translateX', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.translateY', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.translateZ', lock=1, keyable = False, channelBox = False)

def lock_scale(obj):
    cmds.setAttr(obj + '.scaleX', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.scaleY', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.scaleZ', lock=1, keyable = False, channelBox = False)


def select_skin_jnt():
    cmds.select("*skin_jnt")

def auto_rigger():

    #right_side_jnt()

    position_locators = cmds.ls("*pos_loc",type = "transform")

    for locator in position_locators:
        cmds.select(locator)
        jnt_name = locator.replace( "pos_loc", "skin_jnt")
        jnt = cmds.joint(n = jnt_name)
        cmds.parent(jnt , w = True, a = True)
        cmds.delete(locator)
        
    cmds.delete("loc_scale_grp")
        

    jnts = cmds.ls("*_jnt",type = "transform")

    for jnt in jnts:
        cmds.select(jnt)
        fk_name = jnt.replace("skin_jnt", "fk_jnt")
        fk_jnt = cmds.duplicate(n = fk_name)
        ik_name = jnt.replace("skin_jnt", "ik_jnt")
        fk_jnt = cmds.duplicate(n = ik_name)


    cmds.parent("wrist_skin_jnt", "elbow_skin_jnt")
    cmds.parent("elbow_skin_jnt", "should_skin_jnt")

    cmds.parent("wrist_fk_jnt", "elbow_fk_jnt")
    cmds.parent("elbow_fk_jnt", "should_fk_jnt")

    cmds.parent("wrist_ik_jnt", "elbow_ik_jnt")
    cmds.parent("elbow_ik_jnt", "should_ik_jnt")

    orientJoint("skin_jnt")
    orientJoint("fk_jnt")
    orientJoint("ik_jnt")

    jnts = cmds.ls("*k_jnt",type = "transform")


    for jnt in jnts:
        ctrl_name = jnt.replace("jnt", "ctrl")
        ctrl = create_circle_x_axis(ctrl_name)
        cmds.parentConstraint(jnt, ctrl, maintainOffset = False)
        cmds.delete(str(ctrl) + "_parent*")

    ctrls = cmds.ls("*_ctrl",type = "transform")

    for ctrl in ctrls:
        cmds.delete(ctrl, constructionHistory = True)
        cmds.setAttr(str(ctrl) + ".overrideEnabled", 1)
        if  "ik" in ctrl:   
            cmds.setAttr(str(ctrl) + ".overrideColor", 17)
        elif "fk" in ctrl:
            cmds.setAttr(str(ctrl) + ".overrideColor", 12)
        grp_name = ctrl.replace("ctrl", "grp")
        off_name = ctrl.replace("ctrl", "off")
        off_grp = cmds.group( em=True, name = off_name)
        grp_grp = cmds.group( em=True, name = grp_name)
        jnt = ctrl.replace("ctrl", "jnt")
        cmds.parentConstraint(ctrl, off_grp, maintainOffset = False)
        cmds.parentConstraint(ctrl, grp_grp, maintainOffset = False)
        cmds.delete(str(off_grp) + "_parent*")
        cmds.delete(str(grp_grp) + "_parent*")
        cmds.parent(ctrl, off_grp)
        cmds.parent(off_grp, grp_grp)
        cmds.parentConstraint(ctrl, jnt, maintainOffset = True)

    parent_groups("ik")
    parent_groups("fk")

    cmds.parentConstraint("should_fk_jnt", "should_ik_jnt", "should_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("elbow_fk_jnt", "elbow_ik_jnt", "elbow_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("wrist_fk_jnt", "wrist_ik_jnt", "wrist_skin_jnt", maintainOffset = True)


    ikfk_switch = cmds.circle(n = "ikfk_ctrl")[0]
    cmds.delete(ikfk_switch, constructionHistory = True)
    cmds.parentConstraint("should_ik_ctrl", ikfk_switch, maintainOffset = False)
    cmds.delete(str(ikfk_switch) + "_parent*")

    group_offset("ikfk_ctrl")



    cmds.addAttr("ikfk_ctrl", ln='IkFk', defaultValue=1.0, minValue=0, maxValue = 1, attributeType='float', keyable=True)
        
    cmds.createNode('reverse', name= "IkFkReverse")
    cmds.connectAttr("ikfk_ctrl" + ".IkFk" , "IkFkReverse" + ".input.inputX" )

    skin_jnts = cmds.ls("*skin_jnt")

    for skin_jnt in skin_jnts:
        jnt_part = skin_jnt.split("_")[0]
        cmds.connectAttr("ikfk_ctrl" + ".IkFk" , skin_jnt +"_parentConstraint1." + jnt_part + "_fk_jntW0" )
        cmds.connectAttr("IkFkReverse" + ".output.outputX" , skin_jnt + "_parentConstraint1."+ jnt_part + "_ik_jntW1" )

    cmds.connectAttr("ikfk_ctrl" + ".IkFk" , "should_fk_grp" + ".visibility" )
    cmds.connectAttr("IkFkReverse" + ".output.outputX", "should_ik_grp" + ".visibility")

    cmds.ikHandle( sj='should_ik_jnt', ee='wrist_ik_jnt')

    ctrls = cmds.ls("*_ctrl")

    for ctrl in ctrls :
        lock_scale(ctrl)
        if "fk" in ctrl:
            lock_translate(ctrl)


    cmds.setAttr("should_fk_jnt" + '.visibility', 0)
    cmds.setAttr("should_ik_jnt" + '.visibility', 0)
    cmds.connectAttr("IkFkReverse" + ".output.outputX", "ikHandle1" + ".visibility")

    mel.eval("cycleCheck -e off")"""


import maya.cmds as cmds
import maya.mel as mel


def create_move_locator(tx, ty, tz, naming):
    locator = cmds.spaceLocator(n = naming)[0]
    cmds.setAttr(locator + ".translateX", tx)
    cmds.setAttr(locator + ".translateY", ty)
    cmds.setAttr(locator + ".translateZ", tz)

def create_pos_locator():
    create_move_locator( 1, 10, 0, naming = "l_should_pos_loc" )
    create_move_locator( 3, 7, 0, naming = "l_elbow_pos_loc" )
    create_move_locator( 5, 5, 0, naming = "l_wrist_pos_loc" )
    cmds.group( em=True, name='loc_scale_grp' )
    position_locators = cmds.ls("*pos_loc",type = "transform")
    for locator in position_locators:
        cmds.parent(locator ,"loc_scale_grp" , a = True)

def orientJoint(extention):
    cmds.select("*_" + str(extention))
    mel.eval("joint -e  -oj xyz -secondaryAxisOrient yup -ch -zso")
    cmds.select("*wrist_" + str(extention))
    mel.eval("joint -e  -oj none -ch -zso")

def create_circle_x_axis(naming):
    ctrl = cmds.circle(n = naming)[0]
    cmds.setAttr(ctrl + ".rotateY", 90)
    cmds.makeIdentity(ctrl, apply=True, t=True, r=True, s=True)
    return ctrl

def parent_groups(named,side):   
    cmds.parent(str(side) + "wrist_" + str(named) + "_grp" , str(side) + "elbow_" + str(named) + "_ctrl")
    cmds.parent(str(side) + "elbow_" + str(named) + "_grp" , str(side) + "should_" + str(named) + "_ctrl")

def group_offset(obj):
    ikfk = cmds.ls("ikfk_ctrl")[0]
    grp_name = ikfk.replace("ctrl", "grp")
    off_name = ikfk.replace("ctrl", "off")
    off_grp = cmds.group( em=True, name = off_name)
    grp_grp = cmds.group( em=True, name = grp_name)
    cmds.parentConstraint(ikfk, off_grp, maintainOffset = False)
    cmds.parentConstraint(ikfk, grp_grp, maintainOffset = False)
    cmds.delete(str(off_grp) + "_parent*")
    cmds.delete(str(grp_grp) + "_parent*")
    cmds.parent(ikfk, off_grp)
    cmds.parent(off_grp, grp_grp)

def lock_translate(obj):
    cmds.setAttr(obj + '.translateX', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.translateY', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.translateZ', lock=1, keyable = False, channelBox = False)

def lock_scale(obj):
    cmds.setAttr(obj + '.scaleX', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.scaleY', lock=1, keyable = False, channelBox = False)
    cmds.setAttr(obj + '.scaleZ', lock=1, keyable = False, channelBox = False)


def select_skin_jnt():
    cmds.select("*skin_jnt")

def auto_rigger():

    position_locators = cmds.ls("*pos_loc",type = "transform")

    for locator in position_locators:
        cmds.select(locator)
        jnt_name = locator.replace( "pos_loc", "skin_jnt")
        jnt = cmds.joint(n = jnt_name)
        cmds.parent(jnt , w = True, a = True)
        cmds.delete(locator)
        
    cmds.delete("loc_scale_grp")
        

    jnts = cmds.ls("*_jnt",type = "transform")

    for jnt in jnts:
        cmds.select(jnt)
        fk_name = jnt.replace("skin_jnt", "fk_jnt")
        fk_jnt = cmds.duplicate(n = fk_name)
        ik_name = jnt.replace("skin_jnt", "ik_jnt")
        fk_jnt = cmds.duplicate(n = ik_name)


    cmds.parent("l_wrist_skin_jnt", "l_elbow_skin_jnt")
    cmds.parent("l_elbow_skin_jnt", "l_should_skin_jnt")

    cmds.parent("l_wrist_fk_jnt", "l_elbow_fk_jnt")
    cmds.parent("l_elbow_fk_jnt", "l_should_fk_jnt")

    cmds.parent("l_wrist_ik_jnt", "l_elbow_ik_jnt")
    cmds.parent("l_elbow_ik_jnt", "l_should_ik_jnt")

    orientJoint("skin_jnt")
    orientJoint("fk_jnt")
    orientJoint("ik_jnt")

    jnts = cmds.ls("*k_jnt",type = "transform")


    for jnt in jnts:
        ctrl_name = jnt.replace("jnt", "ctrl")
        ctrl = create_circle_x_axis(ctrl_name)
        cmds.parentConstraint(str(jnt), str(ctrl), maintainOffset = False)
        cmds.delete(str(ctrl) + "_parent*")

    ctrls = cmds.ls("*_ctrl",type = "transform")

    for ctrl in ctrls:
        cmds.delete(ctrl, constructionHistory = True)
        cmds.setAttr(str(ctrl) + ".overrideEnabled", 1)
        if  "ik" in ctrl:   
            cmds.setAttr(str(ctrl) + ".overrideColor", 17)
        elif "fk" in ctrl:
            cmds.setAttr(str(ctrl) + ".overrideColor", 12)
        grp_name = ctrl.replace("ctrl", "grp")
        off_name = ctrl.replace("ctrl", "off")
        off_grp = cmds.group( em=True, name = off_name)
        grp_grp = cmds.group( em=True, name = grp_name)
        jnt = ctrl.replace("ctrl", "jnt")
        cmds.parentConstraint(ctrl, off_grp, maintainOffset = False)
        cmds.parentConstraint(ctrl, grp_grp, maintainOffset = False)
        cmds.delete(str(off_grp) + "_parent*")
        cmds.delete(str(grp_grp) + "_parent*")
        cmds.parent(ctrl, off_grp)
        cmds.parent(off_grp, grp_grp)
        cmds.parentConstraint(ctrl, jnt, maintainOffset = True)

    parent_groups("ik", "l_")
    parent_groups("fk", "l_")

    cmds.parentConstraint("l_should_fk_jnt", "l_should_ik_jnt", "l_should_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("l_elbow_fk_jnt", "l_elbow_ik_jnt", "l_elbow_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("l_wrist_fk_jnt", "l_wrist_ik_jnt", "l_wrist_skin_jnt", maintainOffset = True)


    ikfk_switch = cmds.circle(n = "l_ikfk_ctrl")[0]
    cmds.delete(ikfk_switch, constructionHistory = True)
    cmds.parentConstraint("l_should_ik_ctrl", ikfk_switch, maintainOffset = False)
    cmds.delete(str(ikfk_switch) + "_parent*")

    group_offset("l_ikfk_ctrl")



    cmds.addAttr("l_ikfk_ctrl", ln='L_IkFk', defaultValue=1.0, minValue=0, maxValue = 1, attributeType='float', keyable=True)
        
    cmds.createNode('reverse', name= "L_IkFkReverse")
    cmds.connectAttr("l_ikfk_ctrl" + ".L_IkFk" , "L_IkFkReverse" + ".input.inputX" )

    skin_jnts = cmds.ls("*skin_jnt")

    for skin_jnt in skin_jnts:
        jnt_part = skin_jnt.split("_")[1]
        cmds.connectAttr("l_ikfk_ctrl" + ".L_IkFk" , skin_jnt +"_parentConstraint1.l_" + jnt_part + "_fk_jntW0" )
        cmds.connectAttr("L_IkFkReverse" + ".output.outputX" , skin_jnt + "_parentConstraint1.l_"+ jnt_part + "_ik_jntW1" )

    cmds.connectAttr("ikfk_ctrl" + ".IkFk" , "l_should_fk_grp" + ".visibility" )
    cmds.connectAttr("IkFkReverse" + ".output.outputX", "l_should_ik_grp" + ".visibility")

    cmds.ikHandle( sj='l_should_ik_jnt', ee='l_wrist_ik_jnt')

    ctrls = cmds.ls("*_ctrl")

    for ctrl in ctrls :
        lock_scale(ctrl)
        if "fk" in ctrl:
            lock_translate(ctrl)


    cmds.setAttr("l_should_fk_jnt" + '.visibility', 0)
    cmds.setAttr("l_should_ik_jnt" + '.visibility', 0)
    cmds.connectAttr("IkFkReverse" + ".output.outputX", "ikHandle1" + ".visibility")

    mel.eval("cycleCheck -e off")

    cmds.group( em=True, name='l_jnt_grp' )

    shoulder_jnts =cmds.ls("*_should*jnt",type = "transform")

    for should in shoulder_jnts:
        cmds.parent(str(should) ,"l_jnt_grp" , a = True)
        
    cmds.duplicate( "l_jnt_grp", n = "r_jnt_grp" )

    cmds.select("r_jnt_grp",  hi = True) 

    mel.eval("searchReplaceNames l_ r_ hierarchy")

    r_jnt_grp = cmds.ls( sl=True)


    for x in r_jnt_grp:
        if "parent" in x:
            cmds.delete(x)
        elif "effector" in x:
            cmds.delete(x)
            
    cmds.setAttr("r_jnt_grp" + ".scaleX", -1)

    jnts = cmds.ls("*r_*k_jnt",type = "transform")

    for jnt in jnts:
        ctrl_name = jnt.replace("jnt", "ctrl")
        ctrl = create_circle_x_axis(ctrl_name)
        cmds.parentConstraint(jnt, ctrl, maintainOffset = False)
        cmds.delete(str(ctrl) + "_parent*")

    ctrls = cmds.ls("r_*k_ctrl",type = "transform")

    for ctrl in ctrls:
        cmds.delete(ctrl, constructionHistory = True)
        cmds.setAttr(str(ctrl) + ".overrideEnabled", 1)
        if  "ik" in ctrl:   
            cmds.setAttr(str(ctrl) + ".overrideColor", 17)
        elif "fk" in ctrl:
            cmds.setAttr(str(ctrl) + ".overrideColor", 12)
        grp_name = ctrl.replace("ctrl", "grp")
        off_name = ctrl.replace("ctrl", "off")
        off_grp = cmds.group( em=True, name = off_name)
        grp_grp = cmds.group( em=True, name = grp_name)
        jnt = ctrl.replace("ctrl", "jnt")
        cmds.parentConstraint(ctrl, off_grp, maintainOffset = False)
        cmds.parentConstraint(ctrl, grp_grp, maintainOffset = False)
        cmds.delete(str(off_grp) + "_parent*")
        cmds.delete(str(grp_grp) + "_parent*")
        cmds.parent(ctrl, off_grp)
        cmds.parent(off_grp, grp_grp)
        cmds.parentConstraint(ctrl, jnt, maintainOffset = True)

    parent_groups("ik", "r_")
    parent_groups("fk", "r_")

    cmds.parentConstraint("r_should_fk_jnt", "r_should_ik_jnt", "r_should_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("r_elbow_fk_jnt", "r_elbow_ik_jnt", "r_elbow_skin_jnt", maintainOffset = True)
    cmds.parentConstraint("r_wrist_fk_jnt", "r_wrist_ik_jnt", "r_wrist_skin_jnt", maintainOffset = True)




    skin_jnts = cmds.ls("r_*skin_jnt")

    for skin_jnt in skin_jnts:
        jnt_part = skin_jnt.split("_")[0]
        cmds.connectAttr("ikfk_ctrl" + ".IkFk" , skin_jnt +"_parentConstraint1." + jnt_part + "_fk_jntW0" )
        cmds.connectAttr("IkFkReverse" + ".output.outputX" , skin_jnt + "_parentConstraint1."+ jnt_part + "_ik_jntW1" )

    cmds.connectAttr("ikfk_ctrl" + ".IkFk" , "r_should_fk_grp" + ".visibility" )
    cmds.connectAttr("IkFkReverse" + ".output.outputX", "r_should_ik_grp" + ".visibility")

    cmds.ikHandle( sj='r_should_ik_jnt', ee='r_wrist_ik_jnt')