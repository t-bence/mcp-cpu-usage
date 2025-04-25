import time

import psutil
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("SecretServer")


@mcp.tool()
def get_secret_number() -> int:
    """Returns a predefined secret number."""
    return 13


from dataclasses import dataclass


@dataclass
class ProcessInfo:
    name: str
    percent: float


@mcp.tool()
def list_processes_cpu_usage() -> list[ProcessInfo]:
    """Lists processes and their CPU usage."""
    processes: list[ProcessInfo] = []
    # You need to call the process listing TWICE! The first will return 0.0
    # for all CPU times, only the second will retrieve true values.
    # You also need to wait at least 0.1 s between the two calls.
    psutil.process_iter(["pid", "name", "cpu_percent", "cpu_times"])
    time.sleep(0.2)
    for proc in psutil.process_iter(["pid", "name", "cpu_percent", "cpu_times"]):
        try:
            processes.append(ProcessInfo(proc.name(), proc.cpu_percent()))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return processes
