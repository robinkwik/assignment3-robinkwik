"""
Purpose : Plots line intensities 7.7/11.3 vs 6.2/11.3 PAH features for M31 and SINGS survey. This also
          saves a LaTex friendly table for PAH line intensities.

Inputs  : 1) Two data files that has Line intensities and their uncertainties for 11 PAH features.
          2) Table 4 from Smith at al. 2007

Outputs : 1) Plot of 7.7/11.3 vs 6.2/11.3 PAH features for M31 and SINGS survey
          2) Saves a LaTex friendly file with PAH line intensities and their uncertainties

Notes  :

"""

import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.ticker import AutoMinorLocator


# Define two arrays to get the atomic line intensity and its uncertainty from the files returned from PAHlines.pro IDL code
PAH_lines = []
PAH_lines_unc = []


PAH_fnames = np.loadtxt("PAHfilenames.dat" , dtype = 'string')  # Reading all the file names of files that has atomic line values

for name in PAH_fnames:
    Line_values = np.loadtxt(name,dtype = 'string',skiprows = 1)

    Line_val = [map(float, a.split()) for a in Line_values[:,0]]  # This line get rid of the power "e" in the atomic data files and make it 10 to the power.
    Line_val_unc = [map(float, a.split()) for a in Line_values[:,1]]

    PAH_lines.append(Line_val)  # Get lined strength into a table
    PAH_lines_unc.append(Line_val_unc)  # Get uncertainty of line streangth into a table


np.savetxt('PAHLines.txt', PAH_lines)
np.savetxt('PAHLines_unc.txt', PAH_lines_unc)

PAHvalues = []

def feature_plots(PAH_val6_2,PAH_val7_7,PAH_val11_3,PAH_unc6_2,PAH_unc7_7,PAH_unc11_3,data) :
    #Plotting  7.7/11.3 vs 6.2/11.3. key word "data" is an integer which defines which data set you want to plot. 1 = M31, 2 = SINGS

    xaxis = []
    yaxis = []
    x_err = []
    y_err = []
    for i in range(np.shape(PAH_val6_2)[0]):
        if PAH_val6_2[i] != 0 and PAH_val7_7[i] != 0 and PAH_val11_3[i] != 0 :

            xaxis.append(PAH_val6_2[i]/ PAH_val11_3[i])
            yaxis.append(PAH_val7_7[i]/ PAH_val11_3[i])
            y_err.append(math.sqrt(((PAH_unc7_7[i]/PAH_val11_3[i])**2) + ((PAH_unc11_3[i]/PAH_val7_7[i])**2)))
            x_err.append(math.sqrt(((PAH_unc6_2[i]/PAH_val11_3[i])**2) + ((PAH_unc11_3[i]/PAH_val6_2[i])**2)))


    y_err = (np.array(y_err)/np.array(yaxis))*0.434
    x_err = (np.array(x_err)/np.array(xaxis))*0.434
    W = 1/(y_err)

    X = [np.log10(a) for a in xaxis]  #use this for logscale
    Y = [np.log10(a) for a in yaxis]  #use this for logscale

    if data == 1:
     plt.errorbar(X,Y,y_err,x_err,'bo', markersize = 20, mfc = 'b', label = 'M31')

    else:
     plt.errorbar(X,Y,y_err,x_err,'s', color = '0.75', markersize = 20, mfc = 'white', label = 'Smith at al. 2007')

    plt.ylabel("Log(AF_7.7/ AF_11.3)", fontsize = 30)
    plt.xlabel("Log(AF_6.2/ AF_11.3)", fontsize = 30)
    plt.legend(loc='lower right',prop={'size':20})
    minorLocator   = AutoMinorLocator(5)
    ax = plt.subplot(111)
    ax.xaxis.set_minor_locator(minorLocator)
    #ax.yaxis.set_minor_locator(minorLocator)

    plt.tick_params(which='both', width=2)
    plt.tick_params(which='major', length=10)
    plt.tick_params(which='minor', length=7, color='k')

plt.show()

PAH_val= np.loadtxt("PAHLines.txt")
PAH_unc= np.loadtxt("PAHLines_unc.txt")

