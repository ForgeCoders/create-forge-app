import os

def create_project(project_name):
    """Creates a new project folder with starter files (README.md and main.py).
    If the folder already exists, prints a massage instead of crashing."""
    try:
        os.makedirs(project_name)
        print(f"Created project folder: {project_name}")

        with open(os.path.join(project_name, "README.md"), "w") as f:
            f.write(f"# {project_name}\n")

        with open(os.path.join(project_name, "main.py"), "w") as f:
            f.write("print('Hello from your new project!')\n")

        print("Starter files generated.")

    except FileExistsError:
        print(f"A project named '{project_name}' already exists. Choose a different name.")