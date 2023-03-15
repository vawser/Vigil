RegisterTableGoal(GOAL_CommonNPCTest29999_Battle, "CommonNPCTest29999_Battle")
REGISTER_GOAL_NO_SUB_GOAL(GOAL_CommonNPCTest29999_Battle, true)
Goal.Initialize = function (arg0, arg1, arg2, arg3)
    return 
end

Goal.Activate = function (arg0, arg1, arg2)
    arg1:DeleteObserve(0)
    arg1:DeleteObserve(1)
    arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5635)
    if arg1:GetBehaviorStateId(PLAN_IDX_AINOTE_STATETYPE) == PLAN_STATETYPE_JUMP_NONATTACK then
        arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 0)
        return 
    elseif ExecWeaponChange(arg0, arg1, arg2) == 1 then
        return 
    elseif ExecFirstAction(arg0, arg1, arg2) == 1 then
        return 
    end
    local local0 = {}
    local local1 = {REGIST_FUNC(arg1, arg2, GeneralNPC_Act01), REGIST_FUNC(arg1, arg2, GeneralNPC_Act02), REGIST_FUNC(arg1, arg2, GeneralNPC_Act03), REGIST_FUNC(arg1, arg2, GeneralNPC_Act04), REGIST_FUNC(arg1, arg2, GeneralNPC_Act05), REGIST_FUNC(arg1, arg2, GeneralNPC_Act06), REGIST_FUNC(arg1, arg2, GeneralNPC_Act07), REGIST_FUNC(arg1, arg2, GeneralNPC_Act08), REGIST_FUNC(arg1, arg2, GeneralNPC_Act09)}
    local1[11] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act11)
    local1[12] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act12)
    local1[21] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act21)
    local1[22] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act22)
    local1[23] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act23)
    local1[24] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act24)
    local1[25] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act25)
    local1[26] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act26)
    local1[27] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act27)
    local1[28] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act28)
    local1[29] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act29)
    local1[30] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act30)
    local1[31] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act31)
    local1[32] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act32)
    local1[35] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act35)
    local1[36] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act36)
    local1[41] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act41)
    local1[42] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act42)
    local1[43] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act43)
    local1[44] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act44)
    local1[45] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act45)
    local1[46] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act46)
    local1[47] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act47)
    local1[48] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act48)
    local1[49] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act49)
    local1[50] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act50)
    local1[51] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act51)
    local1[52] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act52)
    local1[61] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act61)
    local1[62] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act62)
    local1[63] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act63)
    local1[64] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act64)
    local1[65] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act65)
    local1[66] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act66)
    local1[67] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act67)
    local1[68] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act68)
    local1[69] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act69)
    local1[70] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act70)
    local1[71] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act71)
    local1[72] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act72)
    local1[101] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act101)
    local1[102] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act102)
    local1[103] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act103)
    local1[104] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act104)
    local1[105] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act105)
    local1[106] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act106)
    local1[107] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act107)
    local1[108] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act108)
    local1[109] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act109)
    local1[110] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act110)
    local1[111] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act111)
    local1[112] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act112)
    local1[120] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act120)
    local1[121] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act121)
    local1[150] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act150)
    local1[151] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act151)
    local1[152] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act152)
    local1[153] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act153)
    local1[154] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act154)
    local1[200] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act200)
    local1[210] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act210)
    local1[220] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act220)
    local1[230] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act230)
    local1[231] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act231)
    local1[232] = REGIST_FUNC(arg1, arg2, GeneralNPC_Act232)
    Common_NPC_AI(arg0, arg1, arg2)
    Common_Battle_Activate_ForCommonNPC(arg1, arg2, MakeNPCProbArr(arg0, arg1, arg2, 1), local1, REGIST_FUNC(arg1, arg2, GeneralNPC_AdjustSpace))
    if arg2:GetSubGoalNum() <= 0 then
        GeneralNPC_Act_onNoSubGoal(arg1, arg2)
    end
    return 
end

Goal.Update = function (arg0, arg1, arg2)
    if arg1:GetStringIndexedNumber("IsExistSpAtPlanning") == 1 and arg1:GetSp(TARGET_SELF) <= 0 then
        arg1:SetStringIndexedNumber("IsExistSpAtPlanning", 0)
        arg2:ClearSubGoal()
        arg1:Replaning()
    end
    if arg2:IsFinishTimer(0) == true and arg1:GetBehaviorStateId(PLAN_IDX_AINOTE_STATETYPE) == PLAN_STATETYPE_CHARGEMAGIC then
        arg2:ClearSubGoal()
        arg2:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
    end
    return Update_Default_NoSubGoal(arg0, arg1, arg2)
end

Goal.Terminate = function (arg0, arg1, arg2)
    return 
end

Goal.Interrupt = function (arg0, arg1, arg2)
    local local0 = {}
    if arg1:IsLadderAct(TARGET_SELF) then
        return false
    elseif arg1:IsInterupt(INTERUPT_ActivateSpecialEffect) and arg1:GetSpecialEffectActivateInterruptId(5635) then
        arg1:DeleteObserveSpecialEffectAttribute(TARGET_SELF, 5635)
        arg2:ClearSubGoal()
        local local1 = NPC_ATK_R2
        local local2 = arg1:GetRandam_Int(1, 100)
        if arg1:GetWeaponBothHandState(TARGET_SELF) == -1 and GetDualAttackType(arg1, arg2) == 1 and fate <= arg1:GetNPCActProb(9030) then
            local1 = NPC_ATK_L1
        end
        arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local1, TARGET_ENE_0, 4, 0, 0)
        return true
    elseif arg1:IsInterupt(INTERUPT_Damaged) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 2)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1201] then
            arg2:ClearSubGoal()
            GeneralNPC_Act01(arg1, arg2)
            return true
        elseif local1 <= local0[1201] + local0[1202] then
            arg2:ClearSubGoal()
            GeneralNPC_Act101(arg1, arg2)
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] then
            arg2:ClearSubGoal()
            GeneralNPC_Act102(arg1, arg2)
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] + local0[1204] then
            arg2:ClearSubGoal()
            GeneralNPC_Act103(arg1, arg2)
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] + local0[1204] + local0[1205] then
            arg2:ClearSubGoal()
            GeneralNPC_Act104(arg1, arg2)
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] + local0[1204] + local0[1205] + local0[1206] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, 1, TARGET_SELF, false, NPC_ATK_L1)
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] + local0[1204] + local0[1205] + local0[1206] + local0[1207] then
            arg2:ClearSubGoal()
            if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 0, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            else
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 1, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            end
            return true
        elseif local1 <= local0[1201] + local0[1202] + local0[1203] + local0[1204] + local0[1205] + local0[1206] + local0[1207] + local0[1208] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_LeaveTarget, 1, TARGET_ENE_0, 3, TARGET_ENE_0, true, NPC_ATK_L1)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_Shoot) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 3)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1301] then
            arg2:ClearSubGoal()
            GeneralNPC_Act102(arg1, arg2)
            return true
        elseif local1 <= local0[1301] + local0[1302] then
            arg2:ClearSubGoal()
            GeneralNPC_Act103(arg1, arg2)
            return true
        elseif local1 <= local0[1301] + local0[1302] + local0[1303] then
            arg2:ClearSubGoal()
            GeneralNPC_Act104(arg1, arg2)
            return true
        elseif local1 <= local0[1301] + local0[1302] + local0[1303] + local0[1304] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, 1, TARGET_SELF, false, NPC_ATK_L1)
            return true
        elseif local1 <= local0[1301] + local0[1302] + local0[1303] + local0[1304] + local0[1305] then
            arg2:ClearSubGoal()
            if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 0, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            else
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 1, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            end
            return true
        elseif local1 <= local0[1301] + local0[1302] + local0[1303] + local0[1304] + local0[1305] + local0[1306] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, 1, TARGET_SELF, false, NPC_ATK_L1)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_FindAttack) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 4)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1401] then
            arg2:ClearSubGoal()
            GeneralNPC_Act101(arg1, arg2)
            return true
        elseif local1 <= local0[1401] + local0[1402] then
            arg2:ClearSubGoal()
            GeneralNPC_Act102(arg1, arg2)
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] then
            arg2:ClearSubGoal()
            GeneralNPC_Act103(arg1, arg2)
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] then
            arg2:ClearSubGoal()
            GeneralNPC_Act104(arg1, arg2)
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] + local0[1405] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, 1, TARGET_SELF, false, NPC_ATK_L1)
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] + local0[1405] + local0[1406] then
            arg2:ClearSubGoal()
            if arg1:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 180) then
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 0, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            else
                arg2:AddSubGoal(GOAL_COMMON_SidewayMove, 1.2, TARGET_ENE_0, 1, arg1:GetRandam_Int(75, 90), true, false, NPC_ATK_L1)
            end
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] + local0[1405] + local0[1406] + local0[1407] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_Guard, 1.2, NPC_ATK_L1, TARGET_ENE_0, GUARD_GOAL_DESIRE_RET_Continue, true)
            return true
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] + local0[1405] + local0[1406] + local0[1407] + local0[1408] then
            arg2:ClearSubGoal()
            GeneralNPC_Act120(arg1, arg2)
        elseif local1 <= local0[1401] + local0[1402] + local0[1403] + local0[1404] + local0[1405] + local0[1406] + local0[1407] + local0[1408] + local0[1409] then
            arg2:ClearSubGoal()
            arg1:AddObserveSpecialEffectAttribute(TARGET_SELF, 5635)
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L2, TARGET_ENE_0, 999, 0, 0)
        end
    end
    if arg1:IsInterupt(INTERUPT_TargetOutOfRange) and arg1:IsTargetOutOfRangeInterruptSlot(0) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 5)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1501] then
            arg2:ClearSubGoal()
            GeneralNPC_Act105(arg1, arg2)
            return true
        elseif local1 <= local0[1501] + local0[1502] then
            arg2:ClearSubGoal()
            GeneralNPC_Act103(arg1, arg2)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_SuccessGuard) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 6)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1601] then
            arg2:ClearSubGoal()
            GeneralNPC_Act101(arg1, arg2)
            return true
        elseif local1 <= local0[1601] + local0[1602] then
            arg2:ClearSubGoal()
            GeneralNPC_Act121(arg1, arg2)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_SuccessParry) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 7)
        if arg1:GetRandam_Int(1, 100) <= local0[1701] then
            arg2:ClearSubGoal()
            local local3 = arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, -1, TARGET_SELF, false, 0)
            local3:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, 999, 0, -1)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_GuardBreak) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 8)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1801] then
            arg2:ClearSubGoal()
            local local3 = arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 1, TARGET_ENE_0, -1, TARGET_SELF, false, 0)
            local3:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, 999, 0, -1)
            return true
        elseif local1 <= local0[1801] + local0[1802] then
            arg2:ClearSubGoal()
            GeneralNPC_Act03(arg1, arg2)
            return true
        elseif local1 <= local0[1801] + local0[1802] + local0[1803] then
            arg2:ClearSubGoal()
            GeneralNPC_Act21(arg1, arg2)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_UseItem) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 9)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[1901] then
            arg2:ClearSubGoal()
            GeneralNPC_Act03(arg1, arg2)
            return true
        elseif local1 <= local0[1901] + local0[1902] then
            arg2:ClearSubGoal()
            GeneralNPC_Act153()
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_ParryTiming) then
        Common_NPC_AI(arg0, arg1, arg2)
        local0 = MakeNPCProbArr(arg0, arg1, arg2, 10)
        local local1 = arg1:GetRandam_Int(1, 100)
        if local1 <= local0[2001] then
            if CanExecArts_Immediately(arg0, arg1, arg2, 42) == 1 then
                arg2:ClearSubGoal()
                arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.2, NPC_ATK_L2, TARGET_ENE_0, 999, 0, 0)
                return true
            end
        elseif local1 <= local0[2001] + local0[2002] then
            arg2:ClearSubGoal()
            GeneralNPC_Act102(arg1, arg2)
            return true
        elseif local1 <= local0[2001] + local0[2002] + local0[2003] then
            arg2:ClearSubGoal()
            GeneralNPC_Act103(arg1, arg2)
            return true
        elseif local1 <= local0[2001] + local0[2002] + local0[2003] + local0[2004] then
            arg2:ClearSubGoal()
            GeneralNPC_Act104(arg1, arg2)
            return true
        elseif local1 <= local0[2001] + local0[2002] + local0[2003] + local0[2004] + local0[2005] then
            arg2:ClearSubGoal()
            GeneralNPC_Act07(arg1, arg2)
            return true
        elseif local1 <= local0[2001] + local0[2002] + local0[2003] + local0[2004] + local0[2005] + local0[2006] then
            arg2:ClearSubGoal()
            arg2:AddSubGoal(GOAL_COMMON_Guard, 1.2, NPC_ATK_L1, TARGET_ENE_0, GUARD_GOAL_DESIRE_RET_Continue, true)
            return true
        end
    end
    if arg1:IsInterupt(INTERUPT_Outside_ObserveArea) then
        arg2:ClearSubGoal()
        arg1:DeleteObserve(0)
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    end
    if arg1:IsInterupt(INTERUPT_Inside_ObserveArea) and arg1:IsInsideObserve(1) then
        arg2:ClearSubGoal()
        arg1:DeleteObserve(1)
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    end
    if not not arg1:IsInterupt(INTERUPT_FindUnfavorableFailedPoint) or arg1:IsInterupt(INTERUPT_MovedEnd_OnFailedPath) then
        arg1:SetStringIndexedNumber("IsUnreachMode", 1)
        return true
    else
        return false
    end
