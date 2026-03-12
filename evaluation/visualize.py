import matplotlib.pyplot as plt

def plot_results(actual, predicted):
    plt.scatter(actual, predicted)
    plt.title('Prediction vs Actual')
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.plot([min(actual), max(actual)], [min(actual), max(actual)], color='red')
    plt.show()
