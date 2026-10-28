# # 从 hardware 文件夹引入 driver
# from hardware.aimdk_driver_template import aimdk_driver
#
# class RobotService:
#     async def do_wave(self, motion_id: int):
#         # 调用 driver
#         return await aimdk_driver.perform_preset_motion(motion_id)
#
#     async def do_speak(self, text: str):
#         return await aimdk_driver.play_tts(text)
#
# robot_service = RobotService()