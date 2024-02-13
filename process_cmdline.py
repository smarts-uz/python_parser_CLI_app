import psutil

# Iterate over all running processes
def cmd_process():
    for proc in psutil.process_iter():
        cmd_list = []
        try:
            # Get process information
            process_info = proc.as_dict(attrs=['pid', 'name', 'cmdline', "status"])

            # Check if process has command line arguments
            if process_info['cmdline']:
                if process_info['name'] == "python.exe":
                    if 'main.py' and 'parsing' in process_info['cmdline']:
                        return process_info['cmdline']
                # if process_info['name'] == "python.exe":  # print only python's proccess list
                #     for cmd in process_info['cmdline']:
                #         print(cmd)

                # return process_info['cmdline']


                # print(
                #     f"PID: {process_info['pid']}, Name: {process_info['name']}, Command Line: {' '.join(process_info['cmdline'])}")
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            pass
