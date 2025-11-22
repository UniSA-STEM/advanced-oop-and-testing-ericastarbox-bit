"""
File: health_record.py
Description: A brief description of this Python module.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""
# health_record.py

from datetime import date

class HealthRecord:
    """
    Represents a single health issue for an animal, such as an injury,
    illness, or behavioural concern.
    """

    VALID_ISSUE_TYPES = ("injury", "illness", "behavioural")

    def __init__(
        self,
        issue_type: str,
        description: str,
        severity: int,
        report_date: date | None = None,
        treatment_plan: str = "",
        notes: str = ""
    ):
        if issue_type not in self.VALID_ISSUE_TYPES:
            raise ValueError(f"Issue type must be one of {self.VALID_ISSUE_TYPES}.")

        if not (1 <= severity <= 5):
            raise ValueError("Severity must be between 1 and 5.")

        self.issue_type = issue_type
        self.description = description
        self.severity = severity
        self.report_date = report_date or date.today()
        self.treatment_plan = treatment_plan
        self.notes = notes

    def __str__(self):
        return (
            f"[{self.report_date}] {self.issue_type.title()} "
            f"(Severity {self.severity}): {self.description}"
        )

