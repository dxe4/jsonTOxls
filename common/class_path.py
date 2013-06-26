import sys,os

def append_path():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    path_list = [os.path.join(project_dir),
                 os.path.join(project_dir,"client/examples"),
                 os.path.join(project_dir,"common"),
                 os.path.join(project_dir,"client"),
                 os.path.join(project_dir,"server")
                 ]

    for path in path_list:
        if path in sys.path:
            continue
        sys.path.append(path)
