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
    RegisterBonfire(1042400000, 1042401950, 0, 0, 0, 5);
    
    InitializeEvent(0, 1042402650, 710670, 1670, 9123, 69230);
    InitializeCommonEvent(0, 90005706, 1042400700, 90101, 0);
    
    // Teleport: Great Colosseum
    InitializeEvent(0, 1042403800, 0);
    
    // Trial
    InitializeEvent(0, 1042404000, 0); // Trial: The Family
    InitializeEvent(0, 1042404001, 0); // Trial: Azur's Vengeance
    InitializeEvent(0, 1042404002, 0); // Trial: Magmatic Cabal
    
    InitializeEvent(0, 1042404090, 0); // Trial: Disable Enemies by Default
    InitializeEvent(0, 1042404093, 0); // Trial: Bloodstain
    
    // Enforced Boundries
    InitializeCommonEvent(0, 90006200, 1042402560, 1042402580);
    InitializeCommonEvent(1, 90006200, 1042402561, 1042402580);
    InitializeCommonEvent(2, 90006200, 1042402562, 1042402580);
    InitializeCommonEvent(3, 90006200, 1042402563, 1042402580);
    InitializeCommonEvent(4, 90006200, 1042402564, 1042402580);
    InitializeCommonEvent(5, 90006200, 1042402565, 1042402580);
    InitializeCommonEvent(6, 90006200, 1042402566, 1042402580);
    InitializeCommonEvent(7, 90006200, 1042402567, 1042402580);
    InitializeCommonEvent(8, 90006200, 1042402568, 1042402580);
    InitializeCommonEvent(9, 90006200, 1042402569, 1042402580);
    InitializeCommonEvent(10, 90006200, 1042402570, 1042402580);
    InitializeCommonEvent(11, 90006200, 1042402571, 1042402580);
    InitializeCommonEvent(12, 90006200, 1042402572, 1042402580);
    InitializeCommonEvent(13, 90006200, 1042402573, 1042402580);
    InitializeCommonEvent(14, 90006200, 1042402574, 1042402580);
    InitializeCommonEvent(15, 90006200, 1042402575, 1042402580);
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

// Teleport: Great Colosseum
$Event(1042403800, Restart, function() {
    WaitFor(EventFlag(1047610302));
    SetEventFlagID(1047610302, OFF);
    
    WarpPlayer(60, 47, 42, 0, 1047420980, 610020);
});

// BGM Start
$Event(1042404080, Restart, function() {
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
$Event(1042404081, Restart, function() {
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
$Event(1042404082, Restart, function() {
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

// Setup Trial Enemies
$Event(1042404090, Restart, function() {
    const group_flag = 1042405100
    
    DisableCharacter(group_flag);
    DisableCharacterCollision(group_flag);
    DisableCharacterAI(group_flag);
    
    // Disable Entrance fogwall
    DisableAsset(1042401960);
    
    EndIf(!PlayerIsInOwnWorld());
    
    // Bard Dhvani
    ForceAnimationPlayback(1042400100, 20019, false, false, false);
    ForceAnimationPlayback(1042400101, 20017, false, false, false);
    SetCharacterTeamType(1042400100, TeamType.FriendlyNPC);
    SetCharacterTeamType(1042400101, TeamType.FriendlyNPC);
});

// Trial - Warp Player Out
$Event(1042404092, Restart, function() {
    SetSpEffect(10000, 7101100);
    WaitFixedTimeSeconds(5.0);
    WarpPlayer(60, 42, 40, 0, 1042400980, 6100603);
    SetAreaWelcomeMessageState(Disabled);
});

// Trial - Move Bloodstain
$Event(1042404093, Restart, function() {
    MoveBloodstainAndDroppedItems(1042402591, 1042402592);
});

// Spawn Boss
$Event(1042404100, Restart, function(X0_4, X4_4) {
    const diff_standard_flag = 1047610380
    const diff_hard_flag = 1047610381
    const diff_nightmare_flag = 1047610382
    
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
    
    WarpCharacterAndCopyFloor(X0_4, TargetEntityType.Area, X4_4, -1, X0_4);
    
    WaitFixedTimeSeconds(0.25);
    
    EnableCharacter(X0_4);
    EnableCharacterAI(X0_4);
    EnableCharacterCollision(X0_4);
});

//---------------------------------------------
// Trial - The Family
//---------------------------------------------
$Event(1042404000, Restart, function() {
    const diff_standard_flag = 1047610380
    const diff_hard_flag = 1047610381
    const diff_nightmare_flag = 1047610382
    
    const gauntlet_type_flag = 1047610320
    
    const start_region_id = 1042402590
    const boss_spawn_id = 1042402520
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    ChangeWeather(Weather.Default, -1, true);
    
    // Player modifier
    if(EventFlag(diff_hard_flag))
    {
        SetSpEffect(10000, 7101111);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        SetSpEffect(10000, 7101110);
    }
    
    EnableAsset(1042401960); // Entrance Fogwall
    InitializeEvent(0, 1042404080, 0); // BGM Start
    
    const boss_father = 1042400750
    const boss_mother = 1042400751
    const boss_child = 1042400752
    
    // The Mother
    DisplayBossHealthBar(Enabled, boss_mother, 0, 190110);
    InitializeEvent(0, 1042404100, boss_mother, boss_spawn_id);
    
    WaitFor(CharacterDead(boss_mother, Equal, 1));
    
    // The Child
    DisplayBossHealthBar(Enabled, boss_child, 1, 190120);
    InitializeEvent(1, 1042404100, boss_child, boss_spawn_id);
    
    WaitFor(CharacterDead(boss_child, Equal, 1));
    
    // The Father
    InitializeEvent(0, 1042404081, 0); // BGM Heatup
    
    DisplayBossHealthBar(Enabled, boss_father, 2, 190100);
    InitializeEvent(2, 1042404100, boss_father, boss_spawn_id);

    WaitFor(CharacterDead(boss_father, Equal, 1));
    
    DisplayBossHealthBar(Disabled, boss_mother, 0, 190110);
    DisplayBossHealthBar(Disabled, boss_child, 1, 190120);
    DisplayBossHealthBar(Disabled, boss_father, 2, 190100);
    
    InitializeEvent(0, 1042404082, 0); // BGM Stop
    
    // Unique Reward
    AwardItemLot(30700)
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3600);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3610);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3620);
    }
    
    InitializeEvent(0, 1042404092, 0); // Warp Player Out
});

//---------------------------------------------
// Trial - Azur's Vengeance
//---------------------------------------------
$Event(1042404001, Restart, function() {
    const diff_standard_flag = 1047610380
    const diff_hard_flag = 1047610381
    const diff_nightmare_flag = 1047610382
    
    const gauntlet_type_flag = 1047610321
    
    const start_region_id = 1042402590
    const boss_spawn_id = 1042402521
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    ChangeWeather(Weather.Default, -1, true);
    
    // Player modifier
    if(EventFlag(diff_hard_flag))
    {
        SetSpEffect(10000, 7101111);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        SetSpEffect(10000, 7101110);
    }
    
    EnableAsset(1042401960); // Entrance Fogwall
    InitializeEvent(0, 1042404080, 0); // BGM Start
    
    const boss_azur = 1042400755
    const boss_disciple_1 = 1042400756
    const boss_disciple_2 = 1042400757
    
    // Azur
    DisplayBossHealthBar(Enabled, boss_azur, 0, 190130);
    InitializeEvent(0, 1042404100, boss_azur, boss_spawn_id);
    
    WaitFixedTimeSeconds(10.0);
    
    // Disciple 1
    InitializeEvent(1, 1042404100, boss_disciple_1, 1042402502);
    
    WaitFixedTimeSeconds(20.0);
    
    // Disciple 2
    InitializeEvent(2, 1042404100, boss_disciple_2, 1042402512);
    
    WaitFixedTimeSeconds(20.0);

    WaitFor(CharacterDead(boss_azur, Equal, 1));
    WaitFor(CharacterDead(boss_disciple_1, Equal, 1));
    WaitFor(CharacterDead(boss_disciple_2, Equal, 1));
    
    DisplayBossHealthBar(Disabled, boss_azur, 0, 190130);
    
    InitializeEvent(0, 1042404082, 0); // BGM Stop
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3600);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3610);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3620);
    }
    
    InitializeEvent(0, 1042404092, 0); // Warp Player Out
});

