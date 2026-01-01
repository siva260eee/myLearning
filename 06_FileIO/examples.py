# Module 6: File I/O - Examples

import os
import json
import csv
from datetime import datetime

print("=" * 60)
print("1. READING FILES")
print("=" * 60)

# First, create a sample file
sample_file = "sample.txt"
with open(sample_file, "w") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python File I/O\n")
    f.write("Line 3: Third line\n")

# Read entire file
print("Reading entire file:")
with open(sample_file, "r") as f:
    content = f.read()
    print(content)

# Read as list of lines
print("\nReading as lines:")
with open(sample_file, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")

# Iterate through file
print("\nIterating through file:")
with open(sample_file, "r") as f:
    for line in f:
        print(f"  {line.strip()}")

print("\n" + "=" * 60)
print("2. WRITING FILES")
print("=" * 60)

# Write (creates/overwrites)
output_file = "output.txt"
with open(output_file, "w") as f:
    f.write("This is line 1\n")
    f.write("This is line 2\n")
    f.write("This is line 3\n")

print(f"Created {output_file}")

# Append to file
with open(output_file, "a") as f:
    f.write("This is appended line\n")
    f.write("Another appended line\n")

print(f"Appended to {output_file}")

# Show content
print("\nContent of output file:")
with open(output_file, "r") as f:
    print(f.read())

print("\n" + "=" * 60)
print("3. FILE PATH OPERATIONS")
print("=" * 60)

# Current directory
print(f"Current directory: {os.getcwd()}")

# Check if file exists
if os.path.exists(output_file):
    print(f"'{output_file}' exists")

# Get file info
if os.path.isfile(output_file):
    print(f"'{output_file}' is a file")

size = os.path.getsize(output_file)
print(f"File size: {size} bytes")

# Get filename without path
filename = os.path.basename(output_file)
print(f"Filename: {filename}")

# Get directory
dirname = os.path.dirname("folder/subfolder/file.txt")
print(f"Directory: {dirname if dirname else '(current)'}")

print("\n" + "=" * 60)
print("4. WORKING WITH JSON")
print("=" * 60)

# Create sample data
student = {
    "name": "Alice",
    "age": 30,
    "grades": [85, 92, 88],
    "courses": ["Python", "Java", "JavaScript"]
}

print(f"Original data: {student}")

# Convert to JSON string
json_string = json.dumps(student, indent=2)
print(f"\nJSON string:\n{json_string}")

# Convert back to dictionary
parsed = json.loads(json_string)
print(f"\nParsed back: {parsed}")

# Write to JSON file
json_file = "student.json"
with open(json_file, "w") as f:
    json.dump(student, f, indent=2)

print(f"\nWrote to {json_file}")

# Read from JSON file
with open(json_file, "r") as f:
    loaded_student = json.load(f)
    print(f"Loaded from file: {loaded_student}")

# Multiple objects to JSON
students = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=2)

print(f"\nWrote {len(students)} students to students.json")

print("\n" + "=" * 60)
print("5. WORKING WITH CSV")
print("=" * 60)

# Create sample CSV data
csv_file = "data.csv"
data = [
    ["Name", "Age", "City", "Score"],
    ["Alice", 30, "NYC", 95],
    ["Bob", 25, "LA", 87],
    ["Charlie", 35, "Chicago", 92]
]

# Write CSV
with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"Created {csv_file}")

# Read CSV as list of lists
print("\nReading CSV as lists:")
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(f"  {row}")

# Read CSV as dictionaries
print("\nReading CSV as dictionaries:")
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"  {row}")

# Write CSV using DictWriter
dict_data = [
    {"Name": "Dave", "Age": 28, "City": "Boston", "Score": 88},
    {"Name": "Eve", "Age": 32, "City": "Seattle", "Score": 91}
]

csv_dict_file = "data_dict.csv"
with open(csv_dict_file, "w", newline="") as f:
    fieldnames = ["Name", "Age", "City", "Score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(dict_data)

print(f"Created {csv_dict_file}")

print("\n" + "=" * 60)
print("6. COPYING AND REMOVING FILES")
print("=" * 60)

# Copy file content
source = output_file
destination = "output_copy.txt"

with open(source, "r") as f_in:
    content = f_in.read()

with open(destination, "w") as f_out:
    f_out.write(content)

print(f"Copied '{source}' to '{destination}'")

print("\n" + "=" * 60)
print("7. ERROR HANDLING")
print("=" * 60)

# Try to read non-existent file
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: File not found!")
except IOError as e:
    print(f"IO Error: {e}")

# Try to write to read-only file
try:
    with open("readonly.txt", "w") as f:
        f.write("test")
except PermissionError:
    print("Error: Permission denied!")

print("\n" + "=" * 60)
print("8. COUNTING LINES AND WORDS")
print("=" * 60)

# Count lines in file
with open(sample_file, "r") as f:
    line_count = sum(1 for line in f)

print(f"Lines in {sample_file}: {line_count}")

# Count words
with open(sample_file, "r") as f:
    content = f.read()
    words = content.split()
    word_count = len(words)

print(f"Words in {sample_file}: {word_count}")

# Count specific word
with open(sample_file, "r") as f:
    content = f.read().lower()
    count = content.count("line")

print(f"Occurrences of 'line': {count}")

print("\n" + "=" * 60)
print("9. READING SPECIFIC LINES")
print("=" * 60)

# Read first N lines
n = 2
with open(sample_file, "r") as f:
    first_n = [f.readline() for _ in range(n)]

print(f"First {n} lines:")
for line in first_n:
    print(f"  {line.strip()}")

# Read lines in range
start, end = 1, 3
with open(sample_file, "r") as f:
    lines = f.readlines()

print(f"\nLines {start} to {end}:")
for i in range(start-1, min(end, len(lines))):
    print(f"  {i+1}: {lines[i].strip()}")

print("\n" + "=" * 60)
print("10. CLEANUP")
print("=" * 60)

# Remove test files
test_files = [sample_file, output_file, "output_copy.txt", 
              json_file, "students.json", csv_file, csv_dict_file]

for file in test_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed {file}")

print("\n" + "=" * 60)
print("END OF EXAMPLES")
print("=" * 60)