end

function ExecWeaponChange(arg0, arg1, arg2)
    local local0 = arg1:GetEquipWeaponIndex(ARM_R)
    local local1 = arg1:GetEquipWeaponId(TARGET_SELF, ARM_R, WEP_Tertiary)
    local local2 = arg1:GetEquipWeaponId(TARGET_SELF, ARM_L, WEP_Tertiary)
    if arg1:HasSpecialEffectId(TARGET_SELF, 18678) then
        if local0 == WEP_Primary then
            if not not arg1:HasSpecialEffectId(TARGET_ENE_0, 1898) or 0 < arg1:GetTimer(11) then
                local local3 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyRight, TARGET_ENE_0, 999, 0, 0)
                local3:SetLifeEndSuccess(true)
                arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
                return 1
            end
        elseif arg1:HasSpecialEffectId(TARGET_ENE_0, 1898) == false and arg1:GetTimer(11) <= 0 then
            local local3 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyRight, TARGET_ENE_0, 999, 0, 0)
            local3:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
            return 1
        end
    end
    if arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R) == 110000 and (arg1:GetEquipWeaponId(TARGET_SELF, ARM_R, WEP_Primary) ~= 110000 or arg1:GetEquipWeaponId(TARGET_SELF, ARM_R, WEP_Secondary) ~= 110000 or local1 ~= 110000) then
        local local3 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyRight, TARGET_ENE_0, 999, 0, 0)
        local3:SetLifeEndSuccess(true)
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
        return 1
    elseif arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L) == 110000 and (arg1:GetEquipWeaponId(TARGET_SELF, ARM_L, WEP_Primary) ~= 110000 or arg1:GetEquipWeaponId(TARGET_SELF, ARM_L, WEP_Secondary) ~= 110000 or local2 ~= 110000) then
        local local3 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0)
        local3:SetLifeEndSuccess(true)
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
        return 1
    end
    local local3 = -1
    if arg1:HasSpecialEffectId(TARGET_SELF, 19393) then
        local3 = 0.7
    elseif arg1:HasSpecialEffectId(TARGET_SELF, 19394) then
        local3 = 0.5
    elseif arg1:HasSpecialEffectId(TARGET_SELF, 19395) then
        local3 = 0.3
    end
    if 0 <= local3 and arg1:GetHpRate(TARGET_SELF) <= local3 then
        if local1 ~= 110000 and local0 ~= WEP_Tertiary then
            local local4 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyRight, TARGET_ENE_0, 999, 0, 0)
            local4:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
            return 1
        elseif local2 ~= 110000 and arg1:GetEquipWeaponIndex(ARM_L) ~= WEP_Tertiary then
            local local4 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.1, NPC_ATK_ArrowKeyLeft, TARGET_ENE_0, 999, 0, 0)
            local4:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0)
            return 1
        end
    end
    return 0
end

function ExecFirstAction(arg0, arg1, arg2)
    if arg1:HasSpecialEffectId(TARGET_SELF, 18678) and arg1:GetTimer(11) <= 0 and arg1:GetEquipWeaponIndex(ARM_R) == WEP_Primary then
        arg1:SetTimer(11, 20)
        GeneralNPC_Act232(arg1, arg2, paramTbl)
        return 1
    else
        return 0
    end
end

function Common_NPC_AI(arg0, arg1, arg2)
    arg1:ResetNPCActProb()
    local local0 = {}
    Common_NPC_AI_GetWeponParam(arg0, arg1, arg2, ARM_R)
    Common_NPC_AI_GetWeponParam(arg0, arg1, arg2, ARM_L)
    local local1 = arg1:GetStringIndexedNumber("R_WeaponType")
    local local2 = arg1:GetStringIndexedNumber("L_WeaponType")
    local local3 = arg1:GetDist(TARGET_ENE_0)
    if local1 == 12 and local2 ~= 10 then
        local1 = 11
    end
    local local4 = 0
    if 7 < local3 then
        local4 = 4
    elseif 5 < local3 then
        local4 = 3
    elseif 3 < local3 then
        local4 = 2
    elseif 1 < local3 then
        local4 = 1
    else
        local4 = 0
    end
    local local5 = 0
    if local1 == 1 then
        local5 = 10
    elseif local1 == 2 then
        local5 = 20
    elseif local1 == 11 then
        local5 = 30
    elseif local1 == 12 then
        local5 = 40
    elseif local1 == 13 then
        local5 = 50
    elseif local1 == 30 and CheckMagicType(arg0, arg1, arg2) == 1 then
        local5 = 100
    elseif local1 == 30 and CheckMagicType(arg0, arg1, arg2) == 2 then
        local5 = 110
    elseif local1 == 30 and CheckMagicType(arg0, arg1, arg2) == 3 then
        local5 = 120
    elseif local1 == 20 then
        local5 = 200
    end
    arg1:AddNPCActProb(local5 + local4)
    local local6 = 0
    if local2 == 1 then
        local6 = 500
    elseif local2 == 2 then
        local6 = 510
    elseif local2 == 20 then
        local6 = 600
    elseif local2 == 30 then
        local6 = 700
    elseif local2 == 10 or local2 == 11 then
        local6 = 800
    end
    arg1:AddNPCActProb(local6 + local4)
    local local7 = arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)
    local local8 = arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)
    local local9 = arg1:GetWeaponBehaviorVarID(local7)
    if 1600 <= local9 and local9 <= 1899 and 3000 <= local9 and local9 <= 3299 then
        arg1:AddNPCActProb(1000 + local4)
    end
    if 1200 <= local9 and local9 <= 1299 then
        arg1:AddNPCActProb(1010 + local4)
    end
    local local10 = GetCondNum_ForArts(arg1, ARM_R)
    local local11 = GetCondNum_ForArts(arg1, ARM_L)
    if 0 < local10 then
        local10 = local10 + local4
        arg1:AddNPCActProb(local10)
    end
    if 0 < local11 and local11 ~= local10 then
        arg1:AddNPCActProb(local11 + local4)
    end
    if arg1:IsTargetGuard(TARGET_ENE_0) == true then
        arg1:AddNPCActProb(3000)
    end
    if arg1:HasSpecialEffectId(TARGET_ENE_0, PLAN_SP_EFFECT_ANIME_SLEEPING) == true then
        arg1:AddNPCActProb(3100)
    end
    local local12 = arg1:GetWeightType(TARGET_SELF)
    if local12 == AI_TARGET_WEIGHT_TYPE_WeightOver then
        arg1:AddNPCActProb(4000)
    elseif local12 == AI_TARGET_WEIGHT_TYPE_Heavy then
        arg1:AddNPCActProb(4010)
    elseif local12 == AI_TARGET_WEIGHT_TYPE_Normal then
        arg1:AddNPCActProb(4020)
    elseif local12 == AI_TARGET_WEIGHT_TYPE_Light then
        arg1:AddNPCActProb(4030)
    end
    if 0.5 <= arg1:GetHpRate(TARGET_SELF) then
        arg1:AddNPCActProb(4100)
    end
    if arg1:GetSp(TARGET_SELF) <= 1 then
        arg1:AddNPCActProb(4200)
        arg1:SetStringIndexedNumber("IsExistSpAtPlanning", 0)
    else
        arg1:SetStringIndexedNumber("IsExistSpAtPlanning", 1)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 12) == false then
        arg1:AddNPCActProb(6000)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 11) == false then
        arg1:AddNPCActProb(6010)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 10) == false then
        arg1:AddNPCActProb(6020)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 20) == false then
        arg1:AddNPCActProb(6030)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 30) == false then
        arg1:AddNPCActProb(6040)
    end
    if HasSpelltypeX(arg0, arg1, arg2, 50) == false then
        arg1:AddNPCActProb(6050)
    end
    local local13 = true
    local local14 = true
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 12, local7) == false then
        arg1:AddNPCActProb(6400)
    else
        local13 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 11, local7) == false then
        arg1:AddNPCActProb(6410)
    else
        local13 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 10, local7) == false then
        arg1:AddNPCActProb(6420)
    else
        local13 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 20, local7) == false then
        arg1:AddNPCActProb(6430)
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 30, local7) == false then
        arg1:AddNPCActProb(6440)
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 50, local7) == false then
        arg1:AddNPCActProb(6450)
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 12, local8) == false then
        arg1:AddNPCActProb(6600)
    else
        local14 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 11, local8) == false then
        arg1:AddNPCActProb(6610)
    else
        local14 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 10, local8) == false then
        arg1:AddNPCActProb(6620)
    else
        local14 = false
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 20, local8) == false then
        arg1:AddNPCActProb(6630)
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 30, local8) == false then
        arg1:AddNPCActProb(6640)
    end
    if HasSpelltypeX_CanUse(arg0, arg1, arg2, 50, local8) == false then
        arg1:AddNPCActProb(6650)
    end
    if arg1:GetStringIndexedNumber("R_WeaponType") == 30 and local13 == true then
        arg1:AddNPCActProb(6800)
    end
    local local15 = 1
    local local16 = arg1:GetToTargetAngle(TARGET_ENE_0)
    if arg1:GetExistMeshOnLineDistSpecifyAngle(TARGET_SELF, local16 - 180, local15, AI_SPA_DIR_TYPE_TargetF) < local15 then
        arg1:AddNPCActProb(7000)
    end
    if arg1:GetExistMeshOnLineDistSpecifyAngle(TARGET_SELF, local16 + 90, local15, AI_SPA_DIR_TYPE_TargetF) < local15 and arg1:GetExistMeshOnLineDistSpecifyAngle(TARGET_SELF, local16 - 90, local15, AI_SPA_DIR_TYPE_TargetF) < local15 then
        arg1:AddNPCActProb(7010)
    end
    if arg1:GetStringIndexedNumber("IsUnreachMode") == 1 then
        if arg1:IsFinishTimer(10) then
            arg1:SetTimer(10, 1)
            if arg1:CheckDoesExistPath(TARGET_ENE_0, AI_DIR_TYPE_CENTER, 0) == true then
                arg1:SetStringIndexedNumber("IsUnreachMode", 0)
            else
                arg1:AddNPCActProb(7800)
            end
        else
            arg1:AddNPCActProb(7800)
        end
    end
    if HasItemtypeX_CanUse(arg0, arg1, arg2, 10) == false then
        arg1:AddNPCActProb(8000)
    end
    if HasItemtypeX_CanUse(arg0, arg1, arg2, 20) == false then
        arg1:AddNPCActProb(8010)
    end
    if HasItemtypeX_CanUse(arg0, arg1, arg2, 30) == false then
        arg1:AddNPCActProb(8020)
    end
    if HasItemtypeX_CanUse(arg0, arg1, arg2, 31) == false then
        arg1:AddNPCActProb(8030)
    end
    if HasItemtypeX_CanUse(arg0, arg1, arg2, 50) == false then
        arg1:AddNPCActProb(8040)
    end
    local local17 = GetBowType(local9)
    local local18 = GetBowType(arg1:GetWeaponBehaviorVarID(local8))
    local local19 = GetArrowType(arg1:GetWeaponBehaviorVarID(arg1:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 0)))
    local local20 = GetArrowType(arg1:GetWeaponBehaviorVarID(arg1:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 1)))
    local local21 = GetBoltType(arg1:GetWeaponBehaviorVarID(arg1:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Bolt, 0)))
    local local22 = GetBoltType(arg1:GetWeaponBehaviorVarID(arg1:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Bolt, 1)))
    local local23 = false
    local local24 = false
    if local17 == 40 then
        if local19 ~= 50 then
            arg1:AddNPCActProb(8400)
        end
        if local20 ~= 50 then
            arg1:AddNPCActProb(8401)
        end
        if local19 ~= 50 and local20 ~= 50 then
            local23 = true
        end
    elseif local17 == 42 then
        if local19 ~= 51 then
            arg1:AddNPCActProb(8400)
        end
        if local20 ~= 51 then
            arg1:AddNPCActProb(8401)
        end
        if local19 ~= 51 and local20 ~= 51 then
            local23 = true
        end
    elseif local17 == 43 then
        if local21 ~= 52 then
            arg1:AddNPCActProb(8400)
        end
        if local22 ~= 52 then
            arg1:AddNPCActProb(8401)
        end
        if local21 ~= 52 and local22 ~= 52 then
            local23 = true
        end
    elseif local17 == 44 then
        if local21 ~= 53 then
            arg1:AddNPCActProb(8400)
        end
        if local22 ~= 53 then
            arg1:AddNPCActProb(8401)
        end
        if local21 ~= 53 and local22 ~= 53 then
            local23 = true
        end
    end
    if local18 == 40 then
        if local19 ~= 50 then
            arg1:AddNPCActProb(8410)
        end
        if local20 ~= 50 then
            arg1:AddNPCActProb(8411)
        end
        if local19 ~= 50 and local20 ~= 50 then
            local24 = true
        end
    elseif local18 == 42 then
        if local19 ~= 51 then
            arg1:AddNPCActProb(8410)
        end
        if local20 ~= 51 then
            arg1:AddNPCActProb(8411)
        end
        if local19 ~= 51 and local20 ~= 51 then
            local24 = true
        end
    elseif local18 == 43 then
        if local21 ~= 52 then
            arg1:AddNPCActProb(8410)
        end
        if local22 ~= 52 then
            arg1:AddNPCActProb(8411)
        end
        if local21 ~= 52 and local22 ~= 52 then
            local24 = true
        end
    elseif local18 == 44 then
        if local21 ~= 53 then
            arg1:AddNPCActProb(8410)
        end
        if local22 ~= 53 then
            arg1:AddNPCActProb(8411)
        end
        if local21 ~= 53 and local22 ~= 53 then
            local23 = true
        end
    end
    local local25 = false
    if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R or arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddNPCActProb(9000)
    elseif arg1:GetStringIndexedNumber("L_WeaponType") ~= 10 then
        arg1:AddNPCActProb(9000)
    end
    if CanExecArts_Immediately(arg0, arg1, arg2, 40) == 0 and CanExecArts_Immediately(arg0, arg1, arg2, 41) == 0 then
        arg1:AddNPCActProb(9005)
    end
    if 0 < arg1:GetTimer(5) then
        arg1:AddNPCActProb(9010)
    end
    if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddNPCActProb(9020)
    elseif arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddNPCActProb(9021)
    else
        arg1:AddNPCActProb(9022)
    end
    if 0 <= GetDualAttackType(arg1, arg2) then
        arg1:AddNPCActProb(9100)
    end
    if GetArtsUsageParam(arg1, ARM_L) == 90000000 then
        arg1:AddNPCActProb(9120)
    end
    if 0 < arg1:GetTimer(3) then
        arg1:AddNPCActProb(9503)
    end
    if 0 < arg1:GetTimer(4) then
        arg1:AddNPCActProb(9504)
    end
    if 0 < arg1:GetTimer(6) then
        arg1:AddNPCActProb(9506)
    end
    if 0 < arg1:GetTimer(7) then
        arg1:AddNPCActProb(9507)
    end
    if 0 < arg1:GetTimer(8) then
        arg1:AddNPCActProb(9508)
    end
    if 0 < arg1:GetTimer(9) then
        arg1:AddNPCActProb(9509)
    end
    if arg1:GetExcelParam(AI_EXCEL_THINK_PARAM_TYPE__thinkAttr_doAdmirer) == 1 then
        local local26 = arg1:GetTeamOrder(ORDER_TYPE_Role)
        if local26 == ROLE_TYPE_Torimaki then
            arg1:AddNPCActProb(9600)
        elseif local26 == ROLE_TYPE_Kankyaku then
            arg1:AddNPCActProb(9700)
        end
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 5020) then
        arg1:AddNPCActProb(15020)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 5021) then
        arg1:AddNPCActProb(15021)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 5022) then
        arg1:AddNPCActProb(15022)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 5023) then
        arg1:AddNPCActProb(15023)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 5024) then
        arg1:AddNPCActProb(15024)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18690) then
        arg1:AddNPCActProb(15030)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18691) then
        arg1:AddNPCActProb(15031)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18692) then
        arg1:AddNPCActProb(15032)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18693) then
        arg1:AddNPCActProb(15033)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18694) then
        arg1:AddNPCActProb(15034)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18695) then
        arg1:AddNPCActProb(15035)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18650) then
        arg1:AddNPCActProb(15036)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18651) then
        arg1:AddNPCActProb(15037)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18652) then
        arg1:AddNPCActProb(15038)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18653) then
        arg1:AddNPCActProb(15039)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18654) then
        arg1:AddNPCActProb(15040)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18655) then
        arg1:AddNPCActProb(15041)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18656) then
        arg1:AddNPCActProb(15042)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18657) then
        arg1:AddNPCActProb(15043)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18658) then
        arg1:AddNPCActProb(15044)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18659) then
        arg1:AddNPCActProb(15045)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18660) then
        arg1:AddNPCActProb(15046)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18661) then
        arg1:AddNPCActProb(15047)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18662) then
        arg1:AddNPCActProb(15048)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18663) then
        arg1:AddNPCActProb(15049)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18664) then
        arg1:AddNPCActProb(15050)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18665) then
        arg1:AddNPCActProb(15051)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18666) then
        arg1:AddNPCActProb(15052)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18667) then
        arg1:AddNPCActProb(15053)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18668) then
        arg1:AddNPCActProb(15054)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18669) then
        arg1:AddNPCActProb(15055)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18670) then
        arg1:AddNPCActProb(15056)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 18671) then
        arg1:AddNPCActProb(15057)
    end
    if arg1:HasSpecialEffectId(TARGET_SELF, 19384) then
        arg1:AddNPCActProb(15058)
    end
    arg1:SetStringIndexedNumber("IsUselessWeapon", 0)
    if (not (arg1:GetStringIndexedNumber("R_WeaponType") ~= 30 or local13 ~= true) or not (arg1:GetStringIndexedNumber("R_WeaponType") ~= 20 or local23 ~= true) or arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R) == 110000) and (not (arg1:GetStringIndexedNumber("L_WeaponType") ~= 30 or local14 ~= true) or not (arg1:GetStringIndexedNumber("L_WeaponType") ~= 20 or local24 ~= true) or arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L) == 110000) then
        arg1:SetStringIndexedNumber("IsUselessWeapon", 1)
    end
    return 
