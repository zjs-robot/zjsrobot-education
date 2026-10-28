from fastapi import APIRouter
from pydantic import BaseModel
from services.robot_service import robot_service

router = APIRouter(prefix="/robot", tags=["Robot"])

class ActionRequest(BaseModel):
    motion_id: int # 1002:挥手 1003: 握手

@router.post("/wave")
async def robot_wave(req: ActionRequest):
    return await robot_service.do_wave(req.motion_id)