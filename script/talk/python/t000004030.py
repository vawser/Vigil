# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Emissary of Mohgwyn
#-----------------------------------------------------
def t000004030_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000004030_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000004030_1000():
    """State 0,2,3"""
    assert t000004030_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000004030_2000():
    """State 0,2,3"""
    assert t000004030_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000004030_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t000004030_x1():
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

def t000004030_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004030_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000004030_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000004030_x1()
    else:
        """State 4,7"""
        call = t000004030_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000004030_x1()
    """State 9"""
    return 0

def t000004030_x4():
    """State 0,1"""
    assert t000004030_x1()
    """State 2"""
    return 0

def t000004030_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000004030_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000004030_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000004030_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000004030_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000004030_x13(val1=val1, z1=z1)
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
            call = t000004030_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000004030_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000004030_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000004030_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000004030_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000004030_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000004030_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000004030_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000004030_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004030_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000004030_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000004030_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000004030_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004030_x10(z6=_, val6=_):
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

def t000004030_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000004030_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000004030_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004030_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000004030_x12():
    """State 0,1"""
    assert t000004030_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000004030_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000004030_x23()
    """State 1"""
    call = t000004030_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000004030_x25()
    """State 4"""
    return 0

def t000004030_x14():
    """State 0,1"""
    assert t000004030_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000004030_x15(val5=30):
    """State 0,1"""
    call = t000004030_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000004030_x26()
    """State 3"""
    return 0

def t000004030_x16():
    """State 0,1"""
    assert t000004030_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000004030_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000004030_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000004030_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000004030_x28()
    """Unused"""
    """State 6"""
    return 0

def t000004030_x18():
    """State 0,2"""
    call = t000004030_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000004030_x19():
    """State 0,1"""
    assert t000004030_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000004030_x20():
    """State 0,1"""
    assert t000004030_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000004030_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000004030_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000004030_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000004030_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000004030_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000004030_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000004030_x23():
    """State 0,1"""
    assert t000004030_x24()
    """State 2"""
    return 0

def t000004030_x24():
    """State 0,1"""
    assert t000004030_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000004030_x25():
    """State 0,1"""
    call = t000004030_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000004030_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004030_x26():
    """State 0,1"""
    call = t000004030_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000004030_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004030_x27():
    """State 0,1"""
    call = t000004030_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000004030_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004030_x28():
    """State 0,1"""
    call = t000004030_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000004030_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004030_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000004030_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000004030_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000004030_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000004030_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004030_x32():
    """State 0,1"""
    assert t000004030_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000004030_x33():
    """State 0,1"""
    assert t000004030_x1()
    """State 2"""
    return 0

def t000004030_x34():
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

def t000004030_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000004030_x100()
    """State 9"""
    return 0

def t000004030_x36():
    """State 0,1"""
    assert t000004030_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

