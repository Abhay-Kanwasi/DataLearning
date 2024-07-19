# Pandas

#### Defination:  
Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.
Pandas is called "pandas" because it helps manage and analyze "panel data," which is data that tracks the same subjects over time. The name also has a playful connection to the cute animal, making it easy to remember.

#### Why Use Pandas?

`Data Manipulation:` Pandas provides powerful tools for manipulating data, such as filtering, grouping, merging, and reshaping datasets.

`Data Cleaning:` It has functions to handle missing data, duplicate data, and other common data cleaning tasks, making it easier to prepare data for analysis.

`Data Analysis:` Pandas allows for easy computation of descriptive statistics and other summary operations on data, making it straightforward to analyze datasets.

`Data Reading and Writing:` It supports reading from and writing to various file formats like CSV, Excel, SQL databases, and more, simplifying the process of importing and exporting data.

`Performance:` Pandas is optimized for performance, making it faster and more efficient for handling large datasets compared to traditional Python data structures like lists and dictionaries.

`Integration:` It integrates well with other data science libraries like NumPy, Matplotlib, and Scikit-Learn, allowing for seamless workflow in data analysis and machine learning tasks.

Sure! Here's an updated version of the instructions for both Ubuntu and Windows:

### Prerequisites 

#### Ubuntu
If you don't have `python3` and `pip` installed on your system, install them using the following commands:

```bash
sudo apt install python3
sudo apt install python3-pip
```

#### Windows
If you don't have `python3` and `pip` installed on your system, follow these steps:

1. Download and install Python from the official website: [Python Downloads](https://www.python.org/downloads/).
2. During installation, make sure to check the box that says "Add Python to PATH."
3. Open Command Prompt and verify the installation by running:
   ```bash
   python --version
   pip --version
   ```

### Installation 

On both Ubuntu and Windows, you can install pandas using pip:

```bash
pip install pandas
```

Now we will start learning pandas from basics.

## What is series ?

A pandas series is like a column in a table. It is one-dimensional array holding data of any type.

## What is Labels ?

If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

This label can be used to access a specified value.