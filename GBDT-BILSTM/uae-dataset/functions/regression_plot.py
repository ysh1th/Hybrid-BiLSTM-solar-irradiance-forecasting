import matplotlib as plt
import seaborn as sns

def regression_plot(model_prediction, y_test):
  plt.figure(figsize=(10, 6))
  sns.scatterplot(x=y_test, y=model_prediction, color='blue', alpha=0.6, label='prediction vs actuals')

  max_val=max(max(y_test), max(model_prediction))
  min_val=min(min(y_test), min(model_prediction))
  plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', label="Perfect Fit (y=x)")

  plt.xlabel("Actual Values")
  plt.ylabel("Predicted Values")
  plt.title("Regression Plot: Predictions vs Actual Values")
  plt.legend()
  plt.grid(True)

  # Show the plot
  plt.show()