'''
使用fastmcp 实现一个fmcp 服务 
'''

import time
from fastmcp import FastMCP
from pydantic import Field


mcp = FastMCP('dust_mcp_server')
''' 
构建mcp服务, 并启动 
该mcp服务包含以下tools: 
1, 获取当前时间
''' 

# tools 1: 获取当前时间
@mcp.tool
async def get_current_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@mcp.tool 
async def get_hello_world(name: str=Field(description="name of the user")) -> str:
    return f"hello {name}"

# 启动 mcp 服务, 监听8087端口, 本机启动, transport 使用http
mcp.run(port=8090, host="127.0.0.1", transport="http")












