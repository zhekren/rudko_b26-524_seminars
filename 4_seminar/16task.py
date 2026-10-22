import re

def extract_info_logs(read_file_path, write_file_path):
    with open(read_file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    
    info_users = re.findall(r'.\bINFO User (\d+)', logs)
    warning_users = re.findall(r'.\bWARNING User (\d+)', logs)
    error_users = re.findall(r'.\bERROR User (\d+)', logs)

    with open(write_file_path, 'w', encoding='utf-8') as file:
        file.write(f"INFO: {len(info_users)}\n")
        file.write(f"WARNING: {len(warning_users)}\n")
        file.write(f"ERROR: {len(error_users)}\n")
    
    return {"ERROR": [int(i) for i in error_users]}

print(extract_info_logs("/Users/jokovich/Desktop/Python_basics/4_seminar/BIGlogs_input.txt", "/Users/jokovich/Desktop/Python_basics/4_seminar/BIGlogs_output.txt"))