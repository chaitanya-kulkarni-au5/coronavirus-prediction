from sklearn import svm, datasets
import pandas as pd
C = 0.1
COVID_DATASET = pd.read_csv("Covid_Dataset.csv")
input_dataset = COVID_DATASET.iloc[:,0:20]
output_dataset = COVID_DATASET.iloc[:,20]
Svc_classifier = svm.SVC(kernel='linear', C=C).fit(input_dataset, output_dataset)