end

function MakeNPCProbArr(arg0, arg1, arg2, arg3)
    local local0 = {}
    local local1 = 0
    if arg3 == 1 then
        local local2 = 1
        for local3 = 1 - local2, 300, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 2 then
        local local2 = 1
        for local3 = 1200 - local2, 1210, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 3 then
        local local2 = 1
        for local3 = 1300 - local2, 1310, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 4 then
        local local2 = 1
        for local3 = 1400 - local2, 1410, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 5 then
        local local2 = 1
        for local3 = 1500 - local2, 1510, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 6 then
        local local2 = 1
        for local3 = 1600 - local2, 1610, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 7 then
        local local2 = 1
        for local3 = 1700 - local2, 1710, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 8 then
        local local2 = 1
        for local3 = 1800 - local2, 1810, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 9 then
        local local2 = 1
        for local3 = 1900 - local2, 1910, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    if arg3 == 10 then
        local local2 = 1
        for local3 = 2000 - local2, 2010, local2 do
            local0[local3] = math.max(0, arg1:GetNPCActProb(local3))
        end
    end
    return local0
end

function GetBowType(arg0)
    local local0 = -1
    if 4000 <= arg0 and arg0 <= 4199 then
        local0 = 40
    elseif 4200 <= arg0 and arg0 <= 4299 then
        local0 = 42
    elseif 4300 <= arg0 and arg0 <= 4399 then
        local0 = 43
    elseif 4400 <= arg0 and arg0 <= 4449 then
        local0 = 44
    end
    return local0
end

function GetArrowType(arg0)
    local local0 = -1
    if 5000 <= arg0 and arg0 <= 5099 then
        local0 = 50
    end
    if 5100 <= arg0 and arg0 <= 5199 then
        local0 = 51
    end
    return local0
end

function GetBoltType(arg0)
    local local0 = -1
    if 5200 <= arg0 and arg0 <= 5299 then
        local0 = 52
    end
    if 5300 <= arg0 and arg0 <= 5399 then
        local0 = 53
    end
    return local0
end

function GetUsageId_AA(arg0, arg1)
    return math.floor(arg1 / 1000000)
end

function GetUsageId_X(arg0, arg1)
    return math.floor(arg0:Mod(arg1, 1000000) / 100000)
end

function GetUsageId_B(arg0, arg1)
    return math.floor(arg0:Mod(arg1, 100000) / 10000)
end

function GetUsageId_CC(arg0, arg1)
    return math.floor(arg0:Mod(arg1, 10000) / 100)
end

function GetUsageId_DD(arg0, arg1)
    local local0 = arg0:Mod(arg1, 100)
    return math.floor()
end

function GetArtsUsageParam(arg0, arg1)
    local local0 = arg0:GetAIUsageParam(2, arg0:GetArtsID(arg1))
    local local1 = arg0:GetCurrentEquipWeaponId(TARGET_SELF, arg1)
    local local2 = GetBowType(arg0:GetWeaponBehaviorVarID(local1))
    local local3 = GetArrowType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 0)))
    local local4 = GetArrowType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 1)))
    if local1 == 110000 or 0 <= GetDualAttackType(arg0, goal) and arg1 == ARM_L then
        local0 = 90000000
    end
    if local2 == 40 then
        if local3 ~= 50 and local4 ~= 50 then
            local0 = -1
        end
    elseif local2 == 42 and local3 ~= 51 and local4 ~= 51 then
        local0 = -1
    end
    return local0
end

function GetCondNum_ForArts(arg0, arg1)
    local local0 = GetArtsUsageParam(arg0, arg1)
    local local1 = GetUsageId_AA(arg0, local0)
    local local2 = -1
    if GetUsageId_X(arg0, local0) == 2 and 0 < arg0:GetTimer(2) then
        return -1
    elseif local1 == 12 then
        local2 = 2000
    elseif local1 == 11 then
        local2 = 2010
    elseif local1 == 10 then
        local2 = 2020
    elseif local1 == 20 then
        local2 = 2030
    elseif local1 == 30 then
        local local3 = GetUsageId_B(arg0, local0)
        if local3 == 0 then
            if arg0:HasSpecialEffectCategory(TARGET_SELF, 156) == false and arg0:HasSpecialEffectCategory(TARGET_SELF, 160) == false and arg0:HasSpecialEffectCategory(TARGET_SELF, 1001) == false then
                local2 = 2040
            end
        elseif local3 == 1 then
            if arg0:HasSpecialEffectCategory(TARGET_SELF, 162) == false and arg0:HasSpecialEffectCategory(TARGET_SELF, 163) == false then
                local2 = 2040
            end
        elseif local3 == 8 and arg0:HasSpecialEffectId(TARGET_ENE_0, 1897) == false then
            local2 = 2040
        end
    elseif local1 == 40 then
        local2 = 2050
    elseif local1 == 41 then
        local2 = 2060
    elseif local1 == 42 then
        local2 = 2070
    elseif local1 == 50 then
        local local3 = GetUsageId_B(arg0, local0)
        if local3 == 0 then
            local2 = 2080
        elseif local3 == 1 and arg0:HasSpecialEffectId(TARGET_ENE_0, 1897) == false then
            local2 = 2080
        end
    end
    return local2
end

function CheckMagicType(arg0, arg1, arg2)
    local local0 = 0
    local local1 = 0
    local local2 = 0
    local local3 = {}
    local3[12] = 0
    local3[11] = 0
    local3[10] = 0
    local local4 = 1
    for local5 = 0 - local4, 6, local4 do
        local2 = GetSpellType(arg0, arg1, arg1:GetEquipMagicId(TARGET_SELF, local5))
        if local2 == 12 or local2 == 11 or local2 == 10 then
            local3[local2] = local3[local2] + 1
        end
    end
    if local3[11] <= local3[10] and local3[12] <= local3[10] then
        return 1
    elseif local3[12] <= local3[11] and local3[10] < local3[11] then
        return 2
    else
        return 3
    end
end

function HasSpelltypeX(arg0, arg1, arg2, arg3)
    local local0 = -1
    local local1 = -1
    local local2, local3 = false
    local local4 = 1
    for local5 = 0 - local4, 9, local4 do
        if GetSpellType(arg0, arg1, arg1:GetEquipMagicId(TARGET_SELF, local5)) == arg3 then
            local2 = true
        end
    end
    return local2
end

function HasSpelltypeX_CanUse(arg0, arg1, arg2, arg3, arg4)
    local local0 = -1
    local local1 = -1
    local local2, local3 = false
    local local4 = 1
    for local5 = 0 - local4, 9, local4 do
        local0 = arg1:GetEquipMagicId(TARGET_SELF, local5)
        if GetSpellType(arg0, arg1, local0) == arg3 and CanUseSpell(arg0, arg1, arg2, local0, arg4) == true then
            local2 = true
        end
    end
    return local2
end

