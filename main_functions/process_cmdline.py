from pprint import pprint

import psutil

# Iterate over all running processes
def cmd_process():
    cmd_list = []
    for proc in psutil.process_iter():
        try:
            # Get process information
            process_info = proc.as_dict(attrs=['pid', 'name', 'cmdline', "status"])

            # Check if process has command line arguments
            if process_info['cmdline']:
                if process_info['name'] == "python.exe":
                    if 'main.py' and 'parsing' in process_info['cmdline']:
                        cmd_list.append(process_info['cmdline'][-1])

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
    return cmd_list
#
# print(cmd_process())
# if f'--ex_id=217'in cmd_process():
#     print('ok')
# else:
#     print('...')