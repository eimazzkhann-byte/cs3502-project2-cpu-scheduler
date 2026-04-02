from models import ScheduleSummary


def calculate_metrics(summary: ScheduleSummary) -> dict:
    results = summary.results

    if not results:
        return {
            "Average Waiting Time": 0.0,
            "Average Turnaround Time": 0.0,
            "Average Response Time": 0.0,
            "CPU Utilization": 0.0,
            "Throughput": 0.0,
        }

    avg_waiting_time = sum(r.waiting_time for r in results) / len(results)
    avg_turnaround_time = sum(r.turnaround_time for r in results) / len(results)
    avg_response_time = sum(r.response_time for r in results) / len(results)

    total_burst_time = sum(r.burst_time for r in results)
    total_elapsed_time = max(r.finish_time for r in results)

    cpu_utilization = (total_burst_time / total_elapsed_time * 100) if total_elapsed_time > 0 else 0.0
    throughput = (len(results) / total_elapsed_time) if total_elapsed_time > 0 else 0.0

    return {
        "Average Waiting Time": avg_waiting_time,
        "Average Turnaround Time": avg_turnaround_time,
        "Average Response Time": avg_response_time,
        "CPU Utilization": cpu_utilization,
        "Throughput": throughput,
    }
