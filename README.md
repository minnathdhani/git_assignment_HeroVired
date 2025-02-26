# Git Assignment - Minnath Dhani

## 📚 Overview

This repository is part of my Git assignment for HeroVired. It showcases the use of Git version control workflows, collaboration strategies, and Python-based computational tasks, including arithmetic operations and geometric calculations.

---

## 📂 Repository Structure

- `calculator.py`: Performs basic arithmetic operations — addition, subtraction, multiplication, division, and square root calculation.
- `geometry_calculator.py`: Computes areas for geometric shapes like circles and rectangles.
- `git_lfs.txt`: Documents the steps for Git Large File Storage (LFS) tracking.
- `large_file.bin`: A sample large binary file tracked using Git LFS.
- `.gitattributes`: Configures how Git handles large files through Git LFS.
- `README.md`: The current file, providing an organized summary of the repository.

---

## 🌿 Branches Overview

- `main`: The stable branch for production-ready code.
- `dev`: The development branch for testing new features and fixing bugs.
- `lfs`: Handles large file tracking via Git LFS.
- `feature/sqrt`: Implements the square root function in `calculator.py`.
- `geometry-calculator`: The main feature branch for geometric calculations, containing sub-features.
- `feature/circle-area`: Develops the area calculation of circles in `geometry_calculator.py`.
- `feature/rectangle-area`: Focuses on rectangle area calculations in `geometry_calculator.py`.

---

## 🛠️ Workflow

### 1️⃣ **CalculatorPlus Implementation**

#### Step 1: Create the Repository

- Initialize a GitHub repository named `git_assignment_HeroVired`.
- Clone the repository locally.

#### Step 2: Set Up Development Environment

- Create and switch to the `dev` branch.
- Add the provided Python code.

#### Step 3: Version 1.0 Release

- Merge `dev` into `main`.
- Tag the release as **v1.0**.
- Add collaborators to the repository.

#### Step 4: Implement Square Root Feature

- Create a new branch `feature/sqrt`.
- Uncomment and implement the `square_root` function in `calculator.py`.
- Commit changes to `feature/sqrt`.

#### Step 5: Bug Fixing

- Switch to `dev` and update the `divide` function to handle division by zero.
- Merge the fix into `dev` and open a pull request to merge it into `main`.

#### Step 6: Version 2.0 Release

- Merge updates from `dev` into `feature/sqrt`.
- Resolve any conflicts.
- Create a pull request to merge `feature/sqrt` into `dev`.
- Merge `dev` into `main` and release **v2.0**.

---

### 2️⃣ **Handling Large Files with Git LFS**

#### Step 1: Set Up Git LFS

- Create a new branch `lfs`:

```bash
git checkout -b lfs
```

- Install Git LFS:
  [Download Git LFS](https://github.com/git-lfs/git-lfs/releases/download/v3.6.1/git-lfs-windows-v3.6.1.exe)
- Configure LFS to track large binary files:

```bash
git lfs install
git lfs track "*.bin"
git add .gitattributes
```

#### Step 2: Upload and Manage Large Files

- Add a file over 200MB:

```bash
git add large_file.bin
git commit -m "Add large binary file"
git push origin lfs
```

- Merge the `lfs` branch into `main` when ready.

---

### 3️⃣ **Geometry Calculator with Git Stash**

#### Step 1: Feature Branch Setup

- Create the main feature branch `geometry-calculator`.
- From there, create sub-branches:
  - `feature/circle-area`: Implements circle area calculations.
  - `feature/rectangle-area`: Implements rectangle area calculations.

#### Step 2: Using Git Stash

- Before switching branches, stash unfinished changes:

```bash
git stash
```

- Restore stashed changes:

```bash
git stash pop
```

#### Step 3: Commit and Merge

- Implement features in both sub-branches.
- Push the changes and create pull requests to merge them into `dev`.
- Merge approved changes into `main`.

---

## 📦 Requirements

Ensure Python 3 is installed. Check your version with:

```bash
python --version
```

---

## 🤝 Collaborators
Harjeet




