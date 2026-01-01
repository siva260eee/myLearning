# Module 8: Real-World Projects

This module contains complete projects that combine everything you've learned. Each project should take 2-3 days.

---

## Project 1: Todo List Manager

**Skills:** Functions, Lists, Dictionaries, File I/O, Error Handling

### Requirements:
1. Add, view, edit, delete todos
2. Mark todos as done/incomplete
3. Save/load from JSON file
4. Display with formatting (ID, text, status, date)
5. Search by keyword

### Structure:
```
TodoItem (named tuple or dict)
    - id
    - text
    - completed
    - created_date

TodoList (class)
    - items (list)
    - add_todo(text)
    - remove_todo(id)
    - update_todo(id, text)
    - mark_done(id)
    - list_all()
    - save_to_file()
    - load_from_file()
```

### Enhanced Features:
- Filter by status (done/pending)
- Priority levels (high, medium, low)
- Due dates
- Categories
- Recurring todos

---

## Project 2: Student Management System

**Skills:** OOP, Classes, File I/O, Dictionaries, Error Handling

### Requirements:
1. Manage students (name, ID, email, enrollments)
2. Manage courses (name, code, credits, instructor)
3. Manage grades
4. Calculate GPA
5. Generate reports

### Classes:
```
Student
    - name, student_id, email
    - courses (list)
    - grades (dict)
    - add_course(course)
    - add_grade(course_id, grade)
    - get_gpa()

Course
    - name, code, credits, instructor
    - max_students
    - enrolled_students (list)
    - enroll_student(student)
    - remove_student(student)

StudentManagementSystem
    - students (dict)
    - courses (dict)
    - add_student()
    - add_course()
    - enroll_student()
    - assign_grade()
    - generate_transcript()
    - find_top_students()
```

### Data Storage:
- Save students to JSON
- Save courses to CSV
- Save grades to CSV

---

## Project 3: Expense Tracker

**Skills:** OOP, Dictionaries, Lists, Data Analysis, File I/O

### Requirements:
1. Log expenses with category, amount, date
2. Categorize spending (food, transport, utilities, etc.)
3. Generate reports by category
4. Calculate totals and averages
5. Budget tracking (set budget, warn if exceeded)
6. Monthly/yearly summaries

### Classes:
```
Expense
    - id, date, category, amount, description

ExpenseTracker
    - expenses (list)
    - budget (dict of category budgets)
    - add_expense()
    - remove_expense()
    - get_by_category()
    - get_by_date_range()
    - total_by_category()
    - check_budget()
    - generate_report()
    - export_csv()
```

### Features:
- Multiple users
- Recurring expenses
- Budget alerts
- Visualization (text-based or with charts)

---

## Project 4: Simple Game (Number Guessing, Hangman, or Tic-Tac-Toe)

**Skills:** Functions, Loops, Conditionals, OOP, File I/O

### Option A: Number Guessing Game
```
- Computer picks number
- User guesses
- Feedback: too high/low
- Track attempts
- High score (save/load)
- Multiple difficulties
```

### Option B: Hangman
```
- Computer picks word
- User guesses letters
- Draw hangman ASCII art
- Track wrong guesses
- Win/lose conditions
- Word list from file
```

### Option C: Tic-Tac-Toe
```
class TicTacToe:
    - board (3x3 grid)
    - current_player
    - make_move(row, col)
    - check_winner()
    - is_board_full()
    - get_valid_moves()
    - display_board()
    - play()  # Main game loop
```

---

## Project 5: Personal Finance Dashboard

**Skills:** OOP, File I/O, Data structures, Error handling, Functions

### Requirements:
1. Track income and expenses
2. Calculate net worth
3. Savings goals
4. Investment portfolio tracking
5. Financial summaries

### Classes:
```
Account
    - type (checking, savings, investment)
    - balance
    - transactions (list)

FinanceManager
    - accounts (dict)
    - income_sources (list)
    - expenses (list)
    - goals (list)
    - calculate_net_worth()
    - get_monthly_summary()
    - get_spending_breakdown()
    - check_goal_progress()
```

---

## Project 6: Library Management System

**Skills:** OOP, Classes, Inheritance, File I/O, Error Handling

