import pins
import vetiver
import logging

logging.basicConfig(level=logging.DEBUG)

b = pins.board_folder('data/model', allow_pickle_read = True)
v = vetiver.VetiverModel.from_pin(b, 'penguin_model')

app = vetiver.VetiverAPI(v, check_prototype = False)
app.run(port = 8080)