from mcp.server.fastmcp import FastMCP

mcp = FastMCP("greetings")


@mcp.tool()
def greeting(name:str) -> str:
    "Send a greetings"
    return f"Hello {name}, Have a Nice day! :)"


if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)