from fastapi import FastAPI
# from routes.robot_router_template import router as robot_router_template
from routes.robot_router import router as robot_router

app = FastAPI(
    title="ZJS Robot Education API",
    description="面向教育机器人的后台服务接口",
    version="0.1.0"
)

# app.include_router(robot_router_template)
app.include_router(robot_router)

@app.get("/", tags=["Health Check"])
def read_root():
    return {"message": "Hello! 机器人服务正在运行中..."}