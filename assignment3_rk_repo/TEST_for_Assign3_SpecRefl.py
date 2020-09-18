# -*- coding: utf-8 -*-
"""
For use in testing Assign3_SpecRefl.py program.
Warning: Ensure test files are stored in same working directory as Assign3_SpecRefl.py for program to function properly.
"""
# Before executing, ensure that working directory is set to desired folder containing all test files from repository.

from Assign3_SpecRefl import ASDSpectralReflectance

asdpoint1 = '2 3 4 5 6'     # Used for testing. Represents columns from the CSV which correspond to measurements taken at sample point 1.
asdpoint2 = '7 8 9 10 11'   # Used for testing. Represents columns from the CSV which correspond to measurements taken at sample point 2.
wb = '1'                    # Used for testing. Represents column from the CSV which corresponds to measurement taken of white board.

ASDSpectralReflectance('Wheat_20200527.csv', asdpoint1, asdpoint2, wb)


from Assign3_SpecRefl import specReflPlot

specReflPlot('spectralReflectance.xlsx')        # Input is output excel file from execution of ASDSpectralReflectance function.
