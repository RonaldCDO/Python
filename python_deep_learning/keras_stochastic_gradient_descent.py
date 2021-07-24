from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

def get_new_model(input_shape):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape=input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return model


lr_to_test = [.000001, 0.01, 1]

for lr in lr_to_test:
    model = get_new_model()
    my_optimizer = SGD(lr=lr)
    model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')
    # model.fit(predictors, target)