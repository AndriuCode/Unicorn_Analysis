import pandas


def numerical_variable_variation(data):
    describe_values = data.describe().round(2)

    print("Valor Minimo: {}\nValor Maximo: {}\nRango: {}\nMedia: {}\nDesviacion Estandar: {}".format(
        describe_values[3],
        describe_values[7],
        describe_values[7] - describe_values[3],
        describe_values[1],
        describe_values[2]
    ))



def average(data, variable):

    variable_mean = data[variable].value_counts().mean()
    count_values_above_mean = len(data[variable].value_counts()[data[variable].value_counts() > variable_mean])
    total_unique_value = data[variable].nunique()
    percentage_above_mean = (count_values_above_mean / total_unique_value) * 100

    return round(percentage_above_mean, 2)