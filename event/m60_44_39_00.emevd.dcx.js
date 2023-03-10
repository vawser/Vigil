// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    RegisterBonfire(1044390000, 1044391950, 0, 0, 0, 5);
    RegisterBonfire(1044390001, 1044391951, 0, 0, 0, 5);
    InitializeCommonEvent(0, 90005726, 4720, 4721, 4723, 1044399255, 1044390710, 1044396700);
    InitializeCommonEvent(0, 90005703, 1044390710, 4721, 4722, 1044399256, 4721, 4720, 4724, 0);
    InitializeCommonEvent(0, 90005704, 1044390710, 4721, 4720, 1044399256, 3);
    InitializeCommonEvent(0, 90005702, 1044390710, 4723, 4720, 4724);
    InitializeCommonEvent(0, 90005704, 1044390700, 4041, 4040, 1044399201, 3);
    InitializeCommonEvent(0, 90005703, 1044390700, 4041, 4042, 1044399201, 4041, 4040, 4043, -1);
    InitializeCommonEvent(0, 90005702, 1044390700, 4043, 4040, 4043);
    InitializeEvent(0, 1044390715, 1044390700, 1044390705, 1044391700);
    InitializeCommonEvent(0, 90005730, 1044399210, 1101004800, 1044399214, 4045, 1044399213, 1044399212);
    InitializeCommonEvent(0, 90005731, 1044399214, 1044390700, 1092616192, 1094713344);
    
    // Jarfield
    EnableAssetInvunerability(400005100);
    
    InitializeEvent(0, 1044390800, 0);
    InitializeEvent(0, 1044390801, 0);
    InitializeEvent(0, 1044390804, 0);
    InitializeEvent(0, 1044390810, 0);
});

$Event(50, Default, function() {
    SetCharacterBackreadState(1044390700, true);
    SetCharacterBackreadState(1044390705, true);
    SetCharacterBackreadState(1044390710, true);
    SetCharacterBackreadState(1044390711, true);
    InitializeCommonEvent(0, 90005261, 1044390200, 1044392200, 1065353216, 1065353216, 1700);
    InitializeCommonEvent(0, 90005261, 1044390201, 1044392200, 1065353216, 0, 1700);
    InitializeCommonEvent(0, 90005261, 1044390202, 1044392202, 1065353216, 1065353216, 1700);
    InitializeCommonEvent(0, 90005261, 1044390203, 1044392202, 1065353216, 1069547520, 1700);
    InitializeCommonEvent(0, 90005261, 1044390204, 1044392202, 1065353216, 0, 1700);
});

$Event(1044393710, Default, function(X0_4) {
    WaitFixedTimeFrames(1);
    SetEventFlagID(1044399250, OFF);
    if (PlayerIsInOwnWorld()) {
        if (EventFlag(4000) && EventFlag(1044392710)) {
            SetEventFlagID(1044392710, OFF);
        }
    }
L10:
    DisableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, true);
L0:
    GotoIf(L1, EventFlag(4000));
    GotoIf(L2, EventFlag(4001));
    GotoIf(L4, EventFlag(4003));
L1:
    EnableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, false);
    ForceAnimationPlayback(X0_4, 30003, false, false, false);
    Goto(L20);
L2:
    EnableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, false);
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    Goto(L20);
L4:
    ForceCharacterTreasure(X0_4);
    DisableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, true);
    DisableAsset(X0_4);
    Goto(L20);
L20:
    WaitFor(EventFlag(1044399250));
    RestartEvent();
});

$Event(1044390715, Restart, function(X0_4, X4_4, X8_4) {
    DisableNetworkSync();
    WaitFixedTimeFrames(1);
    EnableCharacter(X4_4);
    SetCharacterBackreadState(X4_4, false);
    ForceAnimationPlayback(X4_4, 90004, false, false, false);
    EnableAsset(X8_4);
    WaitFixedTimeFrames(1);
    if (PlayerIsInOwnWorld()) {
        if (EventFlag(4040)) {
            SetEventFlagID(1044399202, OFF);
        }
    }
L19:
    if (!EventFlag(4045)) {
        DisableCharacter(X0_4);
        SetCharacterBackreadState(X0_4, true);
        WaitFor(EventFlag(4045));
        RestartEvent();
    }
L5:
    GotoIf(L0, EventFlag(4040));
    GotoIf(L1, EventFlag(4041));
    GotoIf(L3, EventFlag(4043));
L0:
    EnableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, false);
    ForceAnimationPlayback(X0_4, 90103, false, false, false);
    Goto(L20);
L1:
    EnableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, false);
    SetCharacterTeamType(X0_4, TeamType.HostileNPC);
    Goto(L20);
