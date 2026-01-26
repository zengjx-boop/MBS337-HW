expression_data = {
    "Gene1": {
        "ctrl": [10.5, 11.2, 10.8],
        "trmt": [25.3, 24.7, 26.1]
    },
    "Gene2": {
        "ctrl": [8.2, 8.5, 8.0],
        "trmt": [12.1, 11.8, 12.5]
    },
    "Gene3": {
        "ctrl": [15.0, 14.8, 15.2],
        "trmt": [18.5, 18.2, 18.8]
    }
}

def mean(values):
    return sum(values) / len(values)

significant_genes = []


for gene in expression_data:
    ctrl_values = expression_data[gene]["ctrl"]
    trmt_values = expression_data[gene]["trmt"]

    ctrl_mean = mean(ctrl_values)
    trmt_mean = mean(trmt_values)

    fold_change = trmt_mean / ctrl_mean

    if fold_change > 2.0 or fold_change < 0.5:
        significant_genes.append(gene)

    print(
        "{gene}: "
        "control mean = {control_mean:.2f}, "
        "treatment mean = {treatment_mean:.2f}, "
        "fold change = {fold_change:.2f}, "
        "\nSignificant genes:"
    )
for gene in significant_genes:
    print(gene)