### Requirements:
1. Manage books and borrowers
2. Track checkouts and returns
3. Due dates and late fees
4. Search by title, author, ISBN
5. Generate reports

### Classes:
```
Item (base class)
    - title, id

Book(Item)
    - author, isbn, year, available_copies

Borrower
    - name, borrower_id, email

Library
    - books (dict)
    - borrowers (dict)
    - checkouts (list)
    - add_book()
    - checkout_book()
    - return_book()
    - check_overdue()
    - search_books()
    - generate_report()
```

---

## Project 7: Simple Web Scraper & Data Analyzer

**Skills:** Functions, File I/O, Error Handling, Data structures

### Requirements:
1. Fetch data from web (use `requests` library)
2. Parse HTML/JSON (use `BeautifulSoup` or `json`)
3. Extract relevant information
4. Save to CSV/JSON
5. Generate statistics

### Example Scraping Projects:
- Weather data from weather API
- News headlines
- Product prices
- Stock data

---

## Project 8: Task Scheduler

**Skills:** OOP, Datetime, File I/O, Scheduling

### Requirements:
1. Create tasks with due dates
2. Set reminders
3. Categorize tasks
4. Priority levels
5. Recurring tasks
6. Generate schedule view

### Classes:
```
Task
    - title, description, due_date
    - priority, category
    - recurrence (daily, weekly, monthly)

Scheduler
    - tasks (list)
    - add_task()
    - complete_task()
    - get_overdue_tasks()
    - get_today_tasks()
    - get_upcoming_tasks(days)
    - display_calendar_view()
```

---

## Getting Started with a Project

### Step 1: Plan
- Write down requirements
- Sketch class structure
- List functions needed
- Plan file format (JSON, CSV, TXT)

### Step 2: Core Functionality
- Create basic classes
- Implement main functions
- Test with simple data

### Step 3: Data Persistence
- Add save/load functions
- Test with file I/O
- Handle errors gracefully

### Step 4: User Interface
- Create menu system
- Add input validation
- Pretty print output
- Add help/instructions

### Step 5: Testing & Polish
- Test all features
- Handle edge cases
- Add error messages
- Improve user experience

---

## Project Checklist

For each project, ensure:

✅ **Classes and OOP**
- Proper encapsulation
- Clear method names
- Inheritance where appropriate

✅ **Error Handling**
- Try/except blocks
- Input validation
- Meaningful error messages

✅ **Data Persistence**
- Save to file (JSON/CSV)
- Load from file
- Handle file errors

✅ **Functions**
- Modular code
- DRY principle (Don't Repeat Yourself)
- Good documentation

✅ **Code Quality**
- Clear variable names
- Comments explaining logic
- Consistent formatting
- No hardcoded values

✅ **Testing**
- Test happy path
- Test error cases
- Test edge cases

---

## Project Difficulty Levels

**Beginner:**
- Todo List Manager (without advanced features)
- Number Guessing Game

**Intermediate:**
- Student Management System
- Expense Tracker
- Simple Hangman

**Advanced:**
- Library Management System
- Task Scheduler
- Web Scraper
- Finance Dashboard

---

## Additional Resources

### Libraries You'll Use:
- `json` - JSON file handling
- `csv` - CSV file handling
- `os` - File system operations
- `datetime` - Date and time
- `random` - Random operations
- `requests` - HTTP requests (for web scraping)
- `BeautifulSoup` - HTML parsing (for web scraping)

### Install additional libraries:
```bash
pip install requests beautifulsoup4
```

---

## Tips for Success

1. **Start Simple** - Build core functionality first
2. **Test Frequently** - Test after each feature
3. **Use Git** - Track changes with version control
4. **Document Code** - Add docstrings and comments
5. **Handle Errors** - Anticipate what can go wrong
6. **Get Feedback** - Show code to others
7. **Refactor** - Improve code as you learn
8. **Have Fun** - Enjoy the process!

---

**You've reached the end of the structured curriculum!**

Next steps:
1. Complete projects in order of difficulty
2. Build your own projects
3. Contribute to open source
4. Study advanced topics (async, threading, decorators)
5. Learn frameworks (Django, Flask for web)

Happy coding! 🐍
