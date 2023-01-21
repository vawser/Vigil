# -*- coding: utf-8 -*-
def t608001110_1():
    """State 0,1"""
    # actionbutton:6000:"Talk"
    t608001110_x4(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    def WhilePaused():
        c1_139(0, 0)
    Quit()

def t608001110_1000():
    """State 0,2,3"""
    assert t608001110_x31()
    """State 1"""
    c1_120(1000)
    Quit()

def t608001110_2000():
    """State 0,2,3"""
    assert t608001110_x32()
    """State 1"""
    c1_120(2000)
    Quit()

def t608001110_x0(actionbutton1=_, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000):
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
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t608001110_x1():
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

def t608001110_x2(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t608001110_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t608001110_x1()
    else:
        """State 4,7"""
        call = t608001110_x28()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t608001110_x1()
    """State 9"""
    return 0

def t608001110_x3():
    """State 0,1"""
    assert t608001110_x1()
    """State 2"""
    return 0

def t608001110_x4(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t608001110_x21(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t608001110_x20()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t608001110_x5(val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t608001110_x8(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t608001110_x12(val1=val1, z1=z1)
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
            call = t608001110_x14(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t608001110_x25() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t608001110_x10(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t608001110_x6(val2=10, val3=12):
    """State 0,1"""
    call = t608001110_x16(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t608001110_x2(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t608001110_x7(flag1=6000, val2=10, val3=12):
    """State 0,8"""
    assert t608001110_x30()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t608001110_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t608001110_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t608001110_x8(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t608001110_x9(z5=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t608001110_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x9(z5=_, val6=_):
    """State 0,1"""
    if f203(z5) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z5)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t608001110_x10(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t608001110_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t608001110_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t608001110_x26()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t608001110_x11():
    """State 0,1"""
    assert t608001110_x9(z5=1101, val6=1101)
    """State 2"""
    return 0

def t608001110_x12(val1=5, z1=1):
    """State 0,2"""
    assert t608001110_x22()
    """State 1"""
    call = t608001110_x13()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t608001110_x24()
    """State 4"""
    return 0

def t608001110_x13():
    """State 0,1"""
    assert t608001110_x9(z5=1000, val6=1000)
    """State 2"""
    return 0

def t608001110_x14(val5=12):
    """State 0,1"""
    call = t608001110_x15()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t608001110_x25()
    """State 3"""
    return 0

def t608001110_x15():
    """State 0,1"""
    assert t608001110_x9(z5=1100, val6=1100)
    """State 2"""
    return 0

def t608001110_x16(val2=10, val3=12):
    """State 0,5"""
    assert t608001110_x30()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t608001110_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t608001110_x27()
    """Unused"""
    """State 6"""
    return 0

def t608001110_x17():
    """State 0,2"""
    call = t608001110_x9(z5=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t608001110_x18():
    """State 0,1"""
    assert t608001110_x9(z5=1001, val6=1001)
    """State 2"""
    return 0

def t608001110_x19():
    """State 0,1"""
    assert t608001110_x9(z5=1103, val6=1103)
    """State 2"""
    return 0

def t608001110_x20():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t608001110_x21(flag1=6000, flag2=6000, flag3=6000, val1=5, val2=10, val3=12, val4=10, val5=12, actionbutton1=6000,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t608001110_x5(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t608001110_x7(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t608001110_x6(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t608001110_x29() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t608001110_x22():
    """State 0,1"""
    assert t608001110_x23()
    """State 2"""
    return 0

def t608001110_x23():
    """State 0,1"""
    assert t608001110_x9(z5=1104, val6=1104)
    """State 2"""
    return 0

def t608001110_x24():
    """State 0,1"""
    call = t608001110_x9(z5=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x25():
    """State 0,1"""
    call = t608001110_x9(z5=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x26():
    """State 0,1"""
    call = t608001110_x9(z5=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x27():
    """State 0,1"""
    call = t608001110_x9(z5=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t608001110_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t608001110_x28():
    """State 0,1"""
    assert t608001110_x9(z5=1002, val6=1002)
    """State 2"""
    return 0

def t608001110_x29():
    """State 0,1"""
    assert t608001110_x1()
    """State 2"""
    return 0

def t608001110_x30():
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

def t608001110_x31():
    """State 0,1"""
    assert t608001110_x33()
    """State 2"""
    return 0

def t608001110_x32():
    """State 0,1"""
    # actionbutton:6380:"Use mirror"
    assert (t608001110_x0(actionbutton1=6380, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
            flag4=6000))
    """State 2"""
    return 0

def t608001110_x33():
    """State 0"""
    while True:
        """State 2"""
        c1_110()
        ClearTalkListData()
        """State 5"""
        # action:26080000:"Apply cosmetics"
        AddTalkListData(1, 26080000, -1)
        
        # Apply Transmogrification
        AddTalkListData(2, 89000000, -1)
        
        # action:26080001:"Leave"
        AddTalkListData(99, 26080001, -1)
        """State 4"""
        ShowShopMessage(1)
        """State 6"""
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        """State 3"""
        if GetTalkListEntryResult() == 1:
            """State 1"""
            ClearTalkActionState()
            OpenCharaMakeMenu(1)
            TurnCharacterToFaceEntity(-1, 10000, -1, -1)
            assert GetCurrentStateElapsedFrames() > 1 and GetWhetherChrEventAnimHasEnded(10000) == 1
            """State 9"""
            def WhilePaused():
                GiveSpEffectToPlayer(9614)
            assert not (CheckSpecificPersonMenuIsOpen(30, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
            """State 8"""
            if DidYouDoSomethingInTheMenu(1) == 1:
                break
            else:
                pass
        # Apply Transmogrification
        elif GetTalkListEntryResult() == 2:
            assert t608001110_x50()
            continue
        else:
            """State 7"""
            break
    """State 10"""
    return 0

# Transmogrification
def t608001110_x50():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Alter Head
        AddTalkListData(1, 89000001, -1)

        # Alter Body
        AddTalkListData(2, 89000002, -1)
        
        # Alter Emissions
        
        # Alter Perspective
        
        # Leave
        AddTalkListData(99, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t608001110_x51()
            continue
        elif GetTalkListEntryResult() == 2:
            assert t608001110_x52()
            continue
        else:
            """State 7"""
            break
    """State 10"""
    return 0

# Alter Head
def t608001110_x51():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Unique Armor
        AddTalkListData(1, 89000013, -1)

        # Heavy Armor
        AddTalkListData(2, 89000010, -1)
        
        # Medium Armor
        AddTalkListData(3, 89000011, -1)
        
        # Light Armor
        AddTalkListData(4, 89000012, -1)
        
        # Reset head transmogrification
        AddTalkListData(5, 89000014, -1)
        
        # Leave
        AddTalkListData(99, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t608001110_x60()
            continue
        elif GetTalkListEntryResult() == 2:
            assert t608001110_x61()
            continue
        elif GetTalkListEntryResult() == 3:
            assert t608001110_x62()
            continue
        elif GetTalkListEntryResult() == 4:
            assert t608001110_x63()
            continue
        elif GetTalkListEntryResult() == 5:
            assert t608001110_x210(89000040, 1047610101, 1)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Head: Unique Armor
def t608001110_x60():
    while True:
        c1_110()
        ClearTalkListData()
        
        # None (ON)
        AddTalkListDataIf(GetEventFlag(1047600998) == 0, 100, 89001000, -1)
        # None (OFF)
        AddTalkListDataIf(GetEventFlag(1047600998) == 1, 500, 89001000, -1)
        
        # Bandit Mask (ON)
        AddTalkListDataIf(GetEventFlag(1047600344) == 0, 101, 89001700, -1)
        # Bandit Mask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600344) == 1, 501, 89001700, -1)

        # Pumpkin Helm (ON)
        AddTalkListDataIf(GetEventFlag(1047600126) == 0, 102, 89001701, -1)
        # Pumpkin Helm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600126) == 1, 502, 89001701, -1)

        # Brave's Leather Helm (ON)
        AddTalkListDataIf(GetEventFlag(1047600202) == 0, 103, 89001702, -1)
        # Brave's Leather Helm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600202) == 1, 503, 89001702, -1)

        # Navy Hood (ON)
        AddTalkListDataIf(GetEventFlag(1047600211) == 0, 104, 89001703, -1)
        # Navy Hood (OFF)
        AddTalkListDataIf(GetEventFlag(1047600211) == 1, 504, 89001703, -1)

        # Envoy Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600240) == 0, 105, 89001704, -1)
        # Envoy Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600240) == 1, 505, 89001704, -1)

        # Twinsage Glintstone Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600241) == 0, 106, 89001705, -1)
        # Twinsage Glintstone Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600241) == 1, 506, 89001705, -1)

        # Olivinus Glintstone Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600243) == 0, 107, 89001706, -1)
        # Olivinus Glintstone Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600243) == 1, 507, 89001706, -1)

        # Lazuli Glintstone Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600244) == 0, 108, 89001707, -1)
        # Lazuli Glintstone Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600244) == 1, 508, 89001707, -1)

        # Karolos Glintstone Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600245) == 0, 109, 89001708, -1)
        # Karolos Glintstone Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600245) == 1, 509, 89001708, -1)

        # Witch's Glintstone Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600246) == 0, 110, 89001709, -1)
        # Witch's Glintstone Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600246) == 1, 510, 89001709, -1)

        # Marionette Soldier Birdhelm (ON)
        AddTalkListDataIf(GetEventFlag(1047600249) == 0, 111, 89001710, -1)
        # Marionette Soldier Birdhelm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600249) == 1, 511, 89001710, -1)

        # Blackguard's Iron Mask (ON)
        AddTalkListDataIf(GetEventFlag(1047600266) == 0, 112, 89001711, -1)
        # Blackguard's Iron Mask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600266) == 1, 512, 89001711, -1)

        # Grass Hair Ornament (ON)
        AddTalkListDataIf(GetEventFlag(1047600279) == 0, 113, 89001712, -1)
        # Grass Hair Ornament (OFF)
        AddTalkListDataIf(GetEventFlag(1047600279) == 1, 513, 89001712, -1)

        # Imp Head (Cat) (ON)
        AddTalkListDataIf(GetEventFlag(1047600324) == 0, 114, 89001713, -1)
        # Imp Head (Cat) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600324) == 1, 514, 89001713, -1)

        # Imp Head (Fanged) (ON)
        AddTalkListDataIf(GetEventFlag(1047600325) == 0, 115, 89001714, -1)
        # Imp Head (Fanged) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600325) == 1, 515, 89001714, -1)

        # Imp Head (Long-Tongued) (ON)
        AddTalkListDataIf(GetEventFlag(1047600326) == 0, 116, 89001715, -1)
        # Imp Head (Long-Tongued) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600326) == 1, 516, 89001715, -1)

        # Imp Head (Corpse) (ON)
        AddTalkListDataIf(GetEventFlag(1047600327) == 0, 117, 89001716, -1)
        # Imp Head (Corpse) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600327) == 1, 517, 89001716, -1)

        # Imp Head (Wolf) (ON)
        AddTalkListDataIf(GetEventFlag(1047600328) == 0, 118, 89001717, -1)
        # Imp Head (Wolf) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600328) == 1, 518, 89001717, -1)

        # Imp Head (Elder) (ON)
        AddTalkListDataIf(GetEventFlag(1047600329) == 0, 119, 89001718, -1)
        # Imp Head (Elder) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600329) == 1, 519, 89001718, -1)

        # Silver Tear Mask (ON)
        AddTalkListDataIf(GetEventFlag(1047600330) == 0, 120, 89001719, -1)
        # Silver Tear Mask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600330) == 1, 520, 89001719, -1)

        # Greathelm (ON)
        AddTalkListDataIf(GetEventFlag(1047600333) == 0, 121, 89001720, -1)
        # Greathelm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600333) == 1, 521, 89001720, -1)

        # Octopus Head (ON)
        AddTalkListDataIf(GetEventFlag(1047600336) == 0, 122, 89001721, -1)
        # Octopus Head (OFF)
        AddTalkListDataIf(GetEventFlag(1047600336) == 1, 522, 89001721, -1)

        # Jar (ON)
        AddTalkListDataIf(GetEventFlag(1047600337) == 0, 123, 89001722, -1)
        # Jar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600337) == 1, 523, 89001722, -1)

        # Nox Mirrorhelm (ON)
        AddTalkListDataIf(GetEventFlag(1047600340) == 0, 124, 89001723, -1)
        # Nox Mirrorhelm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600340) == 1, 524, 89001723, -1)

        # Iji's Mirrorhelm (ON)
        AddTalkListDataIf(GetEventFlag(1047600341) == 0, 125, 89001724, -1)
        # Iji's Mirrorhelm (OFF)
        AddTalkListDataIf(GetEventFlag(1047600341) == 1, 525, 89001724, -1)

        # Greathood (ON)
        AddTalkListDataIf(GetEventFlag(1047600347) == 0, 126, 89001725, -1)
        # Greathood (OFF)
        AddTalkListDataIf(GetEventFlag(1047600347) == 1, 526, 89001725, -1)

        # Ash-of-War Scarab (ON)
        AddTalkListDataIf(GetEventFlag(1047600400) == 0, 127, 89001726, -1)
        # Ash-of-War Scarab (OFF)
        AddTalkListDataIf(GetEventFlag(1047600400) == 1, 527, 89001726, -1)

        # Incantation Scarab (ON)
        AddTalkListDataIf(GetEventFlag(1047600401) == 0, 128, 89001727, -1)
        # Incantation Scarab (OFF)
        AddTalkListDataIf(GetEventFlag(1047600401) == 1, 528, 89001727, -1)

        # Glintstone Scarab (ON)
        AddTalkListDataIf(GetEventFlag(1047600402) == 0, 129, 89001728, -1)
        # Glintstone Scarab (OFF)
        AddTalkListDataIf(GetEventFlag(1047600402) == 1, 529, 89001728, -1)

        # Crimson Tear Scarab (ON)
        AddTalkListDataIf(GetEventFlag(1047600403) == 0, 130, 89001729, -1)
        # Crimson Tear Scarab (OFF)
        AddTalkListDataIf(GetEventFlag(1047600403) == 1, 530, 89001729, -1)

        # Cerulean Tear Scarab (ON)
        AddTalkListDataIf(GetEventFlag(1047600404) == 0, 131, 89001730, -1)
        # Cerulean Tear Scarab (OFF)
        AddTalkListDataIf(GetEventFlag(1047600404) == 1, 531, 89001730, -1)

        # Mushroom Crown (ON)
        AddTalkListDataIf(GetEventFlag(1047600419) == 0, 132, 89001731, -1)
        # Mushroom Crown (OFF)
        AddTalkListDataIf(GetEventFlag(1047600419) == 1, 532, 89001731, -1)

        # Black Dumpling (ON)
        AddTalkListDataIf(GetEventFlag(1047600420) == 0, 133, 89001732, -1)
        # Black Dumpling (OFF)
        AddTalkListDataIf(GetEventFlag(1047600420) == 1, 533, 89001732, -1)

        # Crab Carcass (ON)
        AddTalkListDataIf(GetEventFlag(1047600422) == 0, 134, 89001733, -1)
        # Crab Carcass (OFF)
        AddTalkListDataIf(GetEventFlag(1047600422) == 1, 534, 89001733, -1)

        # Diallos's Mask (ON)
        AddTalkListDataIf(GetEventFlag(1047600182) == 0, 135, 89001734, -1)
        # Diallos's Mask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600182) == 1, 535, 89001734, -1)
        
        # Mask of the Mother (ON)
        AddTalkListDataIf(GetEventFlag(1047600427) == 0, 136, 89001735, -1)
        # Mask of the Mother (OFF)
        AddTalkListDataIf(GetEventFlag(1047600427) == 1, 536, 89001735, -1)

        # Mask of the Child (ON)
        AddTalkListDataIf(GetEventFlag(1047600428) == 0, 137, 89001736, -1)
        # Mask of the Child (OFF)
        AddTalkListDataIf(GetEventFlag(1047600428) == 1, 537, 89001736, -1)
        
        # Mask of the Father (ON)
        AddTalkListDataIf(GetEventFlag(1047600429) == 0, 138, 89001737, -1)
        # Mask of the Father (OFF)
        AddTalkListDataIf(GetEventFlag(1047600429) == 1, 538, 89001737, -1)
        
        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # None (ON)
        if GetTalkListEntryResult() == 100:
            assert t608001110_x210(89000020, 1047600998, 1) 
            return 0
        # None (OFF)
        elif GetTalkListEntryResult() == 500:
            assert t608001110_x210(89000021, 1047600998, 0) 
            return 0
        # Bandit Mask (ON)
        elif GetTalkListEntryResult() == 101:
            assert t608001110_x210(89000020, 1047600344, 1)
            return 0
        # Bandit Mask (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x210(89000021, 1047600344, 0)
            return 0
        # Pumpkin Helm (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x210(89000020, 1047600126, 1)
            return 0
        # Pumpkin Helm (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x210(89000021, 1047600126, 0)
            return 0
        # Brave's Leather Helm (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x210(89000020, 1047600202, 1)
            return 0
        # Brave's Leather Helm (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x210(89000021, 1047600202, 0)
            return 0
        # Navy Hood (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x210(89000020, 1047600211, 1)
            return 0
        # Navy Hood (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x210(89000021, 1047600211, 0)
            return 0
        # Envoy Crown (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x210(89000020, 1047600240, 1)
            return 0
        # Envoy Crown (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x210(89000021, 1047600240, 0)
            return 0
        # Twinsage Glintstone Crown (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x210(89000020, 1047600241, 1)
            return 0
        # Twinsage Glintstone Crown (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x210(89000021, 1047600241, 0)
            return 0
        # Olivinus Glintstone Crown (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x210(89000020, 1047600243, 1)
            return 0
        # Olivinus Glintstone Crown (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x210(89000021, 1047600243, 0)
            return 0
        # Lazuli Glintstone Crown (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x210(89000020, 1047600244, 1)
            return 0
        # Lazuli Glintstone Crown (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x210(89000021, 1047600244, 0)
            return 0
        # Karolos Glintstone Crown (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x210(89000020, 1047600245, 1)
            return 0
        # Karolos Glintstone Crown (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x210(89000021, 1047600245, 0)
            return 0
        # Witch's Glintstone Crown (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x210(89000020, 1047600246, 1)
            return 0
        # Witch's Glintstone Crown (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x210(89000021, 1047600246, 0)
            return 0
        # Marionette Soldier Birdhelm (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x210(89000020, 1047600249, 1)
            return 0
        # Marionette Soldier Birdhelm (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x210(89000021, 1047600249, 0)
            return 0
        # Blackguard's Iron Mask (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x210(89000020, 1047600266, 1)
            return 0
        # Blackguard's Iron Mask (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x210(89000021, 1047600266, 0)
            return 0
        # Grass Hair Ornament (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x210(89000020, 1047600279, 1)
            return 0
        # Grass Hair Ornament (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x210(89000021, 1047600279, 0)
            return 0
        # Imp Head (Cat) (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x210(89000020, 1047600324, 1)
            return 0
        # Imp Head (Cat) (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x210(89000021, 1047600324, 0)
            return 0
        # Imp Head (Fanged) (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x210(89000020, 1047600325, 1)
            return 0
        # Imp Head (Fanged) (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x210(89000021, 1047600325, 0)
            return 0
        # Imp Head (Long-Tongued) (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x210(89000020, 1047600326, 1)
            return 0
        # Imp Head (Long-Tongued) (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x210(89000021, 1047600326, 0)
            return 0
        # Imp Head (Corpse) (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x210(89000020, 1047600327, 1)
            return 0
        # Imp Head (Corpse) (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x210(89000021, 1047600327, 0)
            return 0
        # Imp Head (Wolf) (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x210(89000020, 1047600328, 1)
            return 0
        # Imp Head (Wolf) (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x210(89000021, 1047600328, 0)
            return 0
        # Imp Head (Elder) (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x210(89000020, 1047600329, 1)
            return 0
        # Imp Head (Elder) (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x210(89000021, 1047600329, 0)
            return 0
        # Silver Tear Mask (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x210(89000020, 1047600330, 1)
            return 0
        # Silver Tear Mask (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x210(89000021, 1047600330, 0)
            return 0
        # Greathelm (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x210(89000020, 1047600333, 1)
            return 0
        # Greathelm (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x210(89000021, 1047600333, 0)
            return 0
        # Octopus Head (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x210(89000020, 1047600336, 1)
            return 0
        # Octopus Head (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x210(89000021, 1047600336, 0)
            return 0
        # Jar (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x210(89000020, 1047600337, 1)
            return 0
        # Jar (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x210(89000021, 1047600337, 0)
            return 0
        # Nox Mirrorhelm (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x210(89000020, 1047600340, 1)
            return 0
        # Nox Mirrorhelm (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x210(89000021, 1047600340, 0)
            return 0
        # Iji's Mirrorhelm (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x210(89000020, 1047600341, 1)
            return 0
        # Iji's Mirrorhelm (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x210(89000021, 1047600341, 0)
            return 0
        # Greathood (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x210(89000020, 1047600347, 1)
            return 0
        # Greathood (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x210(89000021, 1047600347, 0)
            return 0
        # Ash-of-War Scarab (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x210(89000020, 1047600400, 1)
            return 0
        # Ash-of-War Scarab (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x210(89000021, 1047600400, 0)
            return 0
        # Incantation Scarab (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x210(89000020, 1047600401, 1)
            return 0
        # Incantation Scarab (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x210(89000021, 1047600401, 0)
            return 0
        # Glintstone Scarab (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x210(89000020, 1047600402, 1)
            return 0
        # Glintstone Scarab (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x210(89000021, 1047600402, 0)
            return 0
        # Crimson Tear Scarab (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x210(89000020, 1047600403, 1)
            return 0
        # Crimson Tear Scarab (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x210(89000021, 1047600403, 0)
            return 0
        # Cerulean Tear Scarab (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x210(89000020, 1047600404, 1)
            return 0
        # Cerulean Tear Scarab (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x210(89000021, 1047600404, 0)
            return 0
        # Mushroom Crown (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x210(89000020, 1047600419, 1)
            return 0
        # Mushroom Crown (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x210(89000021, 1047600419, 0)
            return 0
        # Black Dumpling (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x210(89000020, 1047600420, 1)
            return 0
        # Black Dumpling (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x210(89000021, 1047600420, 0)
            return 0
        # Crab Carcass (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x210(89000020, 1047600422, 1)
            return 0
        # Crab Carcass (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x210(89000021, 1047600422, 0)
            return 0
        # Diallos's Mask (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x210(89000020, 1047600182, 1)
            return 0
        # Diallos's Mask (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x210(89000021, 1047600182, 0)
            return 0
        # Mask of the Mother (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x210(89000020, 1047600427, 1)
            return 0
        # Mask of the Mother (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x210(89000021, 1047600427, 0)
            return 0
        # Mask of the Child (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x210(89000020, 1047600428, 1)
            return 0
        # Mask of the Child (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x210(89000021, 1047600428, 0)
            return 0
        # Mask of the Father (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x210(89000020, 1047600429, 1)
            return 0
        # Mask of the Father (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x210(89000021, 1047600429, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Head: Heavy Armor
def t608001110_x61():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Bull-Goat (ON)
        AddTalkListDataIf(GetEventFlag(1047600028) == 0, 101, 89001100, -1)
        # Bull-Goat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600028) == 1, 501, 89001100, -1)

        # Fire Prelate (ON)
        AddTalkListDataIf(GetEventFlag(1047600112) == 0, 102, 89001101, -1)
        # Fire Prelate (OFF)
        AddTalkListDataIf(GetEventFlag(1047600112) == 1, 502, 89001101, -1)

        # Fire Prelate (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600114) == 0, 103, 89001102, -1)
        # Fire Prelate (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600114) == 1, 503, 89001102, -1)

        # Lionel (ON)
        AddTalkListDataIf(GetEventFlag(1047600176) == 0, 104, 89001103, -1)
        # Lionel (OFF)
        AddTalkListDataIf(GetEventFlag(1047600176) == 1, 504, 89001103, -1)

        # Lionel (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600178) == 0, 105, 89001105, -1)
        # Lionel (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600178) == 1, 505, 89001105, -1)

        # Omen (ON)
        AddTalkListDataIf(GetEventFlag(1047600300) == 0, 106, 89001104, -1)
        # Omen (OFF)
        AddTalkListDataIf(GetEventFlag(1047600300) == 1, 506, 89001104, -1)

        # Tree Sentinel (ON)
        AddTalkListDataIf(GetEventFlag(1047600072) == 0, 107, 89001106, -1)
        # Tree Sentinel (OFF)
        AddTalkListDataIf(GetEventFlag(1047600072) == 1, 507, 89001106, -1)

        # Tree Sentinel (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600074) == 0, 108, 89001107, -1)
        # Tree Sentinel (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600074) == 1, 508, 89001107, -1)

        # Veteran (ON)
        AddTalkListDataIf(GetEventFlag(1047600220) == 0, 109, 89001108, -1)
        # Veteran (OFF)
        AddTalkListDataIf(GetEventFlag(1047600220) == 1, 509, 89001108, -1)

        # Veteran (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600222) == 0, 110, 89001109, -1)
        # Veteran (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600222) == 1, 510, 89001109, -1)

        # Beast Champion (ON)
        AddTalkListDataIf(GetEventFlag(1047600203) == 0, 111, 89001110, -1)
        # Beast Champion (OFF)
        AddTalkListDataIf(GetEventFlag(1047600203) == 1, 511, 89001110, -1)

        # Beast Champion (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600205) == 0, 112, 89001111, -1)
        # Beast Champion (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600205) == 1, 512, 89001111, -1)

        # Banished Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600046) == 0, 113, 89001112, -1)
        # Banished Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600046) == 1, 513, 89001112, -1)

        # Banished Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600048) == 0, 114, 89001113, -1)
        # Banished Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600048) == 1, 514, 89001113, -1)

        # General Radahn (ON)
        AddTalkListDataIf(GetEventFlag(1047600131) == 0, 115, 89001114, -1)
        # General Radahn (OFF)
        AddTalkListDataIf(GetEventFlag(1047600131) == 1, 515, 89001114, -1)

        # General Radahn (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600133) == 0, 116, 89001115, -1)
        # General Radahn (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600133) == 1, 516, 89001115, -1)

        # Malformed Dragon (ON)
        AddTalkListDataIf(GetEventFlag(1047600070) == 0, 117, 89001116, -1)
        # Malformed Dragon (OFF)
        AddTalkListDataIf(GetEventFlag(1047600070) == 1, 517, 89001116, -1)

        # Scaled (ON)
        AddTalkListDataIf(GetEventFlag(1047600008) == 0, 118, 89001117, -1)
        # Scaled (OFF)
        AddTalkListDataIf(GetEventFlag(1047600008) == 1, 518, 89001117, -1)

        # Scaled (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600010) == 0, 119, 89001118, -1)
        # Scaled (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600010) == 1, 519, 89001118, -1)

        # Crucible Axe (ON)
        AddTalkListDataIf(GetEventFlag(1047600145) == 0, 120, 89001119, -1)
        # Crucible Axe (OFF)
        AddTalkListDataIf(GetEventFlag(1047600145) == 1, 520, 89001119, -1)

        # Crucible Axe (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600147) == 0, 121, 89001120, -1)
        # Crucible Axe (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600147) == 1, 521, 89001120, -1)

        # Crucible Tree (ON)
        AddTalkListDataIf(GetEventFlag(1047600149) == 0, 122, 89001121, -1)
        # Crucible Tree (OFF)
        AddTalkListDataIf(GetEventFlag(1047600149) == 1, 522, 89001121, -1)

        # Royal Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600076) == 0, 123, 89001122, -1)
        # Royal Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600076) == 1, 523, 89001122, -1)

        # Royal Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600078) == 0, 124, 89001123, -1)
        # Royal Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600078) == 1, 524, 89001123, -1)

        # Cleanrot (ON)
        AddTalkListDataIf(GetEventFlag(1047600104) == 0, 125, 89001124, -1)
        # Cleanrot (OFF)
        AddTalkListDataIf(GetEventFlag(1047600104) == 1, 525, 89001124, -1)

        # Cleanrot (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600106) == 0, 126, 89001125, -1)
        # Cleanrot (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600106) == 1, 526, 89001125, -1)

        # Blaidd (ON)
        AddTalkListDataIf(GetEventFlag(1047600036) == 0, 127, 89001126, -1)
        # Blaidd (OFF)
        AddTalkListDataIf(GetEventFlag(1047600036) == 1, 527, 89001126, -1)

        # Blaidd (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600038) == 0, 128, 89001127, -1)
        # Blaidd (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600038) == 1, 528, 89001127, -1)

        # Night's Cavalry (ON)
        AddTalkListDataIf(GetEventFlag(1047600058) == 0, 129, 89001128, -1)
        # Night's Cavalry (OFF)
        AddTalkListDataIf(GetEventFlag(1047600058) == 1, 529, 89001128, -1)

        # Night's Cavalry (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600060) == 0, 130, 89001129, -1)
        # Night's Cavalry (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600060) == 1, 530, 89001129, -1)

        # Maliketh (ON)
        AddTalkListDataIf(GetEventFlag(1047600212) == 0, 131, 89001130, -1)
        # Maliketh (OFF)
        AddTalkListDataIf(GetEventFlag(1047600212) == 1, 531, 89001130, -1)

        # Maliketh (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600214) == 0, 132, 89001131, -1)
        # Maliketh (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600214) == 1, 532, 89001131, -1)

        # Twinned (ON)
        AddTalkListDataIf(GetEventFlag(1047600159) == 0, 133, 89001132, -1)
        # Twinned (OFF)
        AddTalkListDataIf(GetEventFlag(1047600159) == 1, 533, 89001132, -1)

        # Twinned (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600161) == 0, 134, 89001133, -1)
        # Twinned (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600161) == 1, 534, 89001133, -1)

        # Hoslow (ON)
        AddTalkListDataIf(GetEventFlag(1047600180) == 0, 135, 89001134, -1)
        # Hoslow (OFF)
        AddTalkListDataIf(GetEventFlag(1047600180) == 1, 535, 89001134, -1)

        # Hoslow (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600184) == 0, 136, 89001135, -1)
        # Hoslow (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600184) == 1, 536, 89001135, -1)

        # Cuckoo Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600368) == 0, 137, 89001136, -1)
        # Cuckoo Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600368) == 1, 537, 89001136, -1)

        # Cuckoo Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600370) == 0, 138, 89001137, -1)
        # Cuckoo Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600370) == 1, 538, 89001137, -1)

        # Briar (ON)
        AddTalkListDataIf(GetEventFlag(1047600050) == 0, 139, 89001138, -1)
        # Briar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600050) == 1, 539, 89001138, -1)

        # Briar (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600052) == 0, 140, 89001139, -1)
        # Briar (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600052) == 1, 540, 89001139, -1)

        # Godrick Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600364) == 0, 141, 89001140, -1)
        # Godrick Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600364) == 1, 541, 89001140, -1)

        # Godrick Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600366) == 0, 142, 89001141, -1)
        # Godrick Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600366) == 1, 542, 89001141, -1)

        # Redmane Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600376) == 0, 143, 89001142, -1)
        # Redmane Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600376) == 1, 543, 89001142, -1)

        # Redmane Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600378) == 0, 144, 89001143, -1)
        # Redmane Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600378) == 1, 544, 89001143, -1)

        # Gelmir Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600360) == 0, 145, 89001144, -1)
        # Gelmir Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600360) == 1, 545, 89001144, -1)

        # Gelmir Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600362) == 0, 146, 89001145, -1)
        # Gelmir Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600362) == 1, 546, 89001145, -1)

        # Leyndell Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600372) == 0, 147, 89001146, -1)
        # Leyndell Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600372) == 1, 547, 89001146, -1)

        # Leyndell Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600374) == 0, 148, 89001147, -1)
        # Leyndell Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600374) == 1, 548, 89001147, -1)

        # Haligtree Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600384) == 0, 149, 89001148, -1)
        # Haligtree Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600384) == 1, 549, 89001148, -1)

        # Haligtree Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600386) == 0, 150, 89001149, -1)
        # Haligtree Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600386) == 1, 550, 89001149, -1)

        # Blackflame Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600110) == 0, 151, 89001150, -1)
        # Blackflame Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600110) == 1, 551, 89001150, -1)

        # Fire Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600108) == 0, 152, 89001151, -1)
        # Fire Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600108) == 1, 552, 89001151, -1)

        # Giant (ON)
        AddTalkListDataIf(GetEventFlag(1047600430) == 0, 153, 89001152, -1)
        # Giant (OFF)
        AddTalkListDataIf(GetEventFlag(1047600430) == 1, 553, 89001152, -1)
        
        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Bull-Goat (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x210(89000020, 1047600028, 1)
            return 0
        # Bull-Goat (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x210(89000021, 1047600028, 0)
            return 0
        # Fire Prelate (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x210(89000020, 1047600112, 1)
            return 0
        # Fire Prelate (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x210(89000021, 1047600112, 0)
            return 0
        # Fire Prelate (Altered) (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x210(89000020, 1047600114, 1)
            return 0
        # Fire Prelate (Altered) (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x210(89000021, 1047600114, 0)
            return 0
        # Lionel (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x210(89000020, 1047600176, 1)
            return 0
        # Lionel (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x210(89000021, 1047600176, 0)
            return 0
        # Lionel (Altered) (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x210(89000020, 1047600178, 1)
            return 0
        # Lionel (Altered) (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x210(89000021, 1047600178, 0)
            return 0
        # Omen (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x210(89000020, 1047600300, 1)
            return 0
        # Omen (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x210(89000021, 1047600300, 0)
            return 0
        # Tree Sentinel (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x210(89000020, 1047600072, 1)
            return 0
        # Tree Sentinel (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x210(89000021, 1047600072, 0)
            return 0
        # Tree Sentinel (Altered) (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x210(89000020, 1047600074, 1)
            return 0
        # Tree Sentinel (Altered) (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x210(89000021, 1047600074, 0)
            return 0
        # Veteran (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x210(89000020, 1047600220, 1)
            return 0
        # Veteran (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x210(89000021, 1047600220, 0)
            return 0
        # Veteran (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x210(89000020, 1047600222, 1)
            return 0
        # Veteran (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x210(89000021, 1047600222, 0)
            return 0
        # Beast Champion (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x210(89000020, 1047600203, 1)
            return 0
        # Beast Champion (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x210(89000021, 1047600203, 0)
            return 0
        # Beast Champion (Altered) (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x210(89000020, 1047600205, 1)
            return 0
        # Beast Champion (Altered) (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x210(89000021, 1047600205, 0)
            return 0
        # Banished Knight (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x210(89000020, 1047600046, 1)
            return 0
        # Banished Knight (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x210(89000021, 1047600046, 0)
            return 0
        # Banished Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x210(89000020, 1047600048, 1)
            return 0
        # Banished Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x210(89000021, 1047600048, 0)
            return 0
        # General Radahn (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x210(89000020, 1047600131, 1)
            return 0
        # General Radahn (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x210(89000021, 1047600131, 0)
            return 0
        # General Radahn (Altered) (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x210(89000020, 1047600133, 1)
            return 0
        # General Radahn (Altered) (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x210(89000021, 1047600133, 0)
            return 0
        # Malformed Dragon (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x210(89000020, 1047600070, 1)
            return 0
        # Malformed Dragon (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x210(89000021, 1047600070, 0)
            return 0
        # Scaled (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x210(89000020, 1047600008, 1)
            return 0
        # Scaled (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x210(89000021, 1047600008, 0)
            return 0
        # Scaled (Altered) (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x210(89000020, 1047600010, 1)
            return 0
        # Scaled (Altered) (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x210(89000021, 1047600010, 0)
            return 0
        # Crucible Axe (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x210(89000020, 1047600145, 1)
            return 0
        # Crucible Axe (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x210(89000021, 1047600145, 0)
            return 0
        # Crucible Axe (Altered) (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x210(89000020, 1047600147, 1)
            return 0
        # Crucible Axe (Altered) (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x210(89000021, 1047600147, 0)
            return 0
        # Crucible Tree (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x210(89000020, 1047600149, 1)
            return 0
        # Crucible Tree (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x210(89000021, 1047600149, 0)
            return 0
        # Royal Knight (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x210(89000020, 1047600076, 1)
            return 0
        # Royal Knight (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x210(89000021, 1047600076, 0)
            return 0
        # Royal Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x210(89000020, 1047600078, 1)
            return 0
        # Royal Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x210(89000021, 1047600078, 0)
            return 0
        # Cleanrot (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x210(89000020, 1047600104, 1)
            return 0
        # Cleanrot (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x210(89000021, 1047600104, 0)
            return 0
        # Cleanrot (Altered) (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x210(89000020, 1047600106, 1)
            return 0
        # Cleanrot (Altered) (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x210(89000021, 1047600106, 0)
            return 0
        # Blaidd (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x210(89000020, 1047600036, 1)
            return 0
        # Blaidd (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x210(89000021, 1047600036, 0)
            return 0
        # Blaidd (Altered) (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x210(89000020, 1047600038, 1)
            return 0
        # Blaidd (Altered) (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x210(89000021, 1047600038, 0)
            return 0
        # Night's Cavalry (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x210(89000020, 1047600058, 1)
            return 0
        # Night's Cavalry (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x210(89000021, 1047600058, 0)
            return 0
        # Night's Cavalry (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x210(89000020, 1047600060, 1)
            return 0
        # Night's Cavalry (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x210(89000021, 1047600060, 0)
            return 0
        # Maliketh (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x210(89000020, 1047600212, 1)
            return 0
        # Maliketh (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x210(89000021, 1047600212, 0)
            return 0
        # Maliketh (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x210(89000020, 1047600214, 1)
            return 0
        # Maliketh (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x210(89000021, 1047600214, 0)
            return 0
        # Twinned (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x210(89000020, 1047600159, 1)
            return 0
        # Twinned (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x210(89000021, 1047600159, 0)
            return 0
        # Twinned (Altered) (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x210(89000020, 1047600161, 1)
            return 0
        # Twinned (Altered) (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x210(89000021, 1047600161, 0)
            return 0
        # Hoslow (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x210(89000020, 1047600180, 1)
            return 0
        # Hoslow (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x210(89000021, 1047600180, 0)
            return 0
        # Hoslow (Altered) (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x210(89000020, 1047600184, 1)
            return 0
        # Hoslow (Altered) (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x210(89000021, 1047600184, 0)
            return 0
        # Cuckoo Knight (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x210(89000020, 1047600368, 1)
            return 0
        # Cuckoo Knight (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x210(89000021, 1047600368, 0)
            return 0
        # Cuckoo Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x210(89000020, 1047600370, 1)
            return 0
        # Cuckoo Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x210(89000021, 1047600370, 0)
            return 0
        # Briar (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x210(89000020, 1047600050, 1)
            return 0
        # Briar (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x210(89000021, 1047600050, 0)
            return 0
        # Briar (Altered) (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x210(89000020, 1047600052, 1)
            return 0
        # Briar (Altered) (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x210(89000021, 1047600052, 0)
            return 0
        # Godrick Knight (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x210(89000020, 1047600364, 1)
            return 0
        # Godrick Knight (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x210(89000021, 1047600364, 0)
            return 0
        # Godrick Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x210(89000020, 1047600366, 1)
            return 0
        # Godrick Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x210(89000021, 1047600366, 0)
            return 0
        # Redmane Knight (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x210(89000020, 1047600376, 1)
            return 0
        # Redmane Knight (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x210(89000021, 1047600376, 0)
            return 0
        # Redmane Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x210(89000020, 1047600378, 1)
            return 0
        # Redmane Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x210(89000021, 1047600378, 0)
            return 0
        # Gelmir Knight (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x210(89000020, 1047600360, 1)
            return 0
        # Gelmir Knight (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x210(89000021, 1047600360, 0)
            return 0
        # Gelmir Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x210(89000020, 1047600362, 1)
            return 0
        # Gelmir Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x210(89000021, 1047600362, 0)
            return 0
        # Leyndell Knight (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x210(89000020, 1047600372, 1)
            return 0
        # Leyndell Knight (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x210(89000021, 1047600372, 0)
            return 0
        # Leyndell Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x210(89000020, 1047600374, 1)
            return 0
        # Leyndell Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x210(89000021, 1047600374, 0)
            return 0
        # Haligtree Knight (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x210(89000020, 1047600384, 1)
            return 0
        # Haligtree Knight (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x210(89000021, 1047600384, 0)
            return 0
        # Haligtree Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x210(89000020, 1047600386, 1)
            return 0
        # Haligtree Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x210(89000021, 1047600386, 0)
            return 0
        # Blackflame Monk (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x210(89000020, 1047600110, 1)
            return 0
        # Blackflame Monk (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x210(89000021, 1047600110, 0)
            return 0
        # Fire Monk (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x210(89000020, 1047600108, 1)
            return 0
        # Fire Monk (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x210(89000021, 1047600108, 0)
            return 0
        # Giant (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x210(89000020, 1047600430, 1)
            return 0
        # Giant (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x210(89000021, 1047600430, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Head: Medium Armor
def t608001110_x62():
    while True:
        c1_110()
        ClearTalkListData()
        
        # All-Knowing (ON)
        AddTalkListDataIf(GetEventFlag(1047600155) == 0, 101, 89001300, -1)
        # All-Knowing (OFF)
        AddTalkListDataIf(GetEventFlag(1047600155) == 1, 501, 89001300, -1)

        # All-Knowing (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600157) == 0, 102, 89001301, -1)
        # All-Knowing (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600157) == 1, 502, 89001301, -1)

        # Royal Remains (ON)
        AddTalkListDataIf(GetEventFlag(1047600196) == 0, 103, 89001302, -1)
        # Royal Remains (OFF)
        AddTalkListDataIf(GetEventFlag(1047600196) == 1, 503, 89001302, -1)

        # Bloodhound Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600224) == 0, 104, 89001303, -1)
        # Bloodhound Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600224) == 1, 504, 89001303, -1)

        # Bloodhound Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600226) == 0, 105, 89001304, -1)
        # Bloodhound Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600226) == 1, 505, 89001304, -1)

        # Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600345) == 0, 106, 89001305, -1)
        # Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600345) == 1, 506, 89001305, -1)

        # Fingerprint (ON)
        AddTalkListDataIf(GetEventFlag(1047600286) == 0, 107, 89001306, -1)
        # Fingerprint (OFF)
        AddTalkListDataIf(GetEventFlag(1047600286) == 1, 507, 89001306, -1)

        # Fingerprint (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600288) == 0, 108, 89001307, -1)
        # Fingerprint (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600288) == 1, 508, 89001307, -1)

        # Carian Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600302) == 0, 109, 89001308, -1)
        # Carian Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600302) == 1, 509, 89001308, -1)

        # Carian Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600304) == 0, 110, 89001309, -1)
        # Carian Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600304) == 1, 510, 89001309, -1)

        # Godrick Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600348) == 0, 111, 89001310, -1)
        # Godrick Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600348) == 1, 511, 89001310, -1)

        # Raya Lucarian Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600350) == 0, 112, 89001311, -1)
        # Raya Lucarian Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600350) == 1, 512, 89001311, -1)

        # Leyndell Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600352) == 0, 113, 89001312, -1)
        # Leyndell Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600352) == 1, 513, 89001312, -1)

        # Radahn Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600354) == 0, 114, 89001313, -1)
        # Radahn Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600354) == 1, 514, 89001313, -1)

        # Haligtree Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600358) == 0, 115, 89001314, -1)
        # Haligtree Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600358) == 1, 515, 89001314, -1)

        # Raging Wolf (ON)
        AddTalkListDataIf(GetEventFlag(1047600250) == 0, 116, 89001315, -1)
        # Raging Wolf (OFF)
        AddTalkListDataIf(GetEventFlag(1047600250) == 1, 516, 89001315, -1)

        # Raging Wolf (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600252) == 0, 117, 89001316, -1)
        # Raging Wolf (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600252) == 1, 517, 89001316, -1)

        # Vagabond Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600186) == 0, 118, 89001317, -1)
        # Vagabond Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600186) == 1, 518, 89001317, -1)

        # Vagabond Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600188) == 0, 119, 89001318, -1)
        # Vagabond Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600188) == 1, 519, 89001318, -1)

        # Mausoleum Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600380) == 0, 120, 89001319, -1)
        # Mausoleum Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600380) == 1, 520, 89001319, -1)

        # Mausoleum Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600382) == 0, 121, 89001320, -1)
        # Mausoleum Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600382) == 1, 521, 89001320, -1)

        # Eccentric (ON)
        AddTalkListDataIf(GetEventFlag(1047600282) == 0, 122, 89001321, -1)
        # Eccentric (OFF)
        AddTalkListDataIf(GetEventFlag(1047600282) == 1, 522, 89001321, -1)

        # Eccentric (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600284) == 0, 123, 89001322, -1)
        # Eccentric (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600284) == 1, 523, 89001322, -1)

        # Drake Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600004) == 0, 124, 89001323, -1)
        # Drake Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600004) == 1, 524, 89001323, -1)

        # Drake Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600006) == 0, 125, 89001324, -1)
        # Drake Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600006) == 1, 525, 89001324, -1)

        # Black Knife (ON)
        AddTalkListDataIf(GetEventFlag(1047600040) == 0, 126, 89001325, -1)
        # Black Knife (OFF)
        AddTalkListDataIf(GetEventFlag(1047600040) == 1, 526, 89001325, -1)

        # Black Knife (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600042) == 0, 127, 89001326, -1)
        # Black Knife (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600042) == 1, 527, 89001326, -1)

        # Exile (ON)
        AddTalkListDataIf(GetEventFlag(1047600044) == 0, 128, 89001327, -1)
        # Exile (OFF)
        AddTalkListDataIf(GetEventFlag(1047600044) == 1, 528, 89001327, -1)

        # Elden Lord (ON)
        AddTalkListDataIf(GetEventFlag(1047600127) == 0, 129, 89001328, -1)
        # Elden Lord (OFF)
        AddTalkListDataIf(GetEventFlag(1047600127) == 1, 529, 89001328, -1)

        # Elden Lord (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600129) == 0, 130, 89001329, -1)
        # Elden Lord (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600129) == 1, 530, 89001329, -1)

        # Ronin (ON)
        AddTalkListDataIf(GetEventFlag(1047600030) == 0, 131, 89001330, -1)
        # Ronin (OFF)
        AddTalkListDataIf(GetEventFlag(1047600030) == 1, 531, 89001330, -1)

        # Ronin (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600032) == 0, 132, 89001331, -1)
        # Ronin (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600032) == 1, 532, 89001331, -1)

        # Chain (ON)
        AddTalkListDataIf(GetEventFlag(1047600331) == 0, 133, 89001332, -1)
        # Chain (OFF)
        AddTalkListDataIf(GetEventFlag(1047600331) == 1, 533, 89001332, -1)

        # Iron (ON)
        AddTalkListDataIf(GetEventFlag(1047600000) == 0, 134, 89001333, -1)
        # Iron (OFF)
        AddTalkListDataIf(GetEventFlag(1047600000) == 1, 534, 89001333, -1)

        # Kaiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600002) == 0, 135, 89001334, -1)
        # Kaiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600002) == 1, 535, 89001334, -1)

        # Mausoleum Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600356) == 0, 136, 89001335, -1)
        # Mausoleum Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600356) == 1, 536, 89001335, -1)

        # Blue Silver (ON)
        AddTalkListDataIf(GetEventFlag(1047600062) == 0, 137, 89001336, -1)
        # Blue Silver (OFF)
        AddTalkListDataIf(GetEventFlag(1047600062) == 1, 537, 89001336, -1)

        # Blue Silver (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600064) == 0, 138, 89001337, -1)
        # Blue Silver (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600064) == 1, 538, 89001337, -1)

        # Zamor (ON)
        AddTalkListDataIf(GetEventFlag(1047600322) == 0, 139, 89001338, -1)
        # Zamor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600322) == 1, 539, 89001338, -1)

        # Malenia (ON)
        AddTalkListDataIf(GetEventFlag(1047600216) == 0, 140, 89001339, -1)
        # Malenia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600216) == 1, 540, 89001339, -1)

        # Malenia (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600218) == 0, 141, 89001340, -1)
        # Malenia (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600218) == 1, 541, 89001340, -1)

        # Guardian (ON)
        AddTalkListDataIf(GetEventFlag(1047600100) == 0, 142, 89001341, -1)
        # Guardian (OFF)
        AddTalkListDataIf(GetEventFlag(1047600100) == 1, 542, 89001341, -1)

        # Guardian (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600102) == 0, 143, 89001342, -1)
        # Guardian (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600102) == 1, 543, 89001342, -1)

        # Duelist (ON)
        AddTalkListDataIf(GetEventFlag(1047600094) == 0, 144, 89001343, -1)
        # Duelist (OFF)
        AddTalkListDataIf(GetEventFlag(1047600094) == 1, 544, 89001343, -1)

        # Duelist (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600096) == 0, 145, 89001344, -1)
        # Duelist (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600096) == 1, 545, 89001344, -1)

        # Land of Reeds (ON)
        AddTalkListDataIf(GetEventFlag(1047600254) == 0, 146, 89001345, -1)
        # Land of Reeds (OFF)
        AddTalkListDataIf(GetEventFlag(1047600254) == 1, 546, 89001345, -1)

        # Land of Reeds (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600256) == 0, 147, 89001346, -1)
        # Land of Reeds (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600256) == 1, 547, 89001346, -1)

        # White Reed (ON)
        AddTalkListDataIf(GetEventFlag(1047600258) == 0, 148, 89001347, -1)
        # White Reed (OFF)
        AddTalkListDataIf(GetEventFlag(1047600258) == 1, 548, 89001347, -1)

        # Godrick Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600388) == 0, 149, 89001348, -1)
        # Godrick Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600388) == 1, 549, 89001348, -1)

        # Raya Lucarian Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600390) == 0, 150, 89001349, -1)
        # Raya Lucarian Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600390) == 1, 550, 89001349, -1)

        # Leyndell Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600392) == 0, 151, 89001350, -1)
        # Leyndell Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600392) == 1, 551, 89001350, -1)

        # Radahn Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600394) == 0, 152, 89001351, -1)
        # Radahn Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600394) == 1, 552, 89001351, -1)

        # Haligtree Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600396) == 0, 153, 89001352, -1)
        # Haligtree Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600396) == 1, 553, 89001352, -1)

        # Nox Swordstress (ON)
        AddTalkListDataIf(GetEventFlag(1047600084) == 0, 154, 89001353, -1)
        # Nox Swordstress (OFF)
        AddTalkListDataIf(GetEventFlag(1047600084) == 1, 554, 89001353, -1)

        # Nox Swordstress (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600086) == 0, 155, 89001354, -1)
        # Nox Swordstress (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600086) == 1, 555, 89001354, -1)

        # Night Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600088) == 0, 156, 89001355, -1)
        # Night Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600088) == 1, 556, 89001355, -1)

        # Confessor (ON)
        AddTalkListDataIf(GetEventFlag(1047600260) == 0, 157, 89001356, -1)
        # Confessor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600260) == 1, 557, 89001356, -1)

        # Confessor (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600262) == 0, 158, 89001357, -1)
        # Confessor (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600262) == 1, 558, 89001357, -1)

        # Nox Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600080) == 0, 159, 89001358, -1)
        # Nox Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600080) == 1, 559, 89001358, -1)

        # Nox Monk (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600082) == 0, 160, 89001359, -1)
        # Nox Monk (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600082) == 1, 560, 89001359, -1)

        # Vulgar Militia (ON)
        AddTalkListDataIf(GetEventFlag(1047600122) == 0, 161, 89001360, -1)
        # Vulgar Militia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600122) == 1, 561, 89001360, -1)

        # Ragged (ON)
        AddTalkListDataIf(GetEventFlag(1047600163) == 0, 162, 89001361, -1)
        # Ragged (OFF)
        AddTalkListDataIf(GetEventFlag(1047600163) == 1, 562, 89001361, -1)

        # Ragged (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600165) == 0, 163, 89001362, -1)
        # Ragged (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600165) == 1, 563, 89001362, -1)

        # Blue Cloth (ON)
        AddTalkListDataIf(GetEventFlag(1047600190) == 0, 164, 89001363, -1)
        # Blue Cloth (OFF)
        AddTalkListDataIf(GetEventFlag(1047600190) == 1, 564, 89001363, -1)

        # Omenkiller (ON)
        AddTalkListDataIf(GetEventFlag(1047600398) == 0, 165, 89001364, -1)
        # Omenkiller (OFF)
        AddTalkListDataIf(GetEventFlag(1047600398) == 1, 565, 89001364, -1)

        # Leather (ON)
        AddTalkListDataIf(GetEventFlag(1047600342) == 0, 166, 89001365, -1)
        # Leather (OFF)
        AddTalkListDataIf(GetEventFlag(1047600342) == 1, 566, 89001365, -1)

        # War Surgeon (ON)
        AddTalkListDataIf(GetEventFlag(1047600192) == 0, 167, 89001366, -1)
        # War Surgeon (OFF)
        AddTalkListDataIf(GetEventFlag(1047600192) == 1, 567, 89001366, -1)

        # War Surgeon (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600194) == 0, 168, 89001367, -1)
        # War Surgeon (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600194) == 1, 568, 89001367, -1)

        # Raptor (ON)
        AddTalkListDataIf(GetEventFlag(1047600280) == 0, 169, 89001368, -1)
        # Raptor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600280) == 1, 569, 89001368, -1)

        # Preceptor (ON)
        AddTalkListDataIf(GetEventFlag(1047600275) == 0, 170, 89001369, -1)
        # Preceptor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600275) == 1, 570, 89001369, -1)

        # Preceptor (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600277) == 0, 171, 89001370, -1)
        # Preceptor (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600277) == 1, 571, 89001370, -1)

        # Rotten Duelist (ON)
        AddTalkListDataIf(GetEventFlag(1047600415) == 0, 172, 89001371, -1)
        # Rotten Duelist (OFF)
        AddTalkListDataIf(GetEventFlag(1047600415) == 1, 572, 89001371, -1)

        # Rotten Duelist (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600417) == 0, 173, 89001372, -1)
        # Rotten Duelist (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600417) == 1, 573, 89001372, -1)

        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # All-Knowing (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x210(89000020, 1047600155, 1)
            return 0
        # All-Knowing (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x210(89000021, 1047600155, 0)
            return 0
        # All-Knowing (Altered) (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x210(89000020, 1047600157, 1)
            return 0
        # All-Knowing (Altered) (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x210(89000021, 1047600157, 0)
            return 0
        # Royal Remains (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x210(89000020, 1047600196, 1)
            return 0
        # Royal Remains (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x210(89000021, 1047600196, 0)
            return 0
        # Bloodhound Knight (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x210(89000020, 1047600224, 1)
            return 0
        # Bloodhound Knight (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x210(89000021, 1047600224, 0)
            return 0
        # Bloodhound Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x210(89000020, 1047600226, 1)
            return 0
        # Bloodhound Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x210(89000021, 1047600226, 0)
            return 0
        # Knight (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x210(89000020, 1047600345, 1)
            return 0
        # Knight (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x210(89000021, 1047600345, 0)
            return 0
        # Fingerprint (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x210(89000020, 1047600286, 1)
            return 0
        # Fingerprint (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x210(89000021, 1047600286, 0)
            return 0
        # Fingerprint (Altered) (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x210(89000020, 1047600288, 1)
            return 0
        # Fingerprint (Altered) (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x210(89000021, 1047600288, 0)
            return 0
        # Carian Knight (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x210(89000020, 1047600302, 1)
            return 0
        # Carian Knight (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x210(89000021, 1047600302, 0)
            return 0
        # Carian Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x210(89000020, 1047600304, 1)
            return 0
        # Carian Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x210(89000021, 1047600304, 0)
            return 0
        # Godrick Soldier (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x210(89000020, 1047600348, 1)
            return 0
        # Godrick Soldier (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x210(89000021, 1047600348, 0)
            return 0
        # Raya Lucarian Soldier (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x210(89000020, 1047600350, 1)
            return 0
        # Raya Lucarian Soldier (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x210(89000021, 1047600350, 0)
            return 0
        # Leyndell Soldier (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x210(89000020, 1047600352, 1)
            return 0
        # Leyndell Soldier (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x210(89000021, 1047600352, 0)
            return 0
        # Radahn Soldier (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x210(89000020, 1047600354, 1)
            return 0
        # Radahn Soldier (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x210(89000021, 1047600354, 0)
            return 0
        # Haligtree Soldier (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x210(89000020, 1047600358, 1)
            return 0
        # Haligtree Soldier (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x210(89000021, 1047600358, 0)
            return 0
        # Raging Wolf (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x210(89000020, 1047600250, 1)
            return 0
        # Raging Wolf (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x210(89000021, 1047600250, 0)
            return 0
        # Raging Wolf (Altered) (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x210(89000020, 1047600252, 1)
            return 0
        # Raging Wolf (Altered) (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x210(89000021, 1047600252, 0)
            return 0
        # Vagabond Knight (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x210(89000020, 1047600186, 1)
            return 0
        # Vagabond Knight (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x210(89000021, 1047600186, 0)
            return 0
        # Vagabond Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x210(89000020, 1047600188, 1)
            return 0
        # Vagabond Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x210(89000021, 1047600188, 0)
            return 0
        # Mausoleum Knight (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x210(89000020, 1047600380, 1)
            return 0
        # Mausoleum Knight (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x210(89000021, 1047600380, 0)
            return 0
        # Mausoleum Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x210(89000020, 1047600382, 1)
            return 0
        # Mausoleum Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x210(89000021, 1047600382, 0)
            return 0
        # Eccentric (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x210(89000020, 1047600282, 1)
            return 0
        # Eccentric (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x210(89000021, 1047600282, 0)
            return 0
        # Eccentric (Altered) (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x210(89000020, 1047600284, 1)
            return 0
        # Eccentric (Altered) (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x210(89000021, 1047600284, 0)
            return 0
        # Drake Knight (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x210(89000020, 1047600004, 1)
            return 0
        # Drake Knight (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x210(89000021, 1047600004, 0)
            return 0
        # Drake Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x210(89000020, 1047600006, 1)
            return 0
        # Drake Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x210(89000021, 1047600006, 0)
            return 0
        # Black Knife (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x210(89000020, 1047600040, 1)
            return 0
        # Black Knife (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x210(89000021, 1047600040, 0)
            return 0
        # Black Knife (Altered) (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x210(89000020, 1047600042, 1)
            return 0
        # Black Knife (Altered) (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x210(89000021, 1047600042, 0)
            return 0
        # Exile (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x210(89000020, 1047600044, 1)
            return 0
        # Exile (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x210(89000021, 1047600044, 0)
            return 0
        # Elden Lord (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x210(89000020, 1047600127, 1)
            return 0
        # Elden Lord (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x210(89000021, 1047600127, 0)
            return 0
        # Elden Lord (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x210(89000020, 1047600129, 1)
            return 0
        # Elden Lord (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x210(89000021, 1047600129, 0)
            return 0
        # Ronin (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x210(89000020, 1047600030, 1)
            return 0
        # Ronin (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x210(89000021, 1047600030, 0)
            return 0
        # Ronin (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x210(89000020, 1047600032, 1)
            return 0
        # Ronin (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x210(89000021, 1047600032, 0)
            return 0
        # Chain (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x210(89000020, 1047600331, 1)
            return 0
        # Chain (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x210(89000021, 1047600331, 0)
            return 0
        # Iron (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x210(89000020, 1047600000, 1)
            return 0
        # Iron (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x210(89000021, 1047600000, 0)
            return 0
        # Kaiden (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x210(89000020, 1047600002, 1)
            return 0
        # Kaiden (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x210(89000021, 1047600002, 0)
            return 0
        # Mausoleum Soldier (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x210(89000020, 1047600356, 1)
            return 0
        # Mausoleum Soldier (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x210(89000021, 1047600356, 0)
            return 0
        # Blue Silver (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x210(89000020, 1047600062, 1)
            return 0
        # Blue Silver (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x210(89000021, 1047600062, 0)
            return 0
        # Blue Silver (Altered) (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x210(89000020, 1047600064, 1)
            return 0
        # Blue Silver (Altered) (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x210(89000021, 1047600064, 0)
            return 0
        # Zamor (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x210(89000020, 1047600322, 1)
            return 0
        # Zamor (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x210(89000021, 1047600322, 0)
            return 0
        # Malenia (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x210(89000020, 1047600216, 1)
            return 0
        # Malenia (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x210(89000021, 1047600216, 0)
            return 0
        # Malenia (Altered) (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x210(89000020, 1047600218, 1)
            return 0
        # Malenia (Altered) (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x210(89000021, 1047600218, 0)
            return 0
        # Guardian (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x210(89000020, 1047600100, 1)
            return 0
        # Guardian (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x210(89000021, 1047600100, 0)
            return 0
        # Guardian (Altered) (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x210(89000020, 1047600102, 1)
            return 0
        # Guardian (Altered) (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x210(89000021, 1047600102, 0)
            return 0
        # Duelist (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x210(89000020, 1047600094, 1)
            return 0
        # Duelist (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x210(89000021, 1047600094, 0)
            return 0
        # Duelist (Altered) (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x210(89000020, 1047600096, 1)
            return 0
        # Duelist (Altered) (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x210(89000021, 1047600096, 0)
            return 0
        # Land of Reeds (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x210(89000020, 1047600254, 1)
            return 0
        # Land of Reeds (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x210(89000021, 1047600254, 0)
            return 0
        # Land of Reeds (Altered) (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x210(89000020, 1047600256, 1)
            return 0
        # Land of Reeds (Altered) (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x210(89000021, 1047600256, 0)
            return 0
        # White Reed (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x210(89000020, 1047600258, 1)
            return 0
        # White Reed (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x210(89000021, 1047600258, 0)
            return 0
        # Godrick Foot Soldier (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x210(89000020, 1047600388, 1)
            return 0
        # Godrick Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x210(89000021, 1047600388, 0)
            return 0
        # Raya Lucarian Foot Soldier (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x210(89000020, 1047600390, 1)
            return 0
        # Raya Lucarian Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x210(89000021, 1047600390, 0)
            return 0
        # Leyndell Foot Soldier (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x210(89000020, 1047600392, 1)
            return 0
        # Leyndell Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x210(89000021, 1047600392, 0)
            return 0
        # Radahn Foot Soldier (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x210(89000020, 1047600394, 1)
            return 0
        # Radahn Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x210(89000021, 1047600394, 0)
            return 0
        # Haligtree Foot Soldier (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x210(89000020, 1047600396, 1)
            return 0
        # Haligtree Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x210(89000021, 1047600396, 0)
            return 0
        # Nox Swordstress (ON)
        elif GetTalkListEntryResult() == 154:
            assert t608001110_x210(89000020, 1047600084, 1)
            return 0
        # Nox Swordstress (OFF)
        elif GetTalkListEntryResult() == 554:
            assert t608001110_x210(89000021, 1047600084, 0)
            return 0
        # Nox Swordstress (Altered) (ON)
        elif GetTalkListEntryResult() == 155:
            assert t608001110_x210(89000020, 1047600086, 1)
            return 0
        # Nox Swordstress (Altered) (OFF)
        elif GetTalkListEntryResult() == 555:
            assert t608001110_x210(89000021, 1047600086, 0)
            return 0
        # Night Maiden (ON)
        elif GetTalkListEntryResult() == 156:
            assert t608001110_x210(89000020, 1047600088, 1)
            return 0
        # Night Maiden (OFF)
        elif GetTalkListEntryResult() == 556:
            assert t608001110_x210(89000021, 1047600088, 0)
            return 0
        # Confessor (ON)
        elif GetTalkListEntryResult() == 157:
            assert t608001110_x210(89000020, 1047600260, 1)
            return 0
        # Confessor (OFF)
        elif GetTalkListEntryResult() == 557:
            assert t608001110_x210(89000021, 1047600260, 0)
            return 0
        # Confessor (Altered) (ON)
        elif GetTalkListEntryResult() == 158:
            assert t608001110_x210(89000020, 1047600262, 1)
            return 0
        # Confessor (Altered) (OFF)
        elif GetTalkListEntryResult() == 558:
            assert t608001110_x210(89000021, 1047600262, 0)
            return 0
        # Nox Monk (ON)
        elif GetTalkListEntryResult() == 159:
            assert t608001110_x210(89000020, 1047600080, 1)
            return 0
        # Nox Monk (OFF)
        elif GetTalkListEntryResult() == 559:
            assert t608001110_x210(89000021, 1047600080, 0)
            return 0
        # Nox Monk (Altered) (ON)
        elif GetTalkListEntryResult() == 160:
            assert t608001110_x210(89000020, 1047600082, 1)
            return 0
        # Nox Monk (Altered) (OFF)
        elif GetTalkListEntryResult() == 560:
            assert t608001110_x210(89000021, 1047600082, 0)
            return 0
        # Vulgar Militia (ON)
        elif GetTalkListEntryResult() == 161:
            assert t608001110_x210(89000020, 1047600122, 1)
            return 0
        # Vulgar Militia (OFF)
        elif GetTalkListEntryResult() == 561:
            assert t608001110_x210(89000021, 1047600122, 0)
            return 0
        # Ragged (ON)
        elif GetTalkListEntryResult() == 162:
            assert t608001110_x210(89000020, 1047600163, 1)
            return 0
        # Ragged (OFF)
        elif GetTalkListEntryResult() == 562:
            assert t608001110_x210(89000021, 1047600163, 0)
            return 0
        # Ragged (Altered) (ON)
        elif GetTalkListEntryResult() == 163:
            assert t608001110_x210(89000020, 1047600165, 1)
            return 0
        # Ragged (Altered) (OFF)
        elif GetTalkListEntryResult() == 563:
            assert t608001110_x210(89000021, 1047600165, 0)
            return 0
        # Blue Cloth (ON)
        elif GetTalkListEntryResult() == 164:
            assert t608001110_x210(89000020, 1047600190, 1)
            return 0
        # Blue Cloth (OFF)
        elif GetTalkListEntryResult() == 564:
            assert t608001110_x210(89000021, 1047600190, 0)
            return 0
        # Omenkiller (ON)
        elif GetTalkListEntryResult() == 165:
            assert t608001110_x210(89000020, 1047600398, 1)
            return 0
        # Omenkiller (OFF)
        elif GetTalkListEntryResult() == 565:
            assert t608001110_x210(89000021, 1047600398, 0)
            return 0
        # Leather (ON)
        elif GetTalkListEntryResult() == 166:
            assert t608001110_x210(89000020, 1047600342, 1)
            return 0
        # Leather (OFF)
        elif GetTalkListEntryResult() == 566:
            assert t608001110_x210(89000021, 1047600342, 0)
            return 0
        # War Surgeon (ON)
        elif GetTalkListEntryResult() == 167:
            assert t608001110_x210(89000020, 1047600192, 1)
            return 0
        # War Surgeon (OFF)
        elif GetTalkListEntryResult() == 567:
            assert t608001110_x210(89000021, 1047600192, 0)
            return 0
        # War Surgeon (Altered) (ON)
        elif GetTalkListEntryResult() == 168:
            assert t608001110_x210(89000020, 1047600194, 1)
            return 0
        # War Surgeon (Altered) (OFF)
        elif GetTalkListEntryResult() == 568:
            assert t608001110_x210(89000021, 1047600194, 0)
            return 0
        # Raptor (ON)
        elif GetTalkListEntryResult() == 169:
            assert t608001110_x210(89000020, 1047600280, 1)
            return 0
        # Raptor (OFF)
        elif GetTalkListEntryResult() == 569:
            assert t608001110_x210(89000021, 1047600280, 0)
            return 0
        # Preceptor (ON)
        elif GetTalkListEntryResult() == 170:
            assert t608001110_x210(89000020, 1047600275, 1)
            return 0
        # Preceptor (OFF)
        elif GetTalkListEntryResult() == 570:
            assert t608001110_x210(89000021, 1047600275, 0)
            return 0
        # Preceptor (Altered) (ON)
        elif GetTalkListEntryResult() == 171:
            assert t608001110_x210(89000020, 1047600277, 1)
            return 0
        # Preceptor (Altered) (OFF)
        elif GetTalkListEntryResult() == 571:
            assert t608001110_x210(89000021, 1047600277, 0)
            return 0
        # Rotten Duelist (ON)
        elif GetTalkListEntryResult() == 172:
            assert t608001110_x210(89000020, 1047600415, 1)
            return 0
        # Rotten Duelist (OFF)
        elif GetTalkListEntryResult() == 572:
            assert t608001110_x210(89000021, 1047600415, 0)
            return 0
        # Rotten Duelist (Altered) (ON)
        elif GetTalkListEntryResult() == 173:
            assert t608001110_x210(89000020, 1047600417, 1)
            return 0
        # Rotten Duelist (Altered) (OFF)
        elif GetTalkListEntryResult() == 573:
            assert t608001110_x210(89000021, 1047600417, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Head: Light Armor
def t608001110_x63():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Nomadic Merchant (ON)
        AddTalkListDataIf(GetEventFlag(1047600066) == 0, 101, 89001500, -1)
        # Nomadic Merchant (OFF)
        AddTalkListDataIf(GetEventFlag(1047600066) == 1, 501, 89001500, -1)

        # Nomadic Merchant (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600068) == 0, 102, 89001501, -1)
        # Nomadic Merchant (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600068) == 1, 502, 89001501, -1)

        # Azur (ON)
        AddTalkListDataIf(GetEventFlag(1047600153) == 0, 103, 89001502, -1)
        # Azur (OFF)
        AddTalkListDataIf(GetEventFlag(1047600153) == 1, 503, 89001502, -1)

        # Lusat (ON)
        AddTalkListDataIf(GetEventFlag(1047600151) == 0, 104, 89001503, -1)
        # Lusat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600151) == 1, 504, 89001503, -1)

        # Crimson Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600209) == 0, 105, 89001504, -1)
        # Crimson Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600209) == 1, 505, 89001504, -1)

        # Prisoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600264) == 0, 106, 89001505, -1)
        # Prisoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600264) == 1, 506, 89001505, -1)

        # Champion (ON)
        AddTalkListDataIf(GetEventFlag(1047600207) == 0, 107, 89001506, -1)
        # Champion (OFF)
        AddTalkListDataIf(GetEventFlag(1047600207) == 1, 507, 89001506, -1)

        # Highwayman (ON)
        AddTalkListDataIf(GetEventFlag(1047600409) == 0, 108, 89001507, -1)
        # Highwayman (OFF)
        AddTalkListDataIf(GetEventFlag(1047600409) == 1, 508, 89001507, -1)

        # Depraved Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600141) == 0, 109, 89001508, -1)
        # Depraved Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600141) == 1, 509, 89001508, -1)

        # Depraved Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600143) == 0, 110, 89001509, -1)
        # Depraved Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600143) == 1, 510, 89001509, -1)

        # Astrologer (ON)
        AddTalkListDataIf(GetEventFlag(1047600172) == 0, 111, 89001510, -1)
        # Astrologer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600172) == 1, 511, 89001510, -1)

        # Astrologer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600174) == 0, 112, 89001511, -1)
        # Astrologer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600174) == 1, 512, 89001511, -1)

        # Albinauric (ON)
        AddTalkListDataIf(GetEventFlag(1047600320) == 0, 113, 89001512, -1)
        # Albinauric (OFF)
        AddTalkListDataIf(GetEventFlag(1047600320) == 1, 513, 89001512, -1)

        # Marionette Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600247) == 0, 114, 89001513, -1)
        # Marionette Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600247) == 1, 514, 89001513, -1)

        # Godskin Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600139) == 0, 115, 89001514, -1)
        # Godskin Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600139) == 1, 515, 89001514, -1)

        # Mushroom (ON)
        AddTalkListDataIf(GetEventFlag(1047600338) == 0, 116, 89001515, -1)
        # Mushroom (OFF)
        AddTalkListDataIf(GetEventFlag(1047600338) == 1, 516, 89001515, -1)

        # Ancestral Fur (ON)
        AddTalkListDataIf(GetEventFlag(1047600090) == 0, 117, 89001516, -1)
        # Ancestral Fur (OFF)
        AddTalkListDataIf(GetEventFlag(1047600090) == 1, 517, 89001516, -1)

        # Ancestral Shaman (ON)
        AddTalkListDataIf(GetEventFlag(1047600092) == 0, 118, 89001517, -1)
        # Ancestral Shaman (OFF)
        AddTalkListDataIf(GetEventFlag(1047600092) == 1, 518, 89001517, -1)

        # Errant Sorcerer (ON)
        AddTalkListDataIf(GetEventFlag(1047600306) == 0, 119, 89001518, -1)
        # Errant Sorcerer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600306) == 1, 519, 89001518, -1)

        # Errant Sorcerer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600308) == 0, 120, 89001519, -1)
        # Errant Sorcerer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600308) == 1, 520, 89001519, -1)

        # Traveling Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600267) == 0, 121, 89001520, -1)
        # Traveling Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600267) == 1, 521, 89001520, -1)

        # Traveling Maiden (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600269) == 0, 122, 89001521, -1)
        # Traveling Maiden (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600269) == 1, 522, 89001521, -1)

        # Queen (ON)
        AddTalkListDataIf(GetEventFlag(1047600135) == 0, 123, 89001522, -1)
        # Queen (OFF)
        AddTalkListDataIf(GetEventFlag(1047600135) == 1, 523, 89001522, -1)

        # Finger Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600271) == 0, 124, 89001523, -1)
        # Finger Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600271) == 1, 524, 89001523, -1)

        # Finger Maiden (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600273) == 0, 125, 89001524, -1)
        # Finger Maiden (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600273) == 1, 525, 89001524, -1)

        # Godskin Apostle (ON)
        AddTalkListDataIf(GetEventFlag(1047600137) == 0, 126, 89001525, -1)
        # Godskin Apostle (OFF)
        AddTalkListDataIf(GetEventFlag(1047600137) == 1, 526, 89001525, -1)

        # Snow Witch (ON)
        AddTalkListDataIf(GetEventFlag(1047600312) == 0, 127, 89001526, -1)
        # Snow Witch (OFF)
        AddTalkListDataIf(GetEventFlag(1047600312) == 1, 527, 89001526, -1)

        # Snow Witch (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600314) == 0, 128, 89001527, -1)
        # Snow Witch (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600314) == 1, 528, 89001527, -1)

        # Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600012) == 0, 129, 89001528, -1)
        # Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600012) == 1, 529, 89001528, -1)

        # Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600014) == 0, 130, 89001529, -1)
        # Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600014) == 1, 530, 89001529, -1)

        # Prophet (ON)
        AddTalkListDataIf(GetEventFlag(1047600167) == 0, 131, 89001530, -1)
        # Prophet (OFF)
        AddTalkListDataIf(GetEventFlag(1047600167) == 1, 531, 89001530, -1)

        # Prophet (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600169) == 0, 132, 89001531, -1)
        # Prophet (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600169) == 1, 532, 89001531, -1)

        # Battlemage (ON)
        AddTalkListDataIf(GetEventFlag(1047600310) == 0, 133, 89001532, -1)
        # Battlemage (OFF)
        AddTalkListDataIf(GetEventFlag(1047600310) == 1, 533, 89001532, -1)

        # Consort (ON)
        AddTalkListDataIf(GetEventFlag(1047600290) == 0, 134, 89001533, -1)
        # Consort (OFF)
        AddTalkListDataIf(GetEventFlag(1047600290) == 1, 534, 89001533, -1)

        # Sage (ON)
        AddTalkListDataIf(GetEventFlag(1047600124) == 0, 135, 89001534, -1)
        # Sage (OFF)
        AddTalkListDataIf(GetEventFlag(1047600124) == 1, 535, 89001534, -1)

        # Goldmask (ON)
        AddTalkListDataIf(GetEventFlag(1047600318) == 0, 136, 89001535, -1)
        # Goldmask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600318) == 1, 536, 89001535, -1)

        # Alberich (ON)
        AddTalkListDataIf(GetEventFlag(1047600020) == 0, 137, 89001536, -1)
        # Alberich (OFF)
        AddTalkListDataIf(GetEventFlag(1047600020) == 1, 537, 89001536, -1)

        # Alberich (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600022) == 0, 138, 89001537, -1)
        # Alberich (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600022) == 1, 538, 89001537, -1)

        # Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600116) == 0, 139, 89001538, -1)
        # Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600116) == 1, 539, 89001538, -1)

        # Wandering Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600118) == 0, 140, 89001539, -1)
        # Wandering Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600118) == 1, 540, 89001539, -1)

        # Old Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600120) == 0, 141, 89001540, -1)
        # Old Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600120) == 1, 541, 89001540, -1)

        # Page (ON)
        AddTalkListDataIf(GetEventFlag(1047600054) == 0, 142, 89001541, -1)
        # Page (OFF)
        AddTalkListDataIf(GetEventFlag(1047600054) == 1, 542, 89001541, -1)

        # Page (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600056) == 0, 143, 89001542, -1)
        # Page (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600056) == 1, 543, 89001542, -1)

        # Sanguine Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600098) == 0, 144, 89001543, -1)
        # Sanguine Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600098) == 1, 544, 89001543, -1)

        # Brave (ON)
        AddTalkListDataIf(GetEventFlag(1047600198) == 0, 145, 89001544, -1)
        # Brave (OFF)
        AddTalkListDataIf(GetEventFlag(1047600198) == 1, 545, 89001544, -1)

        # Brave (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600200) == 0, 146, 89001545, -1)
        # Brave (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600200) == 1, 546, 89001545, -1)

        # Travelling Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600016) == 0, 147, 89001546, -1)
        # Travelling Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600016) == 1, 547, 89001546, -1)

        # Travelling Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600018) == 0, 148, 89001547, -1)
        # Travelling Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600018) == 1, 548, 89001547, -1)

        # Spellblade (ON)
        AddTalkListDataIf(GetEventFlag(1047600024) == 0, 149, 89001548, -1)
        # Spellblade (OFF)
        AddTalkListDataIf(GetEventFlag(1047600024) == 1, 549, 89001548, -1)

        # Spellblade (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600026) == 0, 150, 89001549, -1)
        # Spellblade (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600026) == 1, 550, 89001549, -1)

        # Commoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600234) == 0, 151, 89001550, -1)
        # Commoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600234) == 1, 551, 89001550, -1)

        # Commoner (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600236) == 0, 152, 89001551, -1)
        # Commoner (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600236) == 1, 552, 89001551, -1)

        # Simple Commoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600238) == 0, 153, 89001552, -1)
        # Simple Commoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600238) == 1, 553, 89001552, -1)

        # Ruler (ON)
        AddTalkListDataIf(GetEventFlag(1047600292) == 0, 154, 89001553, -1)
        # Ruler (OFF)
        AddTalkListDataIf(GetEventFlag(1047600292) == 1, 554, 89001553, -1)

        # Upper-Class (ON)
        AddTalkListDataIf(GetEventFlag(1047600294) == 0, 155, 89001554, -1)
        # Upper-Class (OFF)
        AddTalkListDataIf(GetEventFlag(1047600294) == 1, 555, 89001554, -1)

        # Fia (ON)
        AddTalkListDataIf(GetEventFlag(1047600405) == 0, 156, 89001555, -1)
        # Fia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600405) == 1, 556, 89001555, -1)

        # Fia (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600407) == 0, 157, 89001556, -1)
        # Fia (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600407) == 1, 557, 89001556, -1)

        # High Page (ON)
        AddTalkListDataIf(GetEventFlag(1047600411) == 0, 158, 89001557, -1)
        # High Page (OFF)
        AddTalkListDataIf(GetEventFlag(1047600411) == 1, 558, 89001557, -1)

        # High Page (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600413) == 0, 159, 89001558, -1)
        # High Page (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600413) == 1, 559, 89001558, -1)

        # Guilty (ON)
        AddTalkListDataIf(GetEventFlag(1047600034) == 0, 160, 89001559, -1)
        # Guilty (OFF)
        AddTalkListDataIf(GetEventFlag(1047600034) == 1, 560, 89001559, -1)

        # Marais (ON)
        AddTalkListDataIf(GetEventFlag(1047600296) == 0, 161, 89001560, -1)
        # Marais (OFF)
        AddTalkListDataIf(GetEventFlag(1047600296) == 1, 561, 89001560, -1)

        # Bloodsoaked (ON)
        AddTalkListDataIf(GetEventFlag(1047600298) == 0, 162, 89001561, -1)
        # Bloodsoaked (OFF)
        AddTalkListDataIf(GetEventFlag(1047600298) == 1, 562, 89001561, -1)

        # Festive (ON)
        AddTalkListDataIf(GetEventFlag(1047600228) == 0, 163, 89001562, -1)
        # Festive (OFF)
        AddTalkListDataIf(GetEventFlag(1047600228) == 1, 563, 89001562, -1)

        # Festive (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600230) == 0, 164, 89001563, -1)
        # Festive (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600230) == 1, 564, 89001563, -1)

        # Blue Festive (ON)
        AddTalkListDataIf(GetEventFlag(1047600232) == 0, 165, 89001564, -1)
        # Blue Festive (OFF)
        AddTalkListDataIf(GetEventFlag(1047600232) == 1, 565, 89001564, -1)

        # Juvenile Scholar (ON)
        AddTalkListDataIf(GetEventFlag(1047600316) == 0, 166, 89001565, -1)
        # Juvenile Scholar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600316) == 1, 566, 89001565, -1)

        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Nomadic Merchant (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x210(89000020, 1047600066, 1)
            return 0
        # Nomadic Merchant (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x210(89000021, 1047600066, 0)
            return 0
        # Nomadic Merchant (Altered) (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x210(89000020, 1047600068, 1)
            return 0
        # Nomadic Merchant (Altered) (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x210(89000021, 1047600068, 0)
            return 0
        # Azur (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x210(89000020, 1047600153, 1)
            return 0
        # Azur (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x210(89000021, 1047600153, 0)
            return 0
        # Lusat (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x210(89000020, 1047600151, 1)
            return 0
        # Lusat (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x210(89000021, 1047600151, 0)
            return 0
        # Crimson Noble (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x210(89000020, 1047600209, 1)
            return 0
        # Crimson Noble (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x210(89000021, 1047600209, 0)
            return 0
        # Prisoner (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x210(89000020, 1047600264, 1)
            return 0
        # Prisoner (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x210(89000021, 1047600264, 0)
            return 0
        # Champion (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x210(89000020, 1047600207, 1)
            return 0
        # Champion (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x210(89000021, 1047600207, 0)
            return 0
        # Highwayman (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x210(89000020, 1047600409, 1)
            return 0
        # Highwayman (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x210(89000021, 1047600409, 0)
            return 0
        # Depraved Perfumer (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x210(89000020, 1047600141, 1)
            return 0
        # Depraved Perfumer (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x210(89000021, 1047600141, 0)
            return 0
        # Depraved Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x210(89000020, 1047600143, 1)
            return 0
        # Depraved Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x210(89000021, 1047600143, 0)
            return 0
        # Astrologer (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x210(89000020, 1047600172, 1)
            return 0
        # Astrologer (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x210(89000021, 1047600172, 0)
            return 0
        # Astrologer (Altered) (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x210(89000020, 1047600174, 1)
            return 0
        # Astrologer (Altered) (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x210(89000021, 1047600174, 0)
            return 0
        # Albinauric (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x210(89000020, 1047600320, 1)
            return 0
        # Albinauric (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x210(89000021, 1047600320, 0)
            return 0
        # Marionette Soldier (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x210(89000020, 1047600247, 1)
            return 0
        # Marionette Soldier (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x210(89000021, 1047600247, 0)
            return 0
        # Godskin Noble (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x210(89000020, 1047600139, 1)
            return 0
        # Godskin Noble (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x210(89000021, 1047600139, 0)
            return 0
        # Mushroom (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x210(89000020, 1047600338, 1)
            return 0
        # Mushroom (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x210(89000021, 1047600338, 0)
            return 0
        # Ancestral Fur (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x210(89000020, 1047600090, 1)
            return 0
        # Ancestral Fur (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x210(89000021, 1047600090, 0)
            return 0
        # Ancestral Shaman (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x210(89000020, 1047600092, 1)
            return 0
        # Ancestral Shaman (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x210(89000021, 1047600092, 0)
            return 0
        # Errant Sorcerer (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x210(89000020, 1047600306, 1)
            return 0
        # Errant Sorcerer (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x210(89000021, 1047600306, 0)
            return 0
        # Errant Sorcerer (Altered) (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x210(89000020, 1047600308, 1)
            return 0
        # Errant Sorcerer (Altered) (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x210(89000021, 1047600308, 0)
            return 0
        # Traveling Maiden (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x210(89000020, 1047600267, 1)
            return 0
        # Traveling Maiden (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x210(89000021, 1047600267, 0)
            return 0
        # Traveling Maiden (Altered) (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x210(89000020, 1047600269, 1)
            return 0
        # Traveling Maiden (Altered) (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x210(89000021, 1047600269, 0)
            return 0
        # Queen (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x210(89000020, 1047600135, 1)
            return 0
        # Queen (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x210(89000021, 1047600135, 0)
            return 0
        # Finger Maiden (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x210(89000020, 1047600271, 1)
            return 0
        # Finger Maiden (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x210(89000021, 1047600271, 0)
            return 0
        # Finger Maiden (Altered) (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x210(89000020, 1047600273, 1)
            return 0
        # Finger Maiden (Altered) (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x210(89000021, 1047600273, 0)
            return 0
        # Godskin Apostle (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x210(89000020, 1047600137, 1)
            return 0
        # Godskin Apostle (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x210(89000021, 1047600137, 0)
            return 0
        # Snow Witch (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x210(89000020, 1047600312, 1)
            return 0
        # Snow Witch (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x210(89000021, 1047600312, 0)
            return 0
        # Snow Witch (Altered) (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x210(89000020, 1047600314, 1)
            return 0
        # Snow Witch (Altered) (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x210(89000021, 1047600314, 0)
            return 0
        # Perfumer (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x210(89000020, 1047600012, 1)
            return 0
        # Perfumer (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x210(89000021, 1047600012, 0)
            return 0
        # Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x210(89000020, 1047600014, 1)
            return 0
        # Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x210(89000021, 1047600014, 0)
            return 0
        # Prophet (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x210(89000020, 1047600167, 1)
            return 0
        # Prophet (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x210(89000021, 1047600167, 0)
            return 0
        # Prophet (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x210(89000020, 1047600169, 1)
            return 0
        # Prophet (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x210(89000021, 1047600169, 0)
            return 0
        # Battlemage (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x210(89000020, 1047600310, 1)
            return 0
        # Battlemage (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x210(89000021, 1047600310, 0)
            return 0
        # Consort (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x210(89000020, 1047600290, 1)
            return 0
        # Consort (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x210(89000021, 1047600290, 0)
            return 0
        # Sage (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x210(89000020, 1047600124, 1)
            return 0
        # Sage (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x210(89000021, 1047600124, 0)
            return 0
        # Goldmask (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x210(89000020, 1047600318, 1)
            return 0
        # Goldmask (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x210(89000021, 1047600318, 0)
            return 0
        # Alberich (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x210(89000020, 1047600020, 1)
            return 0
        # Alberich (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x210(89000021, 1047600020, 0)
            return 0
        # Alberich (Altered) (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x210(89000020, 1047600022, 1)
            return 0
        # Alberich (Altered) (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x210(89000021, 1047600022, 0)
            return 0
        # Aristocrat (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x210(89000020, 1047600116, 1)
            return 0
        # Aristocrat (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x210(89000021, 1047600116, 0)
            return 0
        # Wandering Aristocrat (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x210(89000020, 1047600118, 1)
            return 0
        # Wandering Aristocrat (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x210(89000021, 1047600118, 0)
            return 0
        # Old Aristocrat (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x210(89000020, 1047600120, 1)
            return 0
        # Old Aristocrat (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x210(89000021, 1047600120, 0)
            return 0
        # Page (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x210(89000020, 1047600054, 1)
            return 0
        # Page (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x210(89000021, 1047600054, 0)
            return 0
        # Page (Altered) (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x210(89000020, 1047600056, 1)
            return 0
        # Page (Altered) (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x210(89000021, 1047600056, 0)
            return 0
        # Sanguine Noble (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x210(89000020, 1047600098, 1)
            return 0
        # Sanguine Noble (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x210(89000021, 1047600098, 0)
            return 0
        # Brave (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x210(89000020, 1047600198, 1)
            return 0
        # Brave (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x210(89000021, 1047600198, 0)
            return 0
        # Brave (Altered) (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x210(89000020, 1047600200, 1)
            return 0
        # Brave (Altered) (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x210(89000021, 1047600200, 0)
            return 0
        # Travelling Perfumer (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x210(89000020, 1047600016, 1)
            return 0
        # Travelling Perfumer (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x210(89000021, 1047600016, 0)
            return 0
        # Travelling Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x210(89000020, 1047600018, 1)
            return 0
        # Travelling Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x210(89000021, 1047600018, 0)
            return 0
        # Spellblade (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x210(89000020, 1047600024, 1)
            return 0
        # Spellblade (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x210(89000021, 1047600024, 0)
            return 0
        # Spellblade (Altered) (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x210(89000020, 1047600026, 1)
            return 0
        # Spellblade (Altered) (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x210(89000021, 1047600026, 0)
            return 0
        # Commoner (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x210(89000020, 1047600234, 1)
            return 0
        # Commoner (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x210(89000021, 1047600234, 0)
            return 0
        # Commoner (Altered) (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x210(89000020, 1047600236, 1)
            return 0
        # Commoner (Altered) (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x210(89000021, 1047600236, 0)
            return 0
        # Simple Commoner (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x210(89000020, 1047600238, 1)
            return 0
        # Simple Commoner (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x210(89000021, 1047600238, 0)
            return 0
        # Ruler (ON)
        elif GetTalkListEntryResult() == 154:
            assert t608001110_x210(89000020, 1047600292, 1)
            return 0
        # Ruler (OFF)
        elif GetTalkListEntryResult() == 554:
            assert t608001110_x210(89000021, 1047600292, 0)
            return 0
        # Upper-Class (ON)
        elif GetTalkListEntryResult() == 155:
            assert t608001110_x210(89000020, 1047600294, 1)
            return 0
        # Upper-Class (OFF)
        elif GetTalkListEntryResult() == 555:
            assert t608001110_x210(89000021, 1047600294, 0)
            return 0
        # Fia (ON)
        elif GetTalkListEntryResult() == 156:
            assert t608001110_x210(89000020, 1047600405, 1)
            return 0
        # Fia (OFF)
        elif GetTalkListEntryResult() == 556:
            assert t608001110_x210(89000021, 1047600405, 0)
            return 0
        # Fia (Altered) (ON)
        elif GetTalkListEntryResult() == 157:
            assert t608001110_x210(89000020, 1047600407, 1)
            return 0
        # Fia (Altered) (OFF)
        elif GetTalkListEntryResult() == 557:
            assert t608001110_x210(89000021, 1047600407, 0)
            return 0
        # High Page (ON)
        elif GetTalkListEntryResult() == 158:
            assert t608001110_x210(89000020, 1047600411, 1)
            return 0
        # High Page (OFF)
        elif GetTalkListEntryResult() == 558:
            assert t608001110_x210(89000021, 1047600411, 0)
            return 0
        # High Page (Altered) (ON)
        elif GetTalkListEntryResult() == 159:
            assert t608001110_x210(89000020, 1047600413, 1)
            return 0
        # High Page (Altered) (OFF)
        elif GetTalkListEntryResult() == 559:
            assert t608001110_x210(89000021, 1047600413, 0)
            return 0
        # Guilty (ON)
        elif GetTalkListEntryResult() == 160:
            assert t608001110_x210(89000020, 1047600034, 1)
            return 0
        # Guilty (OFF)
        elif GetTalkListEntryResult() == 560:
            assert t608001110_x210(89000021, 1047600034, 0)
            return 0
        # Marais (ON)
        elif GetTalkListEntryResult() == 161:
            assert t608001110_x210(89000020, 1047600296, 1)
            return 0
        # Marais (OFF)
        elif GetTalkListEntryResult() == 561:
            assert t608001110_x210(89000021, 1047600296, 0)
            return 0
        # Bloodsoaked (ON)
        elif GetTalkListEntryResult() == 162:
            assert t608001110_x210(89000020, 1047600298, 1)
            return 0
        # Bloodsoaked (OFF)
        elif GetTalkListEntryResult() == 562:
            assert t608001110_x210(89000021, 1047600298, 0)
            return 0
        # Festive (ON)
        elif GetTalkListEntryResult() == 163:
            assert t608001110_x210(89000020, 1047600228, 1)
            return 0
        # Festive (OFF)
        elif GetTalkListEntryResult() == 563:
            assert t608001110_x210(89000021, 1047600228, 0)
            return 0
        # Festive (Altered) (ON)
        elif GetTalkListEntryResult() == 164:
            assert t608001110_x210(89000020, 1047600230, 1)
            return 0
        # Festive (Altered) (OFF)
        elif GetTalkListEntryResult() == 564:
            assert t608001110_x210(89000021, 1047600230, 0)
            return 0
        # Blue Festive (ON)
        elif GetTalkListEntryResult() == 165:
            assert t608001110_x210(89000020, 1047600232, 1)
            return 0
        # Blue Festive (OFF)
        elif GetTalkListEntryResult() == 565:
            assert t608001110_x210(89000021, 1047600232, 0)
            return 0
        # Juvenile Scholar (ON)
        elif GetTalkListEntryResult() == 166:
            assert t608001110_x210(89000020, 1047600316, 1)
            return 0
        # Juvenile Scholar (OFF)
        elif GetTalkListEntryResult() == 566:
            assert t608001110_x210(89000021, 1047600316, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Body
def t608001110_x52():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Unique Armor
        AddTalkListData(1, 89000013, -1)

        # Heavy Armor
        AddTalkListData(2, 89000010, -1)
        
        # Medium Armor
        AddTalkListData(3, 89000011, -1)
        
        # Light Armor
        AddTalkListData(4, 89000012, -1)
        
        # Reset body transmogrification
        AddTalkListData(5, 89000015, -1)
        
        # Leave
        AddTalkListData(99, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t608001110_x70()
            continue
        elif GetTalkListEntryResult() == 2:
            assert t608001110_x71()
            continue
        elif GetTalkListEntryResult() == 3:
            assert t608001110_x72()
            continue
        elif GetTalkListEntryResult() == 4:
            assert t608001110_x73()
            continue
        elif GetTalkListEntryResult() == 5:
            assert t608001110_x211(89000040, 1047610101, 1)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Body: Unique Armor
def t608001110_x70():
    while True:
        c1_110()
        ClearTalkListData()
        
        # None (ON)
        AddTalkListDataIf(GetEventFlag(1047600999) == 0, 100, 89001000, -1)
        # None (OFF)
        AddTalkListDataIf(GetEventFlag(1047600999) == 1, 500, 89001000, -1)
        
        # Lazuli Robe (ON)
        AddTalkListDataIf(GetEventFlag(1047600421) == 0, 101, 89001800, -1)
        # Lazuli Robe (OFF)
        AddTalkListDataIf(GetEventFlag(1047600421) == 1, 501, 89001800, -1)

        # Eye Surcoat (ON)
        AddTalkListDataIf(GetEventFlag(1047600334) == 0, 102, 89001801, -1)
        # Eye Surcoat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600334) == 1, 502, 89001801, -1)

        # Tree Surcoat (ON)
        AddTalkListDataIf(GetEventFlag(1047600335) == 0, 103, 89001802, -1)
        # Tree Surcoat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600335) == 1, 503, 89001802, -1)

        # Millicent (ON)
        AddTalkListDataIf(GetEventFlag(1047600423) == 0, 104, 89001803, -1)
        # Millicent (OFF)
        AddTalkListDataIf(GetEventFlag(1047600423) == 1, 504, 89001803, -1)

        # Rotten (ON)
        AddTalkListDataIf(GetEventFlag(1047600424) == 0, 105, 89001804, -1)
        # Rotten (OFF)
        AddTalkListDataIf(GetEventFlag(1047600424) == 1, 505, 89001804, -1)

        # Deathbed (ON)
        AddTalkListDataIf(GetEventFlag(1047600425) == 0, 106, 89001805, -1)
        # Deathbed (OFF)
        AddTalkListDataIf(GetEventFlag(1047600425) == 1, 506, 89001805, -1)

        # Disabled for now since it more of a layering piece
        # Fell Omen Cloak (ON)
        # AddTalkListDataIf(GetEventFlag(1047600426) == 0, 107, 89001806, -1)
        # Fell Omen Cloak (OFF)
        # AddTalkListDataIf(GetEventFlag(1047600426) == 1, 507, 89001806, -1)

        # Raya Lucaria Scholar (ON)
        AddTalkListDataIf(GetEventFlag(1047600242) == 0, 108, 89001807, -1)
        # Raya Lucaria Scholar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600242) == 1, 508, 89001807, -1)

        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # None (ON)
        if GetTalkListEntryResult() == 100:
            assert t608001110_x211(89000030, 1047600999, 1) 
            return 0
        # None (OFF)
        elif GetTalkListEntryResult() == 500:
            assert t608001110_x211(89000031, 1047600999, 0) 
            return 0
        # Lazuli Robe (ON)
        elif GetTalkListEntryResult() == 101:
            assert t608001110_x211(89000020, 1047600421, 1)
            return 0
        # Lazuli Robe (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x211(89000021, 1047600421, 0)
            return 0
        # Eye Surcoat (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x211(89000020, 1047600334, 1)
            return 0
        # Eye Surcoat (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x211(89000021, 1047600334, 0)
            return 0
        # Tree Surcoat (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x211(89000020, 1047600335, 1)
            return 0
        # Tree Surcoat (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x211(89000021, 1047600335, 0)
            return 0
        # Millicent (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x211(89000020, 1047600423, 1)
            return 0
        # Millicent (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x211(89000021, 1047600423, 0)
            return 0
        # Rotten (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x211(89000020, 1047600424, 1)
            return 0
        # Rotten (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x211(89000021, 1047600424, 0)
            return 0
        # Deathbed (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x211(89000020, 1047600425, 1)
            return 0
        # Deathbed (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x211(89000021, 1047600425, 0)
            return 0
        # Fell Omen Cloak (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x211(89000020, 1047600426, 1)
            return 0
        # Fell Omen Cloak (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x211(89000021, 1047600426, 0)
            return 0
        # Raya Lucaria Scholar (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x211(89000020, 1047600242, 1)
            return 0
        # Raya Lucaria Scholar (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x211(89000021, 1047600242, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Body: Heavy Armor
def t608001110_x71():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Bull-Goat (ON)
        AddTalkListDataIf(GetEventFlag(1047600029) == 0, 101, 89001100, -1)
        # Bull-Goat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600029) == 1, 501, 89001100, -1)

        # Fire Prelate (ON)
        AddTalkListDataIf(GetEventFlag(1047600113) == 0, 102, 89001101, -1)
        # Fire Prelate (OFF)
        AddTalkListDataIf(GetEventFlag(1047600113) == 1, 502, 89001101, -1)

        # Fire Prelate (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600115) == 0, 103, 89001102, -1)
        # Fire Prelate (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600115) == 1, 503, 89001102, -1)

        # Lionel (ON)
        AddTalkListDataIf(GetEventFlag(1047600177) == 0, 104, 89001103, -1)
        # Lionel (OFF)
        AddTalkListDataIf(GetEventFlag(1047600177) == 1, 504, 89001103, -1)

        # Lionel (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600179) == 0, 105, 89001105, -1)
        # Lionel (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600179) == 1, 505, 89001105, -1)

        # Omen (ON)
        AddTalkListDataIf(GetEventFlag(1047600301) == 0, 106, 89001104, -1)
        # Omen (OFF)
        AddTalkListDataIf(GetEventFlag(1047600301) == 1, 506, 89001104, -1)

        # Tree Sentinel (ON)
        AddTalkListDataIf(GetEventFlag(1047600073) == 0, 107, 89001106, -1)
        # Tree Sentinel (OFF)
        AddTalkListDataIf(GetEventFlag(1047600073) == 1, 507, 89001106, -1)

        # Tree Sentinel (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600075) == 0, 108, 89001107, -1)
        # Tree Sentinel (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600075) == 1, 508, 89001107, -1)

        # Veteran (ON)
        AddTalkListDataIf(GetEventFlag(1047600221) == 0, 109, 89001108, -1)
        # Veteran (OFF)
        AddTalkListDataIf(GetEventFlag(1047600221) == 1, 509, 89001108, -1)

        # Veteran (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600223) == 0, 110, 89001109, -1)
        # Veteran (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600223) == 1, 510, 89001109, -1)

        # Beast Champion (ON)
        AddTalkListDataIf(GetEventFlag(1047600204) == 0, 111, 89001110, -1)
        # Beast Champion (OFF)
        AddTalkListDataIf(GetEventFlag(1047600204) == 1, 511, 89001110, -1)

        # Beast Champion (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600206) == 0, 112, 89001111, -1)
        # Beast Champion (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600206) == 1, 512, 89001111, -1)

        # Banished Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600047) == 0, 113, 89001112, -1)
        # Banished Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600047) == 1, 513, 89001112, -1)

        # Banished Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600049) == 0, 114, 89001113, -1)
        # Banished Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600049) == 1, 514, 89001113, -1)

        # General Radahn (ON)
        AddTalkListDataIf(GetEventFlag(1047600132) == 0, 115, 89001114, -1)
        # General Radahn (OFF)
        AddTalkListDataIf(GetEventFlag(1047600132) == 1, 515, 89001114, -1)

        # General Radahn (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600134) == 0, 116, 89001115, -1)
        # General Radahn (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600134) == 1, 516, 89001115, -1)

        # Malformed Dragon (ON)
        AddTalkListDataIf(GetEventFlag(1047600071) == 0, 117, 89001116, -1)
        # Malformed Dragon (OFF)
        AddTalkListDataIf(GetEventFlag(1047600071) == 1, 517, 89001116, -1)

        # Scaled (ON)
        AddTalkListDataIf(GetEventFlag(1047600009) == 0, 118, 89001117, -1)
        # Scaled (OFF)
        AddTalkListDataIf(GetEventFlag(1047600009) == 1, 518, 89001117, -1)

        # Scaled (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600011) == 0, 119, 89001118, -1)
        # Scaled (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600011) == 1, 519, 89001118, -1)

        # Crucible Axe (ON)
        AddTalkListDataIf(GetEventFlag(1047600146) == 0, 120, 89001119, -1)
        # Crucible Axe (OFF)
        AddTalkListDataIf(GetEventFlag(1047600146) == 1, 520, 89001119, -1)

        # Crucible Axe (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600148) == 0, 121, 89001120, -1)
        # Crucible Axe (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600148) == 1, 521, 89001120, -1)

        # Crucible Tree (ON)
        AddTalkListDataIf(GetEventFlag(1047600150) == 0, 122, 89001121, -1)
        # Crucible Tree (OFF)
        AddTalkListDataIf(GetEventFlag(1047600150) == 1, 522, 89001121, -1)

        # Royal Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600077) == 0, 123, 89001122, -1)
        # Royal Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600077) == 1, 523, 89001122, -1)

        # Royal Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600079) == 0, 124, 89001123, -1)
        # Royal Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600079) == 1, 524, 89001123, -1)

        # Cleanrot (ON)
        AddTalkListDataIf(GetEventFlag(1047600105) == 0, 125, 89001124, -1)
        # Cleanrot (OFF)
        AddTalkListDataIf(GetEventFlag(1047600105) == 1, 525, 89001124, -1)

        # Cleanrot (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600107) == 0, 126, 89001125, -1)
        # Cleanrot (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600107) == 1, 526, 89001125, -1)

        # Blaidd (ON)
        AddTalkListDataIf(GetEventFlag(1047600037) == 0, 127, 89001126, -1)
        # Blaidd (OFF)
        AddTalkListDataIf(GetEventFlag(1047600037) == 1, 527, 89001126, -1)

        # Blaidd (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600039) == 0, 128, 89001127, -1)
        # Blaidd (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600039) == 1, 528, 89001127, -1)

        # Night's Cavalry (ON)
        AddTalkListDataIf(GetEventFlag(1047600059) == 0, 129, 89001128, -1)
        # Night's Cavalry (OFF)
        AddTalkListDataIf(GetEventFlag(1047600059) == 1, 529, 89001128, -1)

        # Night's Cavalry (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600061) == 0, 130, 89001129, -1)
        # Night's Cavalry (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600061) == 1, 530, 89001129, -1)

        # Maliketh (ON)
        AddTalkListDataIf(GetEventFlag(1047600213) == 0, 131, 89001130, -1)
        # Maliketh (OFF)
        AddTalkListDataIf(GetEventFlag(1047600213) == 1, 531, 89001130, -1)

        # Maliketh (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600215) == 0, 132, 89001131, -1)
        # Maliketh (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600215) == 1, 532, 89001131, -1)

        # Twinned (ON)
        AddTalkListDataIf(GetEventFlag(1047600160) == 0, 133, 89001132, -1)
        # Twinned (OFF)
        AddTalkListDataIf(GetEventFlag(1047600160) == 1, 533, 89001132, -1)

        # Twinned (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600162) == 0, 134, 89001133, -1)
        # Twinned (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600162) == 1, 534, 89001133, -1)

        # Hoslow (ON)
        AddTalkListDataIf(GetEventFlag(1047600181) == 0, 135, 89001134, -1)
        # Hoslow (OFF)
        AddTalkListDataIf(GetEventFlag(1047600181) == 1, 535, 89001134, -1)

        # Hoslow (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600185) == 0, 136, 89001135, -1)
        # Hoslow (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600185) == 1, 536, 89001135, -1)

        # Cuckoo Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600369) == 0, 137, 89001136, -1)
        # Cuckoo Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600369) == 1, 537, 89001136, -1)

        # Cuckoo Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600371) == 0, 138, 89001137, -1)
        # Cuckoo Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600371) == 1, 538, 89001137, -1)

        # Briar (ON)
        AddTalkListDataIf(GetEventFlag(1047600051) == 0, 139, 89001138, -1)
        # Briar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600051) == 1, 539, 89001138, -1)

        # Briar (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600053) == 0, 140, 89001139, -1)
        # Briar (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600053) == 1, 540, 89001139, -1)

        # Godrick Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600365) == 0, 141, 89001140, -1)
        # Godrick Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600365) == 1, 541, 89001140, -1)

        # Godrick Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600367) == 0, 142, 89001141, -1)
        # Godrick Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600367) == 1, 542, 89001141, -1)

        # Redmane Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600377) == 0, 143, 89001142, -1)
        # Redmane Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600377) == 1, 543, 89001142, -1)

        # Redmane Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600379) == 0, 144, 89001143, -1)
        # Redmane Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600379) == 1, 544, 89001143, -1)

        # Gelmir Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600361) == 0, 145, 89001144, -1)
        # Gelmir Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600361) == 1, 545, 89001144, -1)

        # Gelmir Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600363) == 0, 146, 89001145, -1)
        # Gelmir Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600363) == 1, 546, 89001145, -1)

        # Leyndell Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600373) == 0, 147, 89001146, -1)
        # Leyndell Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600373) == 1, 547, 89001146, -1)

        # Leyndell Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600375) == 0, 148, 89001147, -1)
        # Leyndell Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600375) == 1, 548, 89001147, -1)

        # Haligtree Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600385) == 0, 149, 89001148, -1)
        # Haligtree Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600385) == 1, 549, 89001148, -1)

        # Haligtree Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600387) == 0, 150, 89001149, -1)
        # Haligtree Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600387) == 1, 550, 89001149, -1)

        # Blackflame Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600111) == 0, 151, 89001150, -1)
        # Blackflame Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600111) == 1, 551, 89001150, -1)

        # Fire Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600109) == 0, 152, 89001151, -1)
        # Fire Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600109) == 1, 552, 89001151, -1)

        # Giant (ON)
        AddTalkListDataIf(GetEventFlag(1047600431) == 0, 153, 89001152, -1)
        # Giant (OFF)
        AddTalkListDataIf(GetEventFlag(1047600431) == 1, 553, 89001152, -1)
        
        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Bull-Goat (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x211(89000020, 1047600029, 1)
            return 0
        # Bull-Goat (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x211(89000021, 1047600029, 0)
            return 0
        # Fire Prelate (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x211(89000020, 1047600113, 1)
            return 0
        # Fire Prelate (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x211(89000021, 1047600113, 0)
            return 0
        # Fire Prelate (Altered) (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x211(89000020, 1047600115, 1)
            return 0
        # Fire Prelate (Altered) (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x211(89000021, 1047600115, 0)
            return 0
        # Lionel (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x211(89000020, 1047600177, 1)
            return 0
        # Lionel (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x211(89000021, 1047600177, 0)
            return 0
        # Lionel (Altered) (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x211(89000020, 1047600179, 1)
            return 0
        # Lionel (Altered) (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x211(89000021, 1047600179, 0)
            return 0
        # Omen (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x211(89000020, 1047600301, 1)
            return 0
        # Omen (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x211(89000021, 1047600301, 0)
            return 0
        # Tree Sentinel (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x211(89000020, 1047600073, 1)
            return 0
        # Tree Sentinel (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x211(89000021, 1047600073, 0)
            return 0
        # Tree Sentinel (Altered) (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x211(89000020, 1047600075, 1)
            return 0
        # Tree Sentinel (Altered) (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x211(89000021, 1047600075, 0)
            return 0
        # Veteran (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x211(89000020, 1047600221, 1)
            return 0
        # Veteran (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x211(89000021, 1047600221, 0)
            return 0
        # Veteran (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x211(89000020, 1047600223, 1)
            return 0
        # Veteran (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x211(89000021, 1047600223, 0)
            return 0
        # Beast Champion (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x211(89000020, 1047600204, 1)
            return 0
        # Beast Champion (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x211(89000021, 1047600204, 0)
            return 0
        # Beast Champion (Altered) (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x211(89000020, 1047600206, 1)
            return 0
        # Beast Champion (Altered) (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x211(89000021, 1047600206, 0)
            return 0
        # Banished Knight (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x211(89000020, 1047600047, 1)
            return 0
        # Banished Knight (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x211(89000021, 1047600047, 0)
            return 0
        # Banished Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x211(89000020, 1047600049, 1)
            return 0
        # Banished Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x211(89000021, 1047600049, 0)
            return 0
        # General Radahn (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x211(89000020, 1047600132, 1)
            return 0
        # General Radahn (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x211(89000021, 1047600132, 0)
            return 0
        # General Radahn (Altered) (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x211(89000020, 1047600134, 1)
            return 0
        # General Radahn (Altered) (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x211(89000021, 1047600134, 0)
            return 0
        # Malformed Dragon (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x211(89000020, 1047600071, 1)
            return 0
        # Malformed Dragon (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x211(89000021, 1047600071, 0)
            return 0
        # Scaled (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x211(89000020, 1047600009, 1)
            return 0
        # Scaled (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x211(89000021, 1047600009, 0)
            return 0
        # Scaled (Altered) (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x211(89000020, 1047600011, 1)
            return 0
        # Scaled (Altered) (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x211(89000021, 1047600011, 0)
            return 0
        # Crucible Axe (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x211(89000020, 1047600146, 1)
            return 0
        # Crucible Axe (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x211(89000021, 1047600146, 0)
            return 0
        # Crucible Axe (Altered) (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x211(89000020, 1047600148, 1)
            return 0
        # Crucible Axe (Altered) (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x211(89000021, 1047600148, 0)
            return 0
        # Crucible Tree (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x211(89000020, 1047600150, 1)
            return 0
        # Crucible Tree (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x211(89000021, 1047600150, 0)
            return 0
        # Royal Knight (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x211(89000020, 1047600077, 1)
            return 0
        # Royal Knight (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x211(89000021, 1047600077, 0)
            return 0
        # Royal Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x211(89000020, 1047600079, 1)
            return 0
        # Royal Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x211(89000021, 1047600079, 0)
            return 0
        # Cleanrot (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x211(89000020, 1047600105, 1)
            return 0
        # Cleanrot (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x211(89000021, 1047600105, 0)
            return 0
        # Cleanrot (Altered) (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x211(89000020, 1047600107, 1)
            return 0
        # Cleanrot (Altered) (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x211(89000021, 1047600107, 0)
            return 0
        # Blaidd (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x211(89000020, 1047600037, 1)
            return 0
        # Blaidd (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x211(89000021, 1047600037, 0)
            return 0
        # Blaidd (Altered) (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x211(89000020, 1047600039, 1)
            return 0
        # Blaidd (Altered) (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x211(89000021, 1047600039, 0)
            return 0
        # Night's Cavalry (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x211(89000020, 1047600059, 1)
            return 0
        # Night's Cavalry (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x211(89000021, 1047600059, 0)
            return 0
        # Night's Cavalry (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x211(89000020, 1047600061, 1)
            return 0
        # Night's Cavalry (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x211(89000021, 1047600061, 0)
            return 0
        # Maliketh (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x211(89000020, 1047600213, 1)
            return 0
        # Maliketh (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x211(89000021, 1047600213, 0)
            return 0
        # Maliketh (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x211(89000020, 1047600215, 1)
            return 0
        # Maliketh (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x211(89000021, 1047600215, 0)
            return 0
        # Twinned (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x211(89000020, 1047600160, 1)
            return 0
        # Twinned (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x211(89000021, 1047600160, 0)
            return 0
        # Twinned (Altered) (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x211(89000020, 1047600162, 1)
            return 0
        # Twinned (Altered) (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x211(89000021, 1047600162, 0)
            return 0
        # Hoslow (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x211(89000020, 1047600181, 1)
            return 0
        # Hoslow (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x211(89000021, 1047600181, 0)
            return 0
        # Hoslow (Altered) (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x211(89000020, 1047600185, 1)
            return 0
        # Hoslow (Altered) (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x211(89000021, 1047600185, 0)
            return 0
        # Cuckoo Knight (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x211(89000020, 1047600369, 1)
            return 0
        # Cuckoo Knight (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x211(89000021, 1047600369, 0)
            return 0
        # Cuckoo Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x211(89000020, 1047600371, 1)
            return 0
        # Cuckoo Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x211(89000021, 1047600371, 0)
            return 0
        # Briar (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x211(89000020, 1047600051, 1)
            return 0
        # Briar (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x211(89000021, 1047600051, 0)
            return 0
        # Briar (Altered) (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x211(89000020, 1047600053, 1)
            return 0
        # Briar (Altered) (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x211(89000021, 1047600053, 0)
            return 0
        # Godrick Knight (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x211(89000020, 1047600365, 1)
            return 0
        # Godrick Knight (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x211(89000021, 1047600365, 0)
            return 0
        # Godrick Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x211(89000020, 1047600367, 1)
            return 0
        # Godrick Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x211(89000021, 1047600367, 0)
            return 0
        # Redmane Knight (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x211(89000020, 1047600377, 1)
            return 0
        # Redmane Knight (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x211(89000021, 1047600377, 0)
            return 0
        # Redmane Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x211(89000020, 1047600379, 1)
            return 0
        # Redmane Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x211(89000021, 1047600379, 0)
            return 0
        # Gelmir Knight (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x211(89000020, 1047600361, 1)
            return 0
        # Gelmir Knight (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x211(89000021, 1047600361, 0)
            return 0
        # Gelmir Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x211(89000020, 1047600363, 1)
            return 0
        # Gelmir Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x211(89000021, 1047600363, 0)
            return 0
        # Leyndell Knight (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x211(89000020, 1047600373, 1)
            return 0
        # Leyndell Knight (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x211(89000021, 1047600373, 0)
            return 0
        # Leyndell Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x211(89000020, 1047600375, 1)
            return 0
        # Leyndell Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x211(89000021, 1047600375, 0)
            return 0
        # Haligtree Knight (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x211(89000020, 1047600385, 1)
            return 0
        # Haligtree Knight (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x211(89000021, 1047600385, 0)
            return 0
        # Haligtree Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x211(89000020, 1047600387, 1)
            return 0
        # Haligtree Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x211(89000021, 1047600387, 0)
            return 0
        # Blackflame Monk (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x211(89000020, 1047600111, 1)
            return 0
        # Blackflame Monk (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x211(89000021, 1047600111, 0)
            return 0
        # Fire Monk (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x211(89000020, 1047600109, 1)
            return 0
        # Fire Monk (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x211(89000021, 1047600109, 0)
            return 0
        # Giant (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x211(89000020, 1047600431, 1)
            return 0
        # Giant (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x211(89000021, 1047600431, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Body: Medium Armor
def t608001110_x72():
    while True:
        c1_110()
        ClearTalkListData()
        
        # All-Knowing (ON)
        AddTalkListDataIf(GetEventFlag(1047600156) == 0, 101, 89001300, -1)
        # All-Knowing (OFF)
        AddTalkListDataIf(GetEventFlag(1047600156) == 1, 501, 89001300, -1)

        # All-Knowing (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600158) == 0, 102, 89001301, -1)
        # All-Knowing (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600158) == 1, 502, 89001301, -1)

        # Royal Remains (ON)
        AddTalkListDataIf(GetEventFlag(1047600197) == 0, 103, 89001302, -1)
        # Royal Remains (OFF)
        AddTalkListDataIf(GetEventFlag(1047600197) == 1, 503, 89001302, -1)

        # Bloodhound Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600225) == 0, 104, 89001303, -1)
        # Bloodhound Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600225) == 1, 504, 89001303, -1)

        # Bloodhound Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600227) == 0, 105, 89001304, -1)
        # Bloodhound Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600227) == 1, 505, 89001304, -1)

        # Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600346) == 0, 106, 89001305, -1)
        # Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600346) == 1, 506, 89001305, -1)

        # Fingerprint (ON)
        AddTalkListDataIf(GetEventFlag(1047600287) == 0, 107, 89001306, -1)
        # Fingerprint (OFF)
        AddTalkListDataIf(GetEventFlag(1047600287) == 1, 507, 89001306, -1)

        # Fingerprint (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600289) == 0, 108, 89001307, -1)
        # Fingerprint (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600289) == 1, 508, 89001307, -1)

        # Carian Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600303) == 0, 109, 89001308, -1)
        # Carian Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600303) == 1, 509, 89001308, -1)

        # Carian Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600305) == 0, 110, 89001309, -1)
        # Carian Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600305) == 1, 510, 89001309, -1)

        # Godrick Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600349) == 0, 111, 89001310, -1)
        # Godrick Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600349) == 1, 511, 89001310, -1)

        # Raya Lucarian Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600351) == 0, 112, 89001311, -1)
        # Raya Lucarian Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600351) == 1, 512, 89001311, -1)

        # Leyndell Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600353) == 0, 113, 89001312, -1)
        # Leyndell Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600353) == 1, 513, 89001312, -1)

        # Radahn Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600355) == 0, 114, 89001313, -1)
        # Radahn Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600355) == 1, 514, 89001313, -1)

        # Haligtree Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600359) == 0, 115, 89001314, -1)
        # Haligtree Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600359) == 1, 515, 89001314, -1)

        # Raging Wolf (ON)
        AddTalkListDataIf(GetEventFlag(1047600251) == 0, 116, 89001315, -1)
        # Raging Wolf (OFF)
        AddTalkListDataIf(GetEventFlag(1047600251) == 1, 516, 89001315, -1)

        # Raging Wolf (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600253) == 0, 117, 89001316, -1)
        # Raging Wolf (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600253) == 1, 517, 89001316, -1)

        # Vagabond Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600187) == 0, 118, 89001317, -1)
        # Vagabond Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600187) == 1, 518, 89001317, -1)

        # Vagabond Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600189) == 0, 119, 89001318, -1)
        # Vagabond Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600189) == 1, 519, 89001318, -1)

        # Mausoleum Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600381) == 0, 120, 89001319, -1)
        # Mausoleum Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600381) == 1, 520, 89001319, -1)

        # Mausoleum Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600383) == 0, 121, 89001320, -1)
        # Mausoleum Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600383) == 1, 521, 89001320, -1)

        # Eccentric (ON)
        AddTalkListDataIf(GetEventFlag(1047600283) == 0, 122, 89001321, -1)
        # Eccentric (OFF)
        AddTalkListDataIf(GetEventFlag(1047600283) == 1, 522, 89001321, -1)

        # Eccentric (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600285) == 0, 123, 89001322, -1)
        # Eccentric (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600285) == 1, 523, 89001322, -1)

        # Drake Knight (ON)
        AddTalkListDataIf(GetEventFlag(1047600005) == 0, 124, 89001323, -1)
        # Drake Knight (OFF)
        AddTalkListDataIf(GetEventFlag(1047600005) == 1, 524, 89001323, -1)

        # Drake Knight (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600007) == 0, 125, 89001324, -1)
        # Drake Knight (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600007) == 1, 525, 89001324, -1)

        # Black Knife (ON)
        AddTalkListDataIf(GetEventFlag(1047600041) == 0, 126, 89001325, -1)
        # Black Knife (OFF)
        AddTalkListDataIf(GetEventFlag(1047600041) == 1, 526, 89001325, -1)

        # Black Knife (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600043) == 0, 127, 89001326, -1)
        # Black Knife (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600043) == 1, 527, 89001326, -1)

        # Exile (ON)
        AddTalkListDataIf(GetEventFlag(1047600045) == 0, 128, 89001327, -1)
        # Exile (OFF)
        AddTalkListDataIf(GetEventFlag(1047600045) == 1, 528, 89001327, -1)

        # Elden Lord (ON)
        AddTalkListDataIf(GetEventFlag(1047600128) == 0, 129, 89001328, -1)
        # Elden Lord (OFF)
        AddTalkListDataIf(GetEventFlag(1047600128) == 1, 529, 89001328, -1)

        # Elden Lord (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600130) == 0, 130, 89001329, -1)
        # Elden Lord (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600130) == 1, 530, 89001329, -1)

        # Ronin (ON)
        AddTalkListDataIf(GetEventFlag(1047600031) == 0, 131, 89001330, -1)
        # Ronin (OFF)
        AddTalkListDataIf(GetEventFlag(1047600031) == 1, 531, 89001330, -1)

        # Ronin (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600033) == 0, 132, 89001331, -1)
        # Ronin (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600033) == 1, 532, 89001331, -1)

        # Chain (ON)
        AddTalkListDataIf(GetEventFlag(1047600332) == 0, 133, 89001332, -1)
        # Chain (OFF)
        AddTalkListDataIf(GetEventFlag(1047600332) == 1, 533, 89001332, -1)

        # Iron (ON)
        AddTalkListDataIf(GetEventFlag(1047600001) == 0, 134, 89001333, -1)
        # Iron (OFF)
        AddTalkListDataIf(GetEventFlag(1047600001) == 1, 534, 89001333, -1)

        # Kaiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600003) == 0, 135, 89001334, -1)
        # Kaiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600003) == 1, 535, 89001334, -1)

        # Mausoleum Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600357) == 0, 136, 89001335, -1)
        # Mausoleum Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600357) == 1, 536, 89001335, -1)

        # Blue Silver (ON)
        AddTalkListDataIf(GetEventFlag(1047600063) == 0, 137, 89001336, -1)
        # Blue Silver (OFF)
        AddTalkListDataIf(GetEventFlag(1047600063) == 1, 537, 89001336, -1)

        # Blue Silver (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600065) == 0, 138, 89001337, -1)
        # Blue Silver (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600065) == 1, 538, 89001337, -1)

        # Zamor (ON)
        AddTalkListDataIf(GetEventFlag(1047600323) == 0, 139, 89001338, -1)
        # Zamor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600323) == 1, 539, 89001338, -1)

        # Malenia (ON)
        AddTalkListDataIf(GetEventFlag(1047600217) == 0, 140, 89001339, -1)
        # Malenia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600217) == 1, 540, 89001339, -1)

        # Malenia (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600219) == 0, 141, 89001340, -1)
        # Malenia (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600219) == 1, 541, 89001340, -1)

        # Guardian (Full Bloom) (ON)
        AddTalkListDataIf(GetEventFlag(1047600101) == 0, 142, 89001373, -1)
        # Guardian (Full Bloom) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600101) == 1, 542, 89001373, -1)

        # Guardian (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600103) == 0, 143, 89001342, -1)
        # Guardian (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600103) == 1, 543, 89001342, -1)

        # Duelist (ON)
        AddTalkListDataIf(GetEventFlag(1047600095) == 0, 144, 89001343, -1)
        # Duelist (OFF)
        AddTalkListDataIf(GetEventFlag(1047600095) == 1, 544, 89001343, -1)

        # Duelist (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600097) == 0, 145, 89001344, -1)
        # Duelist (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600097) == 1, 545, 89001344, -1)

        # Land of Reeds (ON)
        AddTalkListDataIf(GetEventFlag(1047600255) == 0, 146, 89001345, -1)
        # Land of Reeds (OFF)
        AddTalkListDataIf(GetEventFlag(1047600255) == 1, 546, 89001345, -1)

        # Land of Reeds (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600257) == 0, 147, 89001346, -1)
        # Land of Reeds (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600257) == 1, 547, 89001346, -1)

        # White Reed (ON)
        AddTalkListDataIf(GetEventFlag(1047600259) == 0, 148, 89001347, -1)
        # White Reed (OFF)
        AddTalkListDataIf(GetEventFlag(1047600259) == 1, 548, 89001347, -1)

        # Godrick Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600389) == 0, 149, 89001348, -1)
        # Godrick Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600389) == 1, 549, 89001348, -1)

        # Raya Lucarian Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600391) == 0, 150, 89001349, -1)
        # Raya Lucarian Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600391) == 1, 550, 89001349, -1)

        # Leyndell Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600393) == 0, 151, 89001350, -1)
        # Leyndell Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600393) == 1, 551, 89001350, -1)

        # Radahn Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600395) == 0, 152, 89001351, -1)
        # Radahn Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600395) == 1, 552, 89001351, -1)

        # Haligtree Foot Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600397) == 0, 153, 89001352, -1)
        # Haligtree Foot Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600397) == 1, 553, 89001352, -1)

        # Nox Swordstress (ON)
        AddTalkListDataIf(GetEventFlag(1047600085) == 0, 154, 89001353, -1)
        # Nox Swordstress (OFF)
        AddTalkListDataIf(GetEventFlag(1047600085) == 1, 554, 89001353, -1)

        # Nox Swordstress (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600087) == 0, 155, 89001354, -1)
        # Nox Swordstress (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600087) == 1, 555, 89001354, -1)

        # Night Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600089) == 0, 156, 89001355, -1)
        # Night Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600089) == 1, 556, 89001355, -1)

        # Confessor (ON)
        AddTalkListDataIf(GetEventFlag(1047600261) == 0, 157, 89001356, -1)
        # Confessor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600261) == 1, 557, 89001356, -1)

        # Confessor (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600263) == 0, 158, 89001357, -1)
        # Confessor (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600263) == 1, 558, 89001357, -1)

        # Nox Monk (ON)
        AddTalkListDataIf(GetEventFlag(1047600081) == 0, 159, 89001358, -1)
        # Nox Monk (OFF)
        AddTalkListDataIf(GetEventFlag(1047600081) == 1, 559, 89001358, -1)

        # Nox Monk (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600083) == 0, 160, 89001359, -1)
        # Nox Monk (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600083) == 1, 560, 89001359, -1)

        # Vulgar Militia (ON)
        AddTalkListDataIf(GetEventFlag(1047600123) == 0, 161, 89001360, -1)
        # Vulgar Militia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600123) == 1, 561, 89001360, -1)

        # Ragged (ON)
        AddTalkListDataIf(GetEventFlag(1047600164) == 0, 162, 89001361, -1)
        # Ragged (OFF)
        AddTalkListDataIf(GetEventFlag(1047600164) == 1, 562, 89001361, -1)

        # Ragged (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600166) == 0, 163, 89001362, -1)
        # Ragged (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600166) == 1, 563, 89001362, -1)

        # Blue Cloth (ON)
        AddTalkListDataIf(GetEventFlag(1047600191) == 0, 164, 89001363, -1)
        # Blue Cloth (OFF)
        AddTalkListDataIf(GetEventFlag(1047600191) == 1, 564, 89001363, -1)

        # Omenkiller (ON)
        AddTalkListDataIf(GetEventFlag(1047600399) == 0, 165, 89001364, -1)
        # Omenkiller (OFF)
        AddTalkListDataIf(GetEventFlag(1047600399) == 1, 565, 89001364, -1)

        # Leather (ON)
        AddTalkListDataIf(GetEventFlag(1047600343) == 0, 166, 89001365, -1)
        # Leather (OFF)
        AddTalkListDataIf(GetEventFlag(1047600343) == 1, 566, 89001365, -1)

        # War Surgeon (ON)
        AddTalkListDataIf(GetEventFlag(1047600193) == 0, 167, 89001366, -1)
        # War Surgeon (OFF)
        AddTalkListDataIf(GetEventFlag(1047600193) == 1, 567, 89001366, -1)

        # War Surgeon (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600195) == 0, 168, 89001367, -1)
        # War Surgeon (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600195) == 1, 568, 89001367, -1)

        # Raptor (ON)
        AddTalkListDataIf(GetEventFlag(1047600281) == 0, 169, 89001368, -1)
        # Raptor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600281) == 1, 569, 89001368, -1)

        # Preceptor (ON)
        AddTalkListDataIf(GetEventFlag(1047600276) == 0, 170, 89001369, -1)
        # Preceptor (OFF)
        AddTalkListDataIf(GetEventFlag(1047600276) == 1, 570, 89001369, -1)

        # Preceptor (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600278) == 0, 171, 89001370, -1)
        # Preceptor (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600278) == 1, 571, 89001370, -1)

        # Rotten Duelist (ON)
        AddTalkListDataIf(GetEventFlag(1047600416) == 0, 172, 89001371, -1)
        # Rotten Duelist (OFF)
        AddTalkListDataIf(GetEventFlag(1047600416) == 1, 572, 89001371, -1)

        # Rotten Duelist (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600418) == 0, 173, 89001372, -1)
        # Rotten Duelist (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600418) == 1, 573, 89001372, -1)

        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # All-Knowing (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x211(89000020, 1047600156, 1)
            return 0
        # All-Knowing (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x211(89000021, 1047600156, 0)
            return 0
        # All-Knowing (Altered) (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x211(89000020, 1047600158, 1)
            return 0
        # All-Knowing (Altered) (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x211(89000021, 1047600158, 0)
            return 0
        # Royal Remains (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x211(89000020, 1047600197, 1)
            return 0
        # Royal Remains (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x211(89000021, 1047600197, 0)
            return 0
        # Bloodhound Knight (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x211(89000020, 1047600225, 1)
            return 0
        # Bloodhound Knight (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x211(89000021, 1047600225, 0)
            return 0
        # Bloodhound Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x211(89000020, 1047600227, 1)
            return 0
        # Bloodhound Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x211(89000021, 1047600227, 0)
            return 0
        # Knight (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x211(89000020, 1047600346, 1)
            return 0
        # Knight (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x211(89000021, 1047600346, 0)
            return 0
        # Fingerprint (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x211(89000020, 1047600287, 1)
            return 0
        # Fingerprint (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x211(89000021, 1047600287, 0)
            return 0
        # Fingerprint (Altered) (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x211(89000020, 1047600289, 1)
            return 0
        # Fingerprint (Altered) (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x211(89000021, 1047600289, 0)
            return 0
        # Carian Knight (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x211(89000020, 1047600303, 1)
            return 0
        # Carian Knight (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x211(89000021, 1047600303, 0)
            return 0
        # Carian Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x211(89000020, 1047600305, 1)
            return 0
        # Carian Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x211(89000021, 1047600305, 0)
            return 0
        # Godrick Soldier (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x211(89000020, 1047600349, 1)
            return 0
        # Godrick Soldier (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x211(89000021, 1047600349, 0)
            return 0
        # Raya Lucarian Soldier (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x211(89000020, 1047600351, 1)
            return 0
        # Raya Lucarian Soldier (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x211(89000021, 1047600351, 0)
            return 0
        # Leyndell Soldier (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x211(89000020, 1047600353, 1)
            return 0
        # Leyndell Soldier (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x211(89000021, 1047600353, 0)
            return 0
        # Radahn Soldier (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x211(89000020, 1047600355, 1)
            return 0
        # Radahn Soldier (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x211(89000021, 1047600355, 0)
            return 0
        # Haligtree Soldier (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x211(89000020, 1047600359, 1)
            return 0
        # Haligtree Soldier (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x211(89000021, 1047600359, 0)
            return 0
        # Raging Wolf (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x211(89000020, 1047600251, 1)
            return 0
        # Raging Wolf (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x211(89000021, 1047600251, 0)
            return 0
        # Raging Wolf (Altered) (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x211(89000020, 1047600253, 1)
            return 0
        # Raging Wolf (Altered) (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x211(89000021, 1047600253, 0)
            return 0
        # Vagabond Knight (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x211(89000020, 1047600187, 1)
            return 0
        # Vagabond Knight (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x211(89000021, 1047600187, 0)
            return 0
        # Vagabond Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x211(89000020, 1047600189, 1)
            return 0
        # Vagabond Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x211(89000021, 1047600189, 0)
            return 0
        # Mausoleum Knight (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x211(89000020, 1047600381, 1)
            return 0
        # Mausoleum Knight (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x211(89000021, 1047600381, 0)
            return 0
        # Mausoleum Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x211(89000020, 1047600383, 1)
            return 0
        # Mausoleum Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x211(89000021, 1047600383, 0)
            return 0
        # Eccentric (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x211(89000020, 1047600283, 1)
            return 0
        # Eccentric (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x211(89000021, 1047600283, 0)
            return 0
        # Eccentric (Altered) (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x211(89000020, 1047600285, 1)
            return 0
        # Eccentric (Altered) (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x211(89000021, 1047600285, 0)
            return 0
        # Drake Knight (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x211(89000020, 1047600005, 1)
            return 0
        # Drake Knight (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x211(89000021, 1047600005, 0)
            return 0
        # Drake Knight (Altered) (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x211(89000020, 1047600007, 1)
            return 0
        # Drake Knight (Altered) (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x211(89000021, 1047600007, 0)
            return 0
        # Black Knife (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x211(89000020, 1047600041, 1)
            return 0
        # Black Knife (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x211(89000021, 1047600041, 0)
            return 0
        # Black Knife (Altered) (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x211(89000020, 1047600043, 1)
            return 0
        # Black Knife (Altered) (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x211(89000021, 1047600043, 0)
            return 0
        # Exile (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x211(89000020, 1047600045, 1)
            return 0
        # Exile (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x211(89000021, 1047600045, 0)
            return 0
        # Elden Lord (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x211(89000020, 1047600128, 1)
            return 0
        # Elden Lord (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x211(89000021, 1047600128, 0)
            return 0
        # Elden Lord (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x211(89000020, 1047600130, 1)
            return 0
        # Elden Lord (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x211(89000021, 1047600130, 0)
            return 0
        # Ronin (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x211(89000020, 1047600031, 1)
            return 0
        # Ronin (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x211(89000021, 1047600031, 0)
            return 0
        # Ronin (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x211(89000020, 1047600033, 1)
            return 0
        # Ronin (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x211(89000021, 1047600033, 0)
            return 0
        # Chain (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x211(89000020, 1047600332, 1)
            return 0
        # Chain (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x211(89000021, 1047600332, 0)
            return 0
        # Iron (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x211(89000020, 1047600001, 1)
            return 0
        # Iron (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x211(89000021, 1047600001, 0)
            return 0
        # Kaiden (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x211(89000020, 1047600003, 1)
            return 0
        # Kaiden (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x211(89000021, 1047600003, 0)
            return 0
        # Mausoleum Soldier (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x211(89000020, 1047600357, 1)
            return 0
        # Mausoleum Soldier (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x211(89000021, 1047600357, 0)
            return 0
        # Blue Silver (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x211(89000020, 1047600063, 1)
            return 0
        # Blue Silver (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x211(89000021, 1047600063, 0)
            return 0
        # Blue Silver (Altered) (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x211(89000020, 1047600065, 1)
            return 0
        # Blue Silver (Altered) (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x211(89000021, 1047600065, 0)
            return 0
        # Zamor (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x211(89000020, 1047600323, 1)
            return 0
        # Zamor (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x211(89000021, 1047600323, 0)
            return 0
        # Malenia (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x211(89000020, 1047600217, 1)
            return 0
        # Malenia (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x211(89000021, 1047600217, 0)
            return 0
        # Malenia (Altered) (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x211(89000020, 1047600219, 1)
            return 0
        # Malenia (Altered) (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x211(89000021, 1047600219, 0)
            return 0
        # Guardian (Full Bloom) (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x211(89000020, 1047600101, 1)
            return 0
        # Guardian (Full Bloom) (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x211(89000021, 1047600101, 0)
            return 0
        # Guardian (Altered) (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x211(89000020, 1047600103, 1)
            return 0
        # Guardian (Altered) (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x211(89000021, 1047600103, 0)
            return 0
        # Duelist (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x211(89000020, 1047600095, 1)
            return 0
        # Duelist (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x211(89000021, 1047600095, 0)
            return 0
        # Duelist (Altered) (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x211(89000020, 1047600097, 1)
            return 0
        # Duelist (Altered) (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x211(89000021, 1047600097, 0)
            return 0
        # Land of Reeds (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x211(89000020, 1047600255, 1)
            return 0
        # Land of Reeds (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x211(89000021, 1047600255, 0)
            return 0
        # Land of Reeds (Altered) (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x211(89000020, 1047600257, 1)
            return 0
        # Land of Reeds (Altered) (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x211(89000021, 1047600257, 0)
            return 0
        # White Reed (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x211(89000020, 1047600259, 1)
            return 0
        # White Reed (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x211(89000021, 1047600259, 0)
            return 0
        # Godrick Foot Soldier (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x211(89000020, 1047600389, 1)
            return 0
        # Godrick Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x211(89000021, 1047600389, 0)
            return 0
        # Raya Lucarian Foot Soldier (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x211(89000020, 1047600391, 1)
            return 0
        # Raya Lucarian Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x211(89000021, 1047600391, 0)
            return 0
        # Leyndell Foot Soldier (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x211(89000020, 1047600393, 1)
            return 0
        # Leyndell Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x211(89000021, 1047600393, 0)
            return 0
        # Radahn Foot Soldier (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x211(89000020, 1047600395, 1)
            return 0
        # Radahn Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x211(89000021, 1047600395, 0)
            return 0
        # Haligtree Foot Soldier (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x211(89000020, 1047600397, 1)
            return 0
        # Haligtree Foot Soldier (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x211(89000021, 1047600397, 0)
            return 0
        # Nox Swordstress (ON)
        elif GetTalkListEntryResult() == 154:
            assert t608001110_x211(89000020, 1047600085, 1)
            return 0
        # Nox Swordstress (OFF)
        elif GetTalkListEntryResult() == 554:
            assert t608001110_x211(89000021, 1047600085, 0)
            return 0
        # Nox Swordstress (Altered) (ON)
        elif GetTalkListEntryResult() == 155:
            assert t608001110_x211(89000020, 1047600087, 1)
            return 0
        # Nox Swordstress (Altered) (OFF)
        elif GetTalkListEntryResult() == 555:
            assert t608001110_x211(89000021, 1047600087, 0)
            return 0
        # Night Maiden (ON)
        elif GetTalkListEntryResult() == 156:
            assert t608001110_x211(89000020, 1047600089, 1)
            return 0
        # Night Maiden (OFF)
        elif GetTalkListEntryResult() == 556:
            assert t608001110_x211(89000021, 1047600089, 0)
            return 0
        # Confessor (ON)
        elif GetTalkListEntryResult() == 157:
            assert t608001110_x211(89000020, 1047600261, 1)
            return 0
        # Confessor (OFF)
        elif GetTalkListEntryResult() == 557:
            assert t608001110_x211(89000021, 1047600261, 0)
            return 0
        # Confessor (Altered) (ON)
        elif GetTalkListEntryResult() == 158:
            assert t608001110_x211(89000020, 1047600263, 1)
            return 0
        # Confessor (Altered) (OFF)
        elif GetTalkListEntryResult() == 558:
            assert t608001110_x211(89000021, 1047600263, 0)
            return 0
        # Nox Monk (ON)
        elif GetTalkListEntryResult() == 159:
            assert t608001110_x211(89000020, 1047600081, 1)
            return 0
        # Nox Monk (OFF)
        elif GetTalkListEntryResult() == 559:
            assert t608001110_x211(89000021, 1047600081, 0)
            return 0
        # Nox Monk (Altered) (ON)
        elif GetTalkListEntryResult() == 160:
            assert t608001110_x211(89000020, 1047600083, 1)
            return 0
        # Nox Monk (Altered) (OFF)
        elif GetTalkListEntryResult() == 560:
            assert t608001110_x211(89000021, 1047600083, 0)
            return 0
        # Vulgar Militia (ON)
        elif GetTalkListEntryResult() == 161:
            assert t608001110_x211(89000020, 1047600123, 1)
            return 0
        # Vulgar Militia (OFF)
        elif GetTalkListEntryResult() == 561:
            assert t608001110_x211(89000021, 1047600123, 0)
            return 0
        # Ragged (ON)
        elif GetTalkListEntryResult() == 162:
            assert t608001110_x211(89000020, 1047600164, 1)
            return 0
        # Ragged (OFF)
        elif GetTalkListEntryResult() == 562:
            assert t608001110_x211(89000021, 1047600164, 0)
            return 0
        # Ragged (Altered) (ON)
        elif GetTalkListEntryResult() == 163:
            assert t608001110_x211(89000020, 1047600166, 1)
            return 0
        # Ragged (Altered) (OFF)
        elif GetTalkListEntryResult() == 563:
            assert t608001110_x211(89000021, 1047600166, 0)
            return 0
        # Blue Cloth (ON)
        elif GetTalkListEntryResult() == 164:
            assert t608001110_x211(89000020, 1047600191, 1)
            return 0
        # Blue Cloth (OFF)
        elif GetTalkListEntryResult() == 564:
            assert t608001110_x211(89000021, 1047600191, 0)
            return 0
        # Omenkiller (ON)
        elif GetTalkListEntryResult() == 165:
            assert t608001110_x211(89000020, 1047600399, 1)
            return 0
        # Omenkiller (OFF)
        elif GetTalkListEntryResult() == 565:
            assert t608001110_x211(89000021, 1047600399, 0)
            return 0
        # Leather (ON)
        elif GetTalkListEntryResult() == 166:
            assert t608001110_x211(89000020, 1047600343, 1)
            return 0
        # Leather (OFF)
        elif GetTalkListEntryResult() == 566:
            assert t608001110_x211(89000021, 1047600343, 0)
            return 0
        # War Surgeon (ON)
        elif GetTalkListEntryResult() == 167:
            assert t608001110_x211(89000020, 1047600193, 1)
            return 0
        # War Surgeon (OFF)
        elif GetTalkListEntryResult() == 567:
            assert t608001110_x211(89000021, 1047600193, 0)
            return 0
        # War Surgeon (Altered) (ON)
        elif GetTalkListEntryResult() == 168:
            assert t608001110_x211(89000020, 1047600195, 1)
            return 0
        # War Surgeon (Altered) (OFF)
        elif GetTalkListEntryResult() == 568:
            assert t608001110_x211(89000021, 1047600195, 0)
            return 0
        # Raptor (ON)
        elif GetTalkListEntryResult() == 169:
            assert t608001110_x211(89000020, 1047600281, 1)
            return 0
        # Raptor (OFF)
        elif GetTalkListEntryResult() == 569:
            assert t608001110_x211(89000021, 1047600281, 0)
            return 0
        # Preceptor (ON)
        elif GetTalkListEntryResult() == 170:
            assert t608001110_x211(89000020, 1047600276, 1)
            return 0
        # Preceptor (OFF)
        elif GetTalkListEntryResult() == 570:
            assert t608001110_x211(89000021, 1047600276, 0)
            return 0
        # Preceptor (Altered) (ON)
        elif GetTalkListEntryResult() == 171:
            assert t608001110_x211(89000020, 1047600278, 1)
            return 0
        # Preceptor (Altered) (OFF)
        elif GetTalkListEntryResult() == 571:
            assert t608001110_x211(89000021, 1047600278, 0)
            return 0
        # Rotten Duelist (ON)
        elif GetTalkListEntryResult() == 172:
            assert t608001110_x211(89000020, 1047600416, 1)
            return 0
        # Rotten Duelist (OFF)
        elif GetTalkListEntryResult() == 572:
            assert t608001110_x211(89000021, 1047600416, 0)
            return 0
        # Rotten Duelist (Altered) (ON)
        elif GetTalkListEntryResult() == 173:
            assert t608001110_x211(89000020, 1047600418, 1)
            return 0
        # Rotten Duelist (Altered) (OFF)
        elif GetTalkListEntryResult() == 573:
            assert t608001110_x211(89000021, 1047600418, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Alter Body: Light Armor
def t608001110_x73():
    while True:
        c1_110()
        ClearTalkListData()
        
        # Nomadic Merchant (ON)
        AddTalkListDataIf(GetEventFlag(1047600067) == 0, 101, 89001500, -1)
        # Nomadic Merchant (OFF)
        AddTalkListDataIf(GetEventFlag(1047600067) == 1, 501, 89001500, -1)

        # Nomadic Merchant (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600069) == 0, 102, 89001501, -1)
        # Nomadic Merchant (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600069) == 1, 502, 89001501, -1)

        # Azur (ON)
        AddTalkListDataIf(GetEventFlag(1047600154) == 0, 103, 89001502, -1)
        # Azur (OFF)
        AddTalkListDataIf(GetEventFlag(1047600154) == 1, 503, 89001502, -1)

        # Lusat (ON)
        AddTalkListDataIf(GetEventFlag(1047600152) == 0, 104, 89001503, -1)
        # Lusat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600152) == 1, 504, 89001503, -1)

        # Crimson Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600210) == 0, 105, 89001504, -1)
        # Crimson Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600210) == 1, 505, 89001504, -1)

        # Prisoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600265) == 0, 106, 89001505, -1)
        # Prisoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600265) == 1, 506, 89001505, -1)

        # Champion (ON)
        AddTalkListDataIf(GetEventFlag(1047600208) == 0, 107, 89001506, -1)
        # Champion (OFF)
        AddTalkListDataIf(GetEventFlag(1047600208) == 1, 507, 89001506, -1)

        # Highwayman (ON)
        AddTalkListDataIf(GetEventFlag(1047600410) == 0, 108, 89001507, -1)
        # Highwayman (OFF)
        AddTalkListDataIf(GetEventFlag(1047600410) == 1, 508, 89001507, -1)

        # Depraved Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600142) == 0, 109, 89001508, -1)
        # Depraved Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600142) == 1, 509, 89001508, -1)

        # Depraved Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600144) == 0, 110, 89001509, -1)
        # Depraved Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600144) == 1, 510, 89001509, -1)

        # Astrologer (ON)
        AddTalkListDataIf(GetEventFlag(1047600173) == 0, 111, 89001510, -1)
        # Astrologer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600173) == 1, 511, 89001510, -1)

        # Astrologer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600175) == 0, 112, 89001511, -1)
        # Astrologer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600175) == 1, 512, 89001511, -1)

        # Albinauric (ON)
        AddTalkListDataIf(GetEventFlag(1047600321) == 0, 113, 89001512, -1)
        # Albinauric (OFF)
        AddTalkListDataIf(GetEventFlag(1047600321) == 1, 513, 89001512, -1)

        # Marionette Soldier (ON)
        AddTalkListDataIf(GetEventFlag(1047600248) == 0, 114, 89001513, -1)
        # Marionette Soldier (OFF)
        AddTalkListDataIf(GetEventFlag(1047600248) == 1, 514, 89001513, -1)

        # Godskin Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600140) == 0, 115, 89001514, -1)
        # Godskin Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600140) == 1, 515, 89001514, -1)

        # Mushroom (ON)
        AddTalkListDataIf(GetEventFlag(1047600339) == 0, 116, 89001515, -1)
        # Mushroom (OFF)
        AddTalkListDataIf(GetEventFlag(1047600339) == 1, 516, 89001515, -1)

        # Ancestral Fur (ON)
        AddTalkListDataIf(GetEventFlag(1047600091) == 0, 117, 89001516, -1)
        # Ancestral Fur (OFF)
        AddTalkListDataIf(GetEventFlag(1047600091) == 1, 517, 89001516, -1)

        # Ancestral Shaman (ON)
        AddTalkListDataIf(GetEventFlag(1047600093) == 0, 118, 89001517, -1)
        # Ancestral Shaman (OFF)
        AddTalkListDataIf(GetEventFlag(1047600093) == 1, 518, 89001517, -1)

        # Errant Sorcerer (ON)
        AddTalkListDataIf(GetEventFlag(1047600307) == 0, 119, 89001518, -1)
        # Errant Sorcerer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600307) == 1, 519, 89001518, -1)

        # Errant Sorcerer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600309) == 0, 120, 89001519, -1)
        # Errant Sorcerer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600309) == 1, 520, 89001519, -1)

        # Traveling Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600268) == 0, 121, 89001520, -1)
        # Traveling Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600268) == 1, 521, 89001520, -1)

        # Traveling Maiden (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600270) == 0, 122, 89001521, -1)
        # Traveling Maiden (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600270) == 1, 522, 89001521, -1)

        # Queen (ON)
        AddTalkListDataIf(GetEventFlag(1047600136) == 0, 123, 89001522, -1)
        # Queen (OFF)
        AddTalkListDataIf(GetEventFlag(1047600136) == 1, 523, 89001522, -1)

        # Finger Maiden (ON)
        AddTalkListDataIf(GetEventFlag(1047600272) == 0, 124, 89001523, -1)
        # Finger Maiden (OFF)
        AddTalkListDataIf(GetEventFlag(1047600272) == 1, 524, 89001523, -1)

        # Finger Maiden (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600274) == 0, 125, 89001524, -1)
        # Finger Maiden (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600274) == 1, 525, 89001524, -1)

        # Godskin Apostle (ON)
        AddTalkListDataIf(GetEventFlag(1047600138) == 0, 126, 89001525, -1)
        # Godskin Apostle (OFF)
        AddTalkListDataIf(GetEventFlag(1047600138) == 1, 526, 89001525, -1)

        # Snow Witch (ON)
        AddTalkListDataIf(GetEventFlag(1047600313) == 0, 127, 89001526, -1)
        # Snow Witch (OFF)
        AddTalkListDataIf(GetEventFlag(1047600313) == 1, 527, 89001526, -1)

        # Snow Witch (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600315) == 0, 128, 89001527, -1)
        # Snow Witch (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600315) == 1, 528, 89001527, -1)

        # Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600013) == 0, 129, 9001528, -1)
        # Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600013) == 1, 529, 9001528, -1)

        # Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600015) == 0, 130, 89001529, -1)
        # Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600015) == 1, 530, 89001529, -1)

        # Prophet (ON)
        AddTalkListDataIf(GetEventFlag(1047600168) == 0, 131, 89001530, -1)
        # Prophet (OFF)
        AddTalkListDataIf(GetEventFlag(1047600168) == 1, 531, 89001530, -1)

        # Prophet (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600170) == 0, 132, 89001531, -1)
        # Prophet (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600170) == 1, 532, 89001531, -1)

        # Corhyn (ON)
        AddTalkListDataIf(GetEventFlag(1047600171) == 0, 133, 89001374, -1)
        # Corhyn (OFF)
        AddTalkListDataIf(GetEventFlag(1047600171) == 1, 533, 89001374, -1)

        # Battlemage (ON)
        AddTalkListDataIf(GetEventFlag(1047600311) == 0, 134, 89001532, -1)
        # Battlemage (OFF)
        AddTalkListDataIf(GetEventFlag(1047600311) == 1, 534, 89001532, -1)

        # Consort (ON)
        AddTalkListDataIf(GetEventFlag(1047600291) == 0, 135, 89001533, -1)
        # Consort (OFF)
        AddTalkListDataIf(GetEventFlag(1047600291) == 1, 535, 89001533, -1)

        # Sage (ON)
        AddTalkListDataIf(GetEventFlag(1047600125) == 0, 136, 89001534, -1)
        # Sage (OFF)
        AddTalkListDataIf(GetEventFlag(1047600125) == 1, 536, 89001534, -1)

        # Goldmask (ON)
        AddTalkListDataIf(GetEventFlag(1047600319) == 0, 137, 89001535, -1)
        # Goldmask (OFF)
        AddTalkListDataIf(GetEventFlag(1047600319) == 1, 537, 89001535, -1)

        # Alberich (ON)
        AddTalkListDataIf(GetEventFlag(1047600021) == 0, 138, 89001536, -1)
        # Alberich (OFF)
        AddTalkListDataIf(GetEventFlag(1047600021) == 1, 538, 89001536, -1)

        # Alberich (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600023) == 0, 139, 89001537, -1)
        # Alberich (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600023) == 1, 539, 89001537, -1)

        # Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600117) == 0, 140, 89001538, -1)
        # Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600117) == 1, 540, 89001538, -1)

        # Wandering Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600119) == 0, 141, 89001539, -1)
        # Wandering Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600119) == 1, 541, 89001539, -1)

        # Old Aristocrat (ON)
        AddTalkListDataIf(GetEventFlag(1047600121) == 0, 142, 89001540, -1)
        # Old Aristocrat (OFF)
        AddTalkListDataIf(GetEventFlag(1047600121) == 1, 542, 89001540, -1)

        # Page (ON)
        AddTalkListDataIf(GetEventFlag(1047600055) == 0, 143, 89001541, -1)
        # Page (OFF)
        AddTalkListDataIf(GetEventFlag(1047600055) == 1, 543, 89001541, -1)

        # Page (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600057) == 0, 144, 89001542, -1)
        # Page (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600057) == 1, 544, 89001542, -1)

        # Sanguine Noble (ON)
        AddTalkListDataIf(GetEventFlag(1047600099) == 0, 145, 89001543, -1)
        # Sanguine Noble (OFF)
        AddTalkListDataIf(GetEventFlag(1047600099) == 1, 545, 89001543, -1)

        # Brave (ON)
        AddTalkListDataIf(GetEventFlag(1047600199) == 0, 146, 89001544, -1)
        # Brave (OFF)
        AddTalkListDataIf(GetEventFlag(1047600199) == 1, 546, 89001544, -1)

        # Brave (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600201) == 0, 147, 89001545, -1)
        # Brave (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600201) == 1, 547, 89001545, -1)

        # Travelling Perfumer (ON)
        AddTalkListDataIf(GetEventFlag(1047600017) == 0, 148, 89001546, -1)
        # Travelling Perfumer (OFF)
        AddTalkListDataIf(GetEventFlag(1047600017) == 1, 548, 89001546, -1)

        # Travelling Perfumer (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600019) == 0, 149, 89001547, -1)
        # Travelling Perfumer (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600019) == 1, 549, 89001547, -1)

        # Spellblade (ON)
        AddTalkListDataIf(GetEventFlag(1047600025) == 0, 150, 89001548, -1)
        # Spellblade (OFF)
        AddTalkListDataIf(GetEventFlag(1047600025) == 1, 550, 89001548, -1)

        # Spellblade (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600027) == 0, 151, 89001549, -1)
        # Spellblade (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600027) == 1, 551, 89001549, -1)

        # Commoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600235) == 0, 152, 89001550, -1)
        # Commoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600235) == 1, 552, 89001550, -1)

        # Commoner (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600237) == 0, 153, 89001551, -1)
        # Commoner (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600237) == 1, 553, 89001551, -1)

        # Simple Commoner (ON)
        AddTalkListDataIf(GetEventFlag(1047600239) == 0, 154, 89001552, -1)
        # Simple Commoner (OFF)
        AddTalkListDataIf(GetEventFlag(1047600239) == 1, 554, 89001552, -1)

        # Ruler (ON)
        AddTalkListDataIf(GetEventFlag(1047600293) == 0, 155, 89001553, -1)
        # Ruler (OFF)
        AddTalkListDataIf(GetEventFlag(1047600293) == 1, 555, 89001553, -1)

        # Upper-Class (ON)
        AddTalkListDataIf(GetEventFlag(1047600295) == 0, 156, 89001554, -1)
        # Upper-Class (OFF)
        AddTalkListDataIf(GetEventFlag(1047600295) == 1, 556, 89001554, -1)

        # Fia (ON)
        AddTalkListDataIf(GetEventFlag(1047600406) == 0, 157, 89001555, -1)
        # Fia (OFF)
        AddTalkListDataIf(GetEventFlag(1047600406) == 1, 557, 89001555, -1)

        # Fia (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600408) == 0, 158, 89001556, -1)
        # Fia (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600408) == 1, 558, 89001556, -1)

        # High Page (ON)
        AddTalkListDataIf(GetEventFlag(1047600412) == 0, 159, 89001557, -1)
        # High Page (OFF)
        AddTalkListDataIf(GetEventFlag(1047600412) == 1, 559, 89001557, -1)

        # High Page (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600414) == 0, 160, 89001558, -1)
        # High Page (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600414) == 1, 560, 89001558, -1)

        # Guilty (ON)
        AddTalkListDataIf(GetEventFlag(1047600035) == 0, 161, 89001559, -1)
        # Guilty (OFF)
        AddTalkListDataIf(GetEventFlag(1047600035) == 1, 561, 89001559, -1)

        # Marais (ON)
        AddTalkListDataIf(GetEventFlag(1047600297) == 0, 162, 89001560, -1)
        # Marais (OFF)
        AddTalkListDataIf(GetEventFlag(1047600297) == 1, 562, 89001560, -1)

        # Bloodsoaked (ON)
        AddTalkListDataIf(GetEventFlag(1047600299) == 0, 163, 89001561, -1)
        # Bloodsoaked (OFF)
        AddTalkListDataIf(GetEventFlag(1047600299) == 1, 563, 89001561, -1)

        # Festive (ON)
        AddTalkListDataIf(GetEventFlag(1047600229) == 0, 164, 89001562, -1)
        # Festive (OFF)
        AddTalkListDataIf(GetEventFlag(1047600229) == 1, 564, 89001562, -1)

        # Festive (Altered) (ON)
        AddTalkListDataIf(GetEventFlag(1047600231) == 0, 165, 89001563, -1)
        # Festive (Altered) (OFF)
        AddTalkListDataIf(GetEventFlag(1047600231) == 1, 565, 89001563, -1)

        # Blue Festive (ON)
        AddTalkListDataIf(GetEventFlag(1047600233) == 0, 166, 89001564, -1)
        # Blue Festive (OFF)
        AddTalkListDataIf(GetEventFlag(1047600233) == 1, 566, 89001564, -1)

        # Juvenile Scholar (ON)
        AddTalkListDataIf(GetEventFlag(1047600317) == 0, 167, 89001565, -1)
        # Juvenile Scholar (OFF)
        AddTalkListDataIf(GetEventFlag(1047600317) == 1, 567, 89001565, -1)

        # Leave
        AddTalkListData(999, 26080001, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # Nomadic Merchant (ON)
        if GetTalkListEntryResult() == 101:
            assert t608001110_x211(89000020, 1047600067, 1)
            return 0
        # Nomadic Merchant (OFF)
        elif GetTalkListEntryResult() == 501:
            assert t608001110_x211(89000021, 1047600067, 0)
            return 0
        # Nomadic Merchant (Altered) (ON)
        elif GetTalkListEntryResult() == 102:
            assert t608001110_x211(89000020, 1047600069, 1)
            return 0
        # Nomadic Merchant (Altered) (OFF)
        elif GetTalkListEntryResult() == 502:
            assert t608001110_x211(89000021, 1047600069, 0)
            return 0
        # Azur (ON)
        elif GetTalkListEntryResult() == 103:
            assert t608001110_x211(89000020, 1047600154, 1)
            return 0
        # Azur (OFF)
        elif GetTalkListEntryResult() == 503:
            assert t608001110_x211(89000021, 1047600154, 0)
            return 0
        # Lusat (ON)
        elif GetTalkListEntryResult() == 104:
            assert t608001110_x211(89000020, 1047600152, 1)
            return 0
        # Lusat (OFF)
        elif GetTalkListEntryResult() == 504:
            assert t608001110_x211(89000021, 1047600152, 0)
            return 0
        # Crimson Noble (ON)
        elif GetTalkListEntryResult() == 105:
            assert t608001110_x211(89000020, 1047600210, 1)
            return 0
        # Crimson Noble (OFF)
        elif GetTalkListEntryResult() == 505:
            assert t608001110_x211(89000021, 1047600210, 0)
            return 0
        # Prisoner (ON)
        elif GetTalkListEntryResult() == 106:
            assert t608001110_x211(89000020, 1047600265, 1)
            return 0
        # Prisoner (OFF)
        elif GetTalkListEntryResult() == 506:
            assert t608001110_x211(89000021, 1047600265, 0)
            return 0
        # Champion (ON)
        elif GetTalkListEntryResult() == 107:
            assert t608001110_x211(89000020, 1047600208, 1)
            return 0
        # Champion (OFF)
        elif GetTalkListEntryResult() == 507:
            assert t608001110_x211(89000021, 1047600208, 0)
            return 0
        # Highwayman (ON)
        elif GetTalkListEntryResult() == 108:
            assert t608001110_x211(89000020, 1047600410, 1)
            return 0
        # Highwayman (OFF)
        elif GetTalkListEntryResult() == 508:
            assert t608001110_x211(89000021, 1047600410, 0)
            return 0
        # Depraved Perfumer (ON)
        elif GetTalkListEntryResult() == 109:
            assert t608001110_x211(89000020, 1047600142, 1)
            return 0
        # Depraved Perfumer (OFF)
        elif GetTalkListEntryResult() == 509:
            assert t608001110_x211(89000021, 1047600142, 0)
            return 0
        # Depraved Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 110:
            assert t608001110_x211(89000020, 1047600144, 1)
            return 0
        # Depraved Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 510:
            assert t608001110_x211(89000021, 1047600144, 0)
            return 0
        # Astrologer (ON)
        elif GetTalkListEntryResult() == 111:
            assert t608001110_x211(89000020, 1047600173, 1)
            return 0
        # Astrologer (OFF)
        elif GetTalkListEntryResult() == 511:
            assert t608001110_x211(89000021, 1047600173, 0)
            return 0
        # Astrologer (Altered) (ON)
        elif GetTalkListEntryResult() == 112:
            assert t608001110_x211(89000020, 1047600175, 1)
            return 0
        # Astrologer (Altered) (OFF)
        elif GetTalkListEntryResult() == 512:
            assert t608001110_x211(89000021, 1047600175, 0)
            return 0
        # Albinauric (ON)
        elif GetTalkListEntryResult() == 113:
            assert t608001110_x211(89000020, 1047600321, 1)
            return 0
        # Albinauric (OFF)
        elif GetTalkListEntryResult() == 513:
            assert t608001110_x211(89000021, 1047600321, 0)
            return 0
        # Marionette Soldier (ON)
        elif GetTalkListEntryResult() == 114:
            assert t608001110_x211(89000020, 1047600248, 1)
            return 0
        # Marionette Soldier (OFF)
        elif GetTalkListEntryResult() == 514:
            assert t608001110_x211(89000021, 1047600248, 0)
            return 0
        # Godskin Noble (ON)
        elif GetTalkListEntryResult() == 115:
            assert t608001110_x211(89000020, 1047600140, 1)
            return 0
        # Godskin Noble (OFF)
        elif GetTalkListEntryResult() == 515:
            assert t608001110_x211(89000021, 1047600140, 0)
            return 0
        # Mushroom (ON)
        elif GetTalkListEntryResult() == 116:
            assert t608001110_x211(89000020, 1047600339, 1)
            return 0
        # Mushroom (OFF)
        elif GetTalkListEntryResult() == 516:
            assert t608001110_x211(89000021, 1047600339, 0)
            return 0
        # Ancestral Fur (ON)
        elif GetTalkListEntryResult() == 117:
            assert t608001110_x211(89000020, 1047600091, 1)
            return 0
        # Ancestral Fur (OFF)
        elif GetTalkListEntryResult() == 517:
            assert t608001110_x211(89000021, 1047600091, 0)
            return 0
        # Ancestral Shaman (ON)
        elif GetTalkListEntryResult() == 118:
            assert t608001110_x211(89000020, 1047600093, 1)
            return 0
        # Ancestral Shaman (OFF)
        elif GetTalkListEntryResult() == 518:
            assert t608001110_x211(89000021, 1047600093, 0)
            return 0
        # Errant Sorcerer (ON)
        elif GetTalkListEntryResult() == 119:
            assert t608001110_x211(89000020, 1047600307, 1)
            return 0
        # Errant Sorcerer (OFF)
        elif GetTalkListEntryResult() == 519:
            assert t608001110_x211(89000021, 1047600307, 0)
            return 0
        # Errant Sorcerer (Altered) (ON)
        elif GetTalkListEntryResult() == 120:
            assert t608001110_x211(89000020, 1047600309, 1)
            return 0
        # Errant Sorcerer (Altered) (OFF)
        elif GetTalkListEntryResult() == 520:
            assert t608001110_x211(89000021, 1047600309, 0)
            return 0
        # Traveling Maiden (ON)
        elif GetTalkListEntryResult() == 121:
            assert t608001110_x211(89000020, 1047600268, 1)
            return 0
        # Traveling Maiden (OFF)
        elif GetTalkListEntryResult() == 521:
            assert t608001110_x211(89000021, 1047600268, 0)
            return 0
        # Traveling Maiden (Altered) (ON)
        elif GetTalkListEntryResult() == 122:
            assert t608001110_x211(89000020, 1047600270, 1)
            return 0
        # Traveling Maiden (Altered) (OFF)
        elif GetTalkListEntryResult() == 522:
            assert t608001110_x211(89000021, 1047600270, 0)
            return 0
        # Queen (ON)
        elif GetTalkListEntryResult() == 123:
            assert t608001110_x211(89000020, 1047600136, 1)
            return 0
        # Queen (OFF)
        elif GetTalkListEntryResult() == 523:
            assert t608001110_x211(89000021, 1047600136, 0)
            return 0
        # Finger Maiden (ON)
        elif GetTalkListEntryResult() == 124:
            assert t608001110_x211(89000020, 1047600272, 1)
            return 0
        # Finger Maiden (OFF)
        elif GetTalkListEntryResult() == 524:
            assert t608001110_x211(89000021, 1047600272, 0)
            return 0
        # Finger Maiden (Altered) (ON)
        elif GetTalkListEntryResult() == 125:
            assert t608001110_x211(89000020, 1047600274, 1)
            return 0
        # Finger Maiden (Altered) (OFF)
        elif GetTalkListEntryResult() == 525:
            assert t608001110_x211(89000021, 1047600274, 0)
            return 0
        # Godskin Apostle (ON)
        elif GetTalkListEntryResult() == 126:
            assert t608001110_x211(89000020, 1047600138, 1)
            return 0
        # Godskin Apostle (OFF)
        elif GetTalkListEntryResult() == 526:
            assert t608001110_x211(89000021, 1047600138, 0)
            return 0
        # Snow Witch (ON)
        elif GetTalkListEntryResult() == 127:
            assert t608001110_x211(89000020, 1047600313, 1)
            return 0
        # Snow Witch (OFF)
        elif GetTalkListEntryResult() == 527:
            assert t608001110_x211(89000021, 1047600313, 0)
            return 0
        # Snow Witch (Altered) (ON)
        elif GetTalkListEntryResult() == 128:
            assert t608001110_x211(89000020, 1047600315, 1)
            return 0
        # Snow Witch (Altered) (OFF)
        elif GetTalkListEntryResult() == 528:
            assert t608001110_x211(89000021, 1047600315, 0)
            return 0
        # Perfumer (ON)
        elif GetTalkListEntryResult() == 129:
            assert t608001110_x211(89000020, 1047600013, 1)
            return 0
        # Perfumer (OFF)
        elif GetTalkListEntryResult() == 529:
            assert t608001110_x211(89000021, 1047600013, 0)
            return 0
        # Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 130:
            assert t608001110_x211(89000020, 1047600015, 1)
            return 0
        # Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 530:
            assert t608001110_x211(89000021, 1047600015, 0)
            return 0
        # Prophet (ON)
        elif GetTalkListEntryResult() == 131:
            assert t608001110_x211(89000020, 1047600168, 1)
            return 0
        # Prophet (OFF)
        elif GetTalkListEntryResult() == 531:
            assert t608001110_x211(89000021, 1047600168, 0)
            return 0
        # Prophet (Altered) (ON)
        elif GetTalkListEntryResult() == 132:
            assert t608001110_x211(89000020, 1047600170, 1)
            return 0
        # Prophet (Altered) (OFF)
        elif GetTalkListEntryResult() == 532:
            assert t608001110_x211(89000021, 1047600170, 0)
            return 0
        # Corhyn (ON)
        elif GetTalkListEntryResult() == 133:
            assert t608001110_x211(89000020, 1047600171, 1)
            return 0
        # Corhyn (OFF)
        elif GetTalkListEntryResult() == 533:
            assert t608001110_x211(89000021, 1047600171, 0)
            return 0
        # Battlemage (ON)
        elif GetTalkListEntryResult() == 134:
            assert t608001110_x211(89000020, 1047600311, 1)
            return 0
        # Battlemage (OFF)
        elif GetTalkListEntryResult() == 534:
            assert t608001110_x211(89000021, 1047600311, 0)
            return 0
        # Consort (ON)
        elif GetTalkListEntryResult() == 135:
            assert t608001110_x211(89000020, 1047600291, 1)
            return 0
        # Consort (OFF)
        elif GetTalkListEntryResult() == 535:
            assert t608001110_x211(89000021, 1047600291, 0)
            return 0
        # Sage (ON)
        elif GetTalkListEntryResult() == 136:
            assert t608001110_x211(89000020, 1047600125, 1)
            return 0
        # Sage (OFF)
        elif GetTalkListEntryResult() == 536:
            assert t608001110_x211(89000021, 1047600125, 0)
            return 0
        # Goldmask (ON)
        elif GetTalkListEntryResult() == 137:
            assert t608001110_x211(89000020, 1047600319, 1)
            return 0
        # Goldmask (OFF)
        elif GetTalkListEntryResult() == 537:
            assert t608001110_x211(89000021, 1047600319, 0)
            return 0
        # Alberich (ON)
        elif GetTalkListEntryResult() == 138:
            assert t608001110_x211(89000020, 1047600021, 1)
            return 0
        # Alberich (OFF)
        elif GetTalkListEntryResult() == 538:
            assert t608001110_x211(89000021, 1047600021, 0)
            return 0
        # Alberich (Altered) (ON)
        elif GetTalkListEntryResult() == 139:
            assert t608001110_x211(89000020, 1047600023, 1)
            return 0
        # Alberich (Altered) (OFF)
        elif GetTalkListEntryResult() == 539:
            assert t608001110_x211(89000021, 1047600023, 0)
            return 0
        # Aristocrat (ON)
        elif GetTalkListEntryResult() == 140:
            assert t608001110_x211(89000020, 1047600117, 1)
            return 0
        # Aristocrat (OFF)
        elif GetTalkListEntryResult() == 540:
            assert t608001110_x211(89000021, 1047600117, 0)
            return 0
        # Wandering Aristocrat (ON)
        elif GetTalkListEntryResult() == 141:
            assert t608001110_x211(89000020, 1047600119, 1)
            return 0
        # Wandering Aristocrat (OFF)
        elif GetTalkListEntryResult() == 541:
            assert t608001110_x211(89000021, 1047600119, 0)
            return 0
        # Old Aristocrat (ON)
        elif GetTalkListEntryResult() == 142:
            assert t608001110_x211(89000020, 1047600121, 1)
            return 0
        # Old Aristocrat (OFF)
        elif GetTalkListEntryResult() == 542:
            assert t608001110_x211(89000021, 1047600121, 0)
            return 0
        # Page (ON)
        elif GetTalkListEntryResult() == 143:
            assert t608001110_x211(89000020, 1047600055, 1)
            return 0
        # Page (OFF)
        elif GetTalkListEntryResult() == 543:
            assert t608001110_x211(89000021, 1047600055, 0)
            return 0
        # Page (Altered) (ON)
        elif GetTalkListEntryResult() == 144:
            assert t608001110_x211(89000020, 1047600057, 1)
            return 0
        # Page (Altered) (OFF)
        elif GetTalkListEntryResult() == 544:
            assert t608001110_x211(89000021, 1047600057, 0)
            return 0
        # Sanguine Noble (ON)
        elif GetTalkListEntryResult() == 145:
            assert t608001110_x211(89000020, 1047600099, 1)
            return 0
        # Sanguine Noble (OFF)
        elif GetTalkListEntryResult() == 545:
            assert t608001110_x211(89000021, 1047600099, 0)
            return 0
        # Brave (ON)
        elif GetTalkListEntryResult() == 146:
            assert t608001110_x211(89000020, 1047600199, 1)
            return 0
        # Brave (OFF)
        elif GetTalkListEntryResult() == 546:
            assert t608001110_x211(89000021, 1047600199, 0)
            return 0
        # Brave (Altered) (ON)
        elif GetTalkListEntryResult() == 147:
            assert t608001110_x211(89000020, 1047600201, 1)
            return 0
        # Brave (Altered) (OFF)
        elif GetTalkListEntryResult() == 547:
            assert t608001110_x211(89000021, 1047600201, 0)
            return 0
        # Travelling Perfumer (ON)
        elif GetTalkListEntryResult() == 148:
            assert t608001110_x211(89000020, 1047600017, 1)
            return 0
        # Travelling Perfumer (OFF)
        elif GetTalkListEntryResult() == 548:
            assert t608001110_x211(89000021, 1047600017, 0)
            return 0
        # Travelling Perfumer (Altered) (ON)
        elif GetTalkListEntryResult() == 149:
            assert t608001110_x211(89000020, 1047600019, 1)
            return 0
        # Travelling Perfumer (Altered) (OFF)
        elif GetTalkListEntryResult() == 549:
            assert t608001110_x211(89000021, 1047600019, 0)
            return 0
        # Spellblade (ON)
        elif GetTalkListEntryResult() == 150:
            assert t608001110_x211(89000020, 1047600025, 1)
            return 0
        # Spellblade (OFF)
        elif GetTalkListEntryResult() == 550:
            assert t608001110_x211(89000021, 1047600025, 0)
            return 0
        # Spellblade (Altered) (ON)
        elif GetTalkListEntryResult() == 151:
            assert t608001110_x211(89000020, 1047600027, 1)
            return 0
        # Spellblade (Altered) (OFF)
        elif GetTalkListEntryResult() == 551:
            assert t608001110_x211(89000021, 1047600027, 0)
            return 0
        # Commoner (ON)
        elif GetTalkListEntryResult() == 152:
            assert t608001110_x211(89000020, 1047600235, 1)
            return 0
        # Commoner (OFF)
        elif GetTalkListEntryResult() == 552:
            assert t608001110_x211(89000021, 1047600235, 0)
            return 0
        # Commoner (Altered) (ON)
        elif GetTalkListEntryResult() == 153:
            assert t608001110_x211(89000020, 1047600237, 1)
            return 0
        # Commoner (Altered) (OFF)
        elif GetTalkListEntryResult() == 553:
            assert t608001110_x211(89000021, 1047600237, 0)
            return 0
        # Simple Commoner (ON)
        elif GetTalkListEntryResult() == 154:
            assert t608001110_x211(89000020, 1047600239, 1)
            return 0
        # Simple Commoner (OFF)
        elif GetTalkListEntryResult() == 554:
            assert t608001110_x211(89000021, 1047600239, 0)
            return 0
        # Ruler (ON)
        elif GetTalkListEntryResult() == 155:
            assert t608001110_x211(89000020, 1047600293, 1)
            return 0
        # Ruler (OFF)
        elif GetTalkListEntryResult() == 555:
            assert t608001110_x211(89000021, 1047600293, 0)
            return 0
        # Upper-Class (ON)
        elif GetTalkListEntryResult() == 156:
            assert t608001110_x211(89000020, 1047600295, 1)
            return 0
        # Upper-Class (OFF)
        elif GetTalkListEntryResult() == 556:
            assert t608001110_x211(89000021, 1047600295, 0)
            return 0
        # Fia (ON)
        elif GetTalkListEntryResult() == 157:
            assert t608001110_x211(89000020, 1047600406, 1)
            return 0
        # Fia (OFF)
        elif GetTalkListEntryResult() == 557:
            assert t608001110_x211(89000021, 1047600406, 0)
            return 0
        # Fia (Altered) (ON)
        elif GetTalkListEntryResult() == 158:
            assert t608001110_x211(89000020, 1047600408, 1)
            return 0
        # Fia (Altered) (OFF)
        elif GetTalkListEntryResult() == 558:
            assert t608001110_x211(89000021, 1047600408, 0)
            return 0
        # High Page (ON)
        elif GetTalkListEntryResult() == 159:
            assert t608001110_x211(89000020, 1047600412, 1)
            return 0
        # High Page (OFF)
        elif GetTalkListEntryResult() == 559:
            assert t608001110_x211(89000021, 1047600412, 0)
            return 0
        # High Page (Altered) (ON)
        elif GetTalkListEntryResult() == 160:
            assert t608001110_x211(89000020, 1047600414, 1)
            return 0
        # High Page (Altered) (OFF)
        elif GetTalkListEntryResult() == 560:
            assert t608001110_x211(89000021, 1047600414, 0)
            return 0
        # Guilty (ON)
        elif GetTalkListEntryResult() == 161:
            assert t608001110_x211(89000020, 1047600035, 1)
            return 0
        # Guilty (OFF)
        elif GetTalkListEntryResult() == 561:
            assert t608001110_x211(89000021, 1047600035, 0)
            return 0
        # Marais (ON)
        elif GetTalkListEntryResult() == 162:
            assert t608001110_x211(89000020, 1047600297, 1)
            return 0
        # Marais (OFF)
        elif GetTalkListEntryResult() == 562:
            assert t608001110_x211(89000021, 1047600297, 0)
            return 0
        # Bloodsoaked (ON)
        elif GetTalkListEntryResult() == 163:
            assert t608001110_x211(89000020, 1047600299, 1)
            return 0
        # Bloodsoaked (OFF)
        elif GetTalkListEntryResult() == 563:
            assert t608001110_x211(89000021, 1047600299, 0)
            return 0
        # Festive (ON)
        elif GetTalkListEntryResult() == 164:
            assert t608001110_x211(89000020, 1047600229, 1)
            return 0
        # Festive (OFF)
        elif GetTalkListEntryResult() == 564:
            assert t608001110_x211(89000021, 1047600229, 0)
            return 0
        # Festive (Altered) (ON)
        elif GetTalkListEntryResult() == 165:
            assert t608001110_x211(89000020, 1047600231, 1)
            return 0
        # Festive (Altered) (OFF)
        elif GetTalkListEntryResult() == 565:
            assert t608001110_x211(89000021, 1047600231, 0)
            return 0
        # Blue Festive (ON)
        elif GetTalkListEntryResult() == 166:
            assert t608001110_x211(89000020, 1047600233, 1)
            return 0
        # Blue Festive (OFF)
        elif GetTalkListEntryResult() == 566:
            assert t608001110_x211(89000021, 1047600233, 0)
            return 0
        # Juvenile Scholar (ON)
        elif GetTalkListEntryResult() == 167:
            assert t608001110_x211(89000020, 1047600317, 1)
            return 0
        # Juvenile Scholar (OFF)
        elif GetTalkListEntryResult() == 567:
            assert t608001110_x211(89000021, 1047600317, 0)
            return 0
        else:
            """State 7"""
            break
    """State 10"""
    return 0
    
# Description Prompt
def t608001110_x200(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
# Change Override (Head)
def t608001110_x210(message=_, flag=_, state=_):
    assert t608001110_x220()
    
    SetEventFlag(flag, state) 
    SetEventFlag(1047610101, 1) 
    #assert t608001110_x200(message)
    return 0
    
# Change Override (Body)
def t608001110_x211(message=_, flag=_, state=_):
    assert t608001110_x221()
    
    SetEventFlag(flag, state) 
    SetEventFlag(1047610101, 1) 
    #assert t608001110_x200(message)
    return 0
    
# Reset Group Flags: Head
def t608001110_x220():
    SetEventFlag(1047600998, 0) 
    SetEventFlag(1047600344, 0) 
    SetEventFlag(1047600126, 0) 
    SetEventFlag(1047600202, 0) 
    SetEventFlag(1047600211, 0) 
    SetEventFlag(1047600240, 0) 
    SetEventFlag(1047600241, 0) 
    SetEventFlag(1047600243, 0) 
    SetEventFlag(1047600244, 0) 
    SetEventFlag(1047600245, 0) 
    SetEventFlag(1047600246, 0) 
    SetEventFlag(1047600249, 0) 
    SetEventFlag(1047600266, 0) 
    SetEventFlag(1047600279, 0) 
    SetEventFlag(1047600324, 0) 
    SetEventFlag(1047600325, 0) 
    SetEventFlag(1047600326, 0) 
    SetEventFlag(1047600327, 0) 
    SetEventFlag(1047600328, 0) 
    SetEventFlag(1047600329, 0) 
    SetEventFlag(1047600330, 0) 
    SetEventFlag(1047600333, 0) 
    SetEventFlag(1047600336, 0) 
    SetEventFlag(1047600337, 0) 
    SetEventFlag(1047600340, 0) 
    SetEventFlag(1047600341, 0) 
    SetEventFlag(1047600347, 0) 
    SetEventFlag(1047600400, 0) 
    SetEventFlag(1047600401, 0) 
    SetEventFlag(1047600402, 0) 
    SetEventFlag(1047600403, 0) 
    SetEventFlag(1047600404, 0) 
    SetEventFlag(1047600419, 0) 
    SetEventFlag(1047600420, 0) 
    SetEventFlag(1047600422, 0) 
    SetEventFlag(1047600182, 0) 
    SetEventFlag(1047600028, 0) 
    SetEventFlag(1047600112, 0) 
    SetEventFlag(1047600114, 0) 
    SetEventFlag(1047600176, 0) 
    SetEventFlag(1047600178, 0) 
    SetEventFlag(1047600300, 0) 
    SetEventFlag(1047600072, 0) 
    SetEventFlag(1047600074, 0) 
    SetEventFlag(1047600220, 0) 
    SetEventFlag(1047600222, 0) 
    SetEventFlag(1047600203, 0) 
    SetEventFlag(1047600205, 0) 
    SetEventFlag(1047600046, 0) 
    SetEventFlag(1047600048, 0) 
    SetEventFlag(1047600131, 0) 
    SetEventFlag(1047600133, 0) 
    SetEventFlag(1047600070, 0) 
    SetEventFlag(1047600008, 0) 
    SetEventFlag(1047600010, 0) 
    SetEventFlag(1047600145, 0) 
    SetEventFlag(1047600147, 0) 
    SetEventFlag(1047600149, 0) 
    SetEventFlag(1047600076, 0) 
    SetEventFlag(1047600078, 0) 
    SetEventFlag(1047600104, 0) 
    SetEventFlag(1047600106, 0) 
    SetEventFlag(1047600036, 0) 
    SetEventFlag(1047600038, 0) 
    SetEventFlag(1047600058, 0) 
    SetEventFlag(1047600060, 0) 
    SetEventFlag(1047600212, 0) 
    SetEventFlag(1047600214, 0) 
    SetEventFlag(1047600159, 0) 
    SetEventFlag(1047600161, 0) 
    SetEventFlag(1047600180, 0) 
    SetEventFlag(1047600184, 0) 
    SetEventFlag(1047600368, 0) 
    SetEventFlag(1047600370, 0) 
    SetEventFlag(1047600050, 0) 
    SetEventFlag(1047600052, 0) 
    SetEventFlag(1047600364, 0) 
    SetEventFlag(1047600366, 0) 
    SetEventFlag(1047600376, 0) 
    SetEventFlag(1047600378, 0) 
    SetEventFlag(1047600360, 0) 
    SetEventFlag(1047600362, 0) 
    SetEventFlag(1047600372, 0) 
    SetEventFlag(1047600374, 0) 
    SetEventFlag(1047600384, 0) 
    SetEventFlag(1047600386, 0) 
    SetEventFlag(1047600110, 0) 
    SetEventFlag(1047600108, 0) 
    SetEventFlag(1047600155, 0) 
    SetEventFlag(1047600157, 0) 
    SetEventFlag(1047600196, 0) 
    SetEventFlag(1047600224, 0) 
    SetEventFlag(1047600226, 0) 
    SetEventFlag(1047600345, 0) 
    SetEventFlag(1047600286, 0) 
    SetEventFlag(1047600288, 0) 
    SetEventFlag(1047600302, 0) 
    SetEventFlag(1047600304, 0) 
    SetEventFlag(1047600348, 0) 
    SetEventFlag(1047600350, 0) 
    SetEventFlag(1047600352, 0) 
    SetEventFlag(1047600354, 0) 
    SetEventFlag(1047600358, 0) 
    SetEventFlag(1047600250, 0) 
    SetEventFlag(1047600252, 0) 
    SetEventFlag(1047600186, 0) 
    SetEventFlag(1047600188, 0) 
    SetEventFlag(1047600380, 0) 
    SetEventFlag(1047600382, 0) 
    SetEventFlag(1047600282, 0) 
    SetEventFlag(1047600284, 0) 
    SetEventFlag(1047600004, 0) 
    SetEventFlag(1047600006, 0) 
    SetEventFlag(1047600040, 0) 
    SetEventFlag(1047600042, 0) 
    SetEventFlag(1047600044, 0) 
    SetEventFlag(1047600127, 0) 
    SetEventFlag(1047600129, 0) 
    SetEventFlag(1047600030, 0) 
    SetEventFlag(1047600032, 0) 
    SetEventFlag(1047600331, 0) 
    SetEventFlag(1047600000, 0) 
    SetEventFlag(1047600002, 0) 
    SetEventFlag(1047600356, 0) 
    SetEventFlag(1047600062, 0) 
    SetEventFlag(1047600064, 0) 
    SetEventFlag(1047600322, 0) 
    SetEventFlag(1047600216, 0) 
    SetEventFlag(1047600218, 0) 
    SetEventFlag(1047600100, 0) 
    SetEventFlag(1047600102, 0) 
    SetEventFlag(1047600094, 0) 
    SetEventFlag(1047600096, 0) 
    SetEventFlag(1047600254, 0) 
    SetEventFlag(1047600256, 0) 
    SetEventFlag(1047600258, 0) 
    SetEventFlag(1047600388, 0) 
    SetEventFlag(1047600390, 0) 
    SetEventFlag(1047600392, 0) 
    SetEventFlag(1047600394, 0) 
    SetEventFlag(1047600396, 0) 
    SetEventFlag(1047600084, 0) 
    SetEventFlag(1047600086, 0) 
    SetEventFlag(1047600088, 0) 
    SetEventFlag(1047600260, 0) 
    SetEventFlag(1047600262, 0) 
    SetEventFlag(1047600080, 0) 
    SetEventFlag(1047600082, 0) 
    SetEventFlag(1047600122, 0) 
    SetEventFlag(1047600163, 0) 
    SetEventFlag(1047600165, 0) 
    SetEventFlag(1047600190, 0) 
    SetEventFlag(1047600398, 0) 
    SetEventFlag(1047600342, 0) 
    SetEventFlag(1047600192, 0) 
    SetEventFlag(1047600194, 0) 
    SetEventFlag(1047600280, 0) 
    SetEventFlag(1047600275, 0) 
    SetEventFlag(1047600277, 0) 
    SetEventFlag(1047600415, 0) 
    SetEventFlag(1047600417, 0) 
    SetEventFlag(1047600066, 0) 
    SetEventFlag(1047600068, 0) 
    SetEventFlag(1047600153, 0) 
    SetEventFlag(1047600151, 0) 
    SetEventFlag(1047600209, 0) 
    SetEventFlag(1047600264, 0) 
    SetEventFlag(1047600207, 0) 
    SetEventFlag(1047600409, 0) 
    SetEventFlag(1047600141, 0) 
    SetEventFlag(1047600143, 0) 
    SetEventFlag(1047600172, 0) 
    SetEventFlag(1047600174, 0) 
    SetEventFlag(1047600320, 0) 
    SetEventFlag(1047600247, 0) 
    SetEventFlag(1047600139, 0) 
    SetEventFlag(1047600338, 0) 
    SetEventFlag(1047600090, 0) 
    SetEventFlag(1047600092, 0) 
    SetEventFlag(1047600306, 0) 
    SetEventFlag(1047600308, 0) 
    SetEventFlag(1047600267, 0) 
    SetEventFlag(1047600269, 0) 
    SetEventFlag(1047600135, 0) 
    SetEventFlag(1047600271, 0) 
    SetEventFlag(1047600273, 0) 
    SetEventFlag(1047600137, 0) 
    SetEventFlag(1047600312, 0) 
    SetEventFlag(1047600314, 0) 
    SetEventFlag(1047600012, 0) 
    SetEventFlag(1047600014, 0) 
    SetEventFlag(1047600167, 0) 
    SetEventFlag(1047600169, 0) 
    SetEventFlag(1047600310, 0) 
    SetEventFlag(1047600290, 0) 
    SetEventFlag(1047600124, 0) 
    SetEventFlag(1047600318, 0) 
    SetEventFlag(1047600020, 0) 
    SetEventFlag(1047600022, 0) 
    SetEventFlag(1047600116, 0) 
    SetEventFlag(1047600118, 0) 
    SetEventFlag(1047600120, 0) 
    SetEventFlag(1047600054, 0) 
    SetEventFlag(1047600056, 0) 
    SetEventFlag(1047600098, 0) 
    SetEventFlag(1047600198, 0) 
    SetEventFlag(1047600200, 0) 
    SetEventFlag(1047600016, 0) 
    SetEventFlag(1047600018, 0) 
    SetEventFlag(1047600024, 0) 
    SetEventFlag(1047600026, 0) 
    SetEventFlag(1047600234, 0) 
    SetEventFlag(1047600236, 0) 
    SetEventFlag(1047600238, 0) 
    SetEventFlag(1047600292, 0) 
    SetEventFlag(1047600294, 0) 
    SetEventFlag(1047600405, 0) 
    SetEventFlag(1047600407, 0) 
    SetEventFlag(1047600411, 0) 
    SetEventFlag(1047600413, 0) 
    SetEventFlag(1047600034, 0) 
    SetEventFlag(1047600296, 0) 
    SetEventFlag(1047600298, 0) 
    SetEventFlag(1047600228, 0) 
    SetEventFlag(1047600230, 0) 
    SetEventFlag(1047600232, 0) 
    SetEventFlag(1047600316, 0)
    SetEventFlag(1047600427, 0)
    SetEventFlag(1047600428, 0)
    SetEventFlag(1047600429, 0)
    SetEventFlag(1047600430, 0)
    
    return 0
    
# Reset Group Flags: Body
def t608001110_x221():
    SetEventFlag(1047600421, 0) 
    SetEventFlag(1047600334, 0) 
    SetEventFlag(1047600335, 0) 
    SetEventFlag(1047600423, 0) 
    SetEventFlag(1047600424, 0) 
    SetEventFlag(1047600425, 0) 
    SetEventFlag(1047600426, 0) 
    SetEventFlag(1047600242, 0) 
    SetEventFlag(1047600029, 0) 
    SetEventFlag(1047600113, 0) 
    SetEventFlag(1047600115, 0) 
    SetEventFlag(1047600177, 0) 
    SetEventFlag(1047600179, 0) 
    SetEventFlag(1047600301, 0) 
    SetEventFlag(1047600073, 0) 
    SetEventFlag(1047600075, 0) 
    SetEventFlag(1047600221, 0) 
    SetEventFlag(1047600223, 0) 
    SetEventFlag(1047600204, 0) 
    SetEventFlag(1047600206, 0) 
    SetEventFlag(1047600047, 0) 
    SetEventFlag(1047600049, 0) 
    SetEventFlag(1047600132, 0) 
    SetEventFlag(1047600134, 0) 
    SetEventFlag(1047600071, 0) 
    SetEventFlag(1047600009, 0) 
    SetEventFlag(1047600011, 0) 
    SetEventFlag(1047600146, 0) 
    SetEventFlag(1047600148, 0) 
    SetEventFlag(1047600150, 0) 
    SetEventFlag(1047600077, 0) 
    SetEventFlag(1047600079, 0) 
    SetEventFlag(1047600105, 0) 
    SetEventFlag(1047600107, 0) 
    SetEventFlag(1047600037, 0) 
    SetEventFlag(1047600039, 0) 
    SetEventFlag(1047600059, 0) 
    SetEventFlag(1047600061, 0) 
    SetEventFlag(1047600213, 0) 
    SetEventFlag(1047600215, 0) 
    SetEventFlag(1047600160, 0) 
    SetEventFlag(1047600162, 0) 
    SetEventFlag(1047600181, 0) 
    SetEventFlag(1047600185, 0) 
    SetEventFlag(1047600369, 0) 
    SetEventFlag(1047600371, 0) 
    SetEventFlag(1047600051, 0) 
    SetEventFlag(1047600053, 0) 
    SetEventFlag(1047600365, 0) 
    SetEventFlag(1047600367, 0) 
    SetEventFlag(1047600377, 0) 
    SetEventFlag(1047600379, 0) 
    SetEventFlag(1047600361, 0) 
    SetEventFlag(1047600363, 0) 
    SetEventFlag(1047600373, 0) 
    SetEventFlag(1047600375, 0) 
    SetEventFlag(1047600385, 0) 
    SetEventFlag(1047600387, 0) 
    SetEventFlag(1047600111, 0) 
    SetEventFlag(1047600109, 0) 
    SetEventFlag(1047600156, 0) 
    SetEventFlag(1047600158, 0) 
    SetEventFlag(1047600197, 0) 
    SetEventFlag(1047600225, 0) 
    SetEventFlag(1047600227, 0) 
    SetEventFlag(1047600346, 0) 
    SetEventFlag(1047600287, 0) 
    SetEventFlag(1047600289, 0) 
    SetEventFlag(1047600303, 0) 
    SetEventFlag(1047600305, 0) 
    SetEventFlag(1047600349, 0) 
    SetEventFlag(1047600351, 0) 
    SetEventFlag(1047600353, 0) 
    SetEventFlag(1047600355, 0) 
    SetEventFlag(1047600359, 0) 
    SetEventFlag(1047600251, 0) 
    SetEventFlag(1047600253, 0) 
    SetEventFlag(1047600187, 0) 
    SetEventFlag(1047600189, 0) 
    SetEventFlag(1047600381, 0) 
    SetEventFlag(1047600383, 0) 
    SetEventFlag(1047600283, 0) 
    SetEventFlag(1047600285, 0) 
    SetEventFlag(1047600005, 0) 
    SetEventFlag(1047600007, 0) 
    SetEventFlag(1047600041, 0) 
    SetEventFlag(1047600043, 0) 
    SetEventFlag(1047600045, 0) 
    SetEventFlag(1047600128, 0) 
    SetEventFlag(1047600130, 0) 
    SetEventFlag(1047600031, 0) 
    SetEventFlag(1047600033, 0) 
    SetEventFlag(1047600332, 0) 
    SetEventFlag(1047600001, 0) 
    SetEventFlag(1047600003, 0) 
    SetEventFlag(1047600357, 0) 
    SetEventFlag(1047600063, 0) 
    SetEventFlag(1047600065, 0) 
    SetEventFlag(1047600323, 0) 
    SetEventFlag(1047600217, 0) 
    SetEventFlag(1047600219, 0) 
    SetEventFlag(1047600101, 0) 
    SetEventFlag(1047600103, 0) 
    SetEventFlag(1047600095, 0) 
    SetEventFlag(1047600097, 0) 
    SetEventFlag(1047600255, 0) 
    SetEventFlag(1047600257, 0) 
    SetEventFlag(1047600259, 0) 
    SetEventFlag(1047600389, 0) 
    SetEventFlag(1047600391, 0) 
    SetEventFlag(1047600393, 0) 
    SetEventFlag(1047600395, 0) 
    SetEventFlag(1047600397, 0) 
    SetEventFlag(1047600085, 0) 
    SetEventFlag(1047600087, 0) 
    SetEventFlag(1047600089, 0) 
    SetEventFlag(1047600261, 0) 
    SetEventFlag(1047600263, 0) 
    SetEventFlag(1047600081, 0) 
    SetEventFlag(1047600083, 0) 
    SetEventFlag(1047600123, 0) 
    SetEventFlag(1047600164, 0) 
    SetEventFlag(1047600166, 0) 
    SetEventFlag(1047600191, 0) 
    SetEventFlag(1047600399, 0) 
    SetEventFlag(1047600343, 0) 
    SetEventFlag(1047600193, 0) 
    SetEventFlag(1047600195, 0) 
    SetEventFlag(1047600281, 0) 
    SetEventFlag(1047600276, 0) 
    SetEventFlag(1047600278, 0) 
    SetEventFlag(1047600416, 0) 
    SetEventFlag(1047600418, 0) 
    SetEventFlag(1047600067, 0) 
    SetEventFlag(1047600069, 0) 
    SetEventFlag(1047600154, 0) 
    SetEventFlag(1047600152, 0) 
    SetEventFlag(1047600210, 0) 
    SetEventFlag(1047600265, 0) 
    SetEventFlag(1047600208, 0) 
    SetEventFlag(1047600410, 0) 
    SetEventFlag(1047600142, 0) 
    SetEventFlag(1047600144, 0) 
    SetEventFlag(1047600173, 0) 
    SetEventFlag(1047600175, 0) 
    SetEventFlag(1047600321, 0) 
    SetEventFlag(1047600248, 0) 
    SetEventFlag(1047600140, 0) 
    SetEventFlag(1047600339, 0) 
    SetEventFlag(1047600091, 0) 
    SetEventFlag(1047600093, 0) 
    SetEventFlag(1047600307, 0) 
    SetEventFlag(1047600309, 0) 
    SetEventFlag(1047600268, 0) 
    SetEventFlag(1047600270, 0) 
    SetEventFlag(1047600136, 0) 
    SetEventFlag(1047600272, 0) 
    SetEventFlag(1047600274, 0) 
    SetEventFlag(1047600138, 0) 
    SetEventFlag(1047600313, 0) 
    SetEventFlag(1047600315, 0) 
    SetEventFlag(1047600013, 0) 
    SetEventFlag(1047600015, 0) 
    SetEventFlag(1047600168, 0) 
    SetEventFlag(1047600170, 0) 
    SetEventFlag(1047600171, 0) 
    SetEventFlag(1047600311, 0) 
    SetEventFlag(1047600291, 0) 
    SetEventFlag(1047600125, 0) 
    SetEventFlag(1047600319, 0) 
    SetEventFlag(1047600021, 0) 
    SetEventFlag(1047600023, 0) 
    SetEventFlag(1047600117, 0) 
    SetEventFlag(1047600119, 0) 
    SetEventFlag(1047600121, 0) 
    SetEventFlag(1047600055, 0) 
    SetEventFlag(1047600057, 0) 
    SetEventFlag(1047600099, 0) 
    SetEventFlag(1047600199, 0) 
    SetEventFlag(1047600201, 0) 
    SetEventFlag(1047600017, 0) 
    SetEventFlag(1047600019, 0) 
    SetEventFlag(1047600025, 0) 
    SetEventFlag(1047600027, 0) 
    SetEventFlag(1047600235, 0) 
    SetEventFlag(1047600237, 0) 
    SetEventFlag(1047600239, 0) 
    SetEventFlag(1047600293, 0) 
    SetEventFlag(1047600295, 0) 
    SetEventFlag(1047600406, 0) 
    SetEventFlag(1047600408, 0) 
    SetEventFlag(1047600412, 0) 
    SetEventFlag(1047600414, 0) 
    SetEventFlag(1047600035, 0) 
    SetEventFlag(1047600297, 0) 
    SetEventFlag(1047600299, 0) 
    SetEventFlag(1047600229, 0) 
    SetEventFlag(1047600231, 0) 
    SetEventFlag(1047600233, 0) 
    SetEventFlag(1047600317, 0)
    SetEventFlag(1047600431, 0)
    
    return 0
    