function CanUseSpell(arg0, arg1, arg2, arg3, arg4)
    local local0 = -1
    local local1 = -1
    local local2 = -1
    local local3 = false
    if arg1:CanShootMagicByType(arg4, arg1:GetMagicCategory(arg3)) == false then
        return false
    end
    local0 = arg1:GetAIUsageParam(0, arg3)
    local1 = GetUsageId_AA(arg1, local0)
    local2 = GetUsageId_B(arg1, local0)
    X_UsageId = GetUsageId_X(arg1, local0)
    if X_UsageId == 1 and 0 < arg1:GetTimer(1) then
        return false
    elseif local1 == 10 then
        local3 = true
    elseif local1 == 11 then
        local3 = true
    elseif local1 == 12 then
        local3 = true
    elseif local1 == 20 then
        local3 = true
    elseif local1 == 30 then
        if local2 == 0 then
            if arg1:HasSpecialEffectCategory(TARGET_SELF, 151) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 156) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 160) == false and arg1:HasSpecialEffectId(TARGET_SELF, 1676000) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 1001) == false then
                local3 = true
            end
        elseif local2 == 1 then
            if arg1:HasSpecialEffectCategory(TARGET_SELF, 162) == false and arg1:CanWeaponEnhance(arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)) then
                local3 = true
            end
        elseif local2 == 2 and arg1:HasSpecialEffectCategory(TARGET_SELF, 163) == false and arg1:GetStringIndexedNumber("L_WeaponType") == 10 == true then
            local3 = true
        end
    elseif local1 == 50 then
        local3 = true
    end
    return local3
end

function GetSpellType(arg0, arg1, arg2)
    local local0 = -1
    local local1 = -1
    local local2 = -1
    if arg2 ~= -1 then
        local2 = GetUsageId_AA(arg1, arg1:GetAIUsageParam(0, arg2))
    end
    return local2
end

function GetRandomSpellId_ByType(arg0, arg1, arg2, arg3, arg4)
    local local0 = 0
    local local1 = 0
    local local2 = 0
    local local3 = 0
    local local4 = {}
    local local5 = {}
    local local6 = nil
    local local7 = 1
    for local8 = 0 - local7, 9, local7 do
        local0 = arg1:GetEquipMagicId(TARGET_SELF, local8)
        if GetSpellType(arg0, arg1, local0) == arg3 and CanUseSpell(arg0, arg1, arg2, local0, arg4) == true then
            local4[local8] = local0
            local3 = local3 + 1
            local5[local3] = local8
        end
    end
    local local9 = 0
    if local3 ~= 0 then
        local local10 = 1
        for local7 = 1 - local10, local3, local10 do
            local9 = local9 + 1 / local3 * 100
            if arg1:GetRandam_Int(1, 100) <= local9 then
                local2 = local4[local5[local7]]
                break
            elseif local7 == local3 then
                local2 = local4[local5[local7]]
            end
        end
    end
    return local2
end

function HasItemtypeX(arg0, arg1, arg2, arg3)
    local local0 = -1
    local local1 = -1
    local local2, local3 = false
    local local4 = 1
    for local5 = 0 - local4, 9, local4 do
        if GetItemType(arg0, arg1, arg1:GetEquipItemId(TARGET_SELF, local5, ITEM_SLOTTYPE_SHORTCUT)) == arg3 then
            local2 = true
            break
        end
    end
    if local2 == false then
        local4 = 1
        for local5 = 0 - local4, 5, local4 do
            if GetItemType(arg0, arg1, arg1:GetEquipItemId(TARGET_SELF, local5, ITEM_SLOTTYPE_TOOLBOX)) == arg3 then
                local2 = true
                break
            end
        end
    end
    return local2
end

function HasItemtypeX_CanUse(arg0, arg1, arg2, arg3)
    local local0 = -1
    local local1 = -1
    local local2, local3 = false
    local local4 = 1
    for local5 = 0 - local4, 9, local4 do
        local0 = arg1:GetEquipItemId(TARGET_SELF, local5, ITEM_SLOTTYPE_SHORTCUT)
        if GetItemType(arg0, arg1, local0) == arg3 and CanUseItem(arg0, arg1, arg2, local0) == true then
            local2 = true
            break
        end
    end
    if local2 == false then
        local4 = 1
        for local5 = 0 - local4, 5, local4 do
            local0 = arg1:GetEquipItemId(TARGET_SELF, local5, ITEM_SLOTTYPE_TOOLBOX)
            if GetItemType(arg0, arg1, local0) == arg3 and CanUseItem(arg0, arg1, arg2, local0) == true then
                local2 = true
                break
            end
        end
    end
    return local2
end

function GetItemType(arg0, arg1, arg2)
    local local0 = -1
    local local1 = -1
    local local2 = -1
    if arg2 ~= -1 then
        local2 = GetUsageId_AA(arg1, arg1:GetAIUsageParam(1, arg2))
    end
    return local2
end

function CanUseItem(arg0, arg1, arg2, arg3)
    local local0 = -1
    local local1 = -1
    local local2 = -1
    local local3 = -1
    local local4 = false
    local0 = arg1:GetAIUsageParam(1, arg3)
    local1 = GetUsageId_AA(arg1, local0)
    local2 = GetUsageId_B(arg1, local0)
    if GetUsageId_X(arg1, local0) == 2 and 0 < arg1:GetTimer(2) then
        return -1
    elseif local1 == 10 then
        if local2 == 9 then
            if arg1:GetStringIndexedNumber("IsUselessWeapon") == 1 then
                local4 = true
            end
        else
            local4 = true
        end
    elseif local1 == 20 then
        if local2 == 7 then
            if arg1:HasSpecialEffectAttribute(TARGET_SELF, 154) == false then
                local4 = true
            end
        elseif local2 == 8 then
            if arg1:HasSpecialEffectId(TARGET_SELF, 5630) == false then
                local4 = true
            end
        else
            local4 = true
        end
    elseif local1 == 30 then
        if local2 == 0 then
            if arg1:HasSpecialEffectCategory(TARGET_SELF, 151) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 156) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 160) == false and arg1:HasSpecialEffectId(TARGET_SELF, 503501) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 1001) == false then
                local4 = true
            end
        elseif local2 == 1 then
            if arg1:CanWeaponEnhance(arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)) and arg1:CanWeaponEnhance(arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)) and arg1:HasSpecialEffectCategory(TARGET_SELF, 163) == false then
                local4 = true
            elseif arg1:CanWeaponEnhance(arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)) and arg1:HasSpecialEffectCategory(TARGET_SELF, 162) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 10000) == false then
                local4 = true
            end
        end
    elseif local1 == 31 then
        if arg1:HasSpecialEffectCategory(TARGET_SELF, 162) == false and arg1:HasSpecialEffectCategory(TARGET_SELF, 10000) == false and arg1:CanWeaponEnhance(arg1:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)) then
            local4 = true
        end
    elseif local1 == 50 then
        local4 = true
    end
    return local4
end

function ChangeEquipItem_ById(arg0, arg1, arg2, arg3)
    local local0 = 0
    local local1 = 0
    local local2 = false
    local local3 = 1
    for local4 = 0 - local3, 9, local3 do
        if arg1:GetEquipItemId(TARGET_SELF, local4, ITEM_SLOTTYPE_SHORTCUT) == arg3 then
            arg1:ChangeEquipItem(local4, ITEM_SLOTTYPE_SHORTCUT)
            local2 = true
            break
        end
    end
    if local2 == false then
        local3 = 1
        for local4 = 0 - local3, 5, local3 do
            if arg1:GetEquipItemId(TARGET_SELF, local4, ITEM_SLOTTYPE_TOOLBOX) == arg3 then
                arg1:ChangeEquipItem(local4, ITEM_SLOTTYPE_TOOLBOX)
                local2 = true
                break
            end
        end
    end
    return local2
end

function GetRandomItemId_ByType(arg0, arg1, arg2, arg3)
    local local0 = 0
    local local1 = 0
    local local2 = 0
    local local3 = 0
    local local4 = {}
    local local5 = nil
    local local6 = 1
    for local7 = 0 - local6, 9, local6 do
        local0 = arg1:GetEquipItemId(TARGET_SELF, local7, ITEM_SLOTTYPE_SHORTCUT)
        if GetItemType(arg0, arg1, local0) == arg3 and CanUseItem(arg0, arg1, arg2, local0) == true then
            local3 = local3 + 1
            local4[local3] = local0
        end
    end
    local6 = 1
    for local7 = 0 - local6, 5, local6 do
        local0 = arg1:GetEquipItemId(TARGET_SELF, local7, ITEM_SLOTTYPE_TOOLBOX)
        if GetItemType(arg0, arg1, local0) == arg3 and CanUseItem(arg0, arg1, arg2, local0) == true then
            local3 = local3 + 1
            local4[local3] = local0
        end
    end
    if local3 ~= 0 then
        local local8 = 0
        local local9 = 1
        for local6 = 1 - local9, local3, local9 do
            local8 = local8 + 1 / local3 * 100
            if arg1:GetRandam_Int(1, 100) <= local8 then
                local2 = local4[local6]
                break
            elseif local6 == local3 then
                local2 = local4[local6]
            end
        end
    end
    return local2
end

function GetDualAttackType(arg0, arg1)
    local local0 = arg0:GetWepCategoryNo(ARM_R)
    local local1 = arg0:GetWepCategoryNo(ARM_L)
    local local2 = arg0:GetWepSpAtkCategoryNo(ARM_L)
    local local3 = -1
    if local0 == PLAN_WEAPON_CATEGORY_SHORT_SWORD then
        if local0 == local1 and local2 ~= 104 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_CLAW then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_STRAIGHT_SWORD then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_TWINBLADE then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_LARGE_SWORD then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_EXTRALARGE_SWORD then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_RAPIER then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_CURVEDSWORD then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_KATANA then
        if local0 == local1 or local2 == 104 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_AX or local0 == PLAN_WEAPON_CATEGORY_HAMMER then
        if local1 == PLAN_WEAPON_CATEGORY_AX or local1 == PLAN_WEAPON_CATEGORY_HAMMER then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_EXTRALARGE_AXHAMMER then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_LARGE_AX or local0 == PLAN_WEAPON_CATEGORY_LARGE_HAMMER then
        if local1 == PLAN_WEAPON_CATEGORY_LARGE_AX or local1 == PLAN_WEAPON_CATEGORY_LARGE_HAMMER then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_FLAIL then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_SPEAR then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_LARGE_SPEAR or local0 == PLAN_WEAPON_CATEGORY_LARGE_RAPIER then
        if local1 == PLAN_WEAPON_CATEGORY_LARGE_SPEAR or local1 == PLAN_WEAPON_CATEGORY_LARGE_RAPIER then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_HALBERD then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_LARGE_CURVEDSWORD then
        if local0 == local1 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_FIST then
        if local0 == local1 and arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R) ~= 110000 and arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L) ~= 110000 then
            local3 = 1
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_WHIP then
        if local0 == local1 then
            local3 = 0
        end
    elseif local0 == PLAN_WEAPON_CATEGORY_LARGE_SCYTHE and local0 == local1 then
        local3 = 1
    end
    return local3
end

function ChangeBothHand_ForArts(arg0, arg1, arg2, arg3)
    local local0 = GetUsageId_AA(arg1, GetArtsUsageParam(arg1, ARM_R))
    local local1 = GetUsageId_AA(arg1, GetArtsUsageParam(arg1, ARM_L))
    local local2 = ARM_R
    local local3 = 0
    if local1 == 90 then
        local3 = 1
        local1 = -1
    end
    if arg3 == local0 and arg3 == local1 then
        if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            local2 = ARM_R
        elseif arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            local2 = ARM_L
        elseif local3 == 0 then
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local2 = ARM_R
        else
            local2 = ARM_R
        end
    elseif arg3 == local0 then
        if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            local2 = ARM_R
        elseif arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local2 = ARM_R
        elseif local3 == 0 then
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local2 = ARM_R
        else
            local2 = ARM_R
        end
    elseif arg3 == local1 then
        if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
            local2 = ARM_L
        elseif arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            local2 = ARM_L
        else
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
            local2 = ARM_L
        end
    else
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_SELF)
        return -1
    end
    return local2
end

function CanExecArts_Immediately(arg0, arg1, arg2, arg3)
    local local0 = GetUsageId_AA(arg1, GetArtsUsageParam(arg1, ARM_R))
    local local1 = GetUsageId_AA(arg1, GetArtsUsageParam(arg1, ARM_L))
    local local2 = 0
    if arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        if local0 == arg3 then
            local2 = 1
        end
    elseif arg1:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        if local1 == arg3 then
            local2 = 1
        end
    else
        local local3 = arg1:GetArtsID(ARM_L)
        if not (300 > local3 or local3 > 399) or local3 == 117 or local3 == 223 or local3 == 701 or local3 == 702 or local3 == 1001 or local3 == 1002 or local3 == 1007 or local3 == 1195 or local3 == 1196 or local3 == 1197 or 400 <= local3 and local3 <= 499 then
            if local1 == arg3 then
                local2 = 1
            end
        elseif local0 == arg3 then
            local2 = 1
        end
    end
    return local2
end

