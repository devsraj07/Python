'''
Week 3- Activity 2: .txt file data analysis - Junk file
===========================================================
Open, read, and process the attached data file. Use the attached `junk.txt` file to:
1. Calculate and report the total number of lines in the file.
2. Add a new line at the end of the file containing exactly: `text file analysis`
3. Convert all text in the `junk.txt` file to lowercase.
4. Save the processed file. Share your GitHub repository link here once you have completed the task.
'''
def file_analysis():
    # Step 1: Calculate and report the total number of lines in the file
    with open("junk.txt", "r") as file:
        lines = file.readlines()
        total_lines = len(lines)
        print(f"Total number of lines in the file: {total_lines}")

    # Step 2: Add a new line at the end of the file
    with open("junk.txt", "a") as file:
        file.write("text file analysis\n")

    # Step 3: Convert all text in the junk.txt file to lowercase
    with open("junk.txt", "r") as file:
        lines = file.readlines()
        lines = [line.lower() for line in lines]

    # Step 4: Save the processed file
    with open("junk.txt", "w") as file:
        file.writelines(lines)

def main():
    file_analysis()

if __name__ == "__main__":
    main()

