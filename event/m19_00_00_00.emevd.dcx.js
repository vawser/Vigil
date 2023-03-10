// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd        
// @linked    [0]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    // Grace: Fractured Marika
    InitializeCommonEvent(0, 9005810, 19000850, 19000000, 19000950, 19001950, 5);
    
    // Grace: Elden Hollow
    InitializeCommonEvent(1, 9005810, 19000800, 19000001, 19000951, 19001951, 5);
    
    // Endings
    InitializeEvent(0, 19000100, 0); // Ending: Fracture/Despair/Duskborn/Order
    InitializeEvent(0, 19000110, 0); // Ending: Age of Stars
    InitializeEvent(0, 19000120, 0); // Ending: Lord of the Frenzied Flame
    
    InitializeEvent(0, 19002500, 0); // Erdtree Door -> Stone Platform
    InitializeEvent(0, 19002501, 0); // Erdtree Door -> Stone Platform (Post Radagon)
    InitializeEvent(0, 19002502, 0); // ?
    InitializeEvent(0, 19002682, 0); // Bloodstain Mover
    InitializeEvent(0, 19002900, 0); // Action: Warp to Stone Platform
    
    InitializeEvent(0, 19002901, 0); // Warp to Elden Beast
    InitializeEvent(0, 19002902, 0); // Elden Hollow -> Stone Platform Teleport
    
    // Elden Beast
    InitializeEvent(0, 19002800, 0); // Elden Beast - Setup
    InitializeEvent(0, 19002830, 0); // Elden Beast - Camera Shift
    InitializeEvent(0, 19002849, 0); // Elden Beast - Common Setup
    
    // Radagon
    InitializeEvent(0, 19002850, 0); // Radagon - Setup
    InitializeEvent(0, 19002859, 0); // Radagon - Common Setup
});

$Event(50, Default, function() {
    InitializeEvent(0, 19000050, 0);
});

// Ending: Fracture/Despair/Duskborn/Order
$Event(19000100, Default, function() {
    if (!PlayerIsInOwnWorld()) {
        DisableAsset(19001100); // Fractured Marika Statue
        DisableAsset(19001101); // Fractured Marika Remains
        EndEvent();
    }
L0:
    EndIf(EventFlag(120));
    
    // Is Age of Stars OR Lord of the Frenzied Flame
    if (!(EventFlag(9400) || EventFlag(9401) || EventFlag(9402) || EventFlag(9403))) 
    {
        
        DisableAsset(19001100); // Fractured Marika Statue
        DisableAsset(19001101); // Fractured Marika Remains
        
        WaitFor(EventFlag(19001100));
        EnableAsset(19001100); // Fractured Marika Statue
        EnableAsset(19001101); // Fractured Marika Remains
        
        // Radagon
        DisableCharacter(19000850);
        DisableCharacterCollision(19000850);
        
        DisableAsset(19001810); // Radagon Statue
        
        // Toggle Cutscene models based on Gender
        WaitFor(
            (!EventFlag(108) || (EventFlag(108) && EventFlag(116)))
                && (EventFlag(9400) || EventFlag(9401) || EventFlag(9402) || EventFlag(9403)));
        if (!((PlayerGender(Gender.Female) && !CharacterHasSpEffect(10000, 361000))
            || (PlayerGender(Gender.Male) && CharacterHasSpEffect(10000, 361000)))) 
        {
            // Male
            SetEventFlagID(780020, OFF);
            SetEventFlagID(780021, ON);
        } 
        else 
        {
            // Female
            SetEventFlagID(780020, ON);
            SetEventFlagID(780021, OFF);
        }
    }
L15:
    // System flag
    SetEventFlagID(19000100, ON);
    SetEventFlagID(19002100, ON);
    
    GotoIf(L13, EventFlag(9403));
    GotoIf(L12, EventFlag(9402));
    GotoIf(L11, EventFlag(9401));
    
    // Ending A-1 (Age of Fracture)
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(19000010, CutscenePlayMode.SkippableWithWhiteFadeOut2, 11712500, 11710000, 10000, 19000, false, false);
    TriggerMultiplayerEvent(10);
    WaitFixedTimeRealFrames(1);
    
    Goto(L15);
    
// Ending A-4 (Age of Order)
L11:
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(19000060, CutscenePlayMode.SkippableWithWhiteFadeOut2, 11712500, 11710000, 10000, 19000, false, false);
    TriggerMultiplayerEvent(20);
    WaitFixedTimeRealFrames(1);
    Goto(L15);
    
// Ending A-3 (Age of Duskborn)
L12:
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(19000070, CutscenePlayMode.SkippableWithWhiteFadeOut2, 11712500, 11710000, 10000, 19000, false, false);
    TriggerMultiplayerEvent(30);
    WaitFixedTimeRealFrames(1);
    Goto(L15);
    
// Ending A-2 (Blessing of Despair)
L13:
    PlayCutsceneToPlayerAndWarpWithStablePositionUpdate(19000080, CutscenePlayMode.SkippableWithWhiteFadeOut2, 11712500, 11710000, 10000, 19000, false, false);
    TriggerMultiplayerEvent(40);
    WaitFixedTimeRealFrames(1);
    Goto(L15);
L15:
    NoOp();
});

