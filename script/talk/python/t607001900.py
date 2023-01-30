# -*- coding: utf-8 -*-
def t607001900_1():
    """State 0,1"""
    t607001900_x4()
    Quit()

def t607001900_x0(actionbutton1=6310, flag1=19001100, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                  flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag1) == 1 or GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1 or GetEventFlag(flag4)
                == 1 or GetEventFlag(flag5) == 1)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if GetEventFlag(flag6) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not
              GetEventFlag(flag4) and not GetEventFlag(flag5)):
            pass
        # actionbutton:6310:"Touch Fractured Marika"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t607001900_x1():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t607001900_x2():
    """State 0"""
    while True:
        """State 2"""
        call = t607001900_x6()
        assert GetDistanceToPlayer() > 5.1
        """State 3"""
        assert t607001900_x1()
        """State 1"""
        assert GetDistanceToPlayer() < 5
    """Unused"""
    """State 4"""
    return 0

def t607001900_x3():
    """State 0"""
    while True:
        """State 2"""
        call = t607001900_x2()
        assert (GetEventFlag(108) == 1 and not GetEventFlag(116)) or not GetEventFlag(19001100)
        """State 1"""
        assert (not GetEventFlag(108) or GetEventFlag(116) == 1) and GetEventFlag(19001100) == 1
    """Unused"""
    """State 3"""
    return 0

def t607001900_x4():
    """State 0"""
    while True:
        """State 2"""
        call = t607001900_x3()
        assert IsClientPlayer() == 1
        """State 1"""
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t607001900_x5():
    """State 0,1"""
    ClearTalkListData()
    c1_110()
    """State 2"""
    
    # Challenge the Greater Will
    AddTalkListDataIf(GetEventFlag(19000800) == 0, 5, 26071004, -1)
    
    # action:26071000:"Mend the Elden Ring"
    AddTalkListData(1, 26071000, -1)
    
    # eventflag:9500:lot:4900:Mending Rune of Perfect Order, action:26071001:"Use Mending Rune of Perfect Order"
    AddTalkListDataIf(GetEventFlag(9500) == 1, 2, 26071001, -1)
    # eventflag:9502:lot:4910:Mending Rune of the Death-Prince, action:26071002:"Use Mending Rune of the Death-Prince"
    AddTalkListDataIf(GetEventFlag(9502) == 1, 3, 26071002, -1)
    # eventflag:9504:lot:4920:Mending Rune of the Fell Curse, action:26071003:"Use Mending Rune of the Fell Curse"
    AddTalkListDataIf(GetEventFlag(9504) == 1, 4, 26071003, -1)
    """State 3"""
    OpenConversationChoicesMenu(0)
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 12"""
    if GetTalkListEntryResult() == 1:
        """State 4,8"""
        SetEventFlag(9400, 1)
    elif GetTalkListEntryResult() == 2:
        """State 5,9"""
        SetEventFlag(9401, 1)
    elif GetTalkListEntryResult() == 3:
        """State 7,10"""
        SetEventFlag(9402, 1)
    elif GetTalkListEntryResult() == 4:
        """State 6,11"""
        SetEventFlag(9403, 1)
    elif GetTalkListEntryResult() == 5:
        SetEventFlag(1047610015, 1)
    else:
        """State 13"""
        pass
    """State 14"""
    return 0

def t607001900_x6():
    """State 0"""
    while True:
        """State 2"""
        if not GetEventFlag(9400) and not GetEventFlag(9401) and not GetEventFlag(9402) and not GetEventFlag(9403):
            """State 3"""
            # actionbutton:6310:"Touch Fractured Marika"
            assert (t607001900_x0(actionbutton1=6310, flag1=19001100, flag2=6000, flag3=6000, flag4=6000,
                    flag5=6000, flag6=6000))
            """State 4"""
            assert t607001900_x5()
        else:
            """State 1"""
            Quit()
    """Unused"""
    """State 5"""
    return 0

