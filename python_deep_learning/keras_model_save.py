from keras.models import load_model
from keras.models import Sequential

model = Sequential()

model.save('model_file.h5')
my_model = load_model('my_model.h5')
# predictions = my_model.predict(data_to_predict_with)
# probability_true = predictions[:, 1]
# my_model.summary()
