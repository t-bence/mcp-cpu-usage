import psutil
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SecretServer")


@mcp.tool()
def get_secret_number() -> int:
    """Returns a predefined secret number."""
    return 13


@mcp.tool()
def list_processes_cpu_usage() -> dict:
    """Lists processes and their CPU usage."""
    processes = {}
    for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
        try:
            info = proc.info
            processes[info["pid"]] = {
                "name": info["name"],
                "cpu_percent": info["cpu_percent"],
            }
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
