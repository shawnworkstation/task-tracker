from enum import Enum
from dataclasses import dataclass
from datetime import datetime

# Define the Enum for task status
class TaskStatus(Enum):
   TODO = "TODO"
   IN_PROGRESS = "IN_PROGRESS"
   DONE = "DONE"

#Create the Dataclass shell and attributes
@dataclass 
class Task:
    id: int
    title: str
    status: TaskStatus
    created_at: datetime
    due_date: datetime | None

    def mark_done(self) -> "Task":
        """Sets status to DONE and returns the updated task instance."""
        self.status = TaskStatus.DONE
        return self

    def is_overdue(self) -> bool:
        """
        Check if the task is past its due date.
        Only returns True if a due date exists and status is NOT DONE.
        """
        if self.due_date is None or self.status == TaskStatus.DONE:
            return False
        return self.due_date < datetime.now()
   