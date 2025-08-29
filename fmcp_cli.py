'''
fastmcp 的客户端 
使用fastmcp 的客户端 连接到 fmcp 服务 
调用 时间工具 获取当前时间 
'''

from fastmcp import Client  

'''
服务端使用 8090 端口, 本机启动, transport 使用 http , ip为 101.200.223.19 
'''

mcp = Client(
    host='101.200.223.19',
    port=8090,
    transport='http'
)

# 调用 时间工具 获取当前时间 
current_time = mcp.get_current_time()
print(current_time)



