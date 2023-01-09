# -*- coding: utf-8 -*-
#-----------------------------------------------------
# UNTITLED
#-----------------------------------------------------
def t000004090_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000004090_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000004090_1000():
    """State 0,2,3"""
    assert t000004090_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000004090_2000():
    """State 0,2,3"""
    assert t000004090_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000004090_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6210:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t000004090_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t000004090_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004090_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000004090_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000004090_x1()
    else:
        """State 4,7"""
        call = t000004090_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000004090_x1()
    """State 9"""
    return 0

def t000004090_x4():
    """State 0,1"""
    assert t000004090_x1()
    """State 2"""
    return 0

def t000004090_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000004090_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000004090_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000004090_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000004090_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000004090_x13(val1=val1, z1=z1)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t000004090_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000004090_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000004090_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000004090_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000004090_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000004090_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000004090_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000004090_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000004090_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004090_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000004090_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000004090_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000004090_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004090_x10(z6=_, val6=_):
    """State 0,1"""
    if f203(z6) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z6)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t000004090_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000004090_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000004090_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004090_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000004090_x12():
    """State 0,1"""
    assert t000004090_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000004090_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000004090_x23()
    """State 1"""
    call = t000004090_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000004090_x25()
    """State 4"""
    return 0

def t000004090_x14():
    """State 0,1"""
    assert t000004090_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000004090_x15(val5=30):
    """State 0,1"""
    call = t000004090_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000004090_x26()
    """State 3"""
    return 0

def t000004090_x16():
    """State 0,1"""
    assert t000004090_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000004090_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000004090_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000004090_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000004090_x28()
    """Unused"""
    """State 6"""
    return 0

def t000004090_x18():
    """State 0,2"""
    call = t000004090_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000004090_x19():
    """State 0,1"""
    assert t000004090_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000004090_x20():
    """State 0,1"""
    assert t000004090_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000004090_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000004090_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000004090_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000004090_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000004090_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000004090_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000004090_x23():
    """State 0,1"""
    assert t000004090_x24()
    """State 2"""
    return 0

