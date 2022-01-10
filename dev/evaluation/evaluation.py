from sklearn.metrics import precision_recall_curve, auc
import numpy as np
import pandas as pd


def evaluation(
    pred: np.ndarray, y: np.ndarray, display=True
) -> list[int, int, int, int]:
    """[summary]

    Args:
        pred (np.ndarray): [description]
        y (np.ndarray): [description]
        display (bool, optional): [description]. Defaults to True.

    Returns:
        list[int, int, int, int]: [description]
    """
    confusion_mat = confusion_matrix(y, pred)

    tn, fp, fn, tp = confusion_mat.ravel()

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    if display:
        print("TN / FP \nFN / TP")
        print(confusion_mat)
        print(f"Precision : {precision}")
        print(f"Recall : {recall}")
        print(f"F1_Score : {f1_score}")

    return tn, fp, fn, tp


def evaluation2(
    score: np.ndarray, y: np.ndarray, display=False
) -> list[float, list[float], list[float], list[float]]:
    """Evaluation with predicted value

    Args:
        score (np.ndarray): Score for each individual, hight value => outlayer, low value => normal
        y (np.ndarray): True TOP_FRAUDE
        display (bool, optional): plot ROC curve. Defaults to False.

    Returns:
        list[float, list[float], list[float], list[float]]: [description]
    """
    precision, recall, thresholds = precision_recall_curve(y, score)
    f1_score = 2 * precision * recall / (precision + recall)

    value = auc(recall, precision)

    if display:
        plt.plot(recall, precision)
        plt.show()

    return value, f1_score, precision, recall


def evaluation3(
    score: np.ndarray, y: np.ndarray, percentage: float, display=True
) -> list[int, int, int, int]:
    """Evaluation with threshold

    Args:
        score (np.ndarray): Score for each individual, hight value => outlayer, low value => normal
        y (np.ndarray): True TOP_FRAUDE
        percentage (float): Threshold over 100 (example: 2%)
        display (bool, optional): display precision, recall, f1_score. Defaults to True.

    Returns:
        tp, fp, fn, tp
    """
    pred = score > sorted(score, key=lambda x: -x)[int(percentage / 100 * len(score))]

    confusion_mat = confusion_matrix(y, pred)

    tn, fp, fn, tp = confusion_mat.ravel()

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * precision * recall / (precision + recall)

    if display:
        print("TN / FP \nFN / TP")
        print(confusion_mat)
        print(f"Precision : {precision}")
        print(f"Recall : {recall}")
        print(f"F1_Score : {f1_score}")

    return tn, fp, fn, tp


# value, f1_score, precision, recall = evaluation2(1/distances.mean(axis=1), np.array(data_quanti["TOP_FRAUDE"]))
