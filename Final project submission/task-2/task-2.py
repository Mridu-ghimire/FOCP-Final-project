import sys

def read_log_file(file_path):
    try:
        with open(file_path, 'r') as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        print(f'Error: Unable to open file "{file_path}"!')
        return []

def parse_log_entry(log_entry):
    cat_type, entry_time, exit_time = map(int, log_entry.strip().split(','))
    return cat_type, entry_time, exit_time

def analyze_cat_shelter_log(log_lines):
    our_cat_visits, other_cats_count = 0, 0
    total_time_in_shelter, longest_stay_duration, shortest_stay_duration = 0, 0, float('inf')

    for log_line in log_lines:
        if log_line.strip() == 'END':
            break

        cat_type, entry_time, exit_time = parse_log_entry(log_line)

        stay_duration = exit_time - entry_time

        if cat_type == 'OURS':
            our_cat_visits += 1
            total_time_in_shelter += stay_duration

            longest_stay_duration = max(longest_stay_duration, stay_duration)
            shortest_stay_duration = min(shortest_stay_duration, stay_duration)
        else:
            other_cats_count += 1

    total_hours_in_shelter, total_minutes_in_shelter = divmod(total_time_in_shelter, 60)
    longest_hours_stayed, longest_minutes_stayed = divmod(longest_stay_duration, 60)
    shortest_hours_stayed, shortest_minutes_stayed = divmod(shortest_stay_duration, 60)

    print("\nLog File Analysis")
    print("==================")
    print(f'Our Cat Visits: {our_cat_visits}')
    print(f'Other Cats Count: {other_cats_count}')
    print(f'Total Time in Shelter: {total_hours_in_shelter} Hours, {total_minutes_in_shelter} Minutes')
    print(f'Average Stay Length: {total_time_in_shelter // our_cat_visits} Minutes')
    print(f'Longest Stay: {longest_hours_stayed} Hours, {longest_minutes_stayed} Minutes')
    print(f'Shortest Stay: {shortest_hours_stayed} Hours, {shortest_minutes_stayed} Minutes')

def main():
    if len(sys.argv) != 2:
        print('Error: Missing command line argument!')
    else:
        log_lines = read_log_file(sys.argv[1])
        analyze_cat_shelter_log(log_lines)

if __name__ == "__main__":
    main()
