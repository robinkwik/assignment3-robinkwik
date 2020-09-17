# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 18:48:00 2020

@author: robin
"""

" Spectral Reflectance Calculation from Raw DN (TXT --> EXCEL File) "

def ASDSpectralReflectance(fileName):
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
    print(col_index)    # Prints column index for use in identifying correct columns for each sample point.

    point_01_cols = input("Enter the column index numbers for sample point 1 (with a space between each column #): ")   # This identifies the columns with data for each sample point (identified through col_index)
    w1_01_cols = list(point_01_cols.split())    # Splits the input column values by the spaces between them and inputs into a list.
    point1 = [int(i) for i in w1_01_cols]       # This gives the integer version of the sample point string list.
    
    w1_01 = df.iloc[:, point1]  # Locate columns specified in the point 1 list and assign them to a variable.
    col_avg_1 = w1_01.mean(axis=1)  # Calculates the average of the sample point columns.
    refl1 = input("Specify column # representing whiteboard reflectance for point 1: ") # Represents which column data corresponds to the whiteboard measurement.
    refl1 = list(refl1)
    refl1 = [int(i) for i in refl1]       # Convert list to integer values.
    refl1_test = df.iloc[:, refl1]
    refl1_test_2 = refl1_test.mean(axis=1)  # Locate white board reference values and calculate mean.
    point1_reflectance = (col_avg_1)/(refl1_test_2)     # Calculate spectral reflectance for point 1 (average of columns for point 1 / whiteboard reflectance values)
    
    w1_02_cols = input("Enter the column index numbers for sample point 2 (with a space between each column #): ")
    w1_02_cols = list(w1_02_cols.split())
    point2 = [int(i) for i in w1_02_cols]
    w1_02 = df.iloc[:, point2]
    col_avg_2 = w1_02.mean(axis=1)
    refl2 = input("Specify column # representing whiteboard reflectance for point 2: ")
    refl2 = list(refl2)
    refl2 = [int(i) for i in refl2] 
    refl2_test = df.iloc[:, refl2]
    refl2_test_2 = refl2_test.mean(axis=1)
    point2_reflectance = (col_avg_2)/(refl2_test_2)
    
    wavelength = df.iloc[:, 0]
    excel_filename = 'spectralReflectance.xlsx'
    sheetName = 'reflectance'
    reflectance_df = pd.DataFrame({'Wavelength (nm)': wavelength, 'Point 1 reflectance': point1_reflectance, 'Point 2 reflectance': point2_reflectance})
    reflectance_df.to_excel(excel_filename, sheet_name= sheetName, index=False)
    
    file_path = os.path.dirname(os.path.realpath(excel_filename))
    print("Output NDVI file", excel_filename, " has been saved to: ", file_path)
    
def specReflPlot(excel_file):
    import pandas as pd
    import os
    import matplotlib
    
    plot_data = pd.read_excel(excel_file, sheet_name='reflectance')
    
    # Plot spectral reflectance (y-axis) vs wavelength in nm (x-axis)
    list_p1_refl = plot_data.iloc[:, 1]
    list_p2_refl = plot_data.iloc[:, 2]
    wavelength = plot_data.iloc[:, 0]
    
    plot_df = pd.DataFrame({
    "wavelength (nm)": wavelength,
    "reflectance point 1": list_p1_refl,
    "reflectance point 2": list_p2_refl
})
    
    specrefl1 = plot_df.plot.line(x="wavelength (nm)", y="reflectance point 1", title = 'Spectral Reflectance of Wheat (Point 1) May 27, 2020', colormap = 'viridis')
    specrefl2 = plot_df.plot.line(x="wavelength (nm)", y="reflectance point 2", title = 'Spectral Reflectance of Wheat (Point 2) May 27, 2020', colormap = 'copper')
    specrefl1.set_ylabel("Spectral Reflectance")
    specrefl2.set_ylabel("Spectral Reflectance")
    specrefl1.set_xlabel("Wavelength (nm)")
    specrefl2.set_xlabel("Wavelength (nm)")
