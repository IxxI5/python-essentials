# Python Essentials

This repository provides the essentials for learning **Python** from scratch using just **VS Code** as the IDE, guiding you through setting up **Python** and **Jupyter** in **Visual Studio Code (VS Code)** for writing and running `.py` and `.ipynb` files.

## Prerequisites

- Install **VS Code**: [Download here](https://code.visualstudio.com/)
- Install **Python**: [Download here](https://www.python.org/downloads/)

  - Make sure to check **"Add Python to PATH"** during installation.

- Open **VS Code**

- **VS Code**: Press `Ctrl + Shift + X` to open the **Extensions** (or click on icon). Search for and install:

  - **Python** (by Microsoft)
  - **Jupyter** (by Microsoft)
  - **Python Test Explorer** (by Little Fox Team)

- **Create** a project folder e.g. `my-project`

- **Create** a python file named `example.py` and type the following lines:

  ```python
  # example.py

  # Get user's name
  name = input("What is your name? ")

  # Print out a greeting
  print(f"Hello, {name}!")
  ```

- **VS Code**: Open the **VS Code terminal** (`Ctrl + "` or select `View`) and run:

  ```sh
  cd my-project

  pip install jupyter pandas numpy matplotlib seaborn
  ```

  These packages allow you to use Jupyter notebooks and perform data analysis efficiently.

- **VS Code**: Ensure VS Code uses the correct Python version.

  - Open **Command Palette** (`Ctrl + Shift + P`)

  - Search for **"Python: Select Interpreter"**

  - Choose the installed Python version

## Running Python Scripts (`.py`)

- Open the `example.py` file in VS Code.
- Click the **Run button** (▶) or press `F5` to execute.
- Alternatively, run the script in the terminal:

  ```sh
  python example.py
  ```

## Running Jupyter Notebooks (`.ipynb`)

- Open an `.ipynb` file in VS Code.
- Click **"Run Cell"** to execute code blocks.

---

✅ You are now ready to write and run Python scripts and Jupyter notebooks in VS Code! 🚀

## Mastering Python: A Stress-Free Alternative to Online Videos

Learning to code from online videos can be overwhelming, especially for beginners. This **Python** tutorial offers a more efficient approach, reminiscent of pre-internet learning. We'll focus on practical examples, building your understanding step by step:

- First, open `python-essentials` git repository in your browser (do **not** download it) and follow the setup instructions in **README.md**.

- Launch **VS Code** and create the project structure:

  - **Create** the `python-essentials/01-basics/01-basics.py`

  - **Read** the code from the first example e.g. `01-basics.py` in your browser and type it (**NO copy/paste**) into your VS Code file

  - **Run** the code, then experiment by changing parts and observing the results

  - **Revert** the changes to the original

  - **Continue** this process for each example, building your experience and understanding through active experimentation, rather than passive memorization.
