from dataclasses import dataclass
from typing import Optional


@dataclass
class Process:
    pid: str
    arrival_time: int
    burst_time: int
    priority: int = 0


@dataclass
class ProcessResult:
    pid: str
    arrival_time: int
    burst_time: int
    priority: int
    start_time: int
    finish_time: int
    waiting_time: int
    turnaround_time: int
    response_time: int


@dataclass
class ScheduleSummary:
    algorithm: str
    results: list[ProcessResult]
    gantt: list[tuple[str, int, int]]