L3:
    ForceCharacterTreasure(X0_4);
    DisableCharacter(X0_4);
    SetCharacterBackreadState(X0_4, true);
    Goto(L20);
L20:
    WaitFor(!EventFlag(4045));
    RestartEvent();
});

// Farm System
$Event(1044390800, Restart, function() {
    DisableNetworkSync();
    
    // Once farm has been visited, empty farm - This is for grace sit
    if(EventFlag(1049630001))
    {
        SetEventFlagID(1049630000, OFF);
        SetEventFlagID(1049630001, OFF);
        SetEventFlagID(1049630002, OFF);
    }
    
    // Enable empty plots by default
    EnableAsset(400005110);
    
    // Disable all plants by default
    DisableAsset(400005200);
    DisableAsset(400005201);
    DisableAsset(400005202);
    DisableAsset(400005203);
    DisableAsset(400005204);
    DisableAsset(400005205);
    DisableAsset(400005206);
    DisableAsset(400005207);
    DisableAsset(400005208);
    DisableAsset(400005209);
    DisableAsset(400005210);
    DisableAsset(400005211);
    DisableAsset(400005212);
    DisableAsset(400005213);
    DisableAsset(400005214);
    DisableAsset(400005215);
    DisableAsset(400005216);
    DisableAsset(400005217);
    DisableAsset(400005218);
    DisableAsset(400005219);
    DisableAsset(400005220);
    DisableAsset(400005221);
    DisableAsset(400005222);
    DisableAsset(400005223);
    DisableAsset(400005224);
    
    WaitFixedTimeFrames(1);
    
    // Farm Ready
    WaitFor(EventFlag(1049630000));
    
    WaitFixedTimeFrames(1);
    
    DisableAsset(400005110);
    
    // Make chosen type visible
    InitializeEvent( 0, 1044390803, 1049630100, 400005200);
    InitializeEvent( 1, 1044390803, 1049630101, 400005201);
    InitializeEvent( 2, 1044390803, 1049630102, 400005202);
    InitializeEvent( 3, 1044390803, 1049630103, 400005203);
    InitializeEvent( 4, 1044390803, 1049630104, 400005204);
    InitializeEvent( 5, 1044390803, 1049630105, 400005205);
    InitializeEvent( 6, 1044390803, 1049630106, 400005206);
    InitializeEvent( 7, 1044390803, 1049630107, 400005207);
    InitializeEvent( 8, 1044390803, 1049630108, 400005208);
    InitializeEvent( 9, 1044390803, 1049630109, 400005209);
    InitializeEvent(10, 1044390803, 1049630110, 400005210);
    InitializeEvent(11, 1044390803, 1049630111, 400005211);
    InitializeEvent(12, 1044390803, 1049630112, 400005212);
    InitializeEvent(13, 1044390803, 1049630113, 400005213);
    InitializeEvent(14, 1044390803, 1049630114, 400005214);
    InitializeEvent(15, 1044390803, 1049630115, 400005215);
    InitializeEvent(16, 1044390803, 1049630116, 400005216);
    InitializeEvent(17, 1044390803, 1049630117, 400005217);
    InitializeEvent(18, 1044390803, 1049630118, 400005218);
    InitializeEvent(19, 1044390803, 1049630119, 400005219);
    InitializeEvent(20, 1044390803, 1049630120, 400005220);
    InitializeEvent(21, 1044390803, 1049630121, 400005221);
    InitializeEvent(22, 1044390803, 1049630122, 400005222);
    InitializeEvent(23, 1044390803, 1049630123, 400005223);
    InitializeEvent(24, 1044390803, 1049630124, 400005224);
});

