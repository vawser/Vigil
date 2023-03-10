// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    // Grace
    RegisterBonfire(1047420000, 1047421950, 0, 0, 0, 5); 
    
    InitializeEvent(0, 1047424000, 0); // Gauntlet: Demi-Human 
    InitializeEvent(0, 1047424001, 0); // Gauntlet: Godrick's Own
    InitializeEvent(0, 1047424002, 0); // Gauntlet: Revenge of the Gladiators
    InitializeEvent(0, 1047424003, 0); // Gauntlet: Misbegotten Crucible
    
    InitializeEvent(0, 1047424090, 0); // Gauntlet: Disable Enemies by Default
    
    InitializeEvent(0, 1047424093, 0); // Gauntlet: Bloodstain
    
    // Enforced Boundries
    InitializeCommonEvent(0, 90006200, 1047422560, 1047422580);
    InitializeCommonEvent(1, 90006200, 1047422561, 1047422580);
    InitializeCommonEvent(2, 90006200, 1047422562, 1047422580);
    InitializeCommonEvent(3, 90006200, 1047422563, 1047422580);
    InitializeCommonEvent(4, 90006200, 1047422564, 1047422580);
    InitializeCommonEvent(5, 90006200, 1047422565, 1047422580);
    InitializeCommonEvent(6, 90006200, 1047422566, 1047422580);
    InitializeCommonEvent(7, 90006200, 1047422567, 1047422580);
    InitializeCommonEvent(8, 90006200, 1047422568, 1047422580);
    InitializeCommonEvent(9, 90006200, 1047422569, 1047422580);
    InitializeCommonEvent(10, 90006200, 1047422570, 1047422580);
    InitializeCommonEvent(11, 90006200, 1047422571, 1047422580);
    InitializeCommonEvent(12, 90006200, 1047422572, 1047422580);
    InitializeCommonEvent(13, 90006200, 1047422573, 1047422580);
    InitializeCommonEvent(14, 90006200, 1047422574, 1047422580);
    InitializeCommonEvent(15, 90006200, 1047422575, 1047422580);
});

$Event(50, Default, function() {
    
});

// BGM Start
$Event(1047424080, Restart, function() {
    if(EventFlag(1047610351)) {
        SetBossBGM(472001, BossBGMState.Start);
    }
    if(EventFlag(1047610352)) {
        SetBossBGM(920900, BossBGMState.Start);
    }
    if(EventFlag(1047610353)) {
        SetBossBGM(213000, BossBGMState.Start);
    }
    if(EventFlag(1047610354)) {
        SetBossBGM(203000, BossBGMState.Start);
    }
    if(EventFlag(1047610355)) {
        SetBossBGM(921400, BossBGMState.Start);
    }
    if(EventFlag(1047610356)) {
        SetBossBGM(471000, BossBGMState.Start);
    }
    if(EventFlag(1047610357)) {
        SetBossBGM(356000, BossBGMState.Start);
    }
    if(EventFlag(1047610358)) {
        SetBossBGM(931000, BossBGMState.Start);
    }
    if(EventFlag(1047610359)) {
        SetBossBGM(473000, BossBGMState.Start);
    }
    if(EventFlag(1047610360)) {
        SetBossBGM(213001, BossBGMState.Start);
    }
    if(EventFlag(1047610361)) {
        SetBossBGM(467000, BossBGMState.Start);
    }
    if(EventFlag(1047610362)) {
        SetBossBGM(920300, BossBGMState.Start);
    }
    if(EventFlag(1047610363)) {
        SetBossBGM(920700, BossBGMState.Start);
    }
    if(EventFlag(1047610364)) {
        SetBossBGM(480000, BossBGMState.Start);
    }
    if(EventFlag(1047610365)) {
        SetBossBGM(476000, BossBGMState.Start);
    }
    if(EventFlag(1047610366)) {
        SetBossBGM(472000, BossBGMState.Start);
    }
    if(EventFlag(1047610367)) {
        SetBossBGM(921100, BossBGMState.Start);
    }
    if(EventFlag(1047610368)) {
        SetBossBGM(211000, BossBGMState.Start);
    }
    if(EventFlag(1047610369)) {
        SetBossBGM(452000, BossBGMState.Start);
    }
    if(EventFlag(1047610370)) {
        SetBossBGM(212000, BossBGMState.Start);
    }
    if(EventFlag(1047610371)) {
        SetBossBGM(920200, BossBGMState.Start);
    }
    if(EventFlag(1047610372)) {
        SetBossBGM(219000, BossBGMState.Start);
    }
});