// Ending: Age of Stars
$Event(19000110, Default, function() {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(120));
    
    if (!(EventFlag(9404) || EventFlag(9405))) 
    {
        WaitFor(
            EventFlag(19001100)
                && EventFlag(1034509406)
                && (!EventFlag(108) || (EventFlag(108) && EventFlag(116))));
        CreateAssetfollowingSFX(19001110, 100, 30070);
        WaitFor(ActionButtonInArea(9610, 19001110) && PlayerIsInOwnWorld());
    }
L15:
    if (!EventFlag(1034509407)) {
        PlayCutsceneToPlayer(19000020, CutscenePlayMode.Skippable, 10000); // Ending B-1 (Age of Stars)
        SetEventFlagID(9404, ON);
        TriggerMultiplayerEvent(50);
    } else {
        PlayCutsceneToPlayer(19000021, CutscenePlayMode.Skippable, 10000); // Ending B-2 (Age of Stars)
        SetEventFlagID(9405, ON);
        TriggerMultiplayerEvent(60);
    }
    WaitFixedTimeRealFrames(1);
    SetEventFlagID(120, ON);
    SetEventFlagID(6010, ON);
    AwardAchievement(2);
    SetPlayerRespawnPoint(11102020);
    SaveRequest();
    SetEventFlagID(21, ON);
});

// Ending: Lord of the Frenzied Flame
$Event(19000120, Default, function() {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(120));
    
    if (!(EventFlag(9406) || EventFlag(9407))) {
        WaitFor(EventFlag(19001100));
        WaitFixedTimeFrames(1);
        WaitFor(EventFlag(108) && !EventFlag(116) && ActionButtonInArea(9620, 19001120));
        ForceAnimationPlayback(10000, 67070, false, false, false);
        WaitFixedTimeSeconds(10);
    }
L15:
    if (!EventFlag(109)) 
    {
        PlayCutsceneToPlayer(19000030, CutscenePlayMode.Skippable, 10000); // Ending C-1 (Lord of the Frenzied Flame)
        SetEventFlagID(9406, ON);
        TriggerMultiplayerEvent(70);
    } 
    else 
    {
        PlayCutsceneToPlayer(19000031, CutscenePlayMode.Skippable, 10000); // Ending C-2 (Lord of the Frenzied Flame)
        SetEventFlagID(9407, ON);
        TriggerMultiplayerEvent(80);
    }
    
    WaitFixedTimeRealFrames(1);
    SetEventFlagID(120, ON);
    SetEventFlagID(6010, ON);
    AwardAchievement(3);
    SetPlayerRespawnPoint(11102020);
    SaveRequest();
    SetEventFlagID(22, ON);
});

$Event(19000050, Default, function() {
    EndIf(ThisEventSlot());
});

