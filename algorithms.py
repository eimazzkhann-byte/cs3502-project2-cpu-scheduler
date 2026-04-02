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


def sjf(processes):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    time = 0
    completed = set()
    results = []
    gantt = []

    while len(completed) < len(processes):
        available = [p for p in processes if p.arrival_time <= time and p.pid not in completed]

        if not available:
            next_arrival = min(p.arrival_time for p in processes if p.pid not in completed)
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        current = min(available, key=lambda p: (p.burst_time, p.arrival_time, p.pid))

        start_time = time
        finish_time = time + current.burst_time
        waiting_time = start_time - current.arrival_time
        turnaround_time = finish_time - current.arrival_time
        response_time = start_time - current.arrival_time

        results.append(
            ProcessResult(
                pid=current.pid,
                arrival_time=current.arrival_time,
                burst_time=current.burst_time,
                priority=current.priority,
                start_time=start_time,
                finish_time=finish_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                response_time=response_time,
            )
        )

        gantt.append((current.pid, start_time, finish_time))
        time = finish_time
        completed.add(current.pid)

    results.sort(key=lambda r: r.pid)
    return ScheduleSummary("SJF", results, gantt)


def priority_non_preemptive(processes):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    time = 0
    completed = set()
    results = []
    gantt = []

    while len(completed) < len(processes):
        available = [p for p in processes if p.arrival_time <= time and p.pid not in completed]

        if not available:
            next_arrival = min(p.arrival_time for p in processes if p.pid not in completed)
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        current = min(available, key=lambda p: (p.priority, p.arrival_time, p.pid))

        start_time = time
        finish_time = time + current.burst_time
        waiting_time = start_time - current.arrival_time
        turnaround_time = finish_time - current.arrival_time
        response_time = start_time - current.arrival_time

        results.append(
            ProcessResult(
                pid=current.pid,
                arrival_time=current.arrival_time,
                burst_time=current.burst_time,
                priority=current.priority,
                start_time=start_time,
                finish_time=finish_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                response_time=response_time,
            )
        )

        gantt.append((current.pid, start_time, finish_time))
        time = finish_time
        completed.add(current.pid)

    results.sort(key=lambda r: r.pid)
    return ScheduleSummary("Priority", results, gantt)


def round_robin(processes, quantum=2):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    remaining = {p.pid: p.burst_time for p in processes}
    first_start = {}
    finish_times = {}
    queue = deque()
    gantt = []
    time = 0
    i = 0

    while i < len(processes) or queue:
        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            if i < len(processes):
                next_time = processes[i].arrival_time
                gantt.append(("IDLE", time, next_time))
                time = next_time
                continue

        current = queue.popleft()

        if current.pid not in first_start:
            first_start[current.pid] = time

        run_time = min(quantum, remaining[current.pid])
        start = time
        end = time + run_time
        gantt.append((current.pid, start, end))

        time = end
        remaining[current.pid] -= run_time

        while i < len(processes) and processes[i].arrival_time <= time:
            queue.append(processes[i])
            i += 1

        if remaining[current.pid] > 0:
            queue.append(current)
        else:
            finish_times[current.pid] = time

    results = []
    for p in processes:
        start_time = first_start[p.pid]
        finish_time = finish_times[p.pid]
        turnaround_time = finish_time - p.arrival_time
        waiting_time = turnaround_time - p.burst_time
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

    results.sort(key=lambda r: r.pid)
    return ScheduleSummary(f"RR(q={quantum})", results, gantt)


def srtf(processes):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    remaining = {p.pid: p.burst_time for p in processes}
    first_start = {}
    finish_times = {}
    gantt = []
    time = 0
    done = set()

    while len(done) < len(processes):
        available = [p for p in processes if p.arrival_time <= time and p.pid not in done]

        if not available:
            next_arrival = min(p.arrival_time for p in processes if p.pid not in done)
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        current = min(available, key=lambda p: (remaining[p.pid], p.arrival_time, p.pid))

        if current.pid not in first_start:
            first_start[current.pid] = time

        start = time
        time += 1
        remaining[current.pid] -= 1
        end = time

        if gantt and gantt[-1][0] == current.pid and gantt[-1][2] == start:
            gantt[-1] = (gantt[-1][0], gantt[-1][1], end)
        else:
            gantt.append((current.pid, start, end))

        if remaining[current.pid] == 0:
            finish_times[current.pid] = time
            done.add(current.pid)

    results = []
    for p in processes:
        start_time = first_start[p.pid]
        finish_time = finish_times[p.pid]
        turnaround_time = finish_time - p.arrival_time
        waiting_time = turnaround_time - p.burst_time
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

    results.sort(key=lambda r: r.pid)
    return ScheduleSummary("SRTF", results, gantt)


def hrrn(processes):
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.pid))
    time = 0
    completed = set()
    results = []
    gantt = []

    while len(completed) < len(processes):
        available = [p for p in processes if p.arrival_time <= time and p.pid not in completed]

        if not available:
            next_arrival = min(p.arrival_time for p in processes if p.pid not in completed)
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        def response_ratio(p):
            waiting = time - p.arrival_time
            return (waiting + p.burst_time) / p.burst_time

        current = max(available, key=lambda p: (response_ratio(p), -p.arrival_time, p.pid))

        start_time = time
        finish_time = time + current.burst_time
        waiting_time = start_time - current.arrival_time
        turnaround_time = finish_time - current.arrival_time
        response_time = start_time - current.arrival_time

        results.append(
            ProcessResult(
                pid=current.pid,
                arrival_time=current.arrival_time,
                burst_time=current.burst_time,
                priority=current.priority,
                start_time=start_time,
                finish_time=finish_time,
                waiting_time=waiting_time,
                turnaround_time=turnaround_time,
                response_time=response_time,
            )
        )

        gantt.append((current.pid, start_time, finish_time))
        time = finish_time
        completed.add(current.pid)

    results.sort(key=lambda r: r.pid)
    return ScheduleSummary("HRRN", results, gantt)
