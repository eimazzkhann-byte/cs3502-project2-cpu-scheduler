def print_results_table(summary, metrics):
    print(f"\nAlgorithm: {summary.algorithm}")
    print("-" * 90)
    print(f"{'PID':<6}{'Arr':<6}{'Burst':<8}{'Prio':<8}{'Start':<8}{'Finish':<8}{'Wait':<8}{'Turn':<8}{'Resp':<8}")
    print("-" * 90)

    for r in summary.results:
        print(f"{r.pid:<6}{r.arrival_time:<6}{r.burst_time:<8}{r.priority:<8}{r.start_time:<8}{r.finish_time:<8}{r.waiting_time:<8}{r.turnaround_time:<8}{r.response_time:<8}")

    print("-" * 90)
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")


def print_gantt(summary):
    print("\nGantt Chart:")
    for pid, start, end in summary.gantt:
        print(f"[{pid}: {start}->{end}]", end=" ")
    print("\n")