// BGM Heatup
$Event(1047424081, Restart, function() {
    if(EventFlag(1047610351)) {
        SetBossBGM(472001, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610352)) {
        SetBossBGM(920900, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610353)) {
        SetBossBGM(213000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610354)) {
        SetBossBGM(203000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610355)) {
        SetBossBGM(921400, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610356)) {
        SetBossBGM(471000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610357)) {
        SetBossBGM(356000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610358)) {
        SetBossBGM(931000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610359)) {
        SetBossBGM(473000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610360)) {
        SetBossBGM(213001, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610361)) {
        SetBossBGM(467000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610362)) {
        SetBossBGM(920300, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610363)) {
        SetBossBGM(920700, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610364)) {
        SetBossBGM(480000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610365)) {
        SetBossBGM(476000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610366)) {
        SetBossBGM(472000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610367)) {
        SetBossBGM(921100, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610368)) {
        SetBossBGM(211000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610369)) {
        SetBossBGM(452000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610370)) {
        SetBossBGM(212000, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610371)) {
        SetBossBGM(920200, BossBGMState.HeatUp);
    }
    if(EventFlag(1047610372)) {
        SetBossBGM(219000, BossBGMState.HeatUp);
    }
});

// BGM Stop
$Event(1047424082, Restart, function() {
    if(EventFlag(1047610351)) {
        SetBossBGM(472001, BossBGMState.Stop1);
    }
    if(EventFlag(1047610352)) {
        SetBossBGM(920900, BossBGMState.Stop1);
    }
    if(EventFlag(1047610353)) {
        SetBossBGM(213000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610354)) {
        SetBossBGM(203000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610355)) {
        SetBossBGM(921400, BossBGMState.Stop1);
    }
    if(EventFlag(1047610356)) {
        SetBossBGM(471000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610357)) {
        SetBossBGM(356000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610358)) {
        SetBossBGM(931000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610359)) {
        SetBossBGM(473000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610360)) {
        SetBossBGM(213001, BossBGMState.Stop1);
    }
    if(EventFlag(1047610361)) {
        SetBossBGM(467000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610362)) {
        SetBossBGM(920300, BossBGMState.Stop1);
    }
    if(EventFlag(1047610363)) {
        SetBossBGM(920700, BossBGMState.Stop1);
    }
    if(EventFlag(1047610364)) {
        SetBossBGM(480000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610365)) {
        SetBossBGM(476000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610366)) {
        SetBossBGM(472000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610367)) {
        SetBossBGM(921100, BossBGMState.Stop1);
    }
    if(EventFlag(1047610368)) {
        SetBossBGM(211000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610369)) {
        SetBossBGM(452000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610370)) {
        SetBossBGM(212000, BossBGMState.Stop1);
    }
    if(EventFlag(1047610371)) {
        SetBossBGM(920200, BossBGMState.Stop1);
    }
    if(EventFlag(1047610372)) {
        SetBossBGM(219000, BossBGMState.Stop1);
    }
});

// Setup Gauntlet Enemies
$Event(1047424090, Restart, function() {
    const gauntlet_enemy_group_flag = 1047425100
    
    DisableCharacter(gauntlet_enemy_group_flag);
    DisableCharacterCollision(gauntlet_enemy_group_flag);
    DisableCharacterAI(gauntlet_enemy_group_flag);
    
    // Disable Entrance fogwall
    DisableAsset(1047421500);
    
    // Bard Sangeet
    EndIf(!PlayerIsInOwnWorld());
    
    ForceAnimationPlayback(1047420100, 20019, false, false, false);
    ForceAnimationPlayback(1047420101, 20017, false, false, false);
    SetCharacterTeamType(1047420100, TeamType.FriendlyNPC);
    SetCharacterTeamType(1047420101, TeamType.FriendlyNPC);
});

// Gauntlet - Warp Player Out
$Event(1047424092, Restart, function() {
    SetSpEffect(10000, 7101100);
    WaitFixedTimeSeconds(5.0);
    WarpPlayer(60, 47, 42, 0, 1047420980, 610020);
    SetAreaWelcomeMessageState(Disabled);
});

// Gauntlet - Move Bloodstain
$Event(1047424093, Restart, function() {
    MoveBloodstainAndDroppedItems(1047422591, 1047422592);
});

