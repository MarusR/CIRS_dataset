# Environment Setup Instructions

## Step-by-step Guide to Set Up the Python Environment

This document provides instructions for setting up a reproducible Python environment for the CIRS-DATASET project using `uv`, the ultra-fast modern Python package manager.

### Prerequisites

Ensure you have Python 3.11+ installed on your system. You can download it from the official Python website.

### Installation Steps

1. **Install `uv` if not already installed:**
   Open your terminal and run:
   ```bash
   pip install uv
   ```

2. **Create a virtual environment:**
   Navigate to the project directory and create a virtual environment:
   ```bash
   uv venv .venv
   ```

3. **Activate the virtual environment:**
   - For Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```
   - For Windows (PowerShell):
     ```bash
     .venv\Scripts\activate
     ```

4. **Install project dependencies:**
   With the virtual environment activated, install the required packages:
   ```bash
   uv pip install -r requirements.txt
   ```

5. **Updating packages:**
   If you need to update the packages in the future, you can run:
   ```bash
   uv pip install --upgrade -r requirements.txt
   ```

6. **Downloading and extraction raw data**:
   To obtain the raw data
   ```bash
   python scripts/downloadRawData.py
   ```

### Notes

- When adding new packages, remember to update the `requirements.txt` file by running:
  ```bash
  uv pip freeze > requirements.txt
  ```

Following these steps will ensure that your environment is set up correctly for the CIRS-DATASET project, allowing for reproducibility and ease of collaboration.