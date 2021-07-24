import numpy as np

from keras.callbacks import EarlyStopping
from keras.models import Sequential

model = Sequential
predictors = np.loadtxt('predictors_data.csv', delimiter=',')
target = np.array([1,2,3], [1,2,3])
early_stopping_monitor = EarlyStopping(patience=2)

model.fit(predictors, target, validation_split=0.3, nb_epoch=20,
          callbacks=[early_stopping_monitor])
