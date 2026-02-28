from mcp.server.fastmcp import FastMCP
from mcp.server.transports.streamable_http import StreamableHTTPTransport

mcp = FastMCP("greetings")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greetings"
    return f"Hello {name}, Have a Nice day! :)"

if __name__ == "__main__":
    transport = StreamableHTTPTransport(
        host="0.0.0.0",
        port=8000
    )
    mcp.run(transport=transport)