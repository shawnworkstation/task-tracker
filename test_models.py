from datetime import datetime, timedelta
from models import Task, TaskStatus

def test_task_creation() -> None:
    """Verifies fields are set correctly on creation and default values apply."""
    now = datetime.now()
    task = Task(
        id = 1,
        title = "task 1",
        status = TaskStatus.TODO,
        created_at = now,
        due_date=None
    )
    assert task.id == 1
    assert task.title == "task 1"
    assert task.status == TaskStatus.TODO
    assert task.created_at == now
    assert task.due_date is None

def test_mark_done_true() -> None:
    """Verifies mark_done updates status to DONE and return self."""
    task = Task(
        id = 2,
        title = "task 2",
        status = TaskStatus.TODO,
        created_at = datetime.now,
        due_date=None        
    )
    result = task.mark_done()
    assert task.status == TaskStatus.DONE
    assert result == task

def test_is_overdue_true() -> None:
    """Verifies task is overdue when due_date is in the past and status is not None"""
    now = datetime.now()
    task = Task(
            id = 3,
            title = "task 3",
            status = TaskStatus.TODO,
            created_at = now - timedelta(days=10),
            due_date= now - timedelta(days=1)       
        )
    assert task.is_overdue() is True


def test_is_overdue_false() -> None:
    """Verifies task is not overdue when status is  Done"""
    now = datetime.now()
    task = Task(
            id = 4,
            title = "task 4",
            status = TaskStatus.DONE,
            created_at = now - timedelta(days=10),
            due_date= now - timedelta(days=1)       
        )
    assert task.is_overdue() is False