// Erdtree Door -> Stone Platform
$Event(19002500, Default, function() 
{
    // Radagon defeated
    if (EventFlag(19000850)) {
        CreateAssetfollowingSFX(19001500, 101, 1530); // Visual on Erdtree Door
        EndEvent();
    }
L0:
    if (!PlayerIsInOwnWorld()) {
        // Radagon Fog-gate used
        if (EventFlag(19002851)) 
        {
            // Warp to Stone Platform
            WarpCharacterAndCopyFloorWithFadeout(20000, TargetEntityType.Area, 19002811, -1, 20000, false, true);
            EndEvent();
        }
    }
L1:
    CreateAssetfollowingSFX(19001500, 101, 1530); // Visual on Erdtree Door
    GotoIf(S0, PlayerIsInOwnWorld());
    GotoIf(L2, EventFlag(19002500));
S0:
    // Wait for player to use Erdtree Door
    WaitFor(PlayerIsInOwnWorld() && !EventFlag(19000850) && ActionButtonInArea(9501, 19001500));
    
    if (PlayerIsInOwnWorld()) {
        SendInvadingPhantomsHome(0);
    }
    
    EndIf(
        CharacterInvadeType(20000, 2)
            || CharacterInvadeType(20000, 3)
            || CharacterInvadeType(20000, 4)
            || CharacterInvadeType(20000, 5)
            || CharacterInvadeType(20000, 7));
            
    ForceAnimationPlayback(10000, 67080, false, false, false);
    
    GotoIf(S1, PlayerIsInOwnWorld());
    GotoIf(L2, EventFlag(19002500));
S1:
    WaitFixedTimeSeconds(2.4);
    CreateAssetfollowingSFX(19001501, 101, 1531);
    GotoIf(S2, PlayerIsInOwnWorld());
    GotoIf(L2, EventFlag(19002500));
S2:
    WaitFixedTimeSeconds(3.6);
    SetNetworkconnectedEventFlagID(19002500, ON);
L2:
    SetEventFlagID(9021, ON);
    
    // Teleport into Stone Platform
    if (PlayerIsInOwnWorld()) {
        PlayCutsceneToPlayerAndWarp(19000040, CutscenePlayMode.SkippableWithWhiteFadeOut, 19002810, 19000000, 10000, 19000, false);
    } else {
        PlayCutsceneToPlayerAndWarp(19000040, CutscenePlayMode.SkippableWithWhiteFadeOut, 19002811, 19000000, 10000, 19000, false);
    }
    
    WaitFixedTimeRealFrames(1);
    if (!EventFlag(119)) {
        SetEventFlagID(119, ON);
    }
    DeleteAssetfollowingSFX(19001501, false);
    if (PlayerIsInOwnWorld()) {
        SetCameraAngle(13.06, -63.07);
    }
});

// Erdtree Door -> Stone Platform (Post-Radagon)
$Event(19002501, Default, function() 
{
    // End if Radagon is still alive (other script handles that)
    EndIf(!EventFlag(19000850));

    // Wait for Door use
    WaitFor(PlayerIsInOwnWorld() && ActionButtonInArea(9501, 19001500));
    
    WarpPlayer(19, 0, 0, 0, 19000980, -1);
});

$Event(19002502, Restart, function() {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(EventFlag(71900));
    EndIf(EventFlag(121));
    WaitFor(PlayerInMap(19, 0, 0, 0) && EventFlag(9123) && !EventFlag(71900) && !EventFlag(121));
    SetSpEffect(10000, 4280);
    SetSpEffect(10000, 4282);
    WaitFor(EventFlag(71900));
    SetSpEffect(10000, 4281);
    SetSpEffect(10000, 4283);
});

$Event(19002682, Restart, function() {
    EndIf(!PlayerIsInOwnWorld());
    EndIf(!EventFlag(121));
    MoveBloodstainAndDroppedItems(19002682, 19002683);
});

