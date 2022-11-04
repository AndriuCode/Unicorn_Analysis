import logging
import seaborn as sns
import matplotlib.pyplot as plt



color = '#20c67a'



def bargraph_without_delimitation(data, variable, size, title, above_average):
    
    plt.figure(figsize=size)

    (
        data[variable]
        .value_counts()
        .reset_index()
        .rename({'index': variable, variable: 'Count'},  axis=1)
        .pipe(
            lambda df: (
                sns.barplot(
                    x=df['Count'],
                    y=df[variable],
                    color=color
                )
            )
        )
    )

    plt.axvline(x=data[variable].value_counts().mean(), linestyle='--', color='red', label='Mean')

    plt.title(title, fontsize=15)

    plt.legend()
    plt.show()
    
    logging.info("{}% above average".format(above_average, variable))



def bargraph_with_delimitation(data, variable, delimitation, size, title, above_average):
    
    plt.figure(figsize=size)

    (
        data[variable]
        .value_counts()
        .reset_index()
        .rename({'index': variable, variable: 'Count'},  axis=1)
        .head(delimitation)
        .pipe(
            lambda df: (
                sns.barplot(
                    x=df['Count'],
                    y=df[variable],
                    color=color
                )
            )
        )
    )

    plt.axvline(x=data[variable].value_counts().mean(), linestyle='--', color='red', label='Mean')

    plt.title(title, fontsize=15)

    plt.legend()
    plt.show()
    
    logging.info("{}% above average".format(above_average, variable))



def histplot_variable_variation(data, variable, size, title):
    
    plt.figure(figsize=size)

    sns.histplot(x=data[variable], bins=200, kde=True, color=color)

    plt.title(title, fontsize=15)

    plt.show()