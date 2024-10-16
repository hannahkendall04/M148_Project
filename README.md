# M148 Project

## Set-Up (for local development on VSCode)
1. Install VSCode from [here](https://code.visualstudio.com/).
2. Open VSCode and create a project directory by clicking on the "Open Folder" button on the welcome screen.
3. From the directory you created, open the terminal by pressing Ctrl+` (or by going to 'View > Terminal') and clone the repository by running the following command:
```bash
git clone https://github.com/atan9611/M148_Project.git
```
4. Create a virtual environment
    * Make sure you have Python installed on your system. If not, download it from [here](https://www.python.org/downloads/).
    * On Mac:
    ```bash
    python -m virtualenv env
    source venv/bin/activate
    pip install -r requirements.txt
    ```
    * On Windows:
    ```bash
    python -m virtualenv env
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
5. Now you are free to make and run .ipynb files in the project directory.