// Elden Beast - Setup
$Event(19002800, Restart, function() {
    // Elden Beast - Defeated
    if (EventFlag(19000800)) 
    {
        // Elden Beast
        DisableCharacter(19000800); 
        DisableCharacterCollision(19000800); 
        ForceCharacterDeath(19000800, false); 
        EndEvent();
    }
    
    // Elden Beast
    DisableCharacterAI(19000800);
    DisableCharacterCollision(19000800); 
    
    // Wait for player to go near Elden Beast
    WaitFor(PlayerIsInOwnWorld() && EntityInRadiusOfEntity(10000, 19000800, 100, 1));
    
    SetNetworkconnectedEventFlagID(19000801, ON);
    SetNetworkconnectedEventFlagID(19002801, ON);
    SetNetworkconnectedEventFlagID(19002806, ON);
    
    SetEventFlagID(9021, ON);
    
    if (PlayerIsInOwnWorld()) {
        SetCameraAngle(-11.33, -25.83);
    }
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(19002803, ON);
    }
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedThisEventSlot(ON);
    }
    
    // Spirit Summons
    EnableCharacterDefaultBackread(35000);
    SetNetworkUpdateRate(35000, true, CharacterUpdateFrequency.AtLeastEvery5Frames);
    WarpCharacterAndCopyFloor(35000, TargetEntityType.Area, 19002813, -1, 19000800);
    WarpCharacterAndCopyFloor(19000130, TargetEntityType.Area, 19002813, -1, 19000800);
    SetCharacterTalkRange(19000130, 200);
    
    // Elden Beast - Start Fight
    EnableCharacter(19000800);
    EnableCharacterCollision(19000800);
    EnableCharacterAI(19000800);
    
    ForceAnimationPlayback(19000800, 20000, false, false, false);
    
    DisplayBossHealthBar(Enabled, 19000800, 0, 902200000);
    ChangeCamera(2200, 2200);
    
    WaitFixedTimeRealFrames(1);
    
    // Spirit Summon Stone
    AttachAssetToCharacter(19000130, 10, 19001130);
    
    // Elden Beast - HP below 0
    WaitFor(CharacterHPValue(19000800) <= 0);
    
    WaitFixedTimeSeconds(4);
    
    // Elden Beast - Play FX
    PlaySE(19008000, SoundType.SFX, 888880000); 
    ChangeCamera(-1, -1);
    
    // Elden Beast - Is Dead
    WaitFor(CharacterDead(19000800));
    
    WaitFixedTimeSeconds(4.5);
    
    DisplayBossHealthBar(Disabled, 19000800, 0, 902200000);
    HandleBossDefeatAndDisplayBanner(19000800, TextBannerType.GodSlain); 
    
    SetEventFlagID(19000800, ON);
    SetEventFlagID(9190, ON);
});

// Elden Beast - Camera Shift
$Event(19002830, Restart, function() {
    DisableNetworkSync(); 
    EndIf(EventFlag(19000800)); // Elden Beast - Defeated
    
    WaitFor(CharacterHasSpEffect(19000800, 18606));
    ChangeCamera(2201, 2201);
    
    WaitFor(!CharacterHasSpEffect(19000800, 18606));
    ChangeCamera(2200, 2200);
    
    RestartEvent();
});

// Elden Beast - Common Setup
$Event(19002849, Restart, function() {
    InitializeCommonEvent(0, 9005800, 19000800, 19001800, 19002800, 19002805, 19005800, 10000, 19002801, 0); // Boss Setup
    InitializeCommonEvent(0, 9005801, 19000800, 19001800, 19002800, 19002805, 19002806, 10000); // Fog-gate Passthrough Setup
    InitializeCommonEvent(0, 9005811, 19000800, 19001800, 5, 19002801); // Fog-gate Setup
    InitializeCommonEvent(0, 9005822, 19000800, 219000, 19002805, 19002806, 0, 19002803, 0, 1); // Boss BGM
});

// Radagon - Setup
$Event(19002850, Restart, function() {
    // Radagon - Defeated
    if (EventFlag(19000850)) 
    {
        // 19002850
        DisableCharacter(19000850); 
        DisableCharacterCollision(19000850); 
        ForceCharacterDeath(19000850, false); 
        EndEvent();
    }
    
    // Radagon
    DisableCharacterAI(19000850);
    DisableCharacter(19000850);
    DisableCharacterCollision(19000850);
    DisableCharacterFadeOnEnable(19000850);
    
    DisableAsset(19001810); // Radagon Statue
    DisableAsset(19001100); // Fractured Marika
    
    // Wait for player to go near Radagon
    WaitFor(PlayerIsInOwnWorld() && EntityInRadiusOfEntity(10000, 19000850, 20, 1));
    
    DisableAsset(19001810); // Radagon Statue
    DisableAsset(19001100); // Fractured Marika
    
    if (PlayerIsInOwnWorld()) {
        SetCameraAngle(14.6, -72.33);
    }
    
    SetNetworkconnectedEventFlagID(19000851, ON);
    SetNetworkconnectedEventFlagID(19002851, ON);
    SetNetworkconnectedEventFlagID(19002856, ON);
    
    // Radagon - Start Fight
    EnableCharacter(19000850);
    EnableCharacterCollision(19000850);
    ForceAnimationPlayback(19000850, 20010, false, false, false);
    EnableCharacterAI(19000850);
    SetNetworkUpdateRate(19000850, true, CharacterUpdateFrequency.AlwaysUpdate);
    DisplayBossHealthBar(Enabled, 19000850, 0, 902190000);
    
    // Radagon - Is Dead
    WaitFor(CharacterDead(19000850));
    
    WaitFixedTimeSeconds(4.5);
    
    DisplayBossHealthBar(Disabled, 19000850, 0, 902190000);
    HandleBossDefeatAndDisplayBanner(19000850, TextBannerType.GodSlain); 
    
    SetEventFlagID(19000850, ON);
    SetEventFlagID(19001100, ON);
    SetEventFlagID(9123, ON);
    
    InitializeEvent(0, 19002910, 0); // Accursed Mode
    
    EndIf(!PlayerIsInOwnWorld());
    
    SetEventFlagID(61123, ON);
    
    EnableAsset(19001100); // Fractured Marika
    EnableAsset(19001850); // Fractured Marika
});

