import pins
import vetiver
import logging
from palmerpenguins import penguins
from pandas import get_dummies
from sklearn.linear_model import LinearRegression

# logging.basicConfig(level=logging.DEBUG)

df = penguins.load_penguins().dropna()
X = get_dummies(df[['bill_length_mm', 'species', 'sex']], drop_first = True)
y = df['body_mass_g']
model = LinearRegression().fit(X, y)

v = vetiver.VetiverModel(model, model_name='penguin_model', prototype_data=X)

# running API here works
# app = vetiver.VetiverAPI(v, check_prototype = True)
# app.run(port = 8080)

model_board = pins.board_folder("data/model", allow_pickle_read = True)
vetiver.vetiver_pin_write(model_board, v)
v2 = vetiver.VetiverModel.from_pin(model_board, 'penguin_model')


print(v.prototype.__annotations__)
print(v2.prototype.__annotations__)

# This does not work because the species_ class has been change from bool to NoneType
# app = vetiver.VetiverAPI(v2, check_prototype = True)
# app.run(port = 8080)

app = vetiver.VetiverAPI(v, check_prototype = True)
app.run(port = 8080)

