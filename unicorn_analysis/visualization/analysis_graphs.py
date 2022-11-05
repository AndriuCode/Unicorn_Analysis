import seaborn as sns
import matplotlib.pyplot as plt


def top_5_companies(data, main_variable, variable_1, variable_2, size, title_1, title_2):
    
    fig, axes = plt.subplots(2, 1, figsize=size)


    (
        data[[main_variable, variable_1]]
        .sort_values(by=variable_1, ascending=False)
        .head(5)
        .pipe(
            lambda df:(
                sns.barplot(
                    data=df,
                    x= main_variable,
                    y= variable_1,
                    color='#20c67a',
                    ax=axes[0]
                )
            )
        ) 
    )

    axes[0].set_title(title_1, fontsize=15)



    (
        data[[main_variable, variable_2]]
        .sort_values(by=variable_2, ascending=False)
        .head(5)
        .pipe(
            lambda df:(
                sns.barplot(
                    data=df,
                    x= main_variable,
                    y= variable_2,
                    color='#17BFD4',
                    ax=axes[1]
                )
            )
        ) 
    )

    axes[1].set_title(title_2, fontsize=15)

    fig.tight_layout()
    plt.show()




def companies_became_unicorns_trend(data, variable_1, variable_2, size, title):

    plt.figure(figsize=size)

    (
        data
        .groupby(variable_1)[variable_2]
        .sum()
        .reset_index()
        .pipe(
            lambda df: (
                sns.lineplot(
                    x=df[variable_1],
                    y=df[variable_2],
                    color='#20c67a'
                )
            )
        )
    )

    plt.title(title, fontsize=15)

    plt.show()




def countries_with_high_ROI_per_company(data, variable_1, variable_2, size, title):
    plt.figure(figsize=size)

    (
        data
        .groupby(variable_1)[[variable_2]]
        .sum()
        .round(2)
        .reset_index()
        .sort_values(by=variable_2, ascending=False)
        .head(10)
        .pipe(
            lambda df: (
                sns.barplot(
                    data= df,
                    x= variable_2,
                    y= variable_1,
                    color='#20c67a'
                )
            )
        )
    )

    plt.title(title, fontsize=15)

    plt.show()




def industry_with_high_ROI_US(data, variable_1, variable_2, size, title):
    plt.figure(figsize=size)

    (
        data
        .groupby(variable_1)[[variable_2]]
        .sum()
        .round(2)
        .reset_index()
        .sort_values(by=variable_2, ascending=False)
        .head(10)
        .pipe(
            lambda df: (
                sns.barplot(
                    data= df,
                    x= variable_2,
                    y= variable_1,
                    color= '#20c67a'
                )
            )
        )
    )

    plt.title(title, fontsize=15)

    plt.show()




def ROI_trend(data, variable_1, variable_2, size, title):
    plt.figure(figsize=size)

    (
        data
        .groupby(variable_1)[variable_2]
        .mean()
        .round(2)
        .reset_index()
        .pipe(
            lambda df: (
                sns.lineplot(
                    data=df,
                    x=variable_1,
                    y=variable_2,
                    color='#20c67a'
                )
            )
        )
    )

    plt.title(title, fontsize=15)

    plt.show()