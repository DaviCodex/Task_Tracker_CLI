
# Task Tracker CLI

Task Tracker CLI is a simple command-line application that allows you to add, update, mark, and delete tasks in a JSON file. The application also lets you view a list of tasks based on their status.

## Features

- **Add Task**: Add a new task with a description and a default status of "todo".
## In-coming features
- **Add pytest**

## Usage

### Add Task

To add a new task, use the `-a` or `--add` argument:

```bash
python3 task_tracker.py -a "New Task Description"
```

### List Tasks

To list tasks based on their status, use the `-l` or `--list` argument. You can specify "todo", "in progress", "done", or "all":

```bash
python3 task_tracker.py -l "todo"
```

### Update Task Description

To update the description of a task, `-u` or `--update` argument. You need to pass the id and the new description:

```bash
python3 task_tracker.py -u 2 "Updated Task Description"
```

### Mark in-progress Status

To mark a task as "in-progress", use the `-mp` or ` --markinprogress` argument. specify the task ID to provide the in-progress status:

```bash
python3 task_tracker.py -mp 2
```

### Mark done Status

To mark a task as "done", use the `-md` or `--markdone` argument. specify the task ID to provide the done status:

```bash
python3 task_tracker.py -md 1
```

### Delete Task

To delete a task `-d` or `--delete` argument to specify the task ID:

```bash
python3 task_tracker.py -d 2
```

## Notes

- Ensure that the `test_tasks.json` file exists in the same directory as the script for it to function correctly.
- The application will create the `test_tasks.json` file if it does not already exist when adding a new task.

## Project Link

For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).
