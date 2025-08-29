'''
使用fastmcp 实现一个fmcp 服务 
'''

import time
from fastmcp import FastMCP


mcp = FastMCP('dust_mcp_server')
''' 
构建mcp服务, 并启动 
该mcp服务包含以下tools: 
1, 获取当前时间
''' 

# tools 1: 获取当前时间
@mcp.tool
def get_current_time() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#mcp.tool 
def get_hello_world(input: str) -> str:
    return f"hello {input}"

# 启动 mcp 服务, 监听8087端口, 本机启动, transport 使用http
mcp.run(port=8090, host="127.0.0.1", transport="http")












