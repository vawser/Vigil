# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Jar of Promise
#-----------------------------------------------------
def t000001200_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000001200_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000001200_1000():
    """State 0,2,3"""
    assert t000001200_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000001200_2000():
    """State 0,2,3"""
    assert t000001200_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000001200_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t000001200_x1():
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

def t000001200_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001200_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000001200_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000001200_x1()
    else:
        """State 4,7"""
        call = t000001200_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000001200_x1()
    """State 9"""
    return 0

def t000001200_x4():
    """State 0,1"""
    assert t000001200_x1()
    """State 2"""
    return 0

def t000001200_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000001200_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000001200_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000001200_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000001200_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000001200_x13(val1=val1, z1=z1)
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
            call = t000001200_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000001200_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000001200_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000001200_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000001200_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000001200_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001200_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000001200_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000001200_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001200_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000001200_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000001200_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000001200_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x10(z6=_, val6=_):
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

def t000001200_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000001200_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000001200_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000001200_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000001200_x12():
    """State 0,1"""
    assert t000001200_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000001200_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000001200_x23()
    """State 1"""
    call = t000001200_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000001200_x25()
    """State 4"""
    return 0

def t000001200_x14():
    """State 0,1"""
    assert t000001200_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000001200_x15(val5=30):
    """State 0,1"""
    call = t000001200_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000001200_x26()
    """State 3"""
    return 0

def t000001200_x16():
    """State 0,1"""
    assert t000001200_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000001200_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000001200_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000001200_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000001200_x28()
    """Unused"""
    """State 6"""
    return 0

def t000001200_x18():
    """State 0,2"""
    call = t000001200_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000001200_x19():
    """State 0,1"""
    assert t000001200_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000001200_x20():
    """State 0,1"""
    assert t000001200_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000001200_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001200_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000001200_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000001200_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000001200_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000001200_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000001200_x23():
    """State 0,1"""
    assert t000001200_x24()
    """State 2"""
    return 0

def t000001200_x24():
    """State 0,1"""
    assert t000001200_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000001200_x25():
    """State 0,1"""
    call = t000001200_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x26():
    """State 0,1"""
    call = t000001200_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x27():
    """State 0,1"""
    call = t000001200_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x28():
    """State 0,1"""
    call = t000001200_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000001200_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000001200_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000001200_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000001200_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000001200_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000001200_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001200_x32():
    """State 0,1"""
    assert t000001200_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000001200_x33():
    """State 0,1"""
    assert t000001200_x1()
    """State 2"""
    return 0

def t000001200_x34():
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

def t000001200_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000001200_x38()
    """State 9"""
    return 0

def t000001200_x36():
    """State 0,1"""
    assert t000001200_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