// Material Collection Control - Plant Type
$Event(1044390801, Restart, function() {
    DisableNetworkSync();
    
    // Once player is in farm area, enable selected type
    WaitFor(InArea(10000, 1044392203, 1));
    
    // Only enable if farm is ready
    WaitFor(EventFlag(1049630000));
    
    // Add Farm Visited flag (this resets farm on reload)
    SetEventFlagID(1049630001, ON);
    
    WaitFixedTimeFrames(1);
    
    // Allow collection of chosen type
    InitializeEvent( 0, 1044390802, 1049630100, 1049630150);
    InitializeEvent( 1, 1044390802, 1049630101, 1049630151);
    InitializeEvent( 2, 1044390802, 1049630102, 1049630152);
    InitializeEvent( 3, 1044390802, 1049630103, 1049630153);
    InitializeEvent( 4, 1044390802, 1049630104, 1049630154);
    InitializeEvent( 5, 1044390802, 1049630105, 1049630155);
    InitializeEvent( 6, 1044390802, 1049630106, 1049630156);
    InitializeEvent( 7, 1044390802, 1049630107, 1049630157);
    InitializeEvent( 8, 1044390802, 1049630108, 1049630158);
    InitializeEvent( 9, 1044390802, 1049630109, 1049630159);
    InitializeEvent(10, 1044390802, 1049630110, 1049630160);
    InitializeEvent(11, 1044390802, 1049630111, 1049630161);
    InitializeEvent(12, 1044390802, 1049630112, 1049630162);
    InitializeEvent(14, 1044390802, 1049630113, 1049630163);
    InitializeEvent(15, 1044390802, 1049630114, 1049630164);
    InitializeEvent(16, 1044390802, 1049630115, 1049630165);
    InitializeEvent(17, 1044390802, 1049630116, 1049630166);
    InitializeEvent(18, 1044390802, 1049630117, 1049630167);
    InitializeEvent(19, 1044390802, 1049630118, 1049630168);
    InitializeEvent(20, 1044390802, 1049630119, 1049630169);
    InitializeEvent(21, 1044390802, 1049630120, 1049630170);
    InitializeEvent(22, 1044390802, 1049630121, 1049630171);
    InitializeEvent(23, 1044390802, 1049630122, 1049630172);
    InitializeEvent(24, 1044390802, 1049630123, 1049630173);
    InitializeEvent(25, 1044390802, 1049630124, 1049630174);
    
    // Once player leaves farm area, restart
    WaitFor(!InArea(10000, 1044392203, 1));
    
    RestartEvent();
});

// Material Collection Control - Area
$Event(1044390804, Restart, function() {
    DisableNetworkSync();
    
    // By default, allow collection
    BatchSetEventFlags(1049630150, 1049630199, OFF);
    
    // Once player is in farm area, block collection
    WaitFor(InArea(10000, 1044392203, 1));
    
    // Block collection
    BatchSetEventFlags(1049630150, 1049630199, ON);
    
    // Once player leaves farm area, restart to allow collection again
    WaitFor(!InArea(10000, 1044392203, 1));
    
    RestartEvent();
});

// Plant Pick Toggle
$Event(1044390802, Restart, function(X0_4, X4_4) {
    if(EventFlag(X0_4))
    {
        SetEventFlagID(X4_4, OFF);
    }
});

// Plant Asset Toggle
$Event(1044390803, Restart, function(X0_4, X4_4) {
    // If Farm is ready, toggle the pick flag for this plant
    if(EventFlag(1049630000))
    {
        if(EventFlag(X0_4))
        {
            EnableAsset(X4_4);
        }
    }
});

// Farm Configuration
$Event(1044390810, Default, function() {
    // Disable all types by default
    BatchSetEventFlags(1049630100, 1049630124, OFF);
    
    // Farm Ready
    WaitFor(EventFlag(1049630000));
    
    // Small Crop
    if(EventFlag(1049630010))
    {
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
    }
    
    // Medium Crop
    if(EventFlag(1049630011))
    {
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
    }
    
    // Large Crop
    if(EventFlag(1049630012))
    {
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
        RandomlySetEventFlagInRange(1049630100, 1049630124, ON);
    }
});
