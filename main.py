from cpu_usage import server

if __name__ == "__main__":
    for proc in server.list_processes_cpu_usage():
        if proc.percent:
            print(f"{proc.name}:{proc.percent:>8}")