// Radagon - Common Setup
$Event(19002859, Restart, function() {
    InitializeCommonEvent(0, 9005800, 19000850, 19001850, 19002850, 19002855, 19005850, 10000, 19002851, 0); // Boss Setup
    InitializeCommonEvent(0, 9005801, 19000850, 19001850, 19002850, 19002855, 19002856, 10000); // Fog-gate Passthrough Setup
    InitializeCommonEvent(0, 9005811, 19000850, 19001850, 5, 19002851); // Fog-gate Setup
    InitializeCommonEvent(0, 9005822, 19000850, 219000, 19002855, 19002856, 0, 19002853, 0, 1); // Boss BGM
});

// Action: Warp to Stone Platform
$Event(19002900, Restart, function() {
    CreateAssetfollowingSFX(19001900, 100, 1300);
    WaitFor(ActionButtonInArea(9000, 19001900));
    WarpCharacterAndCopyFloorWithFadeout(10000, TargetEntityType.Area, 19002900, -1, 10000, false, false);
});

// Warp to Elden Beast
$Event(19002901, Restart, function() {
    WaitFor(EventFlag(1047610015));
    
    SetEventFlagID(1047610015, OFF);
    //WarpPlayer(19, 0, 0, 0, 19000981, -1);
    
    // Teleport into Elden Beast arena
    if (PlayerIsInOwnWorld()) {
        PlayCutsceneToPlayerAndWarp(19000000, CutscenePlayMode.Skippable, 19002812, 19000000, 10000, 0, false);
    } 
    else {
        PlayCutsceneToPlayerAndWarp(19000000, CutscenePlayMode.Skippable, 19002813, 19000000, 10000, 0, false);
    }
    
    WaitFixedTimeRealFrames(1);
        
    if (PlayerIsInOwnWorld()) {
        SetCameraAngle(-11.33, -25.83);
    }
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedEventFlagID(19002803, ON);
    }
    if (PlayerIsInOwnWorld()) {
        SetNetworkconnectedThisEventSlot(ON);
    }
});

// Elden Hollow -> Stone Platform Teleport
$Event(19002902, Restart, function() {
    DisableAsset(19001811);
        
    WaitFor(EventFlag(19000800));
    
    EnableAsset(19001811);
    
    WaitFor(ActionButtonInArea(6350, 19001811));
    
    WarpPlayer(19, 0, 0, 0, 19000980, -1);
});

// Accursed - Clear Notes
$Event(19002910, Restart, function() {
    // Accursed
    if(!EventFlag(1047610025) && EventFlag(1047610154))
    {
        SetEventFlagID(1047610025, ON);
        AwardItemLot(60990);
        
        // Remove the Accursed Notes
        RemoveItemFromPlayer(ItemType.Goods, 25000, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25001, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25002, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25003, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25004, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25005, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25006, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25007, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25008, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25009, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25010, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25011, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25012, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25013, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25014, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25015, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25016, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25017, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25018, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25019, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25020, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25021, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25022, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25023, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25024, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25025, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25026, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25027, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25028, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25029, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25030, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25031, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25032, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25033, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25034, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25035, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25036, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25037, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25038, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25039, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25040, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25041, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25042, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25043, -99);
        RemoveItemFromPlayer(ItemType.Goods, 25044, -99);
    }
});