function ArtsAction_ByCC(arg0, arg1, arg2, arg3, arg4)
    local local0 = GetArtsUsageParam(arg1, arg3)
    local local1 = GetUsageId_AA(arg1, local0)
    local local2 = GetUsageId_CC(arg1, local0)
    local local3 = arg4
    if local1 < 20 and local2 ~= 40 and local2 ~= 41 and local2 ~= 42 then
        NPC_Approach_Act_Flex(arg1, arg2, arg4, arg4 + 2, arg4 + 2, 50, 0, 1.8, 2)
    end
    if local2 == 0 then
        arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 10 then
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 11 then
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 12 then
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 14 then
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 15 then
        local3 = local3 + 5
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 16 then
        local3 = local3 + 5
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 17 then
        local3 = local3 + 5
        arg2:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboRepeat, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0, 0)
        arg2:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L2, TARGET_ENE_0, local3, 0, 0)
    elseif local2 == 20 then
        local local4 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg1:GetRandam_Float(1, 3.5), NPC_ATK_L2Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local4:SetLifeEndSuccess(true)
        arg2:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
    elseif local2 == 30 then
        if local1 == 12 then
            arg1:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
            local local5 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, NPC_ATK_L2Hold, TARGET_ENE_0, -99, 0, 0, 0, 0)
            local5:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
        else
            arg1:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
            local local5 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, NPC_ATK_L2Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
            local5:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
        end
    elseif local2 == 40 then
        local local5 = NPC_ATK_L2Hold_R1
        if arg1:GetRandam_Int(0, 1) == 1 then
            local5 = NPC_ATK_L2Hold_R2
        end
        if arg4 < arg1:GetDist(TARGET_ENE_0) then
            arg2:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, arg4, TARGET_ENE_0, true, NPC_ATK_L2Hold, GUARD_GOAL_DESIRE_RET_Failed, false)
        else
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L2Hold, TARGET_ENE_0, 999, 0, 0, 0, 0)
        end
        arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, local5, TARGET_ENE_0, local3, 0, 0, 0, 0)
    elseif local2 == 41 then
        local local5 = GetArtsShotButton(arg1, arg3, NPC_ATK_L2Hold_R1, NPC_ATK_L2Hold_R2)
        if local5 == NPC_ATK_DownHold_L2Hold then
            arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1.5, local5, TARGET_ENE_0, 999, 0, 0, 0, 0)
        else
            arg2:AddSubGoal(GOAL_COMMON_NpcStanceAttack_WithMove, 20, TARGET_ENE_0, local5, 3, 0, 0, 0, 0)
        end
    elseif local2 == 42 then
        local local5 = GetArtsShotButton(arg1, arg3, NPC_ATK_L2Hold_R1, NPC_ATK_L2Hold_R2)
        arg1:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        if local5 == NPC_ATK_DownHold_L2Hold then
            arg2:AddSubGoal(GOAL_COMMON_LeaveTarget, 0.1, TARGET_ENE_0, 8, TARGET_ENE_0, true, -1)
        else
            local local4 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L2Hold, TARGET_ENE_0, 999, 0, 0, 0, 0)
            local4:SetLifeEndSuccess(true)
            local4 = arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg1:GetRandam_Float(3, 4), local5, TARGET_ENE_0, 999, 0, 0, 0, 0)
            local4:SetLifeEndSuccess(true)
            arg2:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_SELF)
        end
    else
        arg2:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_L2, TARGET_ENE_0, 999, 0, 0)
    end
    if GetUsageId_X(arg1, local0) == 2 then
        arg1:SetTimer(2, 10)
    end
    return 
end

function GetArtsShotButton(arg0, arg1, arg2, arg3)
    local local0 = GetBowType(arg0:GetWeaponBehaviorVarID(arg0:GetCurrentEquipWeaponId(TARGET_SELF, arg1)))
    local local1 = GetArrowType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 0)))
    local local2 = GetArrowType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Arrow, 1)))
    local local3 = GetBoltType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Bolt, 0)))
    local local4 = GetBoltType(arg0:GetWeaponBehaviorVarID(arg0:GetEquipArrowBoltId(TARGET_SELF, ARROW_OR_BOLT_Bolt, 1)))
    local local5 = 1
    local local6 = 1
    if local0 == 40 then
        if local1 ~= 50 then
            local5 = 0
        end
        if local2 ~= 50 then
            local6 = 0
        end
    elseif local0 == 42 then
        if local1 ~= 51 then
            local5 = 0
        end
        if local2 ~= 51 then
            local6 = 0
        end
    elseif local0 == 43 then
        if local3 ~= 52 then
            local5 = 0
        end
        if local4 ~= 52 then
            local6 = 0
        end
    elseif local0 == 44 then
        if local3 ~= 53 then
            local5 = 0
        end
        if local4 ~= 53 then
            local6 = 0
        end
    end
    if local5 == 1 and local6 == 1 then
        if arg0:GetRandam_Int(0, 1) == 1 then
            return arg2
        else
            return arg3
        end
    elseif local5 == 1 and local6 == 0 then
        return arg2
    elseif local5 == 0 and local6 == 1 then
        return arg3
    else
        return NPC_ATK_DownHold_L2Hold
    end
end

function GeneralNPC_Act01(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = 0
    local local2 = 0
    local local3 = arg0:GetNPCActProb(9020)
    local local4 = NPC_ATK_R1
    local local5 = arg0:GetStringIndexedNumber("R_ComboNum_R1")
    local local6 = false
    local local7 = false
    local local8 = false
    local local9 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local7 = true
        local4 = NPC_ATK_L1
    elseif arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9000) then
        local8 = true
    else
        local8 = false
    end
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        if local7 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local9 = false
        elseif local8 == true then
            local9 = true
        elseif 1 <= local0 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local9 = false
        else
            local9 = true
        end
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        if local7 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local9 = false
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            if local8 == true then
                if 1 <= local0 then
                    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
                    local9 = true
                else
                    local9 = false
                end
            else
                local9 = false
            end
        end
    elseif local7 == true then
        local9 = false
    elseif local8 == true then
        if 1 <= local0 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local9 = true
        else
            local9 = false
        end
    else
        local9 = false
    end
    if local9 == true then
        local1 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_First")
        local2 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_Second")
        local6 = false
    else
        local1 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_First")
        local2 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_Second")
        if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
            local6 = true
        else
            local6 = false
        end
    end
    if local6 == false then
        arg0:AddNPCActProb(9000)
        local3 = arg0:GetNPCActProb(9020)
    end
    local local10 = false
    if arg0:GetRandam_Int(1, 100) <= local3 then
        local10 = true
        local3 = 100
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1 + 2, local1 + 2, 50, local3, 1.8, 2)
    if local1 <= local0 and arg0:GetRandam_Int(1, 100) <= 50 and local10 == true then
        if arg0:IsInsideTargetCustom(TARGET_ENE_0, TARGET_SELF, AI_DIR_TYPE_L, 180, 180, 10) == true then
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        else
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        end
    end
    if 6 <= local5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, local4, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, local4, TARGET_ENE_0, local2, 0, 0)
    elseif local5 == 5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, local4, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, local4, TARGET_ENE_0, local2, 0, 0)
    elseif local5 == 4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, local4, TARGET_ENE_0, local2, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, local4, TARGET_ENE_0, local2, 0, 0)
    elseif local5 == 3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, local4, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, local4, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, local4, TARGET_ENE_0, local2, 0, 0)
    elseif local5 == 2 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, local4, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, local4, TARGET_ENE_0, local2, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, local4, TARGET_ENE_0, local1, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act02(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = 0
    local local2 = 0
    local local3 = arg0:GetNPCActProb(9020)
    local local4 = false
    local local5 = false
    local local6 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9010) then
        local5 = true
    else
        local5 = false
    end
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        if local5 == true then
            local6 = true
        elseif 1 <= local0 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local6 = false
        else
            local6 = true
        end
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        if local5 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            if 1 <= local0 then
                arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
                local6 = true
            else
                local6 = false
            end
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local6 = false
        end
    elseif local5 == true then
        if 1 <= local0 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local6 = true
        else
            local6 = false
        end
    else
        local6 = false
    end
    if local6 == true then
        local1 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR2_First")
        local2 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR2_Second")
        local4 = false
    else
        local1 = arg0:GetStringIndexedNumber("R_Dist_OneHandR2_First")
        local2 = arg0:GetStringIndexedNumber("R_Dist_OneHandR2_Second")
        if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
            local4 = true
        else
            local4 = false
        end
    end
    if local4 == false then
        arg0:AddNPCActProb(9000)
        local3 = arg0:GetNPCActProb(9020)
    end
    local local7 = false
    if arg0:GetRandam_Int(1, 100) <= local3 then
        local7 = true
        local3 = 100
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1 + 2, local1 + 2, 50, local3, 1.8, 2)
    if local1 <= local0 and arg0:GetRandam_Int(1, 100) <= 50 and local7 == true then
        if arg0:IsInsideTargetCustom(TARGET_ENE_0, TARGET_SELF, AI_DIR_TYPE_L, 180, 180, 10) == true then
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        else
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        end
    end
    local local8 = arg0:GetRandam_Int(1, 100)
    if arg0:GetStringIndexedNumber("R_ComboNum_R2") == 2 then
        if local8 <= 80 then
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local1, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local2, 0, 0)
        elseif local8 <= 90 then
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local1, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local2, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local1, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local2, 0, 0)
        end
    elseif local8 <= 80 then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local1, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local1, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act03(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = arg0:GetDist(TARGET_ENE_0)
    local local2 = -1
    local local3 = arg0:GetNPCActProb(9020)
    local local4 = false
    local local5 = NPC_ATK_DashR1
    local local6 = false
    if arg0:GetRandam_Int(1, 100) <= 50 then
        local5 = NPC_ATK_DashR1
        if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
            local6 = true
            local5 = NPC_ATK_DashL1
        end
    else
        local5 = NPC_ATK_DashR2
    end
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        if local6 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
            local4 = true
        end
    elseif arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local4 = true
    end
    if local4 == false then
        arg0:AddNPCActProb(9000)
        local3 = arg0:GetNPCActProb(9020)
    end
    if arg0:GetRandam_Int(1, 100) <= local3 then
        local2 = NPC_ATK_L1
    end
    arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("R_Dist_DashR1"), TARGET_SELF, local2)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, local5, TARGET_ENE_0, 999, 0, 0)
    return 
end

function GeneralNPC_Act04(arg0, arg1, arg2)
    local local0 = false
    local local1 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local0 = true
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local1 = true
        local0 = false
    end
    if local1 == false then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R and local0 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local2 = NPC_ATK_NONE
    local local3 = NPC_ATK_UpLeft_ButtonXmark
    local local4 = NPC_ATK_UpRight_ButtonXmark
    local local5 = NPC_ATK_Up_ButtonXmark
    if local1 == true then
        local3 = NPC_ATK_UpLeft_L2
        local4 = NPC_ATK_UpRight_L2
        local5 = NPC_ATK_Up_L2
    end
    if 5 <= arg0:GetDist(TARGET_ENE_0) and SpaceCheck(arg0, arg1, 0, 5) == true then
        local2 = local5
    elseif SpaceCheck(arg0, arg1, -45, 5) == true then
        if SpaceCheck(arg0, arg1, 45, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local2 = local3
            else
                local2 = local4
            end
        else
            local2 = local4
        end
    elseif SpaceCheck(arg0, arg1, 45, 5) == true then
        local2 = local4
    end
    if local2 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local2, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("R_Dist_RollingR1"), arg0:GetStringIndexedNumber("R_Dist_RollingR2"), 50, local0)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act05(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = false
    local local2 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local1 = true
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local2 = true
        local1 = false
    end
    if local2 == false then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R and local1 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local3 = NPC_ATK_NONE
    local local4 = NPC_ATK_Left_ButtonXmark
    local local5 = NPC_ATK_Right_ButtonXmark
    if local2 == true then
        local4 = NPC_ATK_Left_L2
        local5 = NPC_ATK_Right_L2
    end
    if SpaceCheck(arg0, arg1, -90, 5) == true then
        if SpaceCheck(arg0, arg1, 90, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local3 = local4
            else
                local3 = local5
            end
        else
            local3 = local4
        end
    elseif SpaceCheck(arg0, arg1, 90, 5) == true then
        local3 = local5
    end
    if local3 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local3, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("R_Dist_RollingR1"), arg0:GetStringIndexedNumber("R_Dist_RollingR2"), 50, local1)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act06(arg0, arg1, arg2)
    local local0 = false
    local local1 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local0 = true
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local1 = true
        local0 = false
    end
    if local1 == false then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R and local0 == true then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local2 = NPC_ATK_NONE
    local local3 = NPC_ATK_DownLeft_ButtonXmark
    local local4 = NPC_ATK_DownRight_ButtonXmark
    local local5 = NPC_ATK_Down_ButtonXmark
    if local1 == true then
        local3 = NPC_ATK_DownLeft_L2
        local4 = NPC_ATK_DownRight_L2
        local5 = NPC_ATK_Down_L2
    end
    if arg0:GetDist(TARGET_ENE_0) <= 1 and SpaceCheck(arg0, arg1, 180, 5) == true then
        local2 = local5
    elseif SpaceCheck(arg0, arg1, -135, 5) == true then
        if SpaceCheck(arg0, arg1, 135, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local2 = local3
            else
                local2 = local4
            end
        else
            local2 = local3
        end
    elseif SpaceCheck(arg0, arg1, 135, 5) == true then
        local2 = local4
    end
    if local2 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local2, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("R_Dist_RollingR1"), arg0:GetStringIndexedNumber("R_Dist_RollingR2"), 50, local0)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act07(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local2 = true
    end
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R and local2 == true then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if SpaceCheck(arg0, arg1, 180, 5) == true then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_ButtonXmark, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("R_Dist_BackStepR1"), arg0:GetStringIndexedNumber("R_Dist_BackStepR2"), 50, local2)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act08(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = 0
    local local1 = 0
    local local2 = false
    local local3 = NPC_ATK_R2
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local2 = true
    else
        local2 = false
    end
    if local2 == false then
        arg0:AddNPCActProb(9000)
        local1 = arg0:GetNPCActProb(9020)
    end
    if GetDualAttackType(arg0, arg1) == 1 and arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local3 = NPC_ATK_L1
    end
    NPC_Approach_Act_Flex(arg0, arg1, 4, 0, 4, 100, local1, 1.8, 2)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.5, NPC_ATK_Up_Jump, TARGET_ENE_0, 999, 0, 90)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local3, TARGET_ENE_0, 999, 0, 90)
    return 
