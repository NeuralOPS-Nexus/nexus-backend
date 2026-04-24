# Contributing to NeuralOps Nexus Backend
First off, thank you for considering contributing to NeuralOps Nexus! It's people like you that make this system powerful.

This document outlines the standard workflow for contributing to the neuralops-nexus-backend repository. Please read through these guidelines completely before starting your work to ensure a smooth review and merge process.

---

## 📋 Step 1: Finding a Task
Before writing any code, you need to select an approved task.

Navigate to our official **Project Task Board** ([refer to the project link provided in Discord](https://github.com/orgs/NeuralOPS-Nexus/projects/3)).

Look for tasks that are marked as **"Ready to Do"**.

Ensure the task you select has **no pending dependencies**.
Assign the task to yourself or leave a comment so others know you are working on it.

## 🍴 Step 2: Forking the Repository
We use a standard Fork-and-Pull workflow.

Go to the ([main repository](https://github.com/mapax-io/neuralops-nexus-backend)).

Click the "Fork" button in the top right corner.

**CRITICAL:** When the fork configuration screen appears, deselect the option that says "Copy only the main branch". We need you to have access to all branches (especially dev).

Complete the fork to your personal GitHub account.

## 💻 Step 3: Local Environment Setup
Now, clone your fork locally and link it back to the main repository to keep your code up to date.

Open your terminal and run the following commands (replace <your-username> with your actual GitHub username):

Bash
#### 1. Clone your forked repository (we recommend cloning into a folder named 'neuralops')
git clone git@github.com:<your-username>/nexus-backend.git neuralops

#### 2. Navigate into the project directory
cd neuralops/

#### 3. Add the original Mapax-io repository as the "upstream" remote
git remote add upstream https://github.com/mapax-io/neuralops-nexus-backend.git

#### 4. Verify your remotes (You should see 'origin' pointing to your fork and 'upstream' pointing to mapax-io)
git remote -v
#### 🌱 Step 4: Branching Strategy
Never work directly on main or dev. Always create a new branch for your work. We use a strict naming convention based on the type of task.

Create and checkout your branch based on the following patterns:

For New Features: feature/<subtask-name>

```bash
git checkout -b feature/user-auth-module
```
For Bug Fixes / Issues: issue/<subtask-name>

```bash
git checkout -b issue/fix-database-timeout
```
## 🛠 Step 5: Making Changes and Committing
Write your code, write tests if applicable, and ensure everything runs locally.

When committing your changes, your commit messages must be descriptive. Include the feature/issue ID, the name of the task, and relevant details.

```bash
##### Stage your changes
git add .
```

#### Commit with a detailed message
git commit -m "feat(ID-123): Implement user auth module. Added JWT validation in apps/auth.py and updated the base models."
## 🚀 Step 6: Pushing to Your Fork
Once your work is committed, push your branch to your forked repository (origin).
```bash
# Push your branch to origin and set the upstream tracking
git push -u origin <your-branch-name>
# Example: 
git push -u origin feature/testchange-usman
```

After the push is successful, your terminal will usually output a direct link to create a Pull Request. It will look something like this:
https://github.com/<your-username>/nexus-backend/pull/new/<your-branch-name>

## 📥 Step 7: Creating the Pull Request (PR)
Click the link provided in your terminal, or go to your GitHub fork to open the Pull Request.

CRITICAL PR INSTRUCTIONS:

Change the Destination Branch: By default, GitHub might try to merge into main. You MUST change the base branch to dev (the destination branch for all active development).

Detailed Description: **Do not leave the PR description blank**. You must write a full, detailed breakdown of your PR, including:



**What code/logic did you add or change?**

**Which specific files were modified or created?**

**Why was this approach taken?**

**Any specific areas you want the reviewer to look at closely.**

Click the "Create Pull Request" button.

## 💬 Step 8: Code Review and Communication
Your work isn't done just because the PR is open!

**Jump into our Discord channel.**

Send a message letting the team know your PR is up. Include a link to the PR and a brief 1-sentence summary of what it does.

A maintainer will review your code. Be prepared to answer questions or make requested changes based on their feedback.

Once approved, a maintainer will merge your branch into dev.

Thank you for contributing! Let's build the Nucleus.