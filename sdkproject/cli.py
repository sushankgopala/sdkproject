import argparse
from sdkproject.creator import create_project_structure

def main():
    parser = argparse.ArgumentParser(prog="sdkproject", description="SDK Project CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    create_parser = subparsers.add_parser("create_rag", help="Create a RAG project structure")
    create_parser.add_argument("project_name", type=str, help="Name of the project")

    args = parser.parse_args()

    if args.command == "create_rag":
        create_project_structure(args.project_name)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
