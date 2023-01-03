import sys
import csv


# python graphing_mental_health_cases.py graphing_file.csv IDs.pdf

import numpy as np 
import matplotlib.pyplot as plt


def main(argv):

  
  if len(argv) != 3:
        print("Usage:",
              "create_ON_phu_cases_plot.py <data file> <graphics file>")
        sys.exit(-1)


  csv_filename = argv[1]
  graphics_filename = argv[2]

  
  try:
    file_fh = open(csv_filename, encoding="utf-8-sig")

  except IOError as err:
    print("Unable to open names file '{}' : {}".format(csv_filename, err),   
           file=sys.stderr)
    sys.exit(1)

  
  fileReader = csv.reader(file_fh)

  fig = plt.figure()

     
  depressive_cases = [] #deprresood
  anxiety_cases = [] #anxiety
  index = [] #age #+ year

  next(fileReader)
  for row_data_fields in fileReader:
      
    depressive_cases.append(int(row_data_fields[0]))
    anxiety_cases.append(int(row_data_fields[1]))
    index.append(row_data_fields[3] + "\n" + " (" + row_data_fields[2] + ")")


  plt.xlabel("Age-range by Year")
  plt.ylabel("% of Cases")
  plt.title("Proportion of Positive Screens for Major Depressive Disorder and Generalized Anxiety Disorder")

  X_axis = np.arange(len(index))



  plt.bar(X_axis - 0.2, depressive_cases , 0.4, label="depression")
  plt.bar(X_axis + 0.2, anxiety_cases, 0.4, label="anxiety")

  plt.xticks(X_axis, index)
  plt.legend()


  fig.savefig(graphics_filename, bbox_inches="tight")


  plt.show()
  

    
main(sys.argv)


