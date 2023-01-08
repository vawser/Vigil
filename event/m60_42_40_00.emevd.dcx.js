// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    RegisterBonfire(1042400000, 1042401950, 0, 0, 0, 5);
    InitializeEvent(0, 1042402650, 710670, 1670, 9123, 69230);
    InitializeCommonEvent(0, 90005706, 1042400700, 90101, 0);
    
    InitializeEvent(0, 1042404000, 0); // Gauntlet: Demi-Human 
    InitializeEvent(0, 1042404003, 0); 
    
    InitializeEvent(0, 1042404090, 0); // Gauntlet: Warp Player In
    InitializeEvent(0, 1042404091, 0); // Gauntlet: Disable Enemies by Default
});

$Event(50, Default, function() {
    SetCharacterBackreadState(1042400700, true);
});

$Event(1042402650, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    DisableNetworkSync();
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(X0_4));
    WaitFor(
        PlayerIsInOwnWorld()
            && EventFlag(X0_4)
            && !(HasMultiplayerState(MultiplayerState.Multiplayer)
                || HasMultiplayerState(MultiplayerState.MultiplayerPending))
            && !CharacterHasSpEffect(10000, 9640));
    ShowTutorialPopup(X4_4, true, true);
    EndIf(EventFlag(X12_4));
    DirectlyGivePlayerItem(ItemType.Goods, X8_4, X0_4, 1);
    SetEventFlagID(X12_4, ON);
});

$Event(1042403700, Restart, function(X0_4) {
    SetCharacterBackreadState(X0_4, false);
    EnableCharacter(X0_4);
    ForceAnimationPlayback(X0_4, 30025, false, false, false);
});

// Arena - Demi-Human
$Event(1042404000, Restart, function() {
    const base_enemy_flag = 1042400500
    
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    const diff_standard_time = 15;
    const diff_hard_time = 12;
    const diff_nightmare_time = 9;
    
    // Type check
    WaitFor(EventFlag(1047610310));
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, 1042402590, 1));
    
    InitializeEvent(0, 1042404100, base_enemy_flag + 0); 
    InitializeEvent(1, 1042404100, base_enemy_flag + 19);
    InitializeEvent(2, 1042404100, base_enemy_flag + 10);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(3, 1042404100, base_enemy_flag + 2);
    InitializeEvent(4, 1042404100, base_enemy_flag + 11);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(5, 1042404100, base_enemy_flag + 8);
    InitializeEvent(6, 1042404100, base_enemy_flag + 3);
    InitializeEvent(7, 1042404100, base_enemy_flag + 20);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(8, 1042404100, base_enemy_flag + 1);
    InitializeEvent(9, 1042404100, base_enemy_flag + 4);
    InitializeEvent(10, 1042404100, base_enemy_flag + 5);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(11, 1042404100, base_enemy_flag + 6);
    InitializeEvent(12, 1042404100, base_enemy_flag + 21);
    InitializeEvent(13, 1042404100, base_enemy_flag + 22);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(14, 1042404100, base_enemy_flag + 12);
    InitializeEvent(15, 1042404100, base_enemy_flag + 13);
    InitializeEvent(16, 1042404100, base_enemy_flag + 7);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(17, 1042404100, base_enemy_flag + 30);
    InitializeEvent(18, 1042404100, base_enemy_flag + 9);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(19, 1042404100, base_enemy_flag + 31);
    InitializeEvent(20, 1042404100, base_enemy_flag + 32);
    InitializeEvent(21, 1042404100, base_enemy_flag + 40);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(22, 1042404100, base_enemy_flag + 14);
    InitializeEvent(23, 1042404100, base_enemy_flag + 15);
    InitializeEvent(24, 1042404100, base_enemy_flag + 16);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(25, 1042404100, base_enemy_flag + 39);
    InitializeEvent(26, 1042404100, base_enemy_flag + 17);
    InitializeEvent(27, 1042404100, base_enemy_flag + 41);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(28, 1042404100, base_enemy_flag + 33);
    InitializeEvent(29, 1042404100, base_enemy_flag + 18);
    InitializeEvent(30, 1042404100, base_enemy_flag + 23);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(31, 1042404100, base_enemy_flag + 24);
    InitializeEvent(32, 1042404100, base_enemy_flag + 25);
    InitializeEvent(33, 1042404100, base_enemy_flag + 26);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(34, 1042404100, base_enemy_flag + 34);
    InitializeEvent(35, 1042404100, base_enemy_flag + 27);
    InitializeEvent(36, 1042404100, base_enemy_flag + 35);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(37, 1042404100, base_enemy_flag + 36);
    InitializeEvent(38, 1042404100, base_enemy_flag + 37);
    InitializeEvent(39, 1042404100, base_enemy_flag + 38);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(40, 1042404100, base_enemy_flag + 28);
    InitializeEvent(41, 1042404100, base_enemy_flag + 29);
    InitializeEvent(42, 1042404100, base_enemy_flag + 42);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(43, 1042404100, base_enemy_flag + 43);
    InitializeEvent(44, 1042404100, base_enemy_flag + 44);
    InitializeEvent(44, 1042404100, base_enemy_flag + 45);
    
    if(EventFlag(diff_standard_flag))
    {
        WaitFixedTimeSeconds(diff_standard_time);
    }
    if(EventFlag(diff_hard_flag))
    {
        WaitFixedTimeSeconds(diff_hard_time);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        WaitFixedTimeSeconds(diff_nightmare_time);
    }
    
    InitializeEvent(45, 1042404100, base_enemy_flag + 46);
    InitializeEvent(46, 1042404100, base_enemy_flag + 47);
    InitializeEvent(47, 1042404100, base_enemy_flag + 48);
    
    // Fixed wait before boss
    WaitFixedTimeSeconds(15);
    
    // Boss
    DisplayBossHealthBar(Enabled, base_enemy_flag + 99, 0, 908000000);
    InitializeEvent(48, 1042404100, base_enemy_flag + 99);
    WaitFor(CharacterDead(base_enemy_flag + 99, Equal, 1));
    DisplayBossHealthBar(Disabled, base_enemy_flag + 99, 0, 908000000);
    
    // Victory Phase
    InitializeEvent(0, 1042404092, 0);
});

