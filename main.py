import os
from typing import Any
import httpx2
from mcp.server import MCPServer
from tavily import TavilyClient
from dotenv import load_dotenv
# Initialize MCPServer

load_dotenv()
mcp = MCPServer("content_mcp")

@mcp.tool()
def doc_search(topic: str)->str:
    """web search tool to search content"""
    tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    response = tavily_client.search(query=topic,
        include_answer="advanced",
        search_depth="advanced")
    return response.get("answer")



if __name__ == "__main__":
    mcp.run(transport="stdio")
