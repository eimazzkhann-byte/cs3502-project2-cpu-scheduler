from algorithms import fcfs
from metrics import calculate_metrics
from utils import print_results_table, print_gantt
from workloads import verification_fcfs_case


def main():
    processes = verification_fcfs_case()
    summary = fcfs(processes)
    metrics = calculate_metrics(summary)

    print_results_table(summary, metrics)
    print_gantt(summary)


if __name__ == "__main__":
    main()
