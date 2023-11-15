import seaborn as sn
import pandas as pd
from biolearn.data_library import DataLibrary
from biolearn.model_gallery import ModelGallery
import matplotlib.pyplot as plt

"""
"Epigenetic Clocks" in GEO Data
=============================================================

This example loads a DNA Methylation data from GEO, calculates multiple epigenetic clocks, and plots them against chronological age. 
"""

#############################################################################
# First load up some methylation data from GEO using the data library
# ---------------------------------------

# Load up GSE41169 blood DNAm data
data_source = DataLibrary().get("GSE41169")  # Get the data source from the DataLibrary
data = data_source.load()  # Load the data from the data source

# The data has the methylation data as well as metadata for each subject
methylation_data = data.dnam  # Extract the methylation data from the loaded data


######################################################################################
# Now run three different clocks on the dataset to produce epigenetic clock ages
# ------------------------------------------------------------------------------------

# Create an instance of ModelGallery
gallery = ModelGallery()

# Note that by default clocks will impute missing data.
# To change this behavior set the imputation= parameter when getting the clock
horvath_results = gallery.get("Horvathv1").predict(methylation_data)
hannum_results = gallery.get("Hannum").predict(methylation_data)
phenoage_results = gallery.get("PhenoAge").predict(methylation_data)

##########################################################################################################
# Finally extract the age data from the metadata from GEO and plot the results using seaborn
# --------------------------------------------------------------------------------------------------------
# Extract the actual age from the metadata
actual_age = data.metadata["age"]
# Create a DataFrame for plotting
plot_data = pd.DataFrame(
    {
        "Horvath": horvath_results,
        "Hannum": hannum_results,
        "PhenoAge": phenoage_results,
        "Age": actual_age,
    }
)
# Set the index of the DataFrame to be the actual age
plot_data.index = plot_data["Age"]

sn.relplot(data=plot_data, kind="scatter")  # Create a scatter plot using seaborn
plt.savefig("outputs/epigenetic_clocks_on_geo.png")  # Save the plot as a .png file