def t000004090_x24():
    """State 0,1"""
    assert t000004090_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000004090_x25():
    """State 0,1"""
    call = t000004090_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000004090_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004090_x26():
    """State 0,1"""
    call = t000004090_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000004090_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004090_x27():
    """State 0,1"""
    call = t000004090_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000004090_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004090_x28():
    """State 0,1"""
    call = t000004090_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000004090_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004090_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000004090_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text2, -1, -1, 0)
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 3"""
    if not mode4:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t000004090_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000004090_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 2"""
    SetEventFlag(z5, 1)
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 4"""
    if not mode3:
        pass
    else:
        """State 3"""
        ReportConversationEndToHavokBehavior()
    """State 6"""
    return 0

def t000004090_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004090_x32():
    """State 0,1"""
    assert t000004090_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000004090_x33():
    """State 0,1"""
    assert t000004090_x1()
    """State 2"""
    return 0

def t000004090_x34():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t000004090_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000004090_x100()
    """State 9"""
    return 0

def t000004090_x36():
    """State 0,1"""
    assert t000004090_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

#----------------------------------------------------
# Gauntlet Music
#----------------------------------------------------
def t000004090_x100():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Purchase Items
        AddTalkListData(1, 80105450, -1)
        
        # Gauntlet Msuic
        AddTalkListData(2, 80105451, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            OpenRegularShop(8000000, 8000999)
            assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2:
            assert t000004090_x101()
            continue
        else:
            """State 6,8"""
            return 0
            
# Music
def t000004090_x101():
    while True:
        ClearTalkListData()
        c1_110()
        
        # None
        AddTalkListDataIf(GetEventFlag(1047610350) == 0, 1, 80105500, -1)
        # None (selected)
        AddTalkListDataIf(GetEventFlag(1047610350) == 1, 50, 80105600, -1)
        
        # Godfrey, First Elden Lord
        AddTalkListDataIf(GetEventFlag(1047610351) == 0, 2, 80105501, -1)
        # Godfrey, First Elden Lord (selected)
        AddTalkListDataIf(GetEventFlag(1047610351) == 1, 51, 80105601, -1)
        
        # Grafted Scion
        AddTalkListDataIf(GetEventFlag(1047610352) == 0, 3, 80105502, -1)
        # Grafted Scion (selected)
        AddTalkListDataIf(GetEventFlag(1047610352) == 1, 52, 80105602, -1)
        
        # Margit, the Fell Omen
        AddTalkListDataIf(GetEventFlag(1047610353) == 0, 4, 80105503, -1)
        # Margit, the Fell Omen (selected)
        AddTalkListDataIf(GetEventFlag(1047610353) == 1, 53, 80105603, -1)
        
        # Rennala, Queen of the Full Moon
        AddTalkListDataIf(GetEventFlag(1047610354) == 0, 5, 80105504, -1)
        # Rennala, Queen of the Full Moon (selected)
        AddTalkListDataIf(GetEventFlag(1047610354) == 1, 54, 80105604, -1)
        
        # Red Wolf of Radagon
        AddTalkListDataIf(GetEventFlag(1047610355) == 0, 6, 80105505, -1)
        # Red Wolf of Radagon (selected)
        AddTalkListDataIf(GetEventFlag(1047610355) == 1, 55, 80105605, -1)
        
        # Rykard, Lord of Blasphemy
        AddTalkListDataIf(GetEventFlag(1047610356) == 0, 7, 80105506, -1)
        # Rykard, Lord of Blasphemy (selected)
        AddTalkListDataIf(GetEventFlag(1047610356) == 1, 56, 80105606, -1)
        
        # Godskin Noble
        AddTalkListDataIf(GetEventFlag(1047610357) == 0, 8, 80105507, -1)
        # Godskin Noble (selected)
        AddTalkListDataIf(GetEventFlag(1047610357) == 1, 57, 80105607, -1)
        
        # Abductor Virgins
        AddTalkListDataIf(GetEventFlag(1047610358) == 0, 9, 80105508, -1)
        # Abductor Virgins (selected)
        AddTalkListDataIf(GetEventFlag(1047610358) == 1, 58, 80105608, -1)
        
        # Starscourge Radahn
        AddTalkListDataIf(GetEventFlag(1047610359) == 0, 10, 80105509, -1)
        # Starscourge Radahn (selected)
        AddTalkListDataIf(GetEventFlag(1047610359) == 1, 59, 80105609, -1)
        
        # Morgott, the Omen King
        AddTalkListDataIf(GetEventFlag(1047610360) == 0, 11, 80105510, -1)
        # Morgott, the Omen King (selected)
        AddTalkListDataIf(GetEventFlag(1047610360) == 1, 60, 80105610, -1)
        
        # Ancestor Spirit
        AddTalkListDataIf(GetEventFlag(1047610361) == 0, 12, 80105511, -1)
        # Ancestor Spirit (selected)
        AddTalkListDataIf(GetEventFlag(1047610361) == 1, 61, 80105611, -1)
        
        # Dragonkin Soldier of Nokstella
        AddTalkListDataIf(GetEventFlag(1047610362) == 0, 13, 80105512, -1)
        # Dragonkin Soldier of Nokstella (selected)
        AddTalkListDataIf(GetEventFlag(1047610362) == 1, 62, 80105612, -1)
        
        # Astel, Naturalborn of the Void
        AddTalkListDataIf(GetEventFlag(1047610363) == 0, 14, 80105513, -1)
        # Astel, Naturalborn of the Void (selected)
        AddTalkListDataIf(GetEventFlag(1047610363) == 1, 63, 80105613, -1)
        
        # Mohg, Lord of Blood
        AddTalkListDataIf(GetEventFlag(1047610364) == 0, 15, 80105514, -1)
        # Mohg, Lord of Blood (selected)
        AddTalkListDataIf(GetEventFlag(1047610364) == 1, 64, 80105614, -1)
        
        # Fire Giant
        AddTalkListDataIf(GetEventFlag(1047610365) == 0, 16, 80105515, -1)
        # Fire Giant (selected)
        AddTalkListDataIf(GetEventFlag(1047610365) == 1, 65, 80105615, -1)
        
        # Hoarah Loux
        AddTalkListDataIf(GetEventFlag(1047610366) == 0, 17, 80105516, -1)
        # Hoarah Loux (selected)
        AddTalkListDataIf(GetEventFlag(1047610366) == 1, 66, 80105616, -1)
        
        # Sir Gideon Ofnir
        AddTalkListDataIf(GetEventFlag(1047610367) == 0, 18, 80105517, -1)
        # Sir Gideon Ofnir (selected)
        AddTalkListDataIf(GetEventFlag(1047610367) == 1, 67, 80105617, -1)
        
        # Maliketh, The Black Blade
        AddTalkListDataIf(GetEventFlag(1047610368) == 0, 19, 80105518, -1)
        #Maliketh, The Black Blade (selected)
        AddTalkListDataIf(GetEventFlag(1047610368) == 1, 68, 80105618, -1)
        
        # Dragonlord Placidusax
        AddTalkListDataIf(GetEventFlag(1047610369) == 0, 20, 80105519, -1)
        # Dragonlord Placidusax (selected)
        AddTalkListDataIf(GetEventFlag(1047610369) == 1, 69, 80105619, -1)
        
        # Malenia, Blade of Miquella
        AddTalkListDataIf(GetEventFlag(1047610370) == 0, 21, 80105520, -1)
        # Malenia, Blade of Miquella (selected)
        AddTalkListDataIf(GetEventFlag(1047610370) == 1, 70, 80105620, -1)
        
        # Loretta, Knight of the Haligtree
        AddTalkListDataIf(GetEventFlag(1047610371) == 0, 22, 80105521, -1)
        # Loretta, Knight of the Haligtree (selected)
        AddTalkListDataIf(GetEventFlag(1047610371) == 1, 71, 80105621, -1)
        
        # Radagon of the Golden Order
        AddTalkListDataIf(GetEventFlag(1047610372) == 0, 23, 80105522, -1)
        # Radagon of the Golden Order (selected)
        AddTalkListDataIf(GetEventFlag(1047610372) == 1, 72, 80105622, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004090_x111(1047610350)
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t000004090_x111(1047610351)
            return 0
        elif GetTalkListEntryResult() == 3:
            assert t000004090_x111(1047610352)
            return 0
        elif GetTalkListEntryResult() == 4:
            assert t000004090_x111(1047610353)
            return 0
        elif GetTalkListEntryResult() == 5:
            assert t000004090_x111(1047610354)
            return 0
        elif GetTalkListEntryResult() == 6:
            assert t000004090_x111(1047610355)
            return 0
        elif GetTalkListEntryResult() == 7:
            assert t000004090_x111(1047610356)
            return 0
        elif GetTalkListEntryResult() == 8:
            assert t000004090_x111(1047610357)
            return 0
        elif GetTalkListEntryResult() == 9:
            assert t000004090_x111(1047610358)
            return 0
        elif GetTalkListEntryResult() == 10:
            assert t000004090_x111(1047610359)
            return 0
        elif GetTalkListEntryResult() == 11:
            assert t000004090_x111(1047610360)
            return 0
        elif GetTalkListEntryResult() == 12:
            assert t000004090_x111(1047610361)
            return 0
        elif GetTalkListEntryResult() == 13:
            assert t000004090_x111(1047610362)
            return 0
        elif GetTalkListEntryResult() == 14:
            assert t000004090_x111(1047610363)
            return 0
        elif GetTalkListEntryResult() == 15:
            assert t000004090_x111(1047610364)
            return 0
        elif GetTalkListEntryResult() == 16:
            assert t000004090_x111(1047610365)
            return 0
        elif GetTalkListEntryResult() == 17:
            assert t000004090_x111(1047610366)
            return 0
        elif GetTalkListEntryResult() == 18:
            assert t000004090_x111(1047610367)
            return 0
        elif GetTalkListEntryResult() == 19:
            assert t000004090_x111(1047610368)
            return 0
        elif GetTalkListEntryResult() == 20:
            assert t000004090_x111(1047610369)
            return 0
        elif GetTalkListEntryResult() == 21:
            assert t000004090_x111(1047610370)
            return 0
        elif GetTalkListEntryResult() == 22:
            assert t000004090_x111(1047610371)
            return 0
        elif GetTalkListEntryResult() == 23:
            assert t000004090_x111(1047610372)
            return 0
        elif GetTalkListEntryResult() >= 50:
            return 0
        else:
            """State 6,8"""
            return 0

# Description Prompt
def t000004090_x110(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Set Theme
def t000004090_x111(flag=_):
    assert t000004090_x110(80105700)
            
    SetEventFlag(1047610350, 0)
    SetEventFlag(1047610351, 0)
    SetEventFlag(1047610352, 0)
    SetEventFlag(1047610353, 0)
    SetEventFlag(1047610354, 0)
    SetEventFlag(1047610355, 0)
    SetEventFlag(1047610356, 0)
    SetEventFlag(1047610357, 0)
    SetEventFlag(1047610358, 0)
    SetEventFlag(1047610359, 0)
    SetEventFlag(1047610360, 0)
    SetEventFlag(1047610361, 0)
    SetEventFlag(1047610362, 0)
    SetEventFlag(1047610363, 0)
    SetEventFlag(1047610364, 0)
    SetEventFlag(1047610365, 0)
    SetEventFlag(1047610366, 0)
    SetEventFlag(1047610367, 0)
    SetEventFlag(1047610368, 0)
    SetEventFlag(1047610369, 0)
    SetEventFlag(1047610370, 0)
    SetEventFlag(1047610371, 0)
    SetEventFlag(1047610372, 0)
    
    SetEventFlag(flag, 1)
    
    return 0
    