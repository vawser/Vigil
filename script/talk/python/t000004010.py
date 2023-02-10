# -*- coding: utf-8 -*-
#-----------------------------------------------------
# Jar of Discipline
#-----------------------------------------------------
def t000004010_1():
    """State 0,1"""
    # actionbutton:6210:"Talk"
    t000004010_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1)
    Quit()

def t000004010_1000():
    """State 0,2,3"""
    assert t000004010_x35()
    """State 1"""
    c1_120(1000)
    Quit()

def t000004010_2000():
    """State 0,2,3"""
    assert t000004010_x36()
    """State 1"""
    c1_120(2000)
    Quit()

def t000004010_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
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

def t000004010_x1():
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

def t000004010_x2():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004010_x3(val2=10, val3=12):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t000004010_x19()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t000004010_x1()
    else:
        """State 4,7"""
        call = t000004010_x32()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t000004010_x1()
    """State 9"""
    return 0

def t000004010_x4():
    """State 0,1"""
    assert t000004010_x1()
    """State 2"""
    return 0

def t000004010_x5(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t000004010_x22(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t000004010_x21()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t000004010_x6(val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t000004010_x9(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t000004010_x13(val1=val1, z1=z1)
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
            call = t000004010_x15(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t000004010_x26() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t000004010_x11(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t000004010_x7(val2=10, val3=12):
    """State 0,1"""
    call = t000004010_x17(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t000004010_x3(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000004010_x8(flag1=3223, val2=10, val3=12):
    """State 0,8"""
    assert t000004010_x34()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t000004010_x20()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004010_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t000004010_x9(actionbutton1=6210, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t000004010_x10(z6=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t000004010_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004010_x10(z6=_, val6=_):
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

def t000004010_x11(val2=10, val3=12):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t000004010_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t000004010_x12()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t000004010_x27()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t000004010_x12():
    """State 0,1"""
    assert t000004010_x10(z6=1101, val6=1101)
    """State 2"""
    return 0

def t000004010_x13(val1=5, z1=1):
    """State 0,2"""
    assert t000004010_x23()
    """State 1"""
    call = t000004010_x14()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t000004010_x25()
    """State 4"""
    return 0

def t000004010_x14():
    """State 0,1"""
    assert t000004010_x10(z6=1000, val6=1000)
    """State 2"""
    return 0

def t000004010_x15(val5=30):
    """State 0,1"""
    call = t000004010_x16()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t000004010_x26()
    """State 3"""
    return 0

def t000004010_x16():
    """State 0,1"""
    assert t000004010_x10(z6=1100, val6=1100)
    """State 2"""
    return 0

def t000004010_x17(val2=10, val3=12):
    """State 0,5"""
    assert t000004010_x34()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t000004010_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t000004010_x28()
    """Unused"""
    """State 6"""
    return 0

def t000004010_x18():
    """State 0,2"""
    call = t000004010_x10(z6=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t000004010_x19():
    """State 0,1"""
    assert t000004010_x10(z6=1001, val6=1001)
    """State 2"""
    return 0

def t000004010_x20():
    """State 0,1"""
    assert t000004010_x10(z6=1103, val6=1103)
    """State 2"""
    return 0

def t000004010_x21():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000004010_x22(flag1=3223, flag2=3221, flag3=3222, val1=5, val2=10, val3=12, val4=30, val5=30, actionbutton1=6210,
                   flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                   z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t000004010_x6(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t000004010_x8(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t000004010_x7(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or (IsPlayerDead() == 1 and not DoesSelfHaveSpEffect(9649)):
            pass
        """State 4"""
        assert t000004010_x33() and (not GetEventFlag(9000) and not IsPlayerDead())
    """Unused"""
    """State 5"""
    return 0

def t000004010_x23():
    """State 0,1"""
    assert t000004010_x24()
    """State 2"""
    return 0

def t000004010_x24():
    """State 0,1"""
    assert t000004010_x10(z6=1104, val6=1104)
    """State 2"""
    return 0

def t000004010_x25():
    """State 0,1"""
    call = t000004010_x10(z6=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t000004010_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004010_x26():
    """State 0,1"""
    call = t000004010_x10(z6=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t000004010_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004010_x27():
    """State 0,1"""
    call = t000004010_x10(z6=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t000004010_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004010_x28():
    """State 0,1"""
    call = t000004010_x10(z6=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t000004010_x4()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t000004010_x29(text2=_, mode4=1):
    """State 0,4"""
    assert t000004010_x2() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000004010_x30(text1=_, z5=_, mode3=1):
    """State 0,5"""
    assert t000004010_x31() and CheckSpecificPersonTalkHasEnded(0) == 1
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

def t000004010_x31():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000004010_x32():
    """State 0,1"""
    assert t000004010_x10(z6=1002, val6=1002)
    """State 2"""
    return 0

def t000004010_x33():
    """State 0,1"""
    assert t000004010_x1()
    """State 2"""
    return 0

def t000004010_x34():
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

def t000004010_x35():
    assert CheckSpecificPersonTalkHasEnded(0) == 1
    """State 8"""
    assert t000004010_x100()
    """State 9"""
    return 0

def t000004010_x36():
    """State 0,1"""
    assert t000004010_x0(actionbutton1=6210, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000, flag4=6000)
                
    """State 4"""
    return 0

#----------------------------------------------------
# Training Options
#----------------------------------------------------
def t000004010_x100():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Spawn Dummy
        AddTalkListData(6, 80103004, -1)
        
        # Formation Type
        AddTalkListData(4, 80103003, -1)
        
        # Enemy Type
        AddTalkListData(5, 80103400, -1)
        
        # Max HP
        AddTalkListData(2, 80103002, -1)
        
        # Absorption
        AddTalkListData(3, 80103001, -1)
        
        # Status
        AddTalkListData(1, 80103000, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x101()
            continue
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x110()
            continue
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x120()
            continue
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x130()
            continue
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x140()
            continue
        elif GetTalkListEntryResult() == 6:
            SetEventFlag(1047610700, 1)
            assert t000004010_x150(80103080)
            return 0
        else:
            """State 6,8"""
            return 0
            
#----------------------------------------------------
# Core Configuration
#----------------------------------------------------
def t000004010_x101():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Can regenerate HP (off)
        AddTalkListDataIf(GetEventFlag(1047610801) == 0, 1, 80103120, -1)
        # Can regenerate HP (on)
        AddTalkListDataIf(GetEventFlag(1047610801) == 1, 1, 80103130, -1)
        
        # Can be staggered (off)
        AddTalkListDataIf(GetEventFlag(1047610802) == 0, 2, 80103121, -1)
        # Can be staggered (on)
        AddTalkListDataIf(GetEventFlag(1047610802) == 1, 2, 80103131, -1)
        
        # Can be inflicted by status effects (off)
        AddTalkListDataIf(GetEventFlag(1047610804) == 0, 3, 80103122, -1)
        # Can be inflicted by status effects (on)
        AddTalkListDataIf(GetEventFlag(1047610804) == 1, 3, 80103132, -1)
        
        # Can fight back (off)
        AddTalkListDataIf(GetEventFlag(1047610803) == 0, 4, 80103123, -1)
        # Can fight back (on)
        AddTalkListDataIf(GetEventFlag(1047610803) == 1, 4, 80103133, -1)
        
        # Can be backstabbed (off)
        AddTalkListDataIf(GetEventFlag(1047610805) == 0, 5, 80103124, -1)
        # Can be backstabbed (off)
        AddTalkListDataIf(GetEventFlag(1047610805) == 1, 5, 80103134, -1)
        
        # Can deal damage (off)
        AddTalkListDataIf(GetEventFlag(1047610806) == 0, 6, 80103125, -1)
        # Can deal damage (on)
        AddTalkListDataIf(GetEventFlag(1047610806) == 1, 6, 80103135, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        # HP Regen
        if GetTalkListEntryResult() == 1:
            assert t000004010_x102(1047610801, 80103020, 80103021)
            return 0
        # Stagger
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x102(1047610802, 80103030, 80103031)
            return 0
        # Aux Inflict
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x102(1047610804, 80103040, 80103041)
            return 0
        # Hostility
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x102(1047610803, 80103050, 80103051)
            return 0
        # Backstabs
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x102(1047610805, 80103060, 80103061)
            return 0
        # Damage
        elif GetTalkListEntryResult() == 6:
            assert t000004010_x102(1047610806, 80103070, 80103071)
            return 0
        else:
            """State 6,8"""
            return 0
          
def t000004010_x102(flag=_, enable_text=_, disable_text=_):
    if(GetEventFlag(flag) == 1):
        SetEventFlag(flag, 0)
        assert t000004010_x150(disable_text)
    else:
        SetEventFlag(flag, 1)
        assert t000004010_x150(enable_text)
          
    return 0
    
#----------------------------------------------------
# HP Configuration
#----------------------------------------------------
def t000004010_x110():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Set Max HP to 2,000
        AddTalkListDataIf(GetEventFlag(1047610810) == 0, 1, 80103100, -1)
        # Set Max HP to 2,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610810) == 1, 1, 80103110, -1)
        
        # Set Max HP to 5,000
        AddTalkListDataIf(GetEventFlag(1047610811) == 0, 2, 80103101, -1)
        # Set Max HP to 5,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610811) == 1, 2, 80103111, -1)
        
        # Set Max HP to 10,000
        AddTalkListDataIf(GetEventFlag(1047610812) == 0, 3, 80103102, -1)
        # Set Max HP to 10,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610812) == 1, 3, 80103112, -1)
        
        # Set Max HP to 20,000
        AddTalkListDataIf(GetEventFlag(1047610813) == 0, 4, 80103103, -1)
        # Set Max HP to 20,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610813) == 1, 4, 80103113, -1)
        
        # Set Max HP to 50,000
        AddTalkListDataIf(GetEventFlag(1047610814) == 0, 5, 80103104, -1)
        # Set Max HP to 50,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610814) == 1, 5, 80103114, -1)
        
        # Set Max HP to 10,000
        AddTalkListDataIf(GetEventFlag(1047610815) == 0, 6, 80103105, -1)
        # Set Max HP to 10,000 (selected)
        AddTalkListDataIf(GetEventFlag(1047610815) == 1, 6, 80103115, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x111(1047610810)
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x111(1047610811)
            return 0
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x111(1047610812)
            return 0
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x111(1047610813)
            return 0
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x111(1047610814)
            return 0
        elif GetTalkListEntryResult() == 6:
            assert t000004010_x111(1047610815)
            return 0
        else:
            """State 6,8"""
            return 0
            
def t000004010_x111(flag=_):
    SetEventFlag(1047610810, 0)
    SetEventFlag(1047610811, 0)
    SetEventFlag(1047610812, 0)
    SetEventFlag(1047610813, 0)
    SetEventFlag(1047610814, 0)
    SetEventFlag(1047610815, 0)
    
    SetEventFlag(flag, 1)
    assert t000004010_x150(80103090)
          
    return 0
    
#----------------------------------------------------
# Absorption Configuration
#----------------------------------------------------
def t000004010_x120():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Standard Absorption
        AddTalkListData(1, 80103200, -1)
        
        # Slash Absorption
        AddTalkListData(2, 80103201, -1)
        
        # Strike Absorption
        AddTalkListData(3, 80103202, -1)
        
        # Thrust Absorption
        AddTalkListData(4, 80103203, -1)
        
        # Magic Absorption
        AddTalkListData(5, 80103204, -1)
        
        # Fire Absorption
        AddTalkListData(6, 80103205, -1)
        
        # Lightning Absorption
        AddTalkListData(7, 80103206, -1)
        
        # Holy Absorption
        AddTalkListData(8, 80103207, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x121(1047610820)
            continue
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x121(1047610870)
            continue
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x121(1047610880)
            continue
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x121(1047610890)
            continue
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x121(1047610830)
            continue
        elif GetTalkListEntryResult() == 6:
            assert t000004010_x121(1047610840)
            continue
        elif GetTalkListEntryResult() == 7:
            assert t000004010_x121(1047610850)
            continue
        elif GetTalkListEntryResult() == 8:
            assert t000004010_x121(1047610860)
            continue
        else:
            """State 6,8"""
            return 0
            
# Absorption Menu
def t000004010_x121(base_flag=_):
    while True:
        ClearTalkListData()
        c1_110()
        
        # None
        AddTalkListDataIf(GetEventFlag(base_flag) == 0, 1, 80103210, -1)
        # None (selected)
        AddTalkListDataIf(GetEventFlag(base_flag) == 1, 1, 80103220, -1)
        
        # +20%
        AddTalkListDataIf(GetEventFlag(base_flag + 1) == 0, 2, 80103211, -1)
        # +20% (selected)
        AddTalkListDataIf(GetEventFlag(base_flag + 1) == 1, 2, 80103221, -1)
        
        # +40%
        AddTalkListDataIf(GetEventFlag(base_flag + 2) == 0, 3, 80103212, -1)
        # +40% (selected)
        AddTalkListDataIf(GetEventFlag(base_flag + 2) == 1, 3, 80103222, -1)
        
        # +60%
        AddTalkListDataIf(GetEventFlag(base_flag + 3) == 0, 4, 80103213, -1)
        # +60% (selected)
        AddTalkListDataIf(GetEventFlag(base_flag + 3) == 1, 4, 80103223, -1)
        
        # +80%
        AddTalkListDataIf(GetEventFlag(base_flag + 4) == 0, 5, 80103214, -1)
        # +80% (selected)
        AddTalkListDataIf(GetEventFlag(base_flag + 4) == 1, 5, 80103224, -1)
        
        # +100%
        AddTalkListDataIf(GetEventFlag(base_flag + 5) == 0, 6, 80103215, -1)
        # +100% (selected)
        AddTalkListDataIf(GetEventFlag(base_flag + 5) == 1, 6, 80103225, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x122(base_flag, base_flag)
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x122(base_flag, base_flag + 1)
            return 0
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x122(base_flag, base_flag + 2)
            return 0
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x122(base_flag, base_flag + 3)
            return 0
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x122(base_flag, base_flag + 4)
            return 0
        elif GetTalkListEntryResult() == 6:
            assert t000004010_x122(base_flag, base_flag + 5)
            return 0
        else:
            """State 6,8"""
            return 0
            
def t000004010_x122(base_flag=_, flag=_):
    SetEventFlag(base_flag, 0)
    SetEventFlag(base_flag + 1, 0)
    SetEventFlag(base_flag + 2, 0)
    SetEventFlag(base_flag + 3, 0)
    SetEventFlag(base_flag + 4, 0)
    SetEventFlag(base_flag + 5, 0)
    
    SetEventFlag(flag, 1)
    assert t000004010_x150(80103230)
          
    return 0
    
#----------------------------------------------------
# Formation Configuration
#----------------------------------------------------
def t000004010_x130():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Single
        AddTalkListDataIf(GetEventFlag(1047610701) == 0, 1, 80103300, -1)
        # Single (selected)
        AddTalkListDataIf(GetEventFlag(1047610701) == 1, 1, 80103310, -1)
        
        # Triangle Triple
        AddTalkListDataIf(GetEventFlag(1047610702) == 0, 2, 80103301, -1)
        # Triangle Triple (selected)
        AddTalkListDataIf(GetEventFlag(1047610702) == 1, 2, 80103311, -1)
        
        # Square Quad
        AddTalkListDataIf(GetEventFlag(1047610703) == 0, 3, 80103302, -1)
        # Square Quad (selected)
        AddTalkListDataIf(GetEventFlag(1047610703) == 1, 3, 80103312, -1)
        
        # Parallel Duo
        AddTalkListDataIf(GetEventFlag(1047610704) == 0, 4, 80103303, -1)
        # Parallel Duo (selected)
        AddTalkListDataIf(GetEventFlag(1047610714) == 1, 4, 80103313, -1)
        
        # Clustered Mass
        AddTalkListDataIf(GetEventFlag(1047610705) == 0, 5, 80103304, -1)
        # Clustered Mass (selected)
        AddTalkListDataIf(GetEventFlag(1047610705) == 1, 5, 80103314, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x131(1047610701)
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x131(1047610702)
            return 0
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x131(1047610703)
            return 0
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x131(1047610704)
            return 0
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x131(1047610705)
            return 0
        else:
            """State 6,8"""
            return 0
            
def t000004010_x131(flag=_):
    SetEventFlag(1047610701, 0)
    SetEventFlag(1047610702, 0)
    SetEventFlag(1047610703, 0)
    SetEventFlag(1047610704, 0)
    SetEventFlag(1047610705, 0)
    
    SetEventFlag(flag, 1)
    SetEventFlag(1047610700, 1)
    
    assert t000004010_x150(80103320)
    
    return 0
    
#----------------------------------------------------
# Type Configuration
#----------------------------------------------------
def t000004010_x140():
    while True:
        ClearTalkListData()
        c1_110()
        
        # Player: Self
        AddTalkListDataIf(GetEventFlag(1047610714) == 0, 4, 80103404, -1)
        # Player: Self (selected)
        AddTalkListDataIf(GetEventFlag(1047610714) == 1, 4, 80103413, -1)
        
        # Player: Random
        AddTalkListDataIf(GetEventFlag(1047610715) == 0, 5, 80103405, -1)
        # Player: Random (selected)
        AddTalkListDataIf(GetEventFlag(1047610715) == 1, 5, 80103414, -1)
        
        # Black Knife Assassin
        AddTalkListDataIf(GetEventFlag(1047610711) == 0, 1, 80103401, -1)
        # Black Knife Assassin (selected)
        AddTalkListDataIf(GetEventFlag(1047610711) == 1, 1, 80103410, -1)
        
        # Runebear
        AddTalkListDataIf(GetEventFlag(1047610712) == 0, 2, 80103402, -1)
        # Runebear (selected)
        AddTalkListDataIf(GetEventFlag(1047610712) == 1, 2, 80103411, -1)
        
        # Imp
        AddTalkListDataIf(GetEventFlag(1047610713) == 0, 3, 80103403, -1)
        # Imp (selected)
        AddTalkListDataIf(GetEventFlag(1047610713) == 1, 3, 80103412, -1)
        
        # Leave
        AddTalkListData(9, 20000009, -1)
        
        ShowShopMessage(1)
        
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        
        if GetTalkListEntryResult() == 1:
            assert t000004010_x141(1047610711)
            return 0
        elif GetTalkListEntryResult() == 2:
            assert t000004010_x141(1047610712)
            return 0
        elif GetTalkListEntryResult() == 3:
            assert t000004010_x141(1047610713)
            return 0
        elif GetTalkListEntryResult() == 4:
            assert t000004010_x141(1047610714)
            return 0
        elif GetTalkListEntryResult() == 5:
            assert t000004010_x141(1047610715)
            return 0
        else:
            """State 6,8"""
            return 0
            
def t000004010_x141(flag=_):
    SetEventFlag(1047610711, 0)
    SetEventFlag(1047610712, 0)
    SetEventFlag(1047610713, 0)
    SetEventFlag(1047610714, 0)
    SetEventFlag(1047610715, 0)
    
    SetEventFlag(flag, 1)
    SetEventFlag(1047610710, 1)
    SetEventFlag(1047610700, 1) # Location Update so they are placed too
    
    assert t000004010_x150(80103490)
    
    return 0
    
#----------------------------------------------------
# Utility
#----------------------------------------------------         
# Description Prompt
def t000004010_x150(action1=_):
    """State 0,1"""
    OpenGenericDialog(8, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0
    
