import sys
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
import numpy as np
import cv2
import os

image = sys.argv[1]
# image_file_path = './../predictions/2-100.png'

# Load digit database
digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Train SVM classifier
classifier = svm.SVC(gamma = 0.001)
classifier.fit(data[:n_samples], digits.target[:n_samples])

# Read image
image_file_path = os.path.abspath(image)
img = cv2.imread(image_file_path)
img = cv2.bitwise_not(img)
img = img[:,:,0]
img = cv2.resize(img, (8, 8))

# Normalize the values in the image to 0-16
minValueInImage = np.min(img)
maxValueInImage = np.max(img)
normaliizeImg = np.floor(np.divide((img - minValueInImage).astype(float),(maxValueInImage-minValueInImage).astype(float))*16)

# Predict
predicted = classifier.predict(normaliizeImg.reshape((1,normaliizeImg.shape[0]*normaliizeImg.shape[1] )))
ts = np.array2string(predicted)
converted_string = str(ts)
print(converted_string)

sys.stdout.flush()


# # Code I tried using for running the classifier training on the data
# # Train SVM classifier
# classifier = svm.SVC(gamma = 0.001)
# # Split data into 50% train and 50% test subsets
# X_train, X_test, y_train, y_test = train_test_split(
#     data, targets, test_size=0.5, shuffle=False)
# # Learn the digits on the train subset
# classifier.fit(X_train, y_train)
# # Predict the value of the digit on the test subset
# predicted = classifier.predict(X_test[0])
# print(predicted)

# # Code I tried to use to solve the reading and base64 decoding process of the image
# image = plt.imread('./../2-reverse-big.png')
# encoded_image = base64.b64encode(image)
# base64_img_bytes = encoded_image.encode('utf-8')
# decoded_image_data = base64.decodebytes(base64_img_bytes)
# binary = base64.b64decode(image)
# image = cv2.imdecode(np.frombuffer(binary, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
# image = np.asarray(bytearray(binary), dtype="uint8")
# npimg = np.frombuffer(binary, dtype=np.uint8)
# image = cv2.imdecode(image, 1)
# decoded_image_data = base64.b64decode(encoded_image)
# npimg = np.frombuffer(decoded_image_data, dtype=np.uint8)
# cv_img = cv2.imdecode(npimg, cv2.IMREAD_GRAYSCALE)