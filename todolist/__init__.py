import webapp
import model

def go():
    model.app.run(debug=True)

__all__ = ["go"]
