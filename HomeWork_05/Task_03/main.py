from functions_block import (
    get_path, 
    load_logs, 
    filter_logs_by_level, 
    count_logs_by_level, 
    display_log_counts, 
    display_log_details
)

def main():
    #callin the function to get the path to the file and the second argument
    log_file_path, log_level  = get_path()
    
    #loading logs from the file
    logs = load_logs(log_file_path)

    #calculating number of items by logs level
    counts = count_logs_by_level(logs)

    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        print(f"\nДеталі логів для рівня '{log_level.upper()}':\n")
        display_log_details(filtered_logs, log_level)
        



if __name__ == "__main__":
    main()