# 📊 Contrast Stretching Script

This repository contains a Python script for performing contrast stretching on image data stored in an Excel file.

## 📋 Table of Contents
- [📖 Description](#-description)
- [✨ Features](#-features)
- [🛠️ Requirements](#-requirements)
- [💾 Installation](#-installation)
- [🚀 Usage](#-usage)
- [📝 Example](#-example)
- [🙏 Acknowledgements](#-acknowledgements)

## 📖 Description

The script reads image data from an Excel file, performs contrast stretching to enhance the image, and saves the processed image data back to a new Excel file. Contrast stretching is a simple image enhancement technique that improves the contrast of an image by stretching the range of pixel values.

## ✨ Features

- Reads image data from an Excel file.
- Converts the data to a NumPy array for processing.
- Performs contrast stretching on the pixel values.
- Saves the contrast-stretched data to a new Excel file.
- Prints the processed data and the file path of the saved data.

## 🛠️ Requirements

- Python 3.x
- pandas
- numpy

## 💾 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Renanuya/contrast-strecthing-python/.git
   cd contrast-stretching-script
   ```

2. Install the required Python packages:
   ```sh
   pip install pandas numpy
   ```

## 🚀 Usage

1. Place your input Excel file (`example_data.xlsx`) in the `data` directory.

2. Run the script:
   ```sh
   python main.py
   ```

3. The script will process the data and save the contrast-stretched image data to `contrast_stretched_example_data.xlsx` in the `data` directory. The processed data and the file path will be printed to the console.

## 📝 Example

Input data:
```
data/example_data.xlsx
```

Output data:
```
data/contrast_stretched_example_data.xlsx
```

## 🙏 Acknowledgements

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)

Feel free to reach out if you have any questions or need further assistance!