// Spawn Enemy in Random Location
$Event(1047424100, Restart, function(X0_4) {
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
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422500, -1, X0_4);
    }
    if(EventFlag(1047620001))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422501, -1, X0_4);
    }
    if(EventFlag(1047620002))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422502, -1, X0_4);
    }
    if(EventFlag(1047620003))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422503, -1, X0_4);
    }
    if(EventFlag(1047620004))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422504, -1, X0_4);
    }
    if(EventFlag(1047620005))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422505, -1, X0_4);
    }
    if(EventFlag(1047620006))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422506, -1, X0_4);
    }
    if(EventFlag(1047620007))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422507, -1, X0_4);
    }
    if(EventFlag(1047620008))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422508, -1, X0_4);
    }
    if(EventFlag(1047620009))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422509, -1, X0_4);
    }
    if(EventFlag(1047620010))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422510, -1, X0_4);
    }
    if(EventFlag(1047620011))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422511, -1, X0_4);
    }
    if(EventFlag(1047620012))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422512, -1, X0_4);
    }
    if(EventFlag(1047620013))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422513, -1, X0_4);
    }
    if(EventFlag(1047620014))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422514, -1, X0_4);
    }
    if(EventFlag(1047620015))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422515, -1, X0_4);
    }
    if(EventFlag(1047620016))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422516, -1, X0_4);
    }
    if(EventFlag(1047620017))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422517, -1, X0_4);
    }
    if(EventFlag(1047620018))
    {
        WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, 1047422518, -1, X0_4);
    }
    
    WaitFixedTimeSeconds(0.25);
    
    EnableCharacter(X0_4);
    EnableCharacterAI(X0_4);
    EnableCharacterCollision(X0_4);
});

// Spawn Enemy in Placed Location
$Event(1047424101, Restart, function(X0_4) {
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
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
    
    WaitFixedTimeSeconds(0.25);
    
    EnableCharacter(X0_4);
    EnableCharacterAI(X0_4);
    EnableCharacterCollision(X0_4);
});

