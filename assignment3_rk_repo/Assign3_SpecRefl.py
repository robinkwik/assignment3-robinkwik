# -*- coding: utf-8 -*-
"""

Usage:
Program calculates spectral reflectance of winter wheat plants from analytical spectral device (ASD) data.

Inputs:
For first function,
1) CSV of ASD data from fieldwork ('Paul_20200527.csv').
    
For second function,
2) XLSX file from first function output ('spectralReflectance.xlsx').
    
Outputs:
1) Excel file (XLSX) of wavelength (nm), and sample point spectral reflectance.
2) Plot of sample point spectral reflectance vs wavelength (nm).
    
Notes:
For more information on ASD devices, refer to the following link: http://www.geo-informatie.nl/courses/grs60312/material2017/manuals/600860-dHH2Manual.pdf
Programs used to convert ASD data to CSV file: ViewSpecPro (ASCII Export --> TXT file), Microsoft Excel (TXT --> CSV).
ASD captures wavelengths from visible (325nm) to near infrared (1075nm).

Warning:
Ensure test files are stored in same location as working directory for program to properly execute!
    
"""

def ASDSpectralReflectance(fileName, sp1cols, sp2cols, wb):
    import pandas as pd
    import os
    
    done = False
    while not done:
        try:
            df = pd.read_csv(fileName)
            done = True
        except IOError: 
            print("Please enter a valid .csv file.")
            break
        except ValueError: 
            print("File contents invalid. Please enter a valid .csv file.")
            break
        
    col_index = [f"{c[0]}:{c[1]}" for c in enumerate(df.columns)]   # Obtains index of column header values, uses list comprehension inspired by: https://pbpython.com/selecting-columns.html. 
    # Use col_index when inputting ASD data from scratch and specifying columns for each point.
    
    w1_01_cols = list(sp1cols.split())    # Splits the input column values by the spaces between them and inputs into a list.
    point1 = [int(i) for i in w1_01_cols]       # This gives the integer version of the sample point string list.
    w1_01 = df.iloc[:, point1]  # Locate columns specified in the point 1 list and assign them to a variable.
    col_avg_1 = w1_01.mean(axis=1)  # Calculates the average of the sample point columns.
    refl1 = list(wb)
    refl1 = [int(i) for i in refl1]       # Convert list to integer values.
    refl1_test = df.iloc[:, refl1]
    refl1_test_2 = refl1_test.mean(axis=1)  # Locate white board reference values and calculate mean.
    point1_reflectance = (col_avg_1)/(refl1_test_2)     # Calculate spectral reflectance for point 1 (average of columns for point 1 / whiteboard reflectance values)
    
    # This portion below repeats the above code, but for point 2.
    w1_02_cols = list(sp2cols.split())
    point2 = [int(i) for i in w1_02_cols]
    w1_02 = df.iloc[:, point2]
    col_avg_2 = w1_02.mean(axis=1)
    refl2 = list(wb)
    refl2 = [int(i) for i in refl2] 
    refl2_test = df.iloc[:, refl2]
    refl2_test_2 = refl2_test.mean(axis=1)
    point2_reflectance = (col_avg_2)/(refl2_test_2)
    
    wavelength = df.iloc[:, 0]      # Returns the CSV columns containing wavelength values.
    excel_filename = 'spectralReflectance.xlsx'     # Specifies output XLSX file name.
    sheetName = 'reflectance'       # Specifies output sheet name for XLSX file.
    reflectance_df = pd.DataFrame({'Wavelength (nm)': wavelength, 'Point 1 reflectance': point1_reflectance, 'Point 2 reflectance': point2_reflectance})    # Creates a dataframe of data for creation of XLSX file.
    reflectance_df.to_excel(excel_filename, sheet_name= sheetName, index=False)     # Uses dataframe to output to excel file with the specified file name and sheet name.
    
    file_path = os.path.dirname(os.path.realpath(excel_filename))       # Assigns the file path to a variable.
    print("Output NDVI file", excel_filename, " has been saved to: ", file_path)        # Outputs string informing user where output file was saved.
    
def specReflPlot(excel_file):       # Function for plotting spectral reflectance of winter wheat plants. Input it the output excel file from function #1.
    import pandas as pd
    
    plot_data = pd.read_excel(excel_file, sheet_name='reflectance')     # Reads excel file.
    
    # Plot spectral reflectance (y-axis) vs wavelength in nm (x-axis)
    list_p1_refl = plot_data.iloc[:, 1]     # Locates column data for sample point 1.
    list_p2_refl = plot_data.iloc[:, 2]     # Locates column data for sample point 2.
    wavelength = plot_data.iloc[:, 0]       # Locates column data for wavelength.
    
    plot_df = pd.DataFrame({
    "wavelength (nm)": wavelength,
    "reflectance point 1": list_p1_refl,
    "reflectance point 2": list_p2_refl
})
    
    # Customizing plots by changing colour, title, and setting axis labels.
    specrefl1 = plot_df.plot.line(x="wavelength (nm)", y="reflectance point 1", title = 'Spectral Reflectance of Wheat (Point 1) May 27, 2020', colormap = 'viridis')
    specrefl2 = plot_df.plot.line(x="wavelength (nm)", y="reflectance point 2", title = 'Spectral Reflectance of Wheat (Point 2) May 27, 2020', colormap = 'copper')
    specrefl1.set_ylabel("Spectral Reflectance")
    specrefl2.set_ylabel("Spectral Reflectance")
    specrefl1.set_xlabel("Wavelength (nm)")
    specrefl2.set_xlabel("Wavelength (nm)")
