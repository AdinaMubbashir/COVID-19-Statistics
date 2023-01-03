
#
#   Packages and modules
#
import sys


import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt

from matplotlib import ticker as ticktools


def main(argv):

    if len(argv) != 3:
        print("Usage:",
                "create_ON_phu_cases_plot.py <data file> <graphics file>")
        sys.exit(-1)
    
    csv_filename = argv[1]
    graphics_filename = argv[2]


    # Open data file using "pandas"

    try:
        csv_df = pd.read_csv(csv_filename)

    except IOError as err:
        print("Unable to open source file", csv_filename,
                ": {}".format(err), file=sys.stderr)
        sys.exit(-1)

    print(csv_df)


    #plotting


    fig = plt.figure()

    plt.title("Rate of ICU Cases Among Vaccinated and Unvaccinated Individuals")
    ax1 = sns.lineplot(x = "DATE", y = "% of ICU_CASES", hue = "VACCINE_STATUS", data=csv_df)


    ax1.xaxis.set_major_locator(ticktools.MaxNLocator(6))

    plt.xticks(rotation = 45, ha = 'right')


    fig.savefig(graphics_filename, bbox_inches="tight")


    plt.show()

    #
    #   End of Function
    #



##
## Call our main function, passing the system argv as the parameter
##
main(sys.argv)

