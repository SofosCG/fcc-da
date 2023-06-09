import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("./medical_examination.csv")

# Add 'overweight' column
df["overweight"] = ((df["weight"]/(df["height"]/100)**2)>25).astype("int8")

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["gluc"] = (df["gluc"]>1).astype("int8")
df["cholesterol"] = (df["cholesterol"]>1).astype("int8")

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df[["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]])

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat["cardio"] = pd.concat([df["cardio"],df["cardio"],df["cardio"],df["cardio"],df["cardio"],df["cardio"]], ignore_index=True)
    
    # Draw the catplot with 'sns.catplot()'
    fig=sns.catplot(data=df_cat, x="variable", col="cardio", kind="count", hue="value")
    fig.set(ylabel="total")
    
    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi'])&
                 (df['height'] >= df['height'].quantile(0.025))&
                 (df['height'] <= df['height'].quantile(0.975))&
                 (df['weight'] >= df['weight'].quantile(0.025))&
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(6,6))

    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, annot=True, mask=mask).get_figure()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
