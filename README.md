# CS 3502 Project 2 CPU Scheduling Simulator

Python console app for CPU scheduling simulation and performance analysis.

## Platform Tested On
Ubuntu running in Oracle VirtualBox on a Windows 11 host.

## Dependencies
- Python 3
- Standard library only

## Included Algorithms
- FCFS
- SJF
- Priority Scheduling
- Round Robin
- SRTF
- HRRN

## Features
- Run built-in verification, CPU-bound, I/O-bound, and mixed workloads
- Enter custom process data manually from the console
- Run one algorithm at a time or compare all algorithms on the same workload
- Show per-process metrics and a simple Gantt chart
- Run a Round Robin quantum experiment using q = 1, 2, 4, 8, and 20

## Project Structure
- `main.py` - menu flow and workload selection
- `models.py` - data classes
- `algorithms.py` - scheduler implementations
- `metrics.py` - performance metric calculations
- `workloads.py` - built-in workloads
- `utils.py` - console formatting helpers

## Run Instructions
```bash
python3 main.py
```

## Notes
This project was built from scratch as a Python console application. That approach is allowed by the assignment as long as the simulator includes correct algorithm implementations, a way to input process data, metric calculation, comparison capability, and clear documentation.
