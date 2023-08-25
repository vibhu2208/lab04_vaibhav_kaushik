flight_table = [
    ("P1", "VSCode", 100, "MID"),
    ("P23", "Eclipse", 234, "MID"),
    ("P93", "Chrome", 189, "High"),
    ("P42", "JDK", 9, "High"),
    ("P9", "CMD", 7, "High"),
    ("P87", "NotePad", 23, "Low")
]

def sort_flight_table(parameter):
    if parameter == 1:
        return sorted(flight_table, key=lambda x: x[0])  # Sort by P_ID
    elif parameter == 2:
        return sorted(flight_table, key=lambda x: x[2])  # Sort by Start Time
    elif parameter == 3:
        priority_order = {"High": 3, "MID": 2, "Low": 1}
        return sorted(flight_table, key=lambda x: priority_order[x[3]])  # Sort by Priority

def main():
    print("Flight Table Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice in [1, 2, 3]:
        sorted_table = sort_flight_table(choice)
        print("Sorted Flight Table:")
        print("P_ID\tProcess\tStart Time\tPriority")
        for row in sorted_table:
            print(f"{row[0]}\t{row[1]}\t{row[2]}\t\t{row[3]}")
    else:
        print("Invalid choice. Please select a valid sorting parameter.")

if __name__ == "__main__":
    main()
