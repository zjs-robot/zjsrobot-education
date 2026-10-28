# from fastapi import APIRouter
# from pydantic import BaseModel
# from services.robot_service_template import robot_service
#
# router = APIRouter(prefix="/robot", tags=["Robot"])
#
# class ActionRequest(BaseModel):
#     motion_id: int
#
# @router.post("/wave")
# async def robot_wave(req: ActionRequest):
#     return await robot_service.do_wave(req.motion_id)
#
# @router.post("/speak")
# async def robot_speak(text: str):
#     return await robot_service.do_speak(text)