//---------------------------------------------
// Gauntlet - Demi-Human Deluge
//---------------------------------------------
$Event(1047424000, Restart, function() {
    const start_region_id = 1047422590
    
    const base_enemy_flag = 1047420500
    const group_enemy_flag = 1047425500
    
    const gauntlet_type_flag = 1047610310
    
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    const diff_standard_time = 15;
    const diff_hard_time = 12;
    const diff_nightmare_time = 9;
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    EnableAsset(1047421500); // Entrance Fogwall
    InitializeEvent(0, 1047424080, 0); // BGM Start
    
    InitializeEvent(0, 1047424100, base_enemy_flag + 0); 
    InitializeEvent(1, 1047424100, base_enemy_flag + 19);
    InitializeEvent(2, 1047424100, base_enemy_flag + 10);
    
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
    
    InitializeEvent(3, 1047424100, base_enemy_flag + 2);
    InitializeEvent(4, 1047424100, base_enemy_flag + 11);
    
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
    
    InitializeEvent(5, 1047424100, base_enemy_flag + 8);
    InitializeEvent(6, 1047424100, base_enemy_flag + 3);
    InitializeEvent(7, 1047424100, base_enemy_flag + 20);
    
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
    
    InitializeEvent(8, 1047424100, base_enemy_flag + 1);
    InitializeEvent(9, 1047424100, base_enemy_flag + 4);
    InitializeEvent(10, 1047424100, base_enemy_flag + 5);
    
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
    
    InitializeEvent(11, 1047424100, base_enemy_flag + 6);
    InitializeEvent(12, 1047424100, base_enemy_flag + 21);
    InitializeEvent(13, 1047424100, base_enemy_flag + 22);
    
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
    
    InitializeEvent(14, 1047424100, base_enemy_flag + 12);
    InitializeEvent(15, 1047424100, base_enemy_flag + 13);
    InitializeEvent(16, 1047424100, base_enemy_flag + 7);
    
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
    
    InitializeEvent(17, 1047424100, base_enemy_flag + 30);
    InitializeEvent(18, 1047424100, base_enemy_flag + 9);
    
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
    
    InitializeEvent(19, 1047424100, base_enemy_flag + 31);
    InitializeEvent(20, 1047424100, base_enemy_flag + 32);
    InitializeEvent(21, 1047424100, base_enemy_flag + 40);
    
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
    
    InitializeEvent(22, 1047424100, base_enemy_flag + 14);
    InitializeEvent(23, 1047424100, base_enemy_flag + 15);
    InitializeEvent(24, 1047424100, base_enemy_flag + 16);
    
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
    
    InitializeEvent(25, 1047424100, base_enemy_flag + 39);
    InitializeEvent(26, 1047424100, base_enemy_flag + 17);
    InitializeEvent(27, 1047424100, base_enemy_flag + 41);
    
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
    
    InitializeEvent(28, 1047424100, base_enemy_flag + 33);
    InitializeEvent(29, 1047424100, base_enemy_flag + 18);
    InitializeEvent(30, 1047424100, base_enemy_flag + 23);
    
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
    
    InitializeEvent(31, 1047424100, base_enemy_flag + 24);
    InitializeEvent(32, 1047424100, base_enemy_flag + 25);
    InitializeEvent(33, 1047424100, base_enemy_flag + 26);
    
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
    
    InitializeEvent(34, 1047424100, base_enemy_flag + 34);
    InitializeEvent(35, 1047424100, base_enemy_flag + 27);
    InitializeEvent(36, 1047424100, base_enemy_flag + 35);
    
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
    
    InitializeEvent(37, 1047424100, base_enemy_flag + 36);
    InitializeEvent(38, 1047424100, base_enemy_flag + 37);
    InitializeEvent(39, 1047424100, base_enemy_flag + 38);
    
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
    
    InitializeEvent(40, 1047424100, base_enemy_flag + 28);
    InitializeEvent(41, 1047424100, base_enemy_flag + 29);
    InitializeEvent(42, 1047424100, base_enemy_flag + 42);
    
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
    
    InitializeEvent(43, 1047424100, base_enemy_flag + 43);
    InitializeEvent(44, 1047424100, base_enemy_flag + 44);
    InitializeEvent(44, 1047424100, base_enemy_flag + 45);
    
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
    
    InitializeEvent(45, 1047424100, base_enemy_flag + 46);
    InitializeEvent(46, 1047424100, base_enemy_flag + 47);
    InitializeEvent(47, 1047424100, base_enemy_flag + 48);
    
    // Fixed wait before boss
    WaitFixedTimeSeconds(15);
    
    // Boss
    InitializeEvent(0, 1047424081, 0); // BGM Heatup
    
    DisplayBossHealthBar(Enabled, base_enemy_flag + 99, 0, 908000000);
    InitializeEvent(48, 1047424100, base_enemy_flag + 99);
    WaitFor(CharacterDead(base_enemy_flag + 99, Equal, 1));
    DisplayBossHealthBar(Disabled, base_enemy_flag + 99, 0, 908000000);
    
    WaitFixedTimeSeconds(15.0);
    
    InitializeEvent(0, 1047424082, 0); // BGM Stop
    
    // Kill all remaining enemies
    ForceCharacterDeath(group_enemy_flag, true); 
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3200);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3210);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3220);
    }
    
    InitializeEvent(0, 1047424092, 0); // Gauntlet: Warp Player Out
});

