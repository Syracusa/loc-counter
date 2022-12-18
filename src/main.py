import os
import datetime
import json

DO_VERBOSE = 0

exclude_dirs =  set(['build', 'env', '.vscode', 'node_modules', 'ext', 'environments'])
exclude_files =  set(['karma.conf.js', 'MainForm.Designer.cs'])

extensions = ('.c', '.h', '.cpp', '.ts', '.js', '.html', '.py', '.sh', '.rs', '.md', '.cs')
locs = {}

def do_log(data :dict):
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    
    filename = f"./log/{date_str}.json"
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent = 4))
        
    date_str = now.strftime("%Y-%m-%d-%H-%M-%S")
    
    filename = f"./log/{date_str}.json"
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent = 4))
        
def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def init_extension_locs(extension_locs: dict):
    for e in extensions:
        extension_locs[e] = 0

def prune_extension_locs(extension_locs: dict):
    for e in extensions:
        if (extension_locs[e] == 0):
            del extension_locs[e]

def count_loc(path):
    loc_acc = 0
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for d in directories:
        loc_acc += count_loc_repo(path, d)
    return loc_acc

def count_loc_repo(path, reponame):  
    repo_loc = 0
    locs[reponame] = {}
    init_extension_locs(locs[reponame])
    for root, dirs, files in os.walk(os.path.join(path, reponame), topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        files[:] = [f for f in files if f not in exclude_files]
        for file in files:
            if file.endswith(extensions):  # count only Python files
                with open(os.path.join(root, file), 'r') as f:
                    ext = get_file_extension(f.name)
                    
                    floc = len(f.readlines())
                    locs['All'][ext] += floc
                    locs[reponame][ext] += floc
                    
                    repo_loc += floc
                    
                    if DO_VERBOSE:
                        print(f'file {file} loc {floc}')
    prune_extension_locs(locs[reponame])
    return repo_loc

locs['All'] = {}
init_extension_locs(locs['All'])

repo_path = './projects/'
loc = count_loc(repo_path)
print(f'Number of lines of code in the repositories: {loc}')

prune_extension_locs(locs['All'])
print(json.dumps(locs, indent = 4))
do_log(locs)