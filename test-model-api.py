import pins
import vetiver

b = pins.board_folder('data/model', allow_pickle_read = True)
v = vetiver.VetiverModel.from_pin(b, 'penguin_model')

app = vetiver.VetiverAPI(v, check_prototype = True)
app.run(port = 8080)