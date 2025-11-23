"""
File: health_record.py
Description: Defines the HealthRecord class, representing health issues for zoo animals.
Author: Erica Box
ID: 110468687
Username: boxey001
This is my own work as defined by the University's Academic Integrity Policy.
"""


from datetime import date


class HealthRecord:
    """
    Represents a single documented health issue for an animal, such as an
    injury, illness, or behavioral concern. Each record includes a description,
    severity, date of the report, and treatment plan.
    """

    # Allowed issue types
    VALID_ISSUE_TYPES = ("injury", "illness", "behavioural")

    # ===============================
    #   CONSTRUCTOR AND ATTRIBUTES
    # ===============================
    def __init__(
        self,
        issue_type: str,
        description: str,
        severity: int,
        report_date: date | None = None,
        treatment_plan: str = "",
        notes: str = ""
    ):

        # Validate the issue type.
        if issue_type not in self.VALID_ISSUE_TYPES:
            raise ValueError(f"Issue type must be one of {self.VALID_ISSUE_TYPES}.")

        # Validate the severity. Must be between 1 and 5.
        if not (1 <= severity <= 5):
            raise ValueError("Severity must be between 1 and 5.")

        # Assign record details
        self.issue_type = issue_type
        self.description = description
        self.severity = severity

        # Use today's date if no report date is provided
        self.report_date = report_date or date.today()

        self.treatment_plan = treatment_plan
        self.notes = notes

    # ===============================
    #  STRING REPRESENTATION METHOD
    # ===============================

    def __str__(self):
        """Returns a human-readable string representation of the record."""
        return (
            f"[{self.report_date}] {self.issue_type.title()} "
            f"(Severity {self.severity}): {self.description}"
        )

