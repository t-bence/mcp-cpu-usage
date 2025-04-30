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


class CPUUsageTool:
    def __init__(self, wait_time: float = 0.5, top_n: int = 3):
        """
        Initializes the CPUUsageTool.

        :param wait_time: Time to wait between CPU usage checks (in seconds).
        :param top_n: Number of top processes to display based on CPU usage.
        """
        self.wait_time = wait_time
        self.top_n = top_n

    @mcp.tool()
    def list_usage(self) -> str:
        """Lists processes and their CPU usage."""
        processes: list[ProcessInfo] = []
        # You need to call the process listing TWICE! The first will return 0.0
        # for all CPU times, only the second will retrieve true values.
        # You also need to wait at least 0.1 s between the two calls.
        psutil.process_iter(["pid", "name", "cpu_percent", "cpu_times"])
        time.sleep(self.wait_time)
        for proc in psutil.process_iter(["pid", "name", "cpu_percent", "cpu_times"]):
            try:
                processes.append(ProcessInfo(proc.name(), proc.cpu_percent()))
            except (
                psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
            ):
                continue

        best_processes = sorted(processes, key=lambda x: x.percent, reverse=True)[
            : self.top_n
        ]
        return "\n".join(f"{proc.name}: {proc.percent:.2f}%" for proc in best_processes)