end

function GeneralNPC_Act09(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = 0
    local local1 = false
    local local2 = NPC_ATK_R2
    local local3 = -1
    if GetDualAttackType(arg0, arg1) == 1 and arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9030) then
        local2 = NPC_ATK_L1
    end
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local1 = true
    else
        local1 = false
    end
    if local1 == false then
        arg0:AddNPCActProb(9000)
        local0 = arg0:GetNPCActProb(9020)
    end
    if arg0:GetRandam_Int(1, 100) <= local0 then
        local3 = NPC_ATK_L1
    end
    arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, 6.8, TARGET_SELF, local3)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.5, NPC_ATK_Dash_Jump, TARGET_ENE_0, 999, 0, 90)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local2, TARGET_ENE_0, 999, 0, 90)
    return 
end

function GeneralNPC_Act11(arg0, arg1, arg2)
    local local0 = 10
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetDist(TARGET_ENE_0)
    local local3 = 90
    local local4 = GetBowType(arg0:GetWeaponBehaviorVarID(arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)))
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            if local4 ~= 43 then
                arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            end
        elseif local4 ~= 43 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    end
    NPC_Approach_Act_Flex(arg0, arg1, 30, 0, 30, 50, 0, 1.8, 2)
    if local4 == 43 then
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
        local5:SetTargetRange(0, 2.5, 999)
    end
    local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R1Hold, TARGET_ENE_0, 999, 0, 0)
    local5:SetTargetRange(0, 2.5, 999)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act12(arg0, arg1, arg2)
    local local0 = 10
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetDist(TARGET_ENE_0)
    local local3 = 90
    local local4 = GetBowType(arg0:GetWeaponBehaviorVarID(arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)))
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            if local4 ~= 43 then
                arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            end
        elseif local4 ~= 43 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        end
    end
    NPC_Approach_Act_Flex(arg0, arg1, 30, 0, 30, 50, 0, 1.8, 2)
    if local4 == 43 then
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 0)
        local5:SetTargetRange(0, 2.5, 999)
    end
    local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2Hold, TARGET_ENE_0, 999, 0, 0)
    local5:SetTargetRange(0, 2.5, 999)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act21(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    local local5 = arg0:GetNPCActProb(9020)
    local local6 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local6 = true
    else
        local6 = false
    end
    if local6 == false then
        arg0:AddNPCActProb(9000)
        local5 = arg0:GetNPCActProb(9020)
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, local5, 1.8, 2)
    if local3 == 1 then
        local local7 = arg0:GetRandam_Int(1, 100)
        local local8 = 20
        local local9 = 30
        local local10 = 30
        local local11 = 20
        local local12 = 0
        local local13 = 0
        local local14 = 1
        if local7 <= local8 then
            local14 = 2
        elseif local7 <= local8 + local9 then
            local14 = 3
        elseif local7 <= local8 + local9 + local10 then
            local14 = 4
        elseif local7 <= local8 + local9 + local10 + local11 then
            local14 = 5
        elseif local7 <= local8 + local9 + local10 + local11 + local12 then
            local14 = 6
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 then
            local14 = 7
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 + 0 then
            local14 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local14, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act22(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act23(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act24(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    local local5 = arg0:GetNPCActProb(9020)
    local local6 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local6 = true
    else
        local6 = false
    end
    if local6 == false then
        arg0:AddNPCActProb(9000)
        local5 = arg0:GetNPCActProb(9020)
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, local5, 1.8, 2)
    if local3 == 1 then
        local local7 = arg0:GetRandam_Int(1, 100)
        local local8 = 20
        local local9 = 30
        local local10 = 30
        local local11 = 20
        local local12 = 0
        local local13 = 0
        local local14 = 1
        if local7 <= local8 then
            local14 = 2
        elseif local7 <= local8 + local9 then
            local14 = 3
        elseif local7 <= local8 + local9 + local10 then
            local14 = 4
        elseif local7 <= local8 + local9 + local10 + local11 then
            local14 = 5
        elseif local7 <= local8 + local9 + local10 + local11 + local12 then
            local14 = 6
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 then
            local14 = 7
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 + 0 then
            local14 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local14, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act25(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act26(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act27(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    local local5 = arg0:GetNPCActProb(9020)
    local local6 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local6 = true
    else
        local6 = false
    end
    if local6 == false then
        arg0:AddNPCActProb(9000)
        local5 = arg0:GetNPCActProb(9020)
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, local5, 1.8, 2)
    if local3 == 1 then
        local local7 = arg0:GetRandam_Int(1, 100)
        local local8 = 20
        local local9 = 30
        local local10 = 30
        local local11 = 20
        local local12 = 0
        local local13 = 0
        local local14 = 1
        if local7 <= local8 then
            local14 = 2
        elseif local7 <= local8 + local9 then
            local14 = 3
        elseif local7 <= local8 + local9 + local10 then
            local14 = 4
        elseif local7 <= local8 + local9 + local10 + local11 then
            local14 = 5
        elseif local7 <= local8 + local9 + local10 + local11 + local12 then
            local14 = 6
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 then
            local14 = 7
        elseif local7 <= local8 + local9 + local10 + local11 + local12 + local13 + 0 then
            local14 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local14, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local8:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act28(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_R1Hold, NPC_ATK_Right_R1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_R1, NPC_ATK_Right_R1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act29(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_R1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_R1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_R1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act30(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 20, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    return 
end

function GeneralNPC_Act31(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 30, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    return 
end

function GeneralNPC_Act32(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 50, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_R)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_R1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    arg0:SetTimer(4, 30)
    return 
end

function GeneralNPC_Act35(arg0, arg1, arg2)
    return 
end

function GeneralNPC_Act36(arg0, arg1, arg2)
    return 
end

function GeneralNPC_Act41(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR1_First")
    local local2 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR1_Second")
    local local3 = arg0:GetStringIndexedNumber("L_ComboNum_R1")
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local4 = arg0:GetNPCActProb(9020)
    local local5 = false
    arg0:AddNPCActProb(9000)
    local4 = arg0:GetNPCActProb(9020)
    local local6 = false
    if arg0:GetRandam_Int(1, 100) <= local4 then
        local6 = true
        local4 = 100
    end
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1 + 2, local1 + 2, 50, local4, 1.8, 2)
    if local1 <= arg0:GetDist(TARGET_ENE_0) and arg0:GetRandam_Int(1, 100) <= 50 and local6 == true then
        if arg0:IsInsideTargetCustom(TARGET_ENE_0, TARGET_SELF, AI_DIR_TYPE_L, 180, 180, 10) == true then
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        else
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        end
    end
    if 6 <= local3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    elseif local3 == 5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    elseif local3 == 4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    elseif local3 == 3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    elseif local3 == 2 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local1, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act42(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR2_First")
    local local3 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR2_Second")
    local local4 = 100
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local5 = arg0:GetNPCActProb(9020)
    arg0:AddNPCActProb(9000)
    NPC_Approach_Act_Flex(arg0, arg1, local2, local2 + 2, local2 + 2, 50, arg0:GetNPCActProb(9020), 1.8, 2)
    if local2 <= arg0:GetDist(TARGET_ENE_0) and arg0:GetRandam_Int(1, 100) <= 50 and UseGuard == true then
        if arg0:IsInsideTargetCustom(TARGET_ENE_0, TARGET_SELF, AI_DIR_TYPE_L, 180, 180, 10) == true then
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        else
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        end
    end
    local local6 = arg0:GetRandam_Int(1, 100)
    if arg0:GetStringIndexedNumber("L_ComboNum_R1") == 2 then
        if local6 <= 80 then
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local2, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local3, 0, 0)
        elseif local6 <= 90 then
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local2, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local3, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local2, 0, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_R2, TARGET_ENE_0, local3, 0, 0)
        end
    elseif local6 <= 80 then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R2, TARGET_ENE_0, local2, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R2Hold, TARGET_ENE_0, local2, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act43(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetStringIndexedNumber("L_Dist_OneHandL2")
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local2 = arg0:GetNPCActProb(9020)
    arg0:AddNPCActProb(9000)
    local local3 = arg0:GetStringIndexedNumber("R_ComboNum_R1")
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1 + 2, local1 + 2, 50, arg0:GetNPCActProb(9020), 1.8, 2)
    if 6 <= local3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
    elseif local3 == 5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
    elseif local3 == 4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
    elseif local3 == 3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1, TARGET_ENE_0, local1, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
    elseif local3 == 2 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1, TARGET_ENE_0, local1, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1, TARGET_ENE_0, AttDist_Second, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_L1, TARGET_ENE_0, local1, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act44(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = arg0:GetDist(TARGET_ENE_0)
    local local2 = arg0:GetStringIndexedNumber("L_Dist_DashR1")
    local local3 = -1
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local4 = arg0:GetNPCActProb(9020)
    local local5 = false
    arg0:AddNPCActProb(9000)
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9020) then
        local3 = NPC_ATK_L1
    end
    if arg0:GetRandam_Int(1, 100) <= 50 then
        arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, local2, TARGET_SELF, local3)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_DashR1, TARGET_ENE_0, 999, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, local2, TARGET_SELF, local3)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_DashR2, TARGET_ENE_0, 999, 0, 0)
    end
    return 
end

function GeneralNPC_Act45(arg0, arg1, arg2)
    local local0 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local0 = true
    end
    local local1 = NPC_ATK_NONE
    local local2 = NPC_ATK_UpLeft_ButtonXmark
    local local3 = NPC_ATK_UpRight_ButtonXmark
    local local4 = NPC_ATK_Up_ButtonXmark
    if local0 == true then
        local2 = NPC_ATK_UpLeft_L2
        local3 = NPC_ATK_UpRight_L2
        local4 = NPC_ATK_Up_L2
    end
    if 5 <= arg0:GetDist(TARGET_ENE_0) and SpaceCheck(arg0, arg1, 0, 5) == true then
        local1 = local4
    elseif SpaceCheck(arg0, arg1, -45, 5) == true then
        if SpaceCheck(arg0, arg1, 45, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local1 = local2
            else
                local1 = local3
            end
        else
            local1 = local3
        end
    elseif SpaceCheck(arg0, arg1, 45, 5) == true then
        local1 = local3
    end
    if local1 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local1, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("L_Dist_RollingR1"), arg0:GetStringIndexedNumber("L_Dist_RollingR2"), 50)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act46(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local1 = true
    end
    local local2 = NPC_ATK_NONE
    local local3 = NPC_ATK_Left_ButtonXmark
    local local4 = NPC_ATK_Right_ButtonXmark
    if local1 == true then
        local3 = NPC_ATK_Left_L2
        local4 = NPC_ATK_Right_L2
    end
    if SpaceCheck(arg0, arg1, -90, 5) == true then
        if SpaceCheck(arg0, arg1, 90, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local2 = local3
            else
                local2 = local4
            end
        else
            local2 = local3
        end
    elseif SpaceCheck(arg0, arg1, 90, 5) == true then
        local2 = local4
    end
    if local2 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local2, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("L_Dist_RollingR1"), arg0:GetStringIndexedNumber("L_Dist_RollingR2"), 50)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act47(arg0, arg1, arg2)
    local local0 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local0 = true
    end
    local local1 = NPC_ATK_NONE
    local local2 = NPC_ATK_DownLeft_ButtonXmark
    local local3 = NPC_ATK_DownRight_ButtonXmark
    local local4 = NPC_ATK_Down_ButtonXmark
    if local0 == true then
        local2 = NPC_ATK_DownLeft_L2
        local3 = NPC_ATK_DownRight_L2
        local4 = NPC_ATK_Down_L2
    end
    if arg0:GetDist(TARGET_ENE_0) <= 1 and SpaceCheck(arg0, arg1, 180, 5) == true then
        local1 = local4
    elseif SpaceCheck(arg0, arg1, -135, 5) == true then
        if SpaceCheck(arg0, arg1, 135, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local1 = local2
            else
                local1 = local3
            end
        else
            local1 = local2
        end
    elseif SpaceCheck(arg0, arg1, 135, 5) == true then
        local1 = local3
    end
    if local1 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local1, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 3, TARGET_ENE_0, arg0:GetStringIndexedNumber("L_Dist_RollingR1"), arg0:GetStringIndexedNumber("L_Dist_RollingR2"), 50)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act48(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetRandam_Int(1, 100)
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    if SpaceCheck(arg0, arg1, 180, 5) == true then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_ButtonXmark, TARGET_ENE_0, 999, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_NPCStepAttack, 1, TARGET_ENE_0, arg0:GetStringIndexedNumber("L_Dist_BackStepR1"), arg0:GetStringIndexedNumber("L_Dist_BackStepR2"), 50)
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act49(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local0 = 0
    local local1 = 0
    local local2 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local2 = true
    else
        local2 = false
    end
    if local2 == false then
        arg0:AddNPCActProb(9000)
        local1 = arg0:GetNPCActProb(9020)
    end
    NPC_Approach_Act_Flex(arg0, arg1, 4, 0, 4, 100, local1, 1.8, 2)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.5, NPC_ATK_Up_Jump, TARGET_ENE_0, 999, 0, 90)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 90)
    return 
end

function GeneralNPC_Act50(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L then
        if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        else
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        end
    end
    local local0 = 0
    local local1 = false
    local local2 = -1
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local1 = true
    else
        local1 = false
    end
    if local1 == false then
        arg0:AddNPCActProb(9000)
        local0 = arg0:GetNPCActProb(9020)
    end
    if arg0:GetRandam_Int(1, 100) <= local0 then
        local2 = NPC_ATK_L1
    end
    arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, 6.8, TARGET_SELF, local2)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 0.5, NPC_ATK_Dash_Jump, TARGET_ENE_0, 999, 0, 90)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2, TARGET_ENE_0, 999, 0, 90)
    return 
end

function GeneralNPC_Act51(arg0, arg1, arg2)
    local local0 = 10
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetDist(TARGET_ENE_0)
    local local3 = arg0:GetRandam_Int(0, 1)
    local local4 = 90
    local local5 = false
    local local6 = GetBowType(arg0:GetWeaponBehaviorVarID(arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)))
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        local5 = true
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        if local6 ~= 43 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
            local5 = true
        end
    elseif local6 ~= 43 then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        local5 = true
    end
    NPC_Approach_Act_Flex(arg0, arg1, 30, 0, 30, 50, 0, 1.8, 2)
    if local6 == 43 then
        local local7 = NPC_ATK_L1
        if local5 == true then
            local7 = NPC_ATK_R1
        end
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local7, TARGET_ENE_0, 999, 0, 0)
        local8:SetTargetRange(0, 2.5, 999)
        local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local7, TARGET_ENE_0, 999, 0, 0)
        local8:SetTargetRange(0, 2.5, 999)
    else
        local local7 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R1Hold, TARGET_ENE_0, 999, 0, 0)
        local7:SetTargetRange(0, 2.5, 999)
    end
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act52(arg0, arg1, arg2)
    local local0 = 10
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetDist(TARGET_ENE_0)
    local local3 = arg0:GetRandam_Int(0, 1)
    local local4 = 90
    local local5 = false
    local local6 = GetBowType(arg0:GetWeaponBehaviorVarID(arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)))
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        local5 = true
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        if local6 ~= 43 then
            arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
            local5 = true
        end
    elseif local6 ~= 43 then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, 999, 0, 0)
        local5 = true
    end
    NPC_Approach_Act_Flex(arg0, arg1, 30, 0, 30, 50, 0, 1.8, 2)
    if local6 == 43 then
        local local7 = NPC_ATK_L2
        if local5 == true then
            local7 = NPC_ATK_R2
        end
        local local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local7, TARGET_ENE_0, 999, 0, 0)
        local8:SetTargetRange(0, 2.5, 999)
        local8 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local7, TARGET_ENE_0, 999, 0, 0)
        local8:SetTargetRange(0, 2.5, 999)
    else
        local local7 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, NPC_ATK_R2Hold, TARGET_ENE_0, 999, 0, 0)
        local7:SetTargetRange(0, 2.5, 999)
    end
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act61(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, 0, 1.8, 2)
    if local3 == 1 then
        local local5 = arg0:GetRandam_Int(1, 100)
        local local6 = 20
        local local7 = 30
        local local8 = 30
        local local9 = 20
        local local10 = 0
        local local11 = 0
        local local12 = 1
        if local5 <= local6 then
            local12 = 2
        elseif local5 <= local6 + local7 then
            local12 = 3
        elseif local5 <= local6 + local7 + local8 then
            local12 = 4
        elseif local5 <= local6 + local7 + local8 + local9 then
            local12 = 5
        elseif local5 <= local6 + local7 + local8 + local9 + local10 then
            local12 = 6
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 then
            local12 = 7
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 + 0 then
            local12 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local12, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act62(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act63(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 12, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 7, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act64(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, arg0:GetNPCActProb(9020), 1.8, 2)
    if local3 == 1 then
        local local5 = arg0:GetRandam_Int(1, 100)
        local local6 = 20
        local local7 = 30
        local local8 = 30
        local local9 = 20
        local local10 = 0
        local local11 = 0
        local local12 = 1
        if local5 <= local6 then
            local12 = 2
        elseif local5 <= local6 + local7 then
            local12 = 3
        elseif local5 <= local6 + local7 + local8 then
            local12 = 4
        elseif local5 <= local6 + local7 + local8 + local9 then
            local12 = 5
        elseif local5 <= local6 + local7 + local8 + local9 + local10 then
            local12 = 6
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 then
            local12 = 7
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 + 0 then
            local12 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local12, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act65(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act66(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 11, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 8, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act67(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local4 = 0
    NPC_Approach_Act_Flex(arg0, arg1, local1, local1, local1 + 6, 0, 0, 1.8, 2)
    if local3 == 1 then
        local local5 = arg0:GetRandam_Int(1, 100)
        local local6 = 20
        local local7 = 30
        local local8 = 30
        local local9 = 20
        local local10 = 0
        local local11 = 0
        local local12 = 1
        if local5 <= local6 then
            local12 = 2
        elseif local5 <= local6 + local7 then
            local12 = 3
        elseif local5 <= local6 + local7 + local8 then
            local12 = 4
        elseif local5 <= local6 + local7 + local8 + local9 then
            local12 = 5
        elseif local5 <= local6 + local7 + local8 + local9 + local10 then
            local12 = 6
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 then
            local12 = 7
        elseif local5 <= local6 + local7 + local8 + local9 + local10 + local11 + 0 then
            local12 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Up_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_F, -1, local12, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local6 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Up_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local6:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Up_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act68(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, arg0:GetRandam_Float(1, 4), NPC_ATK_Left_L1Hold, NPC_ATK_Right_L1Hold, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 1, NPC_ATK_Left_L1, NPC_ATK_Right_L1, TARGET_ENE_0, local1, AI_DIR_TYPE_L, AI_DIR_TYPE_R, 1, 2, 0, 0, -1, -1)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act69(arg0, arg1, arg2)
    local local0 = GetRandomSpellId_ByType(self, arg0, arg1, 10, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L))
    Common_NPC_AI_GetSpellUseDist(self, arg0, arg1, local0)
    local local1 = arg0:GetStringIndexedNumber("Spell_ApproachDist")
    local local2 = arg0:GetAIUsageParam(0, local0)
    local local3 = GetUsageId_CC(arg0, local2)
    arg0:ChangeEquipMagicByMagicParamId(local0)
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    if local3 == 1 then
        local local4 = arg0:GetRandam_Int(1, 100)
        local local5 = 20
        local local6 = 30
        local local7 = 30
        local local8 = 20
        local local9 = 0
        local local10 = 0
        local local11 = 1
        if local4 <= local5 then
            local11 = 2
        elseif local4 <= local5 + local6 then
            local11 = 3
        elseif local4 <= local5 + local6 + local7 then
            local11 = 4
        elseif local4 <= local5 + local6 + local7 + local8 then
            local11 = 5
        elseif local4 <= local5 + local6 + local7 + local8 + local9 then
            local11 = 6
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 then
            local11 = 7
        elseif local4 <= local5 + local6 + local7 + local8 + local9 + local10 + 0 then
            local11 = 8
        end
        arg1:AddSubGoal(GOAL_COMMON_NpcComboAttack_WithMove, 30, NPC_ATK_Down_L1, -1, TARGET_ENE_0, local1, AI_DIR_TYPE_B, -1, local11, 2, 0, 0, -1, -1)
    elseif local3 == 2 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 2.2), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    elseif local3 == 3 then
        arg0:AddObserveAreaCustom(1, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 180, 180, 4)
        arg1:SetTimer(0, 6)
        local local5 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, arg0:GetRandam_Float(1, 4), NPC_ATK_Down_L1Hold, TARGET_ENE_0, 0, 0, 0, 0, 0)
        local5:SetLifeEndSuccess(true)
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_Down_L1, TARGET_ENE_0, local1, 0, 0)
    end
    arg1:AddSubGoal(GOAL_COMMON_SetTimerRealtime, 0.1, 9, 2)
    if GetUsageId_X(arg0, local2) == 1 then
        arg0:SetTimer(1, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act70(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 20, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    return 
end

function GeneralNPC_Act71(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 30, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    return 
end

function GeneralNPC_Act72(arg0, arg1, arg2)
    arg0:ChangeEquipMagicByMagicParamId(GetRandomSpellId_ByType(self, arg0, arg1, 50, arg0:GetCurrentEquipWeaponId(TARGET_SELF, ARM_L)))
    if arg0:IsBothHandMode(TARGET_SELF) then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local0 = arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, NPC_ATK_L1, TARGET_ENE_0, 999, 0, 0)
    local0:SetLifeEndSuccess(true)
    arg1:AddSubGoal(GOAL_COMMON_Wait, 0.2, TARGET_ENE_0)
    arg0:SetTimer(4, 30)
    return 
end

function GeneralNPC_Act101(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetRandam_Int(1, 100)
    if SpaceCheck(arg0, arg1, 180, 5) == true then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonXmark, TARGET_ENE_0, 999, 0, 0)
    end
    arg0:SetTimer(6, 1)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act102(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local1 = true
    end
    local local2 = NPC_ATK_NONE
    local local3 = NPC_ATK_Up_ButtonXmark
    local local4 = NPC_ATK_UpLeft_ButtonXmark
    local local5 = NPC_ATK_UpRight_ButtonXmark
    if local1 == true then
        local3 = NPC_ATK_Up_L2
        local4 = NPC_ATK_UpLeft_L2
        local5 = NPC_ATK_UpRight_L2
    end
    if 5 <= arg0:GetDist(TARGET_ENE_0) and SpaceCheck(arg0, arg1, 0, 5) == true then
        local2 = local3
    elseif SpaceCheck(arg0, arg1, -45, 5) == true then
        if SpaceCheck(arg0, arg1, 45, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local2 = local4
            else
                local2 = local5
            end
        else
            local2 = local4
        end
    elseif SpaceCheck(arg0, arg1, 45, 5) == true then
        local2 = local5
    end
    if local2 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local2, TARGET_ENE_0, 999, 0, 0)
        arg0:SetTimer(6, 1)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act103(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetRandam_Int(1, 100)
    local local3 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local3 = true
    end
    local local4 = NPC_ATK_NONE
    local local5 = NPC_ATK_Left_ButtonXmark
    local local6 = NPC_ATK_Right_ButtonXmark
    if local3 == true then
        local5 = NPC_ATK_Left_L2
        local6 = NPC_ATK_Right_L2
    end
    if SpaceCheck(arg0, arg1, -90, 5) == true then
        if SpaceCheck(arg0, arg1, 90, 5) == true then
            if local1 <= 50 then
                local4 = local5
            else
                local4 = local6
            end
        else
            local4 = local5
        end
    elseif SpaceCheck(arg0, arg1, 90, 5) == true then
        local4 = local6
    elseif arg0:GetStringIndexedNumber("IsUnreachMode") == 1 then
        if local1 <= 50 then
            local4 = local5
        else
            local4 = local6
        end
    end
    if local4 ~= NPC_ATK_NONE then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local4, TARGET_ENE_0, 999, 0, 0)
        arg0:SetTimer(6, 1)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act104(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9040) then
        local1 = true
    end
    local local2 = NPC_ATK_NONE
    local local3 = NPC_ATK_Down_ButtonXmark
    local local4 = NPC_ATK_DownLeft_ButtonXmark
    local local5 = NPC_ATK_DownRight_ButtonXmark
    if local1 == true then
        local3 = NPC_ATK_Down_L2
        local4 = NPC_ATK_DownLeft_L2
        local5 = NPC_ATK_DownRight_L2
    end
    if arg0:GetDist(TARGET_ENE_0) <= 1 and SpaceCheck(arg0, arg1, 180, 5) == true then
        local2 = local3
    elseif SpaceCheck(arg0, arg1, -135, 5) == true then
        if SpaceCheck(arg0, arg1, 135, 5) == true then
            if arg0:GetRandam_Int(1, 100) <= 50 then
                local2 = local4
            else
                local2 = local5
            end
        else
            local2 = local4
        end
    elseif SpaceCheck(arg0, arg1, 135, 5) == true then
        local2 = local5
    end
    if local2 ~= NPC_ATK_NONE or arg0:GetStringIndexedNumber("IsUnreachMode") == 1 then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 2, local2, TARGET_ENE_0, 999, 0, 0)
        arg0:SetTimer(6, 1)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act105(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetNPCActProb(9020)
    local local2 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L and arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local2 = true
    end
    if local2 == false then
        arg0:AddNPCActProb(9000)
        local1 = arg0:GetNPCActProb(9020)
    end
    local local3 = 0
    if SpaceCheck(arg0, arg1, -90, 1) == true then
        if SpaceCheck(arg0, arg1, 90, 1) == true then
            if arg0:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
                local3 = 0
            else
                local3 = 1
            end
        else
            local3 = 0
        end
    elseif SpaceCheck(arg0, arg1, 90, 1) == true then
        local3 = 1
    else
        GetWellSpace_Odds = 100
        return GetWellSpace_Odds
    end
    local local4 = -1
    if arg0:GetRandam_Int(1, 100) <= local1 then
        local4 = NPC_ATK_L1
    end
    arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 1, TARGET_ENE_0, local3, arg0:GetRandam_Int(75, 90), true, true, local4)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act106(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = 1.8
    local local2 = 7
    local local3 = arg0:GetNPCActProb(9020)
    local local4 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L and arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local4 = true
    end
    if local4 == false then
        arg0:AddNPCActProb(9000)
        local3 = arg0:GetNPCActProb(9020)
    end
    local local5 = -1
    if arg0:GetRandam_Int(1, 100) <= local3 then
        local5 = NPC_ATK_L1
    end
    if local2 <= arg0:GetDist(TARGET_ENE_0) and local5 == NPC_ATK_L1 then
        arg1:AddSubGoal(GOAL_COMMON_Guard, local1, local5, TARGET_ENE_0, true, true)
    else
        arg1:AddSubGoal(GOAL_COMMON_LeaveTarget, local1, TARGET_ENE_0, local2, TARGET_ENE_0, true, local5)
    end
    GetWellSpace_Odds = 100
    return GetWellSpace_Odds
end

function GeneralNPC_Act107(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetNPCActProb(9020)
    local local2 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L and arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local2 = true
    end
    if local2 == false then
        arg0:AddNPCActProb(9000)
        local1 = arg0:GetNPCActProb(9020)
    end
    local local3 = -1
    if arg0:GetRandam_Int(1, 100) <= local1 then
        local3 = NPC_ATK_L1
    end
    arg1:AddSubGoal(GOAL_COMMON_DashTarget, 3, TARGET_ENE_0, 2, TARGET_SELF, local3)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act108(arg0, arg1, arg2)
    arg1:AddSubGoal(GOAL_COMMON_Guard, 3, NPC_ATK_L1Hold, TARGET_ENE_0, GUARD_GOAL_DESIRE_RET_Continue, true)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act109(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0, 0, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    arg0:SetTimer(5, 7)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act110(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, AttDist, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, AttDist, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0, 0, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleL, TARGET_ENE_0, AttDist, 0, 0)
    end
    arg0:SetTimer(5, 7)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act111(arg0, arg1, arg2)
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, AttDist, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, AttDist, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_Wait, 0.5, TARGET_ENE_0, 0, 0, 0)
    end
    arg0:SetTimer(5, 7)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act112(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetNPCActProb(9020)
    local local2 = false
    if arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_R and arg0:GetWeaponBothHandState(TARGET_SELF) ~= ARM_L and arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local2 = true
    end
    if local2 == false then
        arg0:AddNPCActProb(9000)
        local1 = arg0:GetNPCActProb(9020)
    end
    local local3 = -1
    if arg0:GetRandam_Int(1, 100) <= local1 then
        local3 = NPC_ATK_L1
    end
    if arg0:GetRandam_Int(1, 100) <= 50 then
        isWalk = true
    end
    arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, TARGET_ENE_0, 15, TARGET_SELF, isWalk, local3)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act120(arg0, arg1, arg2)
    local local0 = arg0:GetRandam_Int(1, 100)
    local local1 = arg0:GetRandam_Int(1, 100)
    local local2 = arg0:GetDist(TARGET_ENE_0)
    local local3 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_First")
    local local4 = arg0:GetStringIndexedNumber("R_ComboNum_R1")
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
    end
    local local5 = 100
    local local6 = arg0:GetNPCActProb(9020)
    local local7 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local7 = true
    else
        local7 = false
    end
    if local7 == false then
        arg0:AddNPCActProb(9000)
        local6 = arg0:GetNPCActProb(9020)
    end
    NPC_Approach_Act_Flex(arg0, arg1, local3, local3 + 2, local3 + 2, 50, local6, 1.8, 2)
    if 6 <= local4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local4 == 5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local4 == 4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local4 == 3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local4 == 2 then
        arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local3, 0, 0)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act121(arg0, arg1, arg2)
    local local0 = arg0:GetDist(TARGET_ENE_0)
    local local1 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_First")
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        local1 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_First")
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        local1 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR1_First")
    end
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_L1Hold_R1, TARGET_ENE_0, local1, 0, 0, 0)
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act150(arg0, arg1, arg2)
    local local0 = GetRandomItemId_ByType(self, arg0, arg1, 20)
    ChangeEquipItem_ById(self, arg0, arg1, local0)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonSquare, TARGET_ENE_0, 999, 0, 0)
    if GetUsageId_X(arg0, arg0:GetAIUsageParam(1, local0)) == 2 then
        arg0:SetTimer(2, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act151(arg0, arg1, arg2)
    local local0 = GetRandomItemId_ByType(self, arg0, arg1, 30)
    ChangeEquipItem_ById(self, arg0, arg1, local0)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonSquare, TARGET_ENE_0, 999, 0, 0)
    if GetUsageId_X(arg0, arg0:GetAIUsageParam(1, local0)) == 2 then
        arg0:SetTimer(2, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act152(arg0, arg1, arg2)
    local local0 = GetRandomItemId_ByType(self, arg0, arg1, 31)
    ChangeEquipItem_ById(self, arg0, arg1, local0)
    local local1 = arg0:GetDist(TARGET_ENE_0)
    local local2 = 0
    local local3 = 0
    local local4 = arg0:GetNPCActProb(9020)
    local local5 = arg0:GetStringIndexedNumber("R_ComboNum_R1")
    local local6 = false
    local local7 = false
    local local8 = false
    if arg0:GetRandam_Int(1, 100) <= arg0:GetNPCActProb(9000) then
        local7 = true
    else
        local7 = false
    end
    if arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_R then
        if local7 == true then
            local8 = true
        elseif 1 <= local1 then
            arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local8 = false
        else
            local8 = true
        end
    elseif arg0:GetWeaponBothHandState(TARGET_SELF) == ARM_L then
        if local7 == true then
            arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            if 1 <= local1 then
                arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
                local8 = true
            else
                local8 = false
            end
        else
            arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local8 = false
        end
    elseif local7 == true then
        if 1 <= local1 then
            arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_ChangeStyleR, TARGET_ENE_0, 999, 0, 0)
            local8 = true
        else
            local8 = false
        end
    else
        local8 = false
    end
    if local8 == true then
        local2 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_First")
        local3 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_Second")
        local6 = false
    else
        local2 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_First")
        local3 = arg0:GetStringIndexedNumber("R_Dist_OneHandR1_Second")
        if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
            local6 = true
        else
            local6 = false
        end
    end
    if local6 == false then
        arg0:AddNPCActProb(9000)
        local4 = arg0:GetNPCActProb(9020)
    end
    local local9 = false
    if arg0:GetRandam_Int(1, 100) <= local4 then
        local9 = true
        local4 = 100
    end
    NPC_Approach_Act_Flex(arg0, arg1, local2, local2 + 2, local2 + 2, 50, local4, 1.8, 2)
    if local2 <= local1 and arg0:GetRandam_Int(1, 100) <= 50 and local9 == true then
        if arg0:IsInsideTargetCustom(TARGET_ENE_0, TARGET_SELF, AI_DIR_TYPE_L, 180, 180, 10) == true then
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 1, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        else
            arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 0.3, TARGET_ENE_0, 0, arg0:GetRandam_Int(75, 90), true, true, NPC_ATK_L1Hold)
        end
    end
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonSquare, TARGET_ENE_0, 999, 0, 0)
    if 6 <= local5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local5 == 5 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local5 == 4 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local5 == 3 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
    elseif local5 == 2 then
        arg1:AddSubGoal(GOAL_COMMON_ComboTunable_SuccessAngle180, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local3, 0, 0)
    else
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_R1, TARGET_ENE_0, local2, 0, 0)
    end
    if GetUsageId_X(arg0, arg0:GetAIUsageParam(1, local0)) == 2 then
        arg0:SetTimer(2, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act153(arg0, arg1, arg2)
    local local0 = GetRandomItemId_ByType(self, arg0, arg1, 10)
    ChangeEquipItem_ById(self, arg0, arg1, local0)
    Common_NPC_AI_GetItemUseDist(self, arg0, arg1, local0, 10)
    local local1 = arg0:GetStringIndexedNumber("Item_ApproachDist")
    local local2 = 100
    local local3 = arg0:GetNPCActProb(9020)
    local local4 = false
    if arg0:GetStringIndexedNumber("L_WeaponType") == 10 then
        local4 = true
    else
        local4 = false
    end
    if local4 == false then
        arg0:AddNPCActProb(9000)
        local3 = arg0:GetNPCActProb(9020)
    end
    if arg0:GetStringIndexedNumber("IsUnreachMode") == 0 then
        NPC_Approach_Act_Flex(arg0, arg1, local1, local1 + 2, local1 + 2, 50, local3, 1.8, 2)
    end
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonSquare, TARGET_ENE_0, 999, 0, 0)
    if GetUsageId_X(arg0, arg0:GetAIUsageParam(1, local0)) == 2 then
        arg0:SetTimer(2, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act154(arg0, arg1, arg2)
    local local0 = GetRandomItemId_ByType(self, arg0, arg1, 50)
    ChangeEquipItem_ById(self, arg0, arg1, local0)
    arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, NPC_ATK_ButtonSquare, TARGET_ENE_0, 999, 0, 0)
    arg0:SetTimer(4, 30)
    if GetUsageId_X(arg0, arg0:GetAIUsageParam(1, local0)) == 2 then
        arg0:SetTimer(2, 10)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act200(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 12)
    local local1 = 0
    if local0 == ARM_R then
        local1 = arg0:GetStringIndexedNumber("R_Dist_TwoHandR1_First")
    elseif local0 == ARM_L then
        local1 = arg0:GetStringIndexedNumber("L_Dist_TwoHandR1_First")
    end
    Common_NPC_AI_GetArtsUseDist(self, arg0, arg1, arg0:GetArtsID(local0), local1)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, arg0:GetStringIndexedNumber("Arts_ApproachDist"))
        arg0:SetTimer(3, 3)
    end
    return 
