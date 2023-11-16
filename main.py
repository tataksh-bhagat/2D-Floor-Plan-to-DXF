import cv2
import numpy as np
import os
import subprocess
import ezdxf
from svgpathtools import svg2paths

# Prompt the user for the path to the image
input_image_path = input("Enter the path to your image: ")

# Check if the provided path is valid
if not os.path.exists(input_image_path):
    print("The specified file does not exist. Please check the path and try again.")
else:
    # Read the image
    image = cv2.imread(input_image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply edge detection
    edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

    # Apply Gaussian blur for noise reduction
    blurred = cv2.GaussianBlur(edges, (5, 5), 0)

    # Threshold the image to ensure it is binary
    _, binary_image = cv2.threshold(blurred, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Use morphological operations to reduce the thickness of lines
    eroded = cv2.erode(binary_image, np.ones((2,2), np.uint8), iterations=1)
    dilated = cv2.dilate(eroded, np.ones((3,3), np.uint8), iterations=1)

    # Construct the output filename by replacing the original extension with .bmp
    output_bmp_path = os.path.splitext(input_image_path)[0] + '_refined_edges.bmp'

    # Save the refined edges image as a .bmp file
    cv2.imwrite(output_bmp_path, dilated)

    # Define the path for the output SVG
    output_svg_path = os.path.splitext(input_image_path)[0] + '_vectorized.svg'

    # Run Potrace, converting the bitmap to an SVG
    subprocess.run(['potrace', output_bmp_path, '-s', '-o', output_svg_path], check=True)

    # Check if the SVG was created successfully
    if os.path.exists(output_svg_path):
        print(f"SVG file created successfully at {output_svg_path}")
        
        # Convert SVG to DXF
        paths, attributes = svg2paths(output_svg_path)

        # Create a new DXF document
        doc = ezdxf.new(dxfversion='R2010')
        msp = doc.modelspace()

        for path in paths:
            for line in path:
                start_point = (line.start.real, line.start.imag)
                end_point = (line.end.real, line.end.imag)
                msp.add_line(start_point, end_point)

        # Save the DXF document
        output_dxf_path = os.path.join(os.path.dirname(input_image_path),'final.dxf')
        doc.saveas(output_dxf_path)
        print(f"DXF file created successfully at {output_dxf_path}")
    else:
        print("SVG file creation failed.")
