# Module 6: File I/O - Exercises

## Exercise 1: Read and Display File
Create a text file and:
1. Read and display all content
2. Count total lines
3. Count total words
4. Count specific word
5. Find longest line

---

## Exercise 2: Create and Write Files
1. Create a file with 10 lines of text
2. Append 5 more lines
3. Read and display
4. Create another file with uppercase version

---

## Exercise 3: Line Processing
1. Read a file
2. Number each line
3. Reverse order of lines
4. Write to new file

Example input:
```
Apple
Banana
Cherry
```

Example output:
```
3: Cherry
2: Banana
1: Apple
```

---

## Exercise 4: JSON Operations
Create a program that:
1. Defines a dictionary of person data (name, age, email, hobbies)
2. Saves to JSON file
3. Loads from JSON file
4. Modifies the data
5. Saves modified version

---

## Exercise 5: CSV Operations
Create a CSV file with student data:
- Name, Student_ID, Grades (3 subjects), GPA

1. Write CSV (create from lists)
2. Read CSV
3. Calculate average grade for each student
4. Find top student
5. Export report to new CSV

---

## Exercise 6: File Copy and Backup
Create functions:
- `copy_file(source, destination)` - copy file
- `create_backup(filename)` - create backup with timestamp
- `list_backups(filename)` - list all backups

---

## Exercise 7: Word Frequency Counter
1. Read a text file
2. Count word frequencies
3. Save results to JSON sorted by frequency
4. Display top 10 words

---

## Exercise 8: Log File Analysis
Create a program that:
1. Generates a log file with entries
2. Reads log file
3. Filters by severity level (INFO, WARNING, ERROR)
4. Generates summary report

Example log format:
```
2024-01-15 10:30 INFO User login
2024-01-15 10:31 WARNING Low disk space
2024-01-15 10:32 ERROR Connection timeout
```

---

## Exercise 9: Config File Management
Create program that:
1. Reads configuration from JSON
2. Allows updating config values
3. Saves changes back to file
4. Has default values for missing keys

Example config:
```json
{
    "app_name": "MyApp",
    "debug": true,
    "port": 8000,
    "database": "mydb"
}
```

---

## Exercise 10: Merge Files
1. Read multiple files
2. Combine content
3. Remove duplicates
4. Write merged file

---

## Challenge Exercises

### Challenge 1: Data Converter
Create program that:
1. Reads CSV
2. Converts to JSON
3. Converts to TXT format
4. Can go the other direction (JSON → CSV)

### Challenge 2: Log Analyzer
Analyze log files:
1. Count errors by type
2. Find error patterns
3. Generate statistics
4. Create HTML report

### Challenge 3: File Backup System
Create backup system:
1. Monitor directory for changes
2. Create backups of modified files
3. Store with timestamp
4. Allow restoration from backup

### Challenge 4: Student Report Card
Create program that:
1. Reads student data from CSV
2. Calculates statistics (GPA, percentile)
3. Generates report as HTML
4. Exports as PDF (use `reportlab` library)

---

## Debugging Exercise

Find and fix errors:

```python
# Bug 1: File not closed
f = open("file.txt", "r")
content = f.read()
print(content)
# Missing: f.close()

# Bug 2: Wrong mode
with open("data.txt", "r") as f:
    f.write("new content")  # Can't write in read mode

# Bug 3: Path issues
file = "C:\Users\name\file.txt"  # Should use raw string or /

# Bug 4: JSON error
data = {"name": 'Alice'}  # JSON needs double quotes
json.dumps(data)

# Bug 5: CSV newline
with open("file.csv", "w") as f:  # Missing newline=""
    writer = csv.writer(f)
```

---

## How to Submit

1. Create `my_solutions.py` in 06_FileIO folder
2. Include test files
3. Test all file operations
4. Handle missing files gracefully
5. Add comments explaining logic

---

**Next:** Module 7: Error Handling and Debugging
