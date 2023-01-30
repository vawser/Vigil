function Platoon005006_Initialize(arg0)
    arg0:SetEnablePlatoonMove(true)
    arg0:SetFormationType(0, 2)
    arg0:SetFormationParam(0, 0, 0)
    arg0:SetFormationParam(1, 0, 0)
    arg0:SetFormationParam(2, 2, -2)
    arg0:SetFormationParam(3, -2, -3)
    arg0:SetFormationParam(4, 1, -5)
    
    arg0:SetBaseMoveRate(0, 10)
    arg0:SetBaseMoveRate(1, 10)
    arg0:SetBaseMoveRate(2, 10)
    arg0:SetBaseMoveRate(3, 10)
    arg0:SetBaseMoveRate(4, 10)
    
    return 
end

function Platoon005006_Activate(arg0)
    return 
end

function Platoon005006_Deactivate(arg0)
    return 
end

function Platoon005006_Update(arg0)
    Platoon_Common_Act(arg0, 1)
    return 
end

return 
