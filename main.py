from cpu_usage.server import CPUUsageTool

if __name__ == "__main__":
    cpu_tool = CPUUsageTool(wait_time=0.5, top_n=3)

    print(cpu_tool.list_usage())