//---------------------------------------------
// Trial - Magmatic Cabal
//---------------------------------------------
$Event(1042404002, Restart, function() {
    const diff_standard_flag = 1047610380
    const diff_hard_flag = 1047610381
    const diff_nightmare_flag = 1047610382
    
    const gauntlet_type_flag = 1047610322
    
    const start_region_id = 1042402590
    const boss_spawn_id = 1042402521
    
    // Wait for player to be in arena
    WaitFor(InArea(10000, start_region_id, 1));
    
    // Type check
    WaitFor(EventFlag(gauntlet_type_flag));
    
    ChangeWeather(Weather.Default, -1, true);
    
    // Player modifier
    if(EventFlag(diff_hard_flag))
    {
        SetSpEffect(10000, 7101111);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        SetSpEffect(10000, 7101110);
    }
    
    EnableAsset(1042401960); // Entrance Fogwall
    InitializeEvent(0, 1042404080, 0); // BGM Start
    
    const boss_lord_of_magma = 1042400760
    const boss_magmatic_knight_1 = 1042400761
    const boss_magmatic_knight_2 = 1042400762
    
    // Magmatic Knight #1
    DisplayBossHealthBar(Enabled, boss_magmatic_knight_1, 0, 190140);
    InitializeEvent(0, 1042404100, boss_magmatic_knight_1, 1042402521);
    
    WaitFor(CharacterDead(boss_magmatic_knight_1, Equal, 1));
    DisplayBossHealthBar(Disabled, boss_magmatic_knight_1, 0, 190140);
    
    // Lord of Magma
    DisplayBossHealthBar(Enabled, boss_lord_of_magma, 0, 190150);
    InitializeEvent(0, 1042404100, boss_lord_of_magma, boss_spawn_id);
    
    // Magmatic Knight #2
    DisplayBossHealthBar(Enabled, boss_magmatic_knight_2, 1, 190140);
    InitializeEvent(2, 1042404100, boss_magmatic_knight_2, 1042402512);

    WaitFor(CharacterDead(boss_lord_of_magma, Equal, 1));
    WaitFor(CharacterDead(boss_magmatic_knight_2, Equal, 1));
    
    DisplayBossHealthBar(Disabled, boss_lord_of_magma, 0, 190150);
    DisplayBossHealthBar(Disabled, boss_magmatic_knight_2, 1, 190140);
    
    InitializeEvent(0, 1042404082, 0); // BGM Stop
    
    // Reward
    if(EventFlag(diff_standard_flag))
    {
        AwardItemLot(3600);
    }
    if(EventFlag(diff_hard_flag))
    {
        AwardItemLot(3610);
    }
    if(EventFlag(diff_nightmare_flag))
    {
        AwardItemLot(3620);
    }
    
    InitializeEvent(0, 1042404092, 0); // Warp Player Out
});
