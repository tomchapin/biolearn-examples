import seaborn as sn
import matplotlib.pyplot as plt
from biolearn.hematology import phenotypic_age
from biolearn.load import load_nhanes
from lifelines import KaplanMeierFitter

"""
"Phenotypic Ages" in NHANES Data
=============================================================

This example loads blood exam data from NHANES 2010, calculates "Phenotypic Ages," and performs survival analyses by phenotypic age. 
"""

#############################################################################
# Loading NHANES 2010 data
# ---------------------------------------
year = 2010  # Setting the year for the data to be loaded
df = load_nhanes(year)  # Loading the NHANES data for the specified year
df["years_until_death"] = (
    df["months_until_death"] / 12
)  # Converting months until death to years

#############################################################################
# Calculate "biological age" based on PhenotypicAge
# ------------------------------------------------------

df["phenotypic_age"] = phenotypic_age(df)

#############################################################################
# Show relation between biological age and chronological age
# ---------------------------------------------------------------

sn.scatterplot(data=df, x="age", y="phenotypic_age", s=2)

# Saving the plot as a .png file
plt.savefig("outputs/phenotypic_age_vs_chronological_age.png")

############################################################################################################################
# Plot survival curve for people with accelerated aging (older biological age) vs decelerated aging (younger biological age)
# --------------------------------------------------------------------------------------------------------------------------
# Creating a new column to identify individuals with accelerated aging
df["biologically_older"] = df["phenotypic_age"] > df["age"]

# Creating a subplot for the survival curves
ax = plt.subplot()

groups = df["biologically_older"]  # Defining the groups for the survival analysis

# Identifying the individuals with decelerated aging
ix = groups == 0

# Defining the time variable for the survival analysis
T = df.years_until_death

# Defining the event variable for the survival analysis
E = df.is_dead

kmf = KaplanMeierFitter()

# Fitting the survival curve for the decelerated aging group
kmf.fit(T[ix], E[ix], label="Biologically younger")

# Plotting the survival curve for the decelerated aging group
ax = kmf.plot_survival_function(ax=ax)

# Fitting the survival curve for the accelerated aging group
# T is the time variable
# E is the event variable
kmf.fit(T[~ix], E[~ix], label="Biologically older")

# Plotting the survival curve for the accelerated aging group
ax = kmf.plot_survival_function()

# Setting the x and y labels
plt.ylabel("Survival")
plt.xlabel("Years")

# Saving the plot as a .png file
plt.savefig("outputs/survival_by_phenotypic_age.png")
