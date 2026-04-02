def print_results_table(summary, metrics):
    print(f"\nAlgorithm: {summary.algorithm}")
    print("-" * 95)
    print(f"{'PID':<6}{'Arr':<6}{'Burst':<8}{'Prio':<8}{'Start':<8}{'Finish':<8}{'Wait':<8}{'Turn':<8}{'Resp':<8}")
    print("-" * 95)

    for r in summary.results:
        print(
            f"{r.pid:<6}{r.arrival_time:<6}{r.burst_time:<8}{r.priority:<8}"
            f"{r.start_time:<8}{r.finish_time:<8}{r.waiting_time:<8}"
            f"{r.turnaround_time:<8}{r.response_time:<8}"
        )

    print("-" * 95)
    for key, value in metrics.items():
        print(f"{key}: {value:.2f}")


def print_gantt(summary):
    print("\nGantt Chart:")
    for pid, start, end in summary.gantt:
        print(f"[{pid}: {start}->{end}]", end=" ")
    print("\n")


def print_comparison_table(comparison_rows):
    print("\nAlgorithm Comparison")
    print("-" * 90)
    print(f"{'Algorithm':<12}{'AWT':<12}{'ATT':<12}{'ART':<12}{'CPU %':<12}{'Throughput':<12}")
    print("-" * 90)

    for row in comparison_rows:
        print(
            f"{row['Algorithm']:<12}"
            f"{row['Average Waiting Time']:<12.2f}"
            f"{row['Average Turnaround Time']:<12.2f}"
            f"{row['Average Response Time']:<12.2f}"
            f"{row['CPU Utilization']:<12.2f}"
            f"{row['Throughput']:<12.2f}"
        )

    print("-" * 90)
