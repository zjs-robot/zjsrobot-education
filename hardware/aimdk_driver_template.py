# import asyncio
#
# class MockAimDKDriver:  # 改名
#     async def perform_preset_motion(self, motion_id: int) -> dict:
#         await asyncio.sleep(0.5)
#         return {"status": "success", "motion_id": motion_id, "mock": True}
#
#     async def play_tts(self, text: str) -> dict:
#         await asyncio.sleep(0.3)
#         return {"status": "success", "text": text, "mock": True}
#
# aimdk_driver = MockAimDKDriver()