end

function GeneralNPC_Act210(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 11)
    Common_NPC_AI_GetArtsUseDist(self, arg0, arg1, arg0:GetArtsID(local0), 5)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, arg0:GetStringIndexedNumber("Arts_ApproachDist"))
        arg0:SetTimer(3, 3)
    end
    return 
end

function GeneralNPC_Act220(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 10)
    Common_NPC_AI_GetArtsUseDist(self, arg0, arg1, arg0:GetArtsID(local0), 12)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, arg0:GetStringIndexedNumber("Arts_ApproachDist"))
        arg0:SetTimer(3, 3)
    end
    return 
end

function GeneralNPC_Act230(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 20)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, 999)
        arg0:SetTimer(3, 3)
    end
    GetWellSpace_Odds = 0
    return GetWellSpace_Odds
end

function GeneralNPC_Act231(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 30)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, 999)
        arg0:SetTimer(3, 3)
    end
    return 
end

function GeneralNPC_Act232(arg0, arg1, arg2)
    local local0 = ChangeBothHand_ForArts(self, arg0, arg1, 50)
    if local0 ~= -1 then
        ArtsAction_ByCC(self, arg0, arg1, local0, 999)
        arg0:SetTimer(4, 30)
        arg0:SetTimer(3, 3)
    end
    return 
end

function GeneralNPC_Act_onNoSubGoal(arg0, arg1, arg2)
    if arg0:GetWeightType(TARGET_SELF) == AI_TARGET_WEIGHT_TYPE_WeightOver or arg0:GetSp(TARGET_SELF) < 0 then
        local local0 = AI_DIR_TYPE_ToR
        if arg0:GetRandam_Int(0, 1) == 1 then
            local0 = AI_DIR_TYPE_ToL
        end
        arg1:AddSubGoal(GOAL_COMMON_ApproachSettingDirection, 2, TARGET_ENE_0, 0.5, TARGET_SELF, false, -1, local0, 2)
    else
        local local0 = NPC_ATK_UpRight_ButtonXmark
        if arg0:GetRandam_Int(0, 1) == 1 then
            local0 = NPC_ATK_UpLeft_ButtonXmark
        end
        arg1:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, local0, TARGET_ENE_0, 999, 0, 0)
    end
    return 
end

function GeneralNPC_AdjustSpace(arg0, arg1, arg2)
    return 
end

return 
