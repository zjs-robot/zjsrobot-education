import asyncio

# 尝试导入 ROS 2 及其消息，如果在你 Windows 电脑上会失败，我们捕获它
try:
    import rclpy
    from rclpy.node import Node
    from aimdk_msgs.srv import SetMcPresetMotion
    from aimdk_msgs.msg import McPresetMotion, McControlArea, RequestHeader

    ROS2_AVAILABLE = True
except ImportError:
    ROS2_AVAILABLE = False
    print("警告: 当前环境没有 ROS 2 或 AimDK，使用模拟数据。")


class RealAimDKDriver:
    def __init__(self):
        self.node = None
        if ROS2_AVAILABLE:
            # 真正的初始化逻辑（在 Ubuntu 上才执行）
            rclpy.init()
            self.node = Node('fastapi_aimdk_driver')
            self.client = self.node.create_client(
                SetMcPresetMotion, '/aimdk_5Fmsgs/srv/SetMcPresetMotion')
        else:
            print("Mock 模式已启动")

    async def perform_preset_motion(self, motion_id: int) -> dict:
        """执行预设动作，比如挥手"""
        # 根据官方文档：1-left, 2-right; 1001-raise, 1002-wave, 1003-handshake, 1004-airkiss
        area_id = 2  # 默认右手
        if not ROS2_AVAILABLE or self.node is None:
            await asyncio.sleep(0.5)
            return {"status": "mock_success", "action": "wave", "motion_id": motion_id}

        # --- 以下代码只会在有 ROS 2 的 Ubuntu 环境执行 ---
        req = SetMcPresetMotion.Request()
        req.header = RequestHeader()
        req.input_source.name = 'fastapi_aimdk'
        req.input_source.priority = 40
        req.input_source.timeout = 1000

        motion = McPresetMotion()
        area = McControlArea()
        motion.value = motion_id
        area.value = area_id
        req.motion = motion
        req.area = area

        # 异步等待服务
        if not self.client.wait_for_service(timeout_sec=2.0):
            return {"status": "error", "message": "AimDK Service Unavailable"}

        req.header.stamp = self.node.get_clock().now().to_msg()
        future = self.client.call_async(req)
        # 简化处理，实际上需要 spin_until_future_complete
        return {"status": "sent_command", "motion_id": motion_id}

    async def play_tts(self, text: str) -> dict:
        # 这里的 TTS 需要配合 AimDK 的语音模块，目前保持 Mock
        await asyncio.sleep(0.3)
        return {"status": "success", "text": text, "mock": True}


aimdk_driver = RealAimDKDriver()