//---------------------------------------------
// Gauntlet - Godrick's Own
//---------------------------------------------
$Event(1047424001, Restart, function() {
    const start_region_id = 1047422590
    
    const base_enemy_flag = 1047420600
    const group_enemy_flag = 1047425600
    
    const gauntlet_type_flag = 1047610311
    
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    const diff_standard_time = 15;
    const diff_hard_time = 12;
    const diff_nightmare_time = 9;
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    EnableAsset(1047421500); // Entrance Fogwall
    InitializeEvent(0, 1047424080, 0); // BGM Start
    
    // Enemy Flow
    InitializeEvent(0, 1047424100, base_enemy_flag); 
    InitializeEvent(1, 1047424100, base_enemy_flag + 1);
    InitializeEvent(2, 1047424100, base_enemy_flag + 2);
    
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
    
    InitializeEvent(3, 1047424100, base_enemy_flag + 3); 
    InitializeEvent(4, 1047424100, base_enemy_flag + 4);
    InitializeEvent(5, 1047424100, base_enemy_flag + 5);
    
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
    
    InitializeEvent(6, 1047424100, base_enemy_flag + 6);
    InitializeEvent(7, 1047424100, base_enemy_flag + 7);
    InitializeEvent(8, 1047424100, base_enemy_flag + 8);
    
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
    
    InitializeEvent(9, 1047424100, base_enemy_flag + 9);
    InitializeEvent(10, 1047424100, base_enemy_flag + 10);
    InitializeEvent(11, 1047424100, base_enemy_flag + 11);
    
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
    
    InitializeEvent(12, 1047424100, base_enemy_flag + 12);
    InitializeEvent(13, 1047424100, base_enemy_flag + 13);
    InitializeEvent(14, 1047424100, base_enemy_flag + 14);
    
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
    
    InitializeEvent(15, 1047424100, base_enemy_flag + 15);
    InitializeEvent(16, 1047424100, base_enemy_flag + 16);
    InitializeEvent(17, 1047424100, base_enemy_flag + 17);
    
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
    
    InitializeEvent(18, 1047424100, base_enemy_flag + 18);
    InitializeEvent(19, 1047424100, base_enemy_flag + 19);
    InitializeEvent(20, 1047424100, base_enemy_flag + 20);
    
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
    
    InitializeEvent(21, 1047424100, base_enemy_flag + 21);
    InitializeEvent(22, 1047424100, base_enemy_flag + 22);
    InitializeEvent(23, 1047424100, base_enemy_flag + 23);
    
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
    
    InitializeEvent(24, 1047424100, base_enemy_flag + 24);
    InitializeEvent(25, 1047424100, base_enemy_flag + 25);
    InitializeEvent(26, 1047424100, base_enemy_flag + 26);
    
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
    
    InitializeEvent(27, 1047424100, base_enemy_flag + 27);
    InitializeEvent(28, 1047424100, base_enemy_flag + 28);
    InitializeEvent(29, 1047424100, base_enemy_flag + 29);
    
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
    
    InitializeEvent(30, 1047424100, base_enemy_flag + 30);
    InitializeEvent(31, 1047424100, base_enemy_flag + 31);
    InitializeEvent(32, 1047424100, base_enemy_flag + 32);
    
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
    
    InitializeEvent(33, 1047424100, base_enemy_flag + 33);
    InitializeEvent(34, 1047424100, base_enemy_flag + 34);
    InitializeEvent(35, 1047424100, base_enemy_flag + 35);
    
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
    
    InitializeEvent(36, 1047424100, base_enemy_flag + 36);
    InitializeEvent(37, 1047424100, base_enemy_flag + 37);
    InitializeEvent(38, 1047424100, base_enemy_flag + 38);
    
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
    
    InitializeEvent(39, 1047424100, base_enemy_flag + 39);
    InitializeEvent(40, 1047424100, base_enemy_flag + 40);
    InitializeEvent(41, 1047424100, base_enemy_flag + 41);
    
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
    
    InitializeEvent(42, 1047424100, base_enemy_flag + 42);
    InitializeEvent(43, 1047424100, base_enemy_flag + 43);
    InitializeEvent(44, 1047424100, base_enemy_flag + 44);
    
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
    
    InitializeEvent(45, 1047424100, base_enemy_flag + 45);
    InitializeEvent(46, 1047424100, base_enemy_flag + 46);
    InitializeEvent(47, 1047424100, base_enemy_flag + 47);
    
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
    
    InitializeEvent(48, 1047424100, base_enemy_flag + 48);
    InitializeEvent(49, 1047424100, base_enemy_flag + 49);
    InitializeEvent(50, 1047424100, base_enemy_flag + 50);
    
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
    InitializeEvent(51, 1047424100, base_enemy_flag + 51);
    InitializeEvent(52, 1047424100, base_enemy_flag + 52);
    InitializeEvent(53, 1047424100, base_enemy_flag + 53);
    
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
    
    InitializeEvent(54, 1047424100, base_enemy_flag + 54);
    InitializeEvent(55, 1047424100, base_enemy_flag + 55);
    InitializeEvent(56, 1047424100, base_enemy_flag + 56);
    
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
    
    InitializeEvent(57, 1047424100, base_enemy_flag + 57);
    InitializeEvent(58, 1047424100, base_enemy_flag + 58);
    InitializeEvent(59, 1047424100, base_enemy_flag + 59);
    
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
    
    InitializeEvent(60, 1047424100, base_enemy_flag + 60);
    InitializeEvent(61, 1047424100, base_enemy_flag + 61);
    InitializeEvent(62, 1047424100, base_enemy_flag + 62);
    
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
    
    InitializeEvent(63, 1047424100, base_enemy_flag + 63);
    InitializeEvent(64, 1047424100, base_enemy_flag + 64);
    InitializeEvent(65, 1047424100, base_enemy_flag + 65);
    
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
    
    InitializeEvent(66, 1047424100, base_enemy_flag + 66);
    InitializeEvent(67, 1047424100, base_enemy_flag + 67);
    
    WaitFixedTimeSeconds(15);
    
    // Boss
    InitializeEvent(0, 1047424081, 0); // BGM Heatup
    
    DisplayBossHealthBar(Enabled, base_enemy_flag + 99, 0, 908000001);
    InitializeEvent(99, 1047424100, base_enemy_flag + 99);
    WaitFor(CharacterDead(base_enemy_flag + 99, Equal, 1));
    DisplayBossHealthBar(Disabled, base_enemy_flag + 99, 0, 908000001);
    
    WaitFixedTimeSeconds(15.0);
    
    InitializeEvent(0, 1047424082, 0); // BGM Stop
    
    // Kill all remaining enemies
    ForceCharacterDeath(group_enemy_flag, true); 
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3300);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3310);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3320);
    }
    
    InitializeEvent(0, 1047424092, 0); // Gauntlet: Warp Player Out
});

//---------------------------------------------
// Gauntlet - Revenge of the Gladiators
//---------------------------------------------
$Event(1047424002, Restart, function() {
    const start_region_id = 1047422590
    
    const base_enemy_flag = 1047420700
    const group_enemy_flag = 1047425700
    
    const gauntlet_type_flag = 1047610312
    
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    const diff_standard_time = 30;
    const diff_hard_time = 24;
    const diff_nightmare_time = 18;
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    EnableAsset(1047421500); // Entrance Fogwall
    InitializeEvent(0, 1047424080, 0); // BGM Start
    
    // Enemy Flow
    InitializeEvent(0, 1047424100, base_enemy_flag + 5);
    
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
    
    InitializeEvent(1, 1047424100, base_enemy_flag + 11);
    
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
    
    InitializeEvent(2, 1047424100, base_enemy_flag + 6);
    InitializeEvent(3, 1047424100, base_enemy_flag + 12);
    
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
    
    InitializeEvent(4, 1047424100, base_enemy_flag + 7);
    InitializeEvent(5, 1047424100, base_enemy_flag + 13);
    
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
    
    InitializeEvent(6, 1047424100, base_enemy_flag);
    
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
    
    InitializeEvent(7, 1047424100, base_enemy_flag + 1);
    
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
    
    InitializeEvent(8, 1047424100, base_enemy_flag + 8);
    InitializeEvent(9, 1047424100, base_enemy_flag + 14);
    
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
    
    InitializeEvent(10, 1047424100, base_enemy_flag + 9);
    InitializeEvent(11, 1047424100, base_enemy_flag + 15);
    
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
    
    InitializeEvent(12, 1047424100, base_enemy_flag + 2);
    
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
    
    InitializeEvent(13, 1047424100, base_enemy_flag + 10);
    InitializeEvent(14, 1047424100, base_enemy_flag + 16);
    
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
    
    InitializeEvent(15, 1047424100, base_enemy_flag + 17);
    InitializeEvent(16, 1047424100, base_enemy_flag + 19);
    
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
    
    InitializeEvent(17, 1047424100, base_enemy_flag + 18);
    InitializeEvent(18, 1047424100, base_enemy_flag + 20);
    
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
    
    InitializeEvent(19, 1047424100, base_enemy_flag + 21);
    
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
    
    InitializeEvent(20, 1047424100, base_enemy_flag + 3);
    
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
    
    InitializeEvent(21, 1047424100, base_enemy_flag + 4);
    
    WaitFixedTimeSeconds(15);
    
    // Boss
    InitializeEvent(0, 1047424081, 0); // BGM Heatup
    
    DisplayBossHealthBar(Enabled, base_enemy_flag + 24, 0, 908000002);
    InitializeEvent(99, 1047424100, base_enemy_flag + 24);
    WaitFor(CharacterDead(base_enemy_flag + 24, Equal, 1));
    DisplayBossHealthBar(Disabled, base_enemy_flag + 24, 0, 908000002);
    
    WaitFixedTimeSeconds(15.0);
    
    InitializeEvent(0, 1047424082, 0); // BGM Stop
    
    // Kill all remaining enemies
    ForceCharacterDeath(group_enemy_flag, true); 
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3400);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3410);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3420);
    }
    
    InitializeEvent(0, 1047424092, 0); // Gauntlet: Warp Player Out
});

