# UCLA M148: Introduction to Data Science Project

Hello! This is the repository for our M148 project. Throughout the quarter, we applied the data science techniques we learned in class to analyze a dataset of our choice. We chose to analyze the [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset), with the initial goal of classifying songs into different genres based on their audio features. We also explored other aspects of the dataset, such as the relationship between audio features and popularity, and the distribution of genres in the dataset. 

Due to less than ideal results from our applied machine learning methods, our end goal morphed into developing our data science skills and learning how to work with a large dataset. You can find our final code below and interact with it however you would like! Hopefully you can learn something from our project as well, and have fun exploring the dataset!

If you would like to run through our entire project, check out our `final_code.ipynb` file. If you would like to look at some more modularized versions of our process, check out the files in the `Data` directory.

## Set-Up (for local development on VSCode)
1. Install VSCode from [here](https://code.visualstudio.com/).
2. Open VSCode and create a project directory by clicking on the "Open Folder" button on the welcome screen.
3. From the directory you created, open the terminal by pressing Ctrl+` (or by going to 'View > Terminal') and clone the repository by running the following command:
```bash
git clone https://github.com/atan9611/M148_Project.git
```
4. Create a virtual environment
    * Make sure you have Python installed on your system. If not, download it from [here](https://www.python.org/downloads/).
    * The `requirements.txt` file can be found in the utils directory in this repository.
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
5. Now you are free to make and run .ipynb files in the project directory!
    * Note: when running cells in a .ipynb file, select the virtual environment you created earlier when prompted by VSCode to select a kernel.