// Arena - Warp Player in and Start
$Event(1042404090, Restart, function() {
    WaitFor(EventFlag(1047610300));
    SetEventFlagID(1047610300, OFF);
    WarpPlayer(60, 42, 40, 0, 1042400981, 610020);
});

// Disable Arena Enemies
$Event(1042404091, Restart, function() {
    DisableCharacter(1042405500);
    DisableCharacterCollision(1042405500);
    DisableCharacterAI(1042405500);
});

// Victory Phase
$Event(1042404092, Restart, function() {
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    WaitFixedTimeSeconds(15.0);
    
    // Kill all remaining enemies
    ForceCharacterDeath(1042405500, true); 
    
    SetSpEffect(10000, 7101100);
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3200);
        AwardItemLot(3300);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3210);
        AwardItemLot(3310);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3220);
        AwardItemLot(3320);
    }
    
    // Return to grace
    WaitFixedTimeSeconds(5.0);
    
    WarpPlayer(60, 42, 40, 0, 1042400980, 610020);
});

// Spawn Enemy in Random Location
$Event(1042404100, Restart, function(X0_4) {
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    BatchSetEventFlags(1047620000, 1047620019, OFF);
    RandomlySetEventFlagInRange(1047620000, 1047620018, ON);
    
    // Apply modifiers
    if(EventFlag(diff_standard_flag))
    {
        SetSpEffect(X0_4, 7101010);
    }
    if(EventFlag(diff_hard_flag))
    {
        SetSpEffect(X0_4, 7101020);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        SetSpEffect(X0_4, 7101030);
    }
    
    // Spawn Locations (update if more are added)
    if(EventFlag(1047620000))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402500, -1, X0_4);
    }
    if(EventFlag(1047620001))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402501, -1, X0_4);
    }
    if(EventFlag(1047620002))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402502, -1, X0_4);
    }
    if(EventFlag(1047620003))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402503, -1, X0_4);
    }
    if(EventFlag(1047620004))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402504, -1, X0_4);
    }
    if(EventFlag(1047620005))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402505, -1, X0_4);
    }
    if(EventFlag(1047620006))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402506, -1, X0_4);
    }
    if(EventFlag(1047620007))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402507, -1, X0_4);
    }
    if(EventFlag(1047620008))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402508, -1, X0_4);
    }
    if(EventFlag(1047620009))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402509, -1, X0_4);
    }
    if(EventFlag(1047620010))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402510, -1, X0_4);
    }
    if(EventFlag(1047620011))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402511, -1, X0_4);
    }
    if(EventFlag(1047620012))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402512, -1, X0_4);
    }
    if(EventFlag(1047620013))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402513, -1, X0_4);
    }
    if(EventFlag(1047620014))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402514, -1, X0_4);
    }
    if(EventFlag(1047620015))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402515, -1, X0_4);
    }
    if(EventFlag(1047620016))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402516, -1, X0_4);
    }
    if(EventFlag(1047620017))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402517, -1, X0_4);
    }
    if(EventFlag(1047620018))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1042402518, -1, X0_4);
    }
    
    // FX here
    
    WaitFixedTimeSeconds(1.0);
    
    EnableCharacter(X0_4);
    EnableCharacterAI(X0_4);
    EnableCharacterCollision(X0_4);
});
