// ==EMEVD==
// @docs    er-common.emedf.json
// @compress    DCX_KRAK
// @game    Sekiro
// @string    N:\GR\data\Param\event\common_func.emevd N:\GR\data\Param\event\common_macro.emevd      
// @linked    [0,82]
// @version    3.4.1
// ==/EMEVD==

$Event(0, Default, function() {
    // Warp Gate: Consecrated Snowfields -> Capital Outskirts
    InitializeEvent(0, 1048543500, 1048541950, 1048540950, 1048540951, 1048540952);
});

// Warp Gate - Setup
$Event(1048543500, Restart, function(X0_4, X4_4, X8_4, X12_4) {
    EndIf(!PlayerIsInOwnWorld());
    
    if (!ThisEventSlot()) {
        DeleteAssetfollowingSFX(X0_4, true);
        WaitFixedTimeFrames(1);
    }
    
    CreateAssetfollowingSFX(X0_4, 200, 806870);
    
    WaitFor(ActionButtonInArea(9140, X0_4);)
    
    WaitFixedTimeSeconds(0.033);
   
    DisplayGenericDialogAndSetEventFlags(4301, PromptType.YESNO, NumberofOptions.TwoButtons, X0_4, 3, X4_4, X8_4, X12_4);
    
    if (!EventFlag(X4_4)) {
        WaitFixedTimeSeconds(1);
        RestartEvent();
    }

    RotateCharacter(10000, X0_4, -1, true);
    ForceAnimationPlayback(10000, 60490, false, false, false);
    
    WaitFixedTimeSeconds(3);
    
    // m60_45_52_0 - Capital Outskirts
    WarpPlayer(60, 45, 52, 0, 1045520981, -1);
});
