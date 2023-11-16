# 2D Floor Plan to DXF
Automate the transformation of 2D house plan images into DXF files with this Python script. Utilizing OpenCV for image processing and Potrace for vectorization, this tool simplifies the conversion process, making it ideal for CAD applications. Streamline your workflow from image to DXF with ease and efficiency.

The script employs image processing techniques to enhance and vectorize an input image and then converts it into a DXF file. The resulting DXF file is compatible with various CAD software, enabling further editing or viewing.

## Instructions for New Users

### Prerequisites
- Python 3.7 or higher installed on your system.
- HomeBrew
#### Python Libraries
- NumPy: Used in conjunction with OpenCV for numerical operations.
- ezdxf: To create and manipulate DXF files.
- svgpathtools: For parsing SVG files.
- Subprocess: For running external commands, like Potrace.

### Set Up Python Virtual Environment

#### Create a New Environment
Create a new virtual environment by running the following command in your terminal:

```bash
python -m venv myenv
```

#### Activate the Environment
Activate the virtual environment with:

On Unix or MacOS:

```bash
source myenv/bin/activate
```

On Windows:

```cmd
myenv\Scripts\activate
```

#### Install Required Packages
Install the required packages using `pip`:

```bash
pip install opencv-python-headless
pip install numpy
pip install ezdxf
pip install svgpathtools
```

The following needs to be installed using `HomeBrew`:

```bash
brew install potrace
```

## Running the Script

1. **Open the Terminal or Command Prompt**.

2. **Navigate to the Directory Containing the Script**.
   - Use the `cd` command to change directories. For example:
     ```bash
     cd path/to/script/directory
     ```

3. **Run the Script**:
   - Execute the script with Python:
     ```bash
     python main.py
     ```

4. **Provide the Input Image Path**:
   - When prompted, enter the full path to your house plan image file. For example:
     ```bash
     /Users/username/Desktop/house_plan.jpg
     ```

5. **Wait for the Script to Process**:
   - The script will process the image and output a DXF file named `final.dxf` in the same directory as the input image.

6. **Check the Output**:
   - Navigate to the directory of your input image to find the `final.dxf` file.

## Key Libraries and Functions

### OpenCV (`cv2`)
A powerful library for image processing tasks.

- `cv2.imread`: Reads an image from a file.
- `cv2.cvtColor`: Converts images to different color spaces; used here for grayscale conversion.
- `cv2.Canny`: Performs edge detection.
- `cv2.GaussianBlur`: Reduces noise in the image.
- `cv2.threshold`: Applies a fixed-level threshold to the image.
- `cv2.erode`, `cv2.dilate`: Perform morphological operations.

### Subprocess
Used for running external commands within Python.

- `subprocess.run`: Executes the Potrace command for vectorizing the image.

### ezdxf
A Python package to create and modify DXF drawings.

- `ezdxf.new`: Initializes a new DXF document.
- `doc.modelspace()`: Accesses the drawing space for graphical entities.

### svgpathtools
Manipulates and analyzes SVG paths.

## Workflow

1. **Input**: User provides the path of the house plan image.
2. **Image Processing**: Includes grayscale conversion, edge detection, and refining using morphological operations.
3. **Vectorization**: Converts the processed BMP image to an SVG using Potrace.
4. **DXF Conversion**: Translates SVG paths into DXF format.
5. **Output**: Saves the final DXF file as `final.dxf`.

### Note
- The script is intended for simple 2D house plan images. The quality of the input image can affect the output.
- For complex or detailed images, additional manual editing in a CAD program might be necessary.

## Contributing

Contributions to enhance the script or add new features are highly encouraged. Feel free to fork the repository, make your changes, and submit a pull request.
