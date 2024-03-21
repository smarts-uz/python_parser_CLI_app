from natsort import os_sorted
import os

def json_search(path):
    html_files = []
    if '/result.json' in path:path = path[:-len('/result.json')]
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith('result') and file.endswith('.json'):
                html_files.append(os.path.join(root, file))
                for d in dirs:dirs.remove(d)

    return os_sorted(html_files)