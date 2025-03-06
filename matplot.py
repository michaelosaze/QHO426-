import matplotlib.pyplot as plt

age_group_labels = ["Children 0-18","Adults 19-25", "Adults 26-34", "Adults 35-54", "Adults 55-64", "Seniors 65+"]
age_group_populations = [75307800,27799100,39817700,81478600,42061700,52784400]
plt.pie(x=age_group_populations,labels=age_group_labels,autopct="%.2f%%",textprops={"fontsize": 14})
plt.title("population distribution by age groups")
plt.show()