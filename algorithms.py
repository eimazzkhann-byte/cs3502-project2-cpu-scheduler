from collections import deque
from models import ProcessResult, ScheduleSummary


def fcfs(processes):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    time = 0
    results = []
    gantt = []

    for p in processes:
        if time < p.arrival_time:
            gantt.append(("IDLE", time, p.arrival_time))
            time = p.arrival_time

        start_time = time
        finish_time = start_time + p.burst_time
        waiting_time = start_time - p.arrival_time
        turnaround_time = finish_time - p.arrival_time
        response_time = start_time - p.arrival_time

        results.append(
            ProcessResult(
                pid=p.pid,
                arrival_time=p.arrival_time,
                burst_time=p.burst_time,
                priority=p.priority,
                start_time=start_time,
                finish_time=finish_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                response_time=response_time,
            )
        )

        gantt.append((p.pid, start_time, finish_time))
        time = finish_time

    return ScheduleSummary("FCFS", results, gantt)