def t000001200_x38():
    """State 0,8"""
    c1_110()
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Select Journey Type
        AddTalkListDataIf(GetEventFlag(1047610150) == 0, 10, 80200000, -1)
        
        # Select Starting Location
        AddTalkListDataIf(GetEventFlag(1047610150) == 0, 12, 80201000, -1)
        
        # Select Journey Modifiers
        AddTalkListDataIf(GetEventFlag(1047610150) == 0, 11, 80202000, -1)
        
        # Build Custom Loadout
        AddTalkListDataIf(GetEventFlag(1047610150) == 0 and GetEventFlag(1047610200) == 1, 13, 80203000, -1)
        
        # Finalize
        AddTalkListDataIf(GetEventFlag(1047610150) == 0 and GetEventFlag(1047610151) == 1 or GetEventFlag(1047610150) == 0 and GetEventFlag(1047610152) == 1 or GetEventFlag(1047610150) == 0 and GetEventFlag(1047610153) == 1 or GetEventFlag(1047610150) == 0 and GetEventFlag(1047610154) == 1, 20, 80200002, -1)
        
        # Memorize spell
        AddTalkListData(4, 15000390, -1)
        
        # Ashes of War
        AddTalkListDataIf(ComparePlayerInventoryNumber(3, 8590, 4, 1, 0) == 1, 8, 15000530, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        
        # Select Journey Type
        if GetTalkListEntryResult() == 10:
            assert t000001200_x39()
            continue
        # Select Journey Modifiers
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x41()
            continue
        # Select Starting Location
        elif GetTalkListEntryResult() == 12:
            assert t000001200_x40()
            continue
        # Build Custom Loadout
        elif GetTalkListEntryResult() == 13:
            assert t000001200_x50()
            continue
        # Finalize
        elif GetTalkListEntryResult() == 20:
            assert t000001200_x101(80200001)
            
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
                SetEventFlag(1047610150, 1)
                SetEventFlag(1047610231, 1)
                return 0
            # Cancel
            elif GetTalkListEntryResult() == 2:
                return 1
            else:
                return 2
   
            return 0
        elif GetTalkListEntryResult() == 4:
            OpenMagicEquip(-1, -1)
            assert not (CheckSpecificPersonMenuIsOpen(11, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 8:
            OpenEquipmentChangeOfPurposeShop()
            assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        else:
            """State 31"""
            return 0
        """State 10"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

# Journey Type
def t000001200_x39():
    """State 0,8"""
    c1_110()
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Tarnished
        AddTalkListDataIf(GetEventFlag(1047610151) == 0, 1, 80200100, -1)
        # Tarnished (Selected)
        AddTalkListDataIf(GetEventFlag(1047610151) == 1, 10, 80200110, -1)
        
        # Explorer
        AddTalkListDataIf(GetEventFlag(1047610152) == 0, 2, 80200101, -1)
        # Explorer (Selected)
        AddTalkListDataIf(GetEventFlag(1047610152) == 1, 11, 80200111, -1)
        
        # Conqueror
        AddTalkListDataIf(GetEventFlag(1047610153) == 0, 3, 80200102, -1)
        # Conqueror (Selected)
        AddTalkListDataIf(GetEventFlag(1047610153) == 1, 12, 80200112, -1)
        
        # Accursed
        AddTalkListDataIf(GetEventFlag(1047610154) == 0, 4, 80200103, -1)
        # Accursed (Selected)
        AddTalkListDataIf(GetEventFlag(1047610154) == 1, 13, 80200113, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        
        # Tarnished
        if GetTalkListEntryResult() == 1:
            assert t000001200_x130(80200200, 1047610151, 1)
            continue
        # Explorer
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x130(80200201, 1047610152, 1)
            continue
        # Conqueror
        elif GetTalkListEntryResult() == 3:
            assert t000001200_x130(80200202, 1047610153, 1)
            continue
        # Accursed
        elif GetTalkListEntryResult() == 4:
            assert t000001200_x130(80200203, 1047610154, 1)
            continue
        # Tarnished (selected)
        elif GetTalkListEntryResult() == 10:
            assert t000001200_x101(80200200)
            return 0
        # Explorer (selected)
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x101(80200201)
            return 0
        # Conqueror (selected)
        elif GetTalkListEntryResult() == 12:
            assert t000001200_x101(80200202)
            return 0
        # Accursed (selected)
        elif GetTalkListEntryResult() == 13:
            assert t000001200_x101(80200203)
            return 0
        else:
            """State 31"""
            return 0
        """State 10"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

# Starting Location
def t000001200_x40():
    """State 0,8"""
    c1_110()
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Here
        AddTalkListDataIf(GetEventFlag(1047610170) == 0, 1, 80201100, -1)
        # Here (Selected)
        AddTalkListDataIf(GetEventFlag(1047610170) == 1, 50, 80201150, -1)
        
        # Random
        AddTalkListDataIf(GetEventFlag(1047610171) == 0, 2, 80201101, -1)
        # Random (Selected)
        AddTalkListDataIf(GetEventFlag(1047610171) == 1, 51, 80201151, -1)
        
        # Limgrave
        AddTalkListDataIf(GetEventFlag(1047610172) == 0, 3, 80201102, -1)
        # Limgrave (Selected)
        AddTalkListDataIf(GetEventFlag(1047610172) == 1, 52, 80201152, -1)
        
        # Weeping Penisula
        AddTalkListDataIf(GetEventFlag(1047610173) == 0, 4, 80201103, -1)
        # Weeping Penisula (Selected)
        AddTalkListDataIf(GetEventFlag(1047610173) == 1, 53, 80201153, -1)
        
        # Liurnia
        AddTalkListDataIf(GetEventFlag(1047610174) == 0, 5, 80201104, -1)
        # Liurnia (Selected)
        AddTalkListDataIf(GetEventFlag(1047610174) == 1, 54, 80201154, -1)
        
        # Mt. Gelmir
        AddTalkListDataIf(GetEventFlag(1047610175) == 0, 6, 80201105, -1)
        # Mt. Gelmir (Selected)
        AddTalkListDataIf(GetEventFlag(1047610175) == 1, 55, 80201155, -1)
        
        # Altus Plateau
        AddTalkListDataIf(GetEventFlag(1047610176) == 0, 7, 80201106, -1)
        # Altus Plateau (Selected)
        AddTalkListDataIf(GetEventFlag(1047610176) == 1, 56, 80201156, -1)
        
        # Caelid
        AddTalkListDataIf(GetEventFlag(1047610178) == 0, 9, 80201108, -1)
        # Caelid (Selected)
        AddTalkListDataIf(GetEventFlag(1047610178) == 1, 58, 80201158, -1)
        
        # Mountaintops of the Giants
        AddTalkListDataIf(GetEventFlag(1047610179) == 0, 10, 80201109, -1)
        # Mountaintops of the Giants (Selected)
        AddTalkListDataIf(GetEventFlag(1047610179) == 1, 59, 80201159, -1)
        
        # Moonlight Altar
        AddTalkListDataIf(GetEventFlag(1047610177) == 0, 8, 80201107, -1)
        # Moonlight Altar (Selected)
        AddTalkListDataIf(GetEventFlag(1047610177) == 1, 57, 80201157, -1)
        
        # Miquella's Haligtree
        AddTalkListDataIf(GetEventFlag(1047610180) == 0, 11, 80201110, -1)
        # Miquella's Haligtree (Selected)
        AddTalkListDataIf(GetEventFlag(1047610180) == 1, 60, 80201160, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        
        # Here
        if GetTalkListEntryResult() == 1:
            assert t000001200_x120(80201200, 1047610170, 1)
            return 0
        # Random
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x120(80201201, 1047610171, 1)
            return 0
        # Limgrave
        elif GetTalkListEntryResult() == 3:
            assert t000001200_x120(80201202, 1047610172, 1)
            return 0
        # Weeping Penisula
        elif GetTalkListEntryResult() == 4:
            assert t000001200_x120(80201203, 1047610173, 1)
            return 0
        # Liurnia of the Lakes
        elif GetTalkListEntryResult() == 5:
            assert t000001200_x120(80201204, 1047610174, 1)
            return 0
        # Mt. Gelmir
        elif GetTalkListEntryResult() == 6:
            assert t000001200_x120(80201205, 1047610175, 1)
            return 0
        # Altus Plateau
        elif GetTalkListEntryResult() == 7:
            assert t000001200_x120(80201206, 1047610176, 1)
            return 0
        # Moonlight Altar
        elif GetTalkListEntryResult() == 8:
            assert t000001200_x120(80201207, 1047610177, 1)
            return 0
        # Caelid
        elif GetTalkListEntryResult() == 9:
            assert t000001200_x120(80201208, 1047610178, 1)
            return 0
        # Mountaintops of the Giants
        elif GetTalkListEntryResult() == 10:
            assert t000001200_x120(80201209, 1047610179, 1)
            return 0
        # Miquella's Haligtree
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x120(80201210, 1047610180, 1)
            return 0
        else:
            return 0
        assert CheckSpecificPersonTalkHasEnded(0) == 1
        
# Journey Modifiers
def t000001200_x41():
    """State 0,8"""
    c1_110()
    while True:
        """State 1"""
        ClearTalkListData()
        
        # Immediate Torrent
        AddTalkListDataIf(GetEventFlag(1047610160) == 0, 1, 80202100, -1)
        # Immediate Torrent (Selected)
        AddTalkListDataIf(GetEventFlag(1047610160) == 1, 10, 80202150, -1)
        
        # Immediate Roundtable Hold
        AddTalkListDataIf(GetEventFlag(1047610161) == 0, 2, 80202101, -1)
        # Immediate Roundtable Hold (Selected)
        AddTalkListDataIf(GetEventFlag(1047610161) == 1, 11, 80202151, -1)
        
        # Reveal Maps
        AddTalkListDataIf(GetEventFlag(1047610162) == 0, 3, 80202102, -1)
        # Reveal Maps (Selected)
        AddTalkListDataIf(GetEventFlag(1047610162) == 1, 12, 80202152, -1)
        
        # Leave
        AddTalkListData(99, 20000009, -1)
        
        """State 6"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 2"""
        
        # Immediate Torrent
        if GetTalkListEntryResult() == 1:
            assert t000001200_x110(80202200, 1047610160, 1)
            return 0
        # Immediate Torrent (selected)
        elif GetTalkListEntryResult() == 10:
            assert t000001200_x110(80202250, 1047610160, 0)
            return 0
        # Immediate Roundtable Hold
        elif GetTalkListEntryResult() == 2:
            assert t000001200_x110(80202201, 1047610161, 1)
            return 0
        # Immediate Roundtable Hold (selected)
        elif GetTalkListEntryResult() == 11:
            assert t000001200_x110(80202251, 1047610161, 0)
            return 0
        # Reveal Maps
        elif GetTalkListEntryResult() == 3:
            assert t000001200_x110(80202202, 1047610162, 1)
            return 0
        # Reveal Maps (selected)
        elif GetTalkListEntryResult() == 12:
            assert t000001200_x110(80202252, 1047610162, 0)
            return 0
        else:
            """State 31"""
            return 0
        """State 10"""
        assert CheckSpecificPersonTalkHasEnded(0) == 1

# Custom Loadout
def t000001200_x50():
    c1110()
    
    while True:
        ClearTalkListData()

        # Weapons
        AddTalkListData(1, 99999000, -1)
        
        # Spells
        AddTalkListData(2, 99999002, -1)
        
        # Armor
        AddTalkListData(3, 99999001, -1)
        
        # Talismans
        AddTalkListData(4, 99999003, -1)
        
        # Ammunition
        AddTalkListData(5, 99999004, -1)
        
        # Ashes of War
        AddTalkListData(6, 99999006, -1)
        
        # Spirit Summons
        AddTalkListData(7, 99999007, -1)
        
        # Items
        AddTalkListData(8, 99999008, -1)
        
        # Runes
        AddTalkListDataIf(GetEventFlag(1047610220) == 0, 9, 99999005, -1)
        
        # Level Up
        AddTalkListData(10, 15000540, -1)
        
        # Leave
        AddTalkListData(99, 26080001, -1)

        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Weapons
        if GetTalkListEntryResult() == 1:
            OpenChampionsEquipmentShop(9100000, 9109999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spells
        elif GetTalkListEntryResult() == 2:
            OpenChampionsEquipmentShop(9120000, 9129999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Armor
        elif GetTalkListEntryResult() == 3:
            OpenChampionsEquipmentShop(9110000, 9119999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Talismans
        elif GetTalkListEntryResult() == 4:
            OpenChampionsEquipmentShop(9130000, 9139999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ammunition
        elif GetTalkListEntryResult() == 5:
            OpenChampionsEquipmentShop(9140000, 9149999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Ashes of War
        elif GetTalkListEntryResult() == 6:
            OpenChampionsEquipmentShop(9150000, 9159999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Spirit Summons
        elif GetTalkListEntryResult() == 7:
            OpenChampionsEquipmentShop(9160000, 9169999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Items
        elif GetTalkListEntryResult() == 8:
            OpenChampionsEquipmentShop(9190000, 9199999)
            assert not (CheckSpecificPersonMenuIsOpen(33, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Runes
        elif GetTalkListEntryResult() == 9:
            SetEventFlag(1047610220, 1)
            GiveSpEffectToPlayer(7000040)
            PlayerEquipmentQuantityChange(3, 22000, -1)
            assert t000001200_x101(99999010)
        # Levelup
        elif GetTalkListEntryResult() == 10:
            OpenSoul()
            assert not (CheckSpecificPersonMenuIsOpen(10, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        # Leave
        elif not (CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0)):
            return 0

# Description Prompt
def t000001200_x101(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Starting Location
def t000001200_x102(flag=_):
    SetEventFlag(1047610170, 0)
    SetEventFlag(1047610171, 0)
    
    SetEventFlag(flag, 1)
    
    return 0
    
# YES/NO Choice
def t000001200_x110(text=_, flag=_, value=_):
    assert t000001200_x101(text)
            
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

    return 0
    
# Location - YES/NO Choice
def t000001200_x120(text=_, flag=_, value=_):
    assert t000001200_x101(text)
            
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
        SetEventFlag(1047610170, 0)
        SetEventFlag(1047610171, 0)
        SetEventFlag(1047610172, 0)
        SetEventFlag(1047610173, 0)
        SetEventFlag(1047610174, 0)
        SetEventFlag(1047610175, 0)
        SetEventFlag(1047610176, 0)
        SetEventFlag(1047610177, 0)
        SetEventFlag(1047610178, 0)
        SetEventFlag(1047610179, 0)#
        
        SetEventFlag(flag, value)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2

    return 0
    
# Difficulty - YES/NO Choice
def t000001200_x130(text=_, flag=_, value=_):
    assert t000001200_x101(text)
            
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
        SetEventFlag(1047610151, 0)
        SetEventFlag(1047610152, 0)
        SetEventFlag(1047610153, 0)
        SetEventFlag(1047610154, 0)
        
        SetEventFlag(flag, value)
        
        return 0
    # Cancel
    elif GetTalkListEntryResult() == 2:
        return 1
    else:
        return 2