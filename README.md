# pyarmy

## Installation Instructions

### Installing with a Batch Script

1. Open your Visual Studio Code workspace.
2. Right-click on the `pyarmy` folder.
3. Select **Open in Integrated Terminal**.
6. In the integrated terminal, run the `.bat` file by typing:
    ```bash
    install.bat
    ```

### Installing a Virtual Environment Manually (don't do this, use the batch script instructions instead)

1. Open your Visual Studio Code workspace.
2. Right-click on the `pyarmy` folder.
3. Select **Open in Integrated Terminal**.
4. Create a virtual environment by typing:
    ```bash
    py -m venv .pyarmy
    ```
5. Activate the virtual environment by typing:
    ```bash
    .pyarmy\Scripts\activate
    ```
6. Install `pygame` by typing:
    ```bash
    python -m pip install pygame
    ```
