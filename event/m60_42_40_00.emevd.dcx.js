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


