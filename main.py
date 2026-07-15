import argparse
from services.task_service import add_task, get_tasks

def main():
    parser = argparse.ArgumentParser(description="Task CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="The title of the task")

    # List command
    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Task added: {task['title']}")
    elif args.command == "list":
        tasks = get_tasks()
        if not tasks:
            print("No tasks yet. Add one with: python main.py add <task>")
        else:
            for t in tasks:
                status = "[x]" if t.get("completed") else "[ ]"
                print(f"{t['id']}. {status} {t['title']}")

if __name__ == "__main__":
    main()
