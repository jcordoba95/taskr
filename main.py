import argparse

tasks = []

def main():
    parser = argparse.ArgumentParser(description="Task CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="The title of the task")
    
    args = parser.parse_args()
    
    if args.command == "add":
        tasks.append(args.title)
        print(f"Task added: {args.title}")

if __name__ == "__main__":
    main()
