function Horse_800000_Logic(arg0)
    if arg0:IsSearchTarget(TARGET_LOCALPLAYER) == true then
        if 30 <= arg0:GetDist(TARGET_LOCALPLAYER) then
            arg0:AddTopGoal(GOAL_COMMON_ApproachTarget, 15, TARGET_LOCALPLAYER, 6, TARGET_SELF, false, -1)
        else
            arg0:AddTopGoal(GOAL_COMMON_Wait, 1, TARGET_NONE)
        end
    end
    return 
end

function Horse_800000_Interupt(arg0, arg1)
    return false
end

return 
