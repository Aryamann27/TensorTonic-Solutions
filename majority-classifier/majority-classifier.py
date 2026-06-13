import numpy as np

def majority_classifier(y_train, X_test):
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    values, cnts = np.unique(y_train, return_counts=True)

    pred_lab = values[np.argmax(cnts)]

    preds = np.full(len(X_test), pred_lab)
    
    return preds