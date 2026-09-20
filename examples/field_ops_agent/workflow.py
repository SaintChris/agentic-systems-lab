#!/usr/bin/env python3
import re
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class FieldNote:
    raw: str
    location: str = ""
    issue: str = ""
    parts_used: list = field(default_factory=list)
    time_spent_minutes: int = 0
    customer_sentiment: str = ""
    follow_up_needed: bool = False


@dataclass
class JobReport:
    job_id: str
    location: str
    issue: str
    parts_used: list
    time_spent_minutes: int
    completed_at: str
    customer_sentiment: str
    summary: str


@dataclass
class FollowUpTask:
    description: str
    priority: str = "medium"


SAMPLE_NOTES = [
    'Customer at 123 Main St reported a leaking pipe. Used 2x 1/2" PVC pipe and sealant. Spent 45 minutes. Customer was upset but appreciative after fix.',
    "Site: 45 Oak Avenue. Broken window latch. Replaced latch. 30 mins. Customer happy.",
    "Location: 78 Pine Rd. Air conditioner not cooling. Checked filter, cleaned. 20 mins. Customer neutral.",
]


def _line_value(note: str, label: str) -> str:
    match = re.search(rf"(?im)^\s*{re.escape(label)}\s*:\s*(.+?)\s*$", note)
    return match.group(1).strip() if match else ""


def parse_note(note: str) -> FieldNote:
    parsed = FieldNote(raw=note)

    parsed.location = _line_value(note, "Location") or _line_value(note, "Site")
    if not parsed.location:
        match = re.search(r"(?i)customer at\s+(.+?)\s+reported", note)
        if match:
            parsed.location = match.group(1).strip().rstrip(".")

    parsed.issue = _line_value(note, "Issue")
    if not parsed.issue:
        match = re.search(r"(?i)reported (?:a|an)?\s*(.+?)\.(?:\s|$)", note)
        if not match:
            match = re.search(r"(?i)broken\s+(.+?)\.(?:\s|$)", note)
        if match:
            parsed.issue = match.group(1).strip()

    parts_text = _line_value(note, "Parts Used")
    if parts_text:
        parsed.parts_used = [p.strip() for p in parts_text.split(",") if p.strip()]
    else:
        match = re.search(r"(?i)used\s+(.+?)\.\s*(?:spent|customer|$)", note)
        if match:
            parsed.parts_used = [
                p.strip()
                for p in re.split(r",|\band\b", match.group(1))
                if p.strip()
            ]

    time_text = _line_value(note, "Time Spent")
    time_source = time_text or note
    match = re.search(r"(?i)(\d+)\s*(?:min|mins|minute|minutes)", time_source)
    if match:
        parsed.time_spent_minutes = int(match.group(1))

    sentiment_match = re.search(
        r"(?i)customer (?:was\s+)?(upset|happy|neutral|satisfied|appreciative)",
        note,
    )
    if sentiment_match:
        parsed.customer_sentiment = sentiment_match.group(1).lower()

    parsed.follow_up_needed = bool(parsed.parts_used) or "follow-up" in note.lower()
    return parsed


def build_report(note: FieldNote) -> JobReport:
    issue = note.issue or "General field-service work"
    location = note.location or "Unspecified location"
    summary = f"{issue} at {location}; {note.time_spent_minutes} minute(s) recorded."
    return JobReport(
        job_id=f"JOB-{int(datetime.utcnow().timestamp())}",
        location=location,
        issue=issue,
        parts_used=note.parts_used,
        time_spent_minutes=note.time_spent_minutes,
        completed_at=datetime.utcnow().isoformat() + "Z",
        customer_sentiment=note.customer_sentiment,
        summary=summary,
    )


def generate_followups(note: FieldNote) -> list:
    tasks = []
    if note.parts_used:
        tasks.append(
            FollowUpTask(
                description="Review/replenish used parts: " + ", ".join(note.parts_used)
            )
        )
    if note.follow_up_needed:
        tasks.append(
            FollowUpTask(description="Schedule follow-up review", priority="high")
        )
    return tasks


# Compatibility alias for earlier documentation.
generate_follow_ups = generate_followups


def draft_customer_email(report: JobReport) -> str:
    return (
        f"Subject: Service update for {report.location}\n\n"
        f"We completed work related to {report.issue}. "
        f"Recorded service time: {report.time_spent_minutes} minute(s). "
        "Please reply if you notice any further issue or need a follow-up visit."
    )


def render_template(report: JobReport) -> str:
    return (
        "## Job Report\n"
        f"- **Job ID:** {report.job_id}\n"
        f"- **Location:** {report.location}\n"
        f"- **Issue:** {report.issue}\n"
        f"- **Parts Used:** {', '.join(report.parts_used) or 'None'}\n"
        f"- **Time Spent:** {report.time_spent_minutes} minutes\n"
        f"- **Completed At:** {report.completed_at}\n"
        f"- **Customer Sentiment:** {report.customer_sentiment or 'N/A'}\n"
        f"- **Summary:** {report.summary}\n"
    )


def main():
    for raw_note in SAMPLE_NOTES:
        note = parse_note(raw_note)
        report = build_report(note)
        tasks = generate_followups(note)
        print(render_template(report))
        if tasks:
            print("### Follow-up Tasks")
            for task in tasks:
                print(f"- [{task.priority}] {task.description}")
        print("---\n")


if __name__ == "__main__":
    main()