#----------------------------------------------------
# Menu
#----------------------------------------------------
def t000004030_x100():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Forge with Blood
        AddTalkListData(1, 89100000, -1)
        
        # Player Castigations
        AddTalkListData(2, 89100020, -1)
        
        # Enemy Castigations
        AddTalkListData(3, 89100021, -1)
        
        # Combat Castigations
        AddTalkListData(4, 89100022, -1)
        
        # Fun Castigations
        AddTalkListData(5, 89100023, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Bloodforge
        if GetTalkListEntryResult() == 1:
            OpenChampionsEquipmentShop(9010000, 9010999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Player Castigations
        elif GetTalkListEntryResult() == 2:
            assert t000004030_x101()
            continue
        # Enemy Castigations
        elif GetTalkListEntryResult() == 3:
            assert t000004030_x102()
            continue
        # Combat Castigations
        elif GetTalkListEntryResult() == 4:
            assert t000004030_x103()
            continue
        # Fun Castigations
        elif GetTalkListEntryResult() == 5:
            assert t000004030_x104()
            continue
        else:
            return 0
           
#----------------------------------------------------
# Castigations (Player)
#----------------------------------------------------
def t000004030_x101():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Bloodthirsty Maw
        AddTalkListDataIf(GetEventFlag(1047610907) == 0, 100, 89100107, -1)
        
        # Bloodthirsty Maw (selected)
        AddTalkListDataIf(GetEventFlag(1047610907) == 1, 200, 89100157, -1)

        # Fresh Meat
        AddTalkListDataIf(GetEventFlag(1047610912) == 0, 101, 89100112, -1)
        
        # Fresh Meat (selected)
        AddTalkListDataIf(GetEventFlag(1047610912) == 1, 201, 89100162, -1)
        
        # Corrupted Flasks
        AddTalkListDataIf(GetEventFlag(1047610913) == 0, 102, 89100113, -1)
        
        # Corrupted Flasks (selected)
        AddTalkListDataIf(GetEventFlag(1047610913) == 1, 202, 89100163, -1)
        
        # Brittle Bones
        AddTalkListDataIf(GetEventFlag(1047610914) == 0, 103, 89100114, -1)
        
        # Brittle Bones (selected)
        AddTalkListDataIf(GetEventFlag(1047610914) == 1, 203, 89100164, -1)
        
        # Lethargic Mind
        AddTalkListDataIf(GetEventFlag(1047610916) == 0, 104, 89100116, -1)
        
        # Lethargic Mind (selected)
        AddTalkListDataIf(GetEventFlag(1047610916) == 1, 204, 89100166, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

        # Bloodthirsty Maw
        if GetTalkListEntryResult() == 100:
            assert t000004030_x110(1047610907, 1, 89100207)
            continue
        # Bloodthirsty Maw (enabled)
        elif GetTalkListEntryResult() == 200:
            assert t000004030_x110(1047610907, 0, 89100307)
            continue
        # Fresh Meat
        elif GetTalkListEntryResult() == 101:
            assert t000004030_x110(1047610912, 1, 89100212)
            continue
        # Fresh Meat (enabled)
        elif GetTalkListEntryResult() == 201:
            assert t000004030_x110(1047610912, 0, 89100312)
            continue
        # Corrupted Flasks
        elif GetTalkListEntryResult() == 102:
            assert t000004030_x110(1047610913, 1, 89100213)
            continue
        # Corrupted Flasks
        elif GetTalkListEntryResult() == 202:
            assert t000004030_x110(1047610913, 0, 89100313)
            continue
        # Brittle Bones
        elif GetTalkListEntryResult() == 103:
            assert t000004030_x110(1047610914, 1, 89100214)
            continue
        # Brittle Bones (enabled)
        elif GetTalkListEntryResult() == 203:
            assert t000004030_x110(1047610914, 0, 89100314)
            continue
        # Lethargic Mind
        elif GetTalkListEntryResult() == 104:
            assert t000004030_x110(1047610916, 1, 89100216)
            continue
        # Lethargic Mind (enabled)
        elif GetTalkListEntryResult() == 204:
            assert t000004030_x110(1047610916, 0, 89100316)
            continue
        else:
            return 0
     
#----------------------------------------------------
# Castigations (Enemy)
#----------------------------------------------------
def t000004030_x102():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Stalwart Adversaries
        AddTalkListDataIf(GetEventFlag(1047610902) == 0, 100, 89100102, -1)
        
        # Stalwart Adversaries (selected)
        AddTalkListDataIf(GetEventFlag(1047610902) == 1, 200, 89100152, -1)
        
        # Regenerative Foes
        AddTalkListDataIf(GetEventFlag(1047610904) == 0, 101, 89100104, -1)
        
        # Regenerative Foes (selected)
        AddTalkListDataIf(GetEventFlag(1047610904) == 1, 201, 89100154, -1)
        
        # Wounded Fury
        AddTalkListDataIf(GetEventFlag(1047610900) == 0, 102, 89100100, -1)
        
        # Wounded Fury (selected)
        AddTalkListDataIf(GetEventFlag(1047610900) == 1, 202, 89100150, -1)
        
        # Thick Hides
        AddTalkListDataIf(GetEventFlag(1047610901) == 0, 103, 89100101, -1)
        
        # Thick Hides (selected)
        AddTalkListDataIf(GetEventFlag(1047610901) == 1, 203, 89100151, -1)
        
        # Spectral Shift
        AddTalkListDataIf(GetEventFlag(1047610910) == 0, 104, 89100110, -1)
        
        # Spectral Shift (selected)
        AddTalkListDataIf(GetEventFlag(1047610910) == 1, 204, 89100160, -1)
        
        # Relentless Approach
        AddTalkListDataIf(GetEventFlag(1047610911) == 0, 105, 89100111, -1)
        
        # Relentless Approach (selected)
        AddTalkListDataIf(GetEventFlag(1047610911) == 1, 205, 89100161, -1)
        
        # Alacrity
        AddTalkListDataIf(GetEventFlag(1047610915) == 0, 106, 89100115, -1)
        
        # Alacrity (selected)
        AddTalkListDataIf(GetEventFlag(1047610915) == 1, 206, 89100165, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Stalwart Adversaries
        if GetTalkListEntryResult() == 100:
            assert t000004030_x110(1047610902, 1, 89100202)
            continue
        # Stalwart Adversaries (enabled)
        elif GetTalkListEntryResult() == 200:
            assert t000004030_x110(1047610902, 0, 89100302)
            continue
        # Regenerative Foes
        elif GetTalkListEntryResult() == 101:
            assert t000004030_x110(1047610904, 1, 89100204)
            continue
        # Regenerative Foes (enabled)
        elif GetTalkListEntryResult() == 201:
            assert t000004030_x110(1047610904, 0, 89100304)
            continue
        # Wounded Fury
        elif GetTalkListEntryResult() == 102:
            assert t000004030_x110(1047610900, 1, 89100200)
            continue
        # Wounded Fury (enabled)
        elif GetTalkListEntryResult() == 202:
            assert t000004030_x110(1047610900, 0, 89100300)
            continue
        # Thick Hides
        elif GetTalkListEntryResult() == 103:
            assert t000004030_x110(1047610901, 1, 89100201)
            continue
        # Thick Hides (enabled)
        elif GetTalkListEntryResult() == 203:
            assert t000004030_x110(1047610901, 0, 89100301)
        # Spectral Shift
        elif GetTalkListEntryResult() == 104:
            assert t000004030_x110(1047610910, 1, 89100210)
            continue
        # Spectral Shift (enabled)
        elif GetTalkListEntryResult() == 204:
            assert t000004030_x110(1047610910, 0, 89100310)
        # Relentless Approach
        elif GetTalkListEntryResult() == 105:
            assert t000004030_x110(1047610911, 1, 89100211)
            continue
        # Relentless Approach (enabled)
        elif GetTalkListEntryResult() == 205:
            assert t000004030_x110(1047610911, 0, 89100311)
        # Alacrity
        elif GetTalkListEntryResult() == 106:
            assert t000004030_x110(1047610915, 1, 89100215)
            continue
        # Alacrity (enabled)
        elif GetTalkListEntryResult() == 206:
            assert t000004030_x110(1047610915, 0, 89100315)
        else:
            return 0
            
#----------------------------------------------------
# Castigations (Combat)
#----------------------------------------------------
def t000004030_x103():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Crippling Strikes
        AddTalkListDataIf(GetEventFlag(1047610903) == 0, 100, 89100103, -1)
        
        # Crippling Strikes (selected)
        AddTalkListDataIf(GetEventFlag(1047610903) == 1, 200, 89100153, -1)
        
        # Fetid Gash
        AddTalkListDataIf(GetEventFlag(1047610905) == 0, 101, 89100105, -1)
        
        # Fetid Gash (selected)
        AddTalkListDataIf(GetEventFlag(1047610905) == 1, 201, 89100155, -1)
        
        # Slumbering Blow
        AddTalkListDataIf(GetEventFlag(1047610908) == 0, 102, 89100108, -1)
        
        # Slumbering Blow (selected)
        AddTalkListDataIf(GetEventFlag(1047610908) == 1, 202, 89100158, -1)
        
        # Frenzying Swat
        AddTalkListDataIf(GetEventFlag(1047610909) == 0, 103, 89100109, -1)
        
        # Frenzying Swat (selected)
        AddTalkListDataIf(GetEventFlag(1047610909) == 1, 203, 89100159, -1)
        
        # Blighted Touch
        AddTalkListDataIf(GetEventFlag(1047610906) == 0, 104, 89100106, -1)
        
        # Blighted Touch (selected)
        AddTalkListDataIf(GetEventFlag(1047610906) == 1, 204, 89100156, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Crippling Strikes
        if GetTalkListEntryResult() == 100:
            assert t000004030_x111(1047610903, 1, 89100203)
            continue
        # Crippling Strikes (enabled)
        elif GetTalkListEntryResult() == 200:
            assert t000004030_x111(1047610903, 0, 89100303)
            continue
        # Fetid Gash
        elif GetTalkListEntryResult() == 101:
            assert t000004030_x111(1047610905, 1, 89100205)
            continue
        # Fetid Gash (enabled)
        elif GetTalkListEntryResult() == 201:
            assert t000004030_x111(1047610905, 0, 89100305)
            continue
        # Slumbering Blow
        elif GetTalkListEntryResult() == 102:
            assert t000004030_x111(1047610908, 1, 89100208)
            continue
        # Slumbering Blow (enabled)
        elif GetTalkListEntryResult() == 202:
            assert t000004030_x111(1047610908, 0, 89100308)
            continue
        # Frenzying Swat
        elif GetTalkListEntryResult() == 103:
            assert t000004030_x111(1047610909, 1, 89100209)
            continue
        # Frenzying Swat (enabled)
        elif GetTalkListEntryResult() == 203:
            assert t000004030_x111(1047610909, 0, 89100309)
            continue
        # Blighted Touch
        elif GetTalkListEntryResult() == 104:
            assert t000004030_x111(1047610906, 1, 89100206)
            continue
        # Blighted Touch (enabled)
        elif GetTalkListEntryResult() == 204:
            assert t000004030_x111(1047610906, 0, 89100306)
            continue
        else:
            return 0
            
#----------------------------------------------------
# Castigations (Fun)
#----------------------------------------------------
def t000004030_x104():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Megamind
        AddTalkListDataIf(GetEventFlag(1047610980) == 0, 100, 89100140, -1)
        
        # Megamind (selected)
        AddTalkListDataIf(GetEventFlag(1047610980) == 1, 200, 89100180, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Megamind
        if GetTalkListEntryResult() == 100:
            assert t000004030_x111(1047610980, 1, 89100240)
            continue
        # Megamind (enabled)
        elif GetTalkListEntryResult() == 200:
            assert t000004030_x111(1047610980, 0, 89100340)
            continue
        else:
            return 0
            
#----------------------------------------------------
# Utility
#----------------------------------------------------
# Castigation prompt
def t000004030_x110(flag=_, value=_, text=_):
    assert t000004030_x150(text)
            
    c1_110()

    ClearTalkListData()
    
    # Yes
    AddTalkListData(1, 80102101, -1)
    
    # No
    AddTalkListData(2, 80102102, -1)
    
    OpenConversationChoicesMenu(0)
    
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

    # Yes
    if GetTalkListEntryResult() == 1:
        SetEventFlag(flag, value)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2
        
# Castigation prompt (combat)
def t000004030_x111(flag=_, value=_, text=_):
    assert t000004030_x150(text)
            
    c1_110()

    ClearTalkListData()
    
    # Yes
    AddTalkListData(1, 80102101, -1)
    
    # No
    AddTalkListData(2, 80102102, -1)
    
    OpenConversationChoicesMenu(0)
    
    assert not (CheckSpecificPersonMenuIsOpen(12, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))

    # Yes
    if GetTalkListEntryResult() == 1:
        SetEventFlag(1047610903, 0)
        SetEventFlag(1047610905, 0)
        SetEventFlag(1047610906, 0)
        SetEventFlag(1047610908, 0)
        SetEventFlag(1047610909, 0)
        
        SetEventFlag(flag, value)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2
        
# Description Prompt
def t000004030_x150(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    