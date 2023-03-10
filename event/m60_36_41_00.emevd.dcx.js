// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common.emevd N:\GR\data\Param\event\m60.emevd N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd 
// @linked    [0,72,138,220]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    RegisterBonfire(1036410000, 1036411950, 0, 0, 0, 5);
    InitializeCommonEvent(0, 90005570, 60824, 54, 1036411500, 2, 1, 0);
    InitializeEvent(0, 1036413700, 1036410700, 1036410705);
    InitializeEvent(0, 1036413701, 1036410700);
    InitializeEvent(0, 1036413702, 1036410700);
    InitializeCommonEvent(0, 90005704, 1036410700, 4101, 4100, 1036419201, 3);
    InitializeCommonEvent(0, 90005703, 1036410700, 4101, 4102, 1036419201, 4101, 4100, 4104, -1);
    InitializeCommonEvent(0, 90005702, 1036410700, 4103, 4100, 4104);
    InitializeCommonEvent(0, 90005750, 1036411700, 4350, 104100, 400410, 400410, 1036419215, 0);
    
    // Warp Gate: Slumbering Wolf's Chack -> Consecrated Snowfield
    InitializeEvent(0, 1036423500, 1036413500, 1036410960, 1036410961, 1036410962);
});

$Event(50, Default, function() {
    SetCharacterBackreadState(1036410700, true);
    SetCharacterBackreadState(1036410705, true);
});

// Warp Gate - Setup
$Event(1036423500, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    
    if (!ThisEventSlot()) {
        DeleteAssetfollowingSFX(X0_4, true);
        WaitFixedTimeFrames(1);
    }
    
    CreateAssetfollowingSFX(X0_4, 200, 806870);
    
    WaitFor(ActionButtonInArea(9140, X0_4);)
    
    WaitFixedTimeSeconds(0.033);
   
    DisplayGenericDialogAndSetEventFlags(4305, PromptType.YESNO, NumberofOptions.TwoButtons, X0_4, 3, X4_4, X8_4, X12_4);
    
    if (!EventFlag(X4_4)) {
        WaitFixedTimeSeconds(1);
        RestartEvent();
    }

    RotateCharacter(10000, X0_4, -1, true);
    ForceAnimationPlayback(10000, 60490, false, false, false);
    
    WaitFixedTimeSeconds(3);
    
    // m60_50_55_00
    WarpPlayer(60, 50, 55, 0, 1050550980, -1);
});

$Event(1036413700, Restart, function(X0_4, X4_4) {
    WaitFixedTimeFrames(1);
    DisableNetworkSync();
    if (PlayerIsInOwnWorld()) {
        if (EventFlag(4100)) {
            SetEventFlagID(1036419203, OFF);
        }
    }
L10:
    SetCharacterBackreadState(X4_4, false);
    EnableCharacter(X4_4);
    SetCharacterTeamType(X4_4, TeamType.Disabled);
    ForceAnimationPlayback(X4_4, 30020, false, false, false);
    if (!EventFlag(4105)) {
        DisableCharacter(X0_4);
        SetCharacterBackreadState(X0_4, true);
        WaitFor(EventFlag(4105));
        RestartEvent();
    }
L5:
    if (EventFlag(1051587800)) {
        DisableCharacter(X0_4);
        SetCharacterBackreadState(X0_4, true);
        SetEventFlagID(1036419215, ON);
    } else {
        GotoIf(L1, EventFlag(4100));
        GotoIf(L2, EventFlag(4101));
        GotoIf(L3, EventFlag(4102));
        GotoIf(L4, EventFlag(4103));
L1:
        SetCharacterBackreadState(X0_4, false);
        EnableCharacter(X0_4);
        SetCharacterTeamType(X0_4, TeamType.FriendlyNPC);
        ForceAnimationPlayback(X0_4, 30020, false, false, false);
        GotoIf(L20, mainGroupAbuse);
L2:
        SetCharacterBackreadState(X0_4, false);
        EnableCharacter(X0_4);
        SetCharacterTeamType(X0_4, TeamType.HostileNPC);
        Goto(L20);
L3:
        SetCharacterBackreadState(X0_4, false);
        EnableCharacter(X0_4);
        SetCharacterTeamType(X0_4, TeamType.HostileNPC);
        Goto(L20);
L4:
        ForceCharacterTreasure(X0_4);
        DisableCharacter(X0_4);
        SetCharacterBackreadState(X0_4, true);
        Goto(L20);
    }
L20:
    WaitFor(!EventFlag(4105));
    RestartEvent();
});

$Event(1036413701, Restart, function(X0_4) {
    WaitFixedTimeFrames(1);
    EndIf(!PlayerIsInOwnWorld());
    EndIf(!EventFlag(4100));
    EndIf(!EventFlag(4105));
    WaitFor(EventFlag(1036419209));
    DisableCharacterCollision(X0_4);
    WaitFixedTimeSeconds(30);
    DisableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, true);
    EndEvent();
});

$Event(1036413702, Restart, function(X0_4) {
    EndIf(EventFlag(4101));
    EndIf(EventFlag(4103));
    WaitFor(CharacterHasSpEffect(X0_4, 9644) || EventFlag(4101));
    EndIf(CharacterHasSpEffect(X0_4, 9644) && !EventFlag(4101));
    ForceAnimationPlayback(X0_4, 20022, false, false, false);
    EndEvent();
});


