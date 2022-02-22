import matplotlib.pyplot as plt
import numpy as np


# Funkcja tworzy sprecyzowany wykres kołowy.
def diff_pie(data, title):
        labels = ['2020↑', '2020↓']
        plt.pie(x=(data['Difference'] > 0).value_counts(), colors=['#77DD76', '#FF6962'], labels=labels
                , autopct='%1.1f%%')
        plt.title(title)
        plt.legend(loc='lower center', labels=['Większe dochody w 2020', 'Mniejsze dochody w 2020'])
        fig = plt.gcf()
        fig.set_size_inches(7, 7)
        plt.show()

# Funkcja tworzy sprecyzowany wykres słupkowy.
def avg_bar(data, title):
        # Zapobiegniecie zmian argumentu.
        data = data.copy(deep=True)
        data = data.sort_values(by=['average_income'])
        if len(data['id']) < 20:
                labels = data['Name']
        y_pos = np.arange(len(data['average_income']))
        plt.bar(x=y_pos, height=data['average_income'], align='center')
        if len(data['id']) < 20:
                plt.xticks(y_pos, labels, rotation=60)
        plt.ylabel('Średni dochód')
        plt.title(title)
        fig = plt.gcf()
        fig.set_size_inches(10, 8)
        plt.show()