//---------------------------------------------
// Gauntlet - Misbegotten Crucible
//---------------------------------------------
$Event(1047424003, Restart, function() {
    const start_region_id = 1047422590
    
    const base_enemy_flag = 1047420725
    const group_enemy_flag = 1047425710
    
    const gauntlet_type_flag = 1047610313
    
    const diff_standard_flag = 1047610390
    const diff_hard_flag = 1047610391
    const diff_nightmare_flag = 1047610392
    
    const diff_standard_time = 15;
    const diff_hard_time = 12;
    const diff_nightmare_time = 9;
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    EnableAsset(1047421500); // Entrance Fogwall
    InitializeEvent(0, 1047424080, 0); // BGM Start
    
    // Enemy Flow
    InitializeEvent(0, 1047424100, base_enemy_flag);
    InitializeEvent(1, 1047424100, base_enemy_flag + 1);
    InitializeEvent(2, 1047424100, base_enemy_flag + 10);
    
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
    
    InitializeEvent(3, 1047424100, base_enemy_flag + 2);
    InitializeEvent(4, 1047424100, base_enemy_flag + 3);
    InitializeEvent(5, 1047424100, base_enemy_flag + 11);
    
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
    
    InitializeEvent(6, 1047424100, base_enemy_flag + 4);
    InitializeEvent(7, 1047424100, base_enemy_flag + 5);
    InitializeEvent(8, 1047424100, base_enemy_flag + 12);
    
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
    
    InitializeEvent(9, 1047424100, base_enemy_flag + 20);
    InitializeEvent(10, 1047424100, base_enemy_flag + 21);
    InitializeEvent(11, 1047424100, base_enemy_flag + 28);
    
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
    
    InitializeEvent(12, 1047424100, base_enemy_flag + 21);
    InitializeEvent(13, 1047424100, base_enemy_flag + 22);
    
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
    
    InitializeEvent(14, 1047424100, base_enemy_flag + 23);
    InitializeEvent(15, 1047424100, base_enemy_flag + 24);
    InitializeEvent(16, 1047424100, base_enemy_flag + 27);
    
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
    
    InitializeEvent(17, 1047424100, base_enemy_flag + 6);
    InitializeEvent(18, 1047424100, base_enemy_flag + 7);
    InitializeEvent(19, 1047424100, base_enemy_flag + 13);
    
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
    
    InitializeEvent(20, 1047424100, base_enemy_flag + 8);
    InitializeEvent(21, 1047424100, base_enemy_flag + 9);
    InitializeEvent(22, 1047424100, base_enemy_flag + 14);
    
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
    
    InitializeEvent(23, 1047424100, base_enemy_flag + 15);
    InitializeEvent(24, 1047424100, base_enemy_flag + 16);
    InitializeEvent(25, 1047424100, base_enemy_flag + 26);
    
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
    
    InitializeEvent(26, 1047424100, base_enemy_flag + 17);
    InitializeEvent(27, 1047424100, base_enemy_flag + 18);
    InitializeEvent(28, 1047424100, base_enemy_flag + 29);
    
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
    
    InitializeEvent(29, 1047424100, base_enemy_flag + 19);
    InitializeEvent(30, 1047424100, base_enemy_flag + 25);
    
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
    
    InitializeEvent(31, 1047424100, base_enemy_flag + 30);
    
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
    
    InitializeEvent(32, 1047424100, base_enemy_flag + 31);
    
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
    
    InitializeEvent(33, 1047424100, base_enemy_flag + 32);
    
    WaitFixedTimeSeconds(15);
    
    // Boss
    InitializeEvent(0, 1047424081, 0); // BGM Heatup
    
    DisplayBossHealthBar(Enabled, base_enemy_flag + 50, 0, 908000003);
    InitializeEvent(99, 1047424100, base_enemy_flag + 50);
    WaitFor(CharacterDead(base_enemy_flag + 50, Equal, 1));
    DisplayBossHealthBar(Disabled, base_enemy_flag + 50, 0, 908000003);
    
    WaitFixedTimeSeconds(15.0);
    
    InitializeEvent(0, 1047424082, 0); // BGM Stop
    
    // Kill all remaining enemies
    ForceCharacterDeath(group_enemy_flag, true); 
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3500);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3510);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3520);
    }
    
    InitializeEvent(0, 1047424092, 0); // Gauntlet: Warp Player Out
});
