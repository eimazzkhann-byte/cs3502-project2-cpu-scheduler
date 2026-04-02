from algorithms import fcfs, sjf, priority_non_preemptive, round_robin, srtf, hrrn
from metrics import calculate_metrics
from utils import print_results_table, print_gantt, print_comparison_table
from workloads import (
    verification_fcfs_case,
    small_mixed_workload,
    cpu_bound_workload,
    io_bound_workload,
    mixed_workload,
)
from models import Process


def manual_input_workload():
    print("\nManual Process Entry")
    print("Enter process data as integers for arrival time, burst time, and priority.")
    count = int(input("How many processes? ").strip())
    processes = []

    for i in range(count):
        print(f"\nProcess {i + 1}")
        pid = input("PID: ").strip()
        arrival = int(input("Arrival Time: ").strip())
        burst = int(input("Burst Time: ").strip())
        priority = int(input("Priority: ").strip())
        processes.append(Process(pid, arrival, burst, priority))

    return processes, "Manual Input Workload"


def get_workload(choice):
    if choice == "1":
        return verification_fcfs_case(), "Verification FCFS Case"
    if choice == "2":
        return small_mixed_workload(), "Small Mixed Workload"
    if choice == "3":
        return cpu_bound_workload(), "CPU-Bound Workload"
    if choice == "4":
        return io_bound_workload(), "I/O-Bound Workload"
    if choice == "5":
        return mixed_workload(), "Mixed Workload"
    if choice == "6":
        return manual_input_workload()
    return None, None


def run_single_algorithm(processes, choice):
    if choice == "1":
        return fcfs(processes)
    if choice == "2":
        return sjf(processes)
    if choice == "3":
        return priority_non_preemptive(processes)
    if choice == "4":
        quantum = int(input("Enter time quantum: ").strip())
        return round_robin(processes, quantum=quantum)
    if choice == "5":
        return srtf(processes)
    if choice == "6":
        return hrrn(processes)
    return None


def compare_all(processes):
    summaries = [
        fcfs(processes),
        sjf(processes),
        priority_non_preemptive(processes),
        round_robin(processes, quantum=2),
        srtf(processes),
        hrrn(processes),
    ]

    comparison_rows = []
    for summary in summaries:
        metrics = calculate_metrics(summary)
        comparison_rows.append({
            "Algorithm": summary.algorithm,
            **metrics,
        })

    print_comparison_table(comparison_rows)


def round_robin_quantum_experiment(processes):
    quanta = [1, 2, 4, 8, 20]
    rows = []

    for q in quanta:
        summary = round_robin(processes, quantum=q)
        metrics = calculate_metrics(summary)
        rows.append({
            "Algorithm": f"RR(q={q})",
            **metrics,
        })

    print_comparison_table(rows)


def main():
    while True:
        print("\nCPU Scheduling Simulator")
        print("1. Verification FCFS Case")
        print("2. Small Mixed Workload")
        print("3. CPU-Bound Workload")
        print("4. I/O-Bound Workload")
        print("5. Mixed Workload")
        print("6. Manual Input Workload")
        print("0. Exit")

        workload_choice = input("Choose a workload: ").strip()

        if workload_choice == "0":
            print("Exiting.")
            break

        processes, workload_name = get_workload(workload_choice)

        if not processes:
            print("Invalid workload choice.")
            continue

        print(f"\nSelected: {workload_name}")
        print("1. FCFS")
        print("2. SJF")
        print("3. Priority")
        print("4. Round Robin")
        print("5. SRTF")
        print("6. HRRN")
        print("7. Compare All")
        print("8. Round Robin Quantum Experiment")

        algo_choice = input("Choose an option: ").strip()

        if algo_choice == "7":
            compare_all(processes)
            continue

        if algo_choice == "8":
            round_robin_quantum_experiment(processes)
            continue

        summary = run_single_algorithm(processes, algo_choice)

        if not summary:
            print("Invalid algorithm choice.")
            continue

        metrics = calculate_metrics(summary)
        print_results_table(summary, metrics)
        print_gantt(summary)


if __name__ == "__main__":
    main()
