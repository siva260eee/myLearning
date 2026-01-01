# Git Branching Strategy

## Overview
This project follows a **feature branch workflow**. Every change, exercise, or project gets its own branch before merging to `main`.

## Branch Naming Convention

### Format
```
<type>/<description>
```

### Types
- **`module/`**: Working on a specific module (e.g., `module/ml-fundamentals`)
- **`exercise/`**: Completing exercises (e.g., `exercise/ml-ex1-5`)
- **`project/`**: Building projects (e.g., `project/wine-classifier`)
- **`fix/`**: Bug fixes (e.g., `fix/data-preprocessing`)
- **`docs/`**: Documentation updates (e.g., `docs/update-readme`)
- **`practice/`**: Daily practice (e.g., `practice/jan-01`)

### Examples
```
module/01-ml-fundamentals
exercise/deep-learning-cnn
project/sentiment-analyzer
fix/model-training-error
practice/daily-jan-15
```

---

## Workflow

### 1️⃣ Start New Work
```bash
# Make sure you're on main and it's up to date
git checkout main
git pull origin main

# Create and switch to new branch
git checkout -b module/ml-fundamentals

# Or use shorthand for both commands above
git checkout main && git pull && git checkout -b exercise/ml-ex1
```

### 2️⃣ Work on Your Branch
```bash
# Make changes, add files, write code...

# Check what changed
git status

# Add changes
git add .
# Or add specific files
git add AI_ML_Journey/01_ML_Fundamentals/my_solutions.py

# Commit with meaningful message
git commit -m "Complete exercises 1-5 in ML Fundamentals"
```

### 3️⃣ Push Branch to GitHub
```bash
# First time pushing this branch
git push -u origin module/ml-fundamentals

# Subsequent pushes (after first time)
git push
```

### 4️⃣ Test Your Changes
```bash
# Run tests, execute code, verify everything works
python AI_ML_Journey/01_ML_Fundamentals/my_solutions.py

# Run specific tests
python -m pytest tests/

# Test your ML model
python your_model.py
```

### 5️⃣ Merge to Main
```bash
# Option A: Local merge (for personal projects)
git checkout main
git pull origin main
git merge module/ml-fundamentals
git push origin main

# Option B: Pull Request on GitHub (recommended)
# 1. Go to https://github.com/siva260eee/myLearning
# 2. Click "Pull Requests" → "New Pull Request"
# 3. Select your branch
# 4. Review changes
# 5. Click "Merge Pull Request"
```

### 6️⃣ Clean Up
```bash
# Delete local branch (after merging)
git branch -d module/ml-fundamentals

# Delete remote branch
git push origin --delete module/ml-fundamentals

# Or use GitHub CLI
gh pr merge --merge --delete-branch
```

---

## Quick Commands

### Daily Practice Workflow
```bash
# Start
git checkout main && git pull && git checkout -b practice/$(date +%b-%d)

# Work and commit
git add . && git commit -m "Daily practice: [topic]"

# Push and merge
git push -u origin practice/$(date +%b-%d)
git checkout main && git merge practice/$(date +%b-%d) && git push
```

### Exercise Completion Workflow
```bash
# Start exercise
git checkout main && git pull && git checkout -b exercise/ml-ex1-3

# Complete exercises, test them
# Add and commit
git add . && git commit -m "Complete ML exercises 1-3"

# Push
git push -u origin exercise/ml-ex1-3

# Merge to main
git checkout main && git merge exercise/ml-ex1-3 && git push

# Clean up
git branch -d exercise/ml-ex1-3
```

### Project Workflow
```bash
# Start project
git checkout main && git pull && git checkout -b project/wine-classifier

# Multiple commits as you work
git add . && git commit -m "Initial project setup"
git add . && git commit -m "Add data preprocessing"
git add . && git commit -m "Implement model training"
git add . && git commit -m "Complete project with evaluation"

# Push regularly
git push -u origin project/wine-classifier  # first time
git push  # subsequent times

# When done and tested
git checkout main && git merge project/wine-classifier && git push
git branch -d project/wine-classifier
```

---

## Helpful Aliases

Add these to your git config for faster workflow:

```bash
# Set up aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.sync "!git checkout main && git pull origin main"

# Now you can use:
git co main          # instead of git checkout main
git br               # instead of git branch
git ci -m "message"  # instead of git commit -m "message"
git st               # instead of git status
git sync             # checkout main and pull in one command
```

---

## Branch Management

### View All Branches
```bash
# Local branches
git branch

# Remote branches
git branch -r

# All branches
git branch -a
```

### Switch Between Branches
```bash
git checkout branch-name

# Or newer syntax
git switch branch-name
```

### Delete Branches
```bash
# Delete local branch (only if merged)
git branch -d branch-name

# Force delete local branch
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name
```

### See Current Branch
```bash
git branch --show-current

# Or in status
git status
```

---

## Best Practices

### ✅ Do:
- Create a branch for every change
- Use descriptive branch names
- Commit often with clear messages
- Test before merging
- Pull main before creating new branches
- Delete branches after merging

### ❌ Don't:
- Work directly on `main` branch
- Create branches with spaces or special characters
- Let branches live forever
- Push untested code to main
- Commit huge changes in one go

---

## Example Workflow Timeline

```
Day 1:
  git checkout -b module/ml-fundamentals
  # Read concepts, work on examples
  git commit -m "Start ML fundamentals module"
  git push -u origin module/ml-fundamentals

Day 2:
  # Continue on same branch
  git commit -m "Complete first 3 exercises"
  git push

Day 3:
  # Finish module
  git commit -m "Complete all ML fundamentals exercises"
  git push
  # Test everything
  git checkout main && git merge module/ml-fundamentals
  git push
  git branch -d module/ml-fundamentals

Day 4:
  git checkout -b module/deep-learning
  # Start next module...
```

---

## Emergency Commands

### Undo Last Commit (not pushed)
```bash
git reset --soft HEAD~1
```

### Discard All Local Changes
```bash
git restore .
# Or
git checkout -- .
```

### See What Would Be Merged
```bash
git checkout main
git diff main..module/ml-fundamentals
```

### Stash Changes Temporarily
```bash
# Save current work
git stash

# Work on something else...

# Restore stashed work
git stash pop
```

---

## GitHub CLI Integration

### Create Branch and Push
```bash
gh repo view --web  # Open repo in browser

# Create PR from command line
gh pr create --title "Complete ML Fundamentals" --body "Completed all exercises"

# Merge PR
gh pr merge --merge --delete-branch
```

---

## Your Typical Session

```bash
# 1. Start your day
cd C:\Users\shiyag01\IdeaProjects\myLearning
git checkout main
git pull origin main

# 2. Start working on something
git checkout -b exercise/ml-ex1

# 3. Work, test, commit
# ... make changes ...
git add .
git commit -m "Complete exercise 1"

# 4. Push to GitHub
git push -u origin exercise/ml-ex1

# 5. Merge when done
git checkout main
git merge exercise/ml-ex1
git push

# 6. Clean up
git branch -d exercise/ml-ex1
git push origin --delete exercise/ml-ex1
```

---

**Remember**: `main` is your production-ready code. All development happens in branches! 🌿
