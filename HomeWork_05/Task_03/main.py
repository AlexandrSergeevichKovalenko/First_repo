from functions_block import *

def main():
    #callin the function to get the path to the file and the second argument
    log_file_path, log_level  = get_path()
    
    #loading logs from the file
    logs = load_logs(log_file_path)

    #calculating number of items by logs level
    counts = count_logs_by_level(logs)

    display_log_counts(counts, log_level)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':\n")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
        



if __name__ == "__main__":
    main()