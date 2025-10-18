You're on the right track — this is a clean and modern setup using `uv`, which is great for reproducible environments. However, to make **Jupyter Notebook work in VS Code**, we need to **add a step** to install and register the `ipykernel` in the virtual environment.

---

## ✅ Updated Setup Instructions (Corrected)

Here’s a revised version of your setup guide with the missing `ipykernel` installation and kernel registration added:

---

### 📄 **Environment Setup Instructions**

## Step-by-step Guide to Set Up the Python Environment

This document provides instructions for setting up a reproducible Python environment for the **CIRS-DATASET** project using [`uv`](https://github.com/astral-sh/uv), the ultra-fast modern Python package manager.

---

### ✅ Prerequisites

Ensure you have **Python 3.11+** installed on your system. You can install it via your system package manager or from the official [Python website](https://www.python.org/downloads/).

---

### 🚀 Installation Steps

1. **Install `uv` if not already installed:**

   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**

   ```bash
   uv venv .venv
   ```

3. **Activate the virtual environment:**

   * **Linux/macOS:**

     ```bash
     source .venv/bin/activate
     ```
   * **Windows (PowerShell):**

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

4. **Install project dependencies:**

   ```bash
   uv pip install -r requirements.txt
   ```

5. **Register the virtual environment as a Jupyter kernel (for VS Code and notebooks):**

   ```bash
   uv pip install ipykernel
   python -m ipykernel install --user --name=cirs-env --display-name "Python (cirsDataSet)"
   ```

6. **Run the data download script:**

   ```bash
   python scripts/downloadRawData.py
   ```

---

### 🔄 Updating Packages

To upgrade all dependencies:

```bash
uv pip install --upgrade -r requirements.txt
```

---

### 📝 Notes

* To add new packages:

  ```bash
  uv pip install <package>
  uv pip freeze > requirements.txt
  ```
* The virtual environment will now show up in **VS Code** under the name `Python (cirsDataSet)` when selecting a Jupyter kernel.

---

### 📦 Example `requirements.txt` (if missing)

Make sure your `requirements.txt` includes at least:

```
jupyter
ipykernel
# plus your other project dependencies
```

You can generate it with:

```bash
uv pip freeze > requirements.txt
```

