from models import Process


def verification_fcfs_case():
    return [
        Process("P1", arrival_time=0, burst_time=4, priority=1),
        Process("P2", arrival_time=1, burst_time=3, priority=2),
        Process("P3", arrival_time=2, burst_time=2, priority=3),
    ]


def small_mixed_workload():
    return [
        Process("P1", 0, 8, 2),
        Process("P2", 1, 4, 1),
        Process("P3", 2, 9, 3),
        Process("P4", 3, 5, 2),
    ]


def cpu_bound_workload():
    return [
        Process("P1", 0, 18, 2),
        Process("P2", 0, 14, 1),
        Process("P3", 0, 20, 3),
        Process("P4", 0, 16, 2),
        Process("P5", 0, 12, 1),
    ]


def io_bound_workload():
    return [
        Process("P1", 0, 2, 2),
        Process("P2", 1, 1, 1),
        Process("P3", 2, 3, 3),
        Process("P4", 3, 2, 2),
        Process("P5", 4, 1, 1),
    ]


def mixed_workload():
    return [
        Process("P1", 0, 12, 3),
        Process("P2", 1, 2, 1),
        Process("P3", 2, 7, 2),
        Process("P4", 4, 1, 1),
        Process("P5", 6, 10, 4),
        Process("P6", 8, 3, 2),
    ]