PAH_unc[np.isnan(PAH_unc)] = 0
PAH_val[np.isnan(PAH_val)] = 0



Num_regions = np.shape(PAH_fnames)[0]  # Number of regions
Num_features = 10 # Number of dust features that we are interested in
PAH_comb = np.zeros((Num_regions,Num_features))  # Defines an array to fill data
PAH_comb_unc = np.zeros((Num_regions,Num_features))  # Defines an array to fill data


PAH_comb[:,0] = PAH_val[:,0]  # 5.7 mu dust feature
PAH_comb[:,1] = PAH_val[:,1]  # 6.2 mu dust feature
PAH_comb[:,2] = np.array(PAH_val[:,2]) + np.array(PAH_val[:,3]) + np.array(PAH_val[:,4]) # 7.7 mu dust feature
PAH_comb[:,3] = PAH_val[:,5]  # 8.3 mu dust feature
PAH_comb[:,4] = PAH_val[:,6]  # 8.6 mu dust feature
PAH_comb[:,5] = PAH_val[:,7]  # 10.7 mu dust feature
PAH_comb[:,6] = np.array(PAH_val[:,8]) + np.array(PAH_val[:,9])  # 11.3 mu dust feature
PAH_comb[:,7] = PAH_val[:,10]  # 12.0 mu dust feature
PAH_comb[:,8] = np.array(PAH_val[:,11]) + np.array(PAH_val[:,12])  # 12.7 mu dust feature
#PAH_comb[:,9] = PAH_val[:,13] # 14.0 mu dust feature
PAH_comb[:,9] = np.array(PAH_val[:,14]) + np.array(PAH_val[:,15]) + np.array(PAH_val[:,16]) + np.array(PAH_val[:,17])


PAH_comb_unc[:,0] = PAH_unc[:,0]  # 5.7 mu dust feature
PAH_comb_unc[:,1] = PAH_unc[:,1]  # 6.2 mu dust feature
PAH_comb_unc[:,2] = np.array(PAH_unc[:,2]) + np.array(PAH_unc[:,3]) + np.array(PAH_unc[:,4]) # 7.7 mu dust feature
PAH_comb_unc[:,3] = PAH_unc[:,5]  # 8.3 mu dust feature
PAH_comb_unc[:,4] = PAH_unc[:,6]  # 8.6 mu dust feature
PAH_comb_unc[:,5] = PAH_unc[:,7]  # 10.7 mu dust feature
PAH_comb_unc[:,6] = np.array(PAH_unc[:,8]) + np.array(PAH_unc[:,9])  # 11.3 mu dust feature
PAH_comb_unc[:,7] = PAH_unc[:,10]  # 12.0 mu dust feature
PAH_comb_unc[:,8] = np.array(PAH_unc[:,11]) + np.array(PAH_unc[:,12])  # 12.7 mu dust feature
#PAH_comb_unc[:,9] = PAH_unc[:,13] # 14.0 mu dust feature
PAH_comb_unc[:,9] = np.array(PAH_unc[:,14]) + np.array(PAH_unc[:,15]) + np.array(PAH_unc[:,16]) + np.array(PAH_unc[:,17])



SINGS_PAH_val = []

SINGS_PAH = np.genfromtxt('SINGS',dtype='str')

for i in range(1,np.shape(SINGS_PAH)[1]):
    Line_val = [map(float, a.split()) for a in SINGS_PAH[:,i]]
    SINGS_PAH_val.append(Line_val)

np.savetxt('SINGS_PAH_val.txt', SINGS_PAH_val)
Sings_PAH= np.loadtxt("SINGS_PAH_val.txt")
feature_plots(Sings_PAH[0,:],Sings_PAH[2,:],Sings_PAH[8,:],Sings_PAH[1,:],Sings_PAH[3,:],Sings_PAH[9,:],2)

feature_plots(PAH_comb[:,1],PAH_comb[:,2],PAH_comb[:,6],PAH_comb_unc[:,1],PAH_comb_unc[:,2],PAH_comb_unc[:,6],1)
