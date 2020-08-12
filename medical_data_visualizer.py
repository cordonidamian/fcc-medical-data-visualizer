import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['overweight'] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[(df['weight'] / ((df['height']/100)**2)) >25, 'overweight'] = 1
df.loc[df['cholesterol'] <= 1, 'cholesterol'] = 0
df.loc[df['gluc'] <= 1, 'gluc'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars='cardio', value_vars=['active','alco','cholesterol','gluc','overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    # fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio').set_ylabels('total')

    g = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio').set_ylabels('total')

    fig = g.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    df_1 = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    

    df_1.reset_index(inplace=True)
    df_1 = df_1.drop(columns=['index'])

    #tc = round(df_1)
    tc = df_1

    # Calculate the correlation matrix
    corr = tc.corr()

    # Generate a mask for the upper triangle
    mask =np.triu(np.ones_like(corr, dtype=np.bool))





    # Set up the matplotlib figure
    #fig, ax = plt.subplots(figsize=(12, 12))
    fig, ax = plt.subplots(figsize=(12, 12))  
    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr,mask=mask, vmax=0.24, vmin=0.08, fmt='01.1f',center = 0, annot = True, linecolor ='white',cbar_kws = {'shrink' : .45, 'format' : '%.2f'}, linewidths = 1)

    


    # Do not modify the next two lines
    ax.figure.savefig('heatmap.png')
    return fig
