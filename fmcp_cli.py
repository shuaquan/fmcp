'''
fastmcp 的客户端 
使用fastmcp 的客户端 连接到 fmcp 服务 
调用 时间工具 获取当前时间 
'''

import asyncio
from fastmcp import Client  

'''
服务端使用 8090 端口, 本机启动, transport 使用 http
默认mcp启动的时候, 后缀为/mcp 需要再服务器nginx上进行配置.
'''

client = Client("https://returnx.cn/mcp")

# 调用 时间工具 获取当前时间 



async def main():
    async with client:
        # Basic server interaction
        await client.ping()
        
        # List available operations
        tools = await client.list_tools()
        print(tools)
        resources = await client.list_resources()
        print(resources)
        prompts = await client.list_prompts()
        print(prompts)
        
        # Execute operations
        result = await client.call_tool("get_current_time")
        print(result)

        result = await client.call_tool("get_hello_world", "world")
        print(result)

asyncio.run(main())