from sklearn.pipeline import Pipeline
from joblib import dump
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config.config import BASE_DIR, MODELS_DIR, REPORT_DIR

def update_model(model: Pipeline) -> None:
    model_dir = MODELS_DIR / 'models.pkl'
    dump(model, model_dir)

def save_simple_metrics_report(train_score: float, test_score:float, validation_score: float, model:Pipeline) -> None:
    with open(REPORT_DIR / 'report.txt', 'w') as report_file:
        report_file.write('# Model Pipeline Description')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}:{value.__repr__()}' + '\n')

        report_file.write('### Train score: {train_score}'+ '\n')
        report_file.write('### Train score: {test_score}'+ '\n')
        report_file.write('### Train score: {validation_score}')

def get_model_performance_test_set(y_real: pd.Series, y_pred:pd.Series) -> None:
    fig, ax = plt.subplots()
    fig.set_figheight(8)
    fig.set_figwidth(8)
    sns.regplot(x=y_pred, y=y_real)
    ax.set_xlabel('Predicted worldwide gross')
    ax.set_ylabel('Real worldwide gross')
    ax.set_title('Behavior of model prediction')
    fig.savefig(REPORT_DIR / 'prediction_behavior.png')