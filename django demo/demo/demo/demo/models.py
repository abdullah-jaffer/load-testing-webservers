import json

class Book:
  def __init__(self, title, IBAN, pages):
    self.title = title
    self.IBAN = IBAN
    self.pages = pages

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__,
                      sort_keys=True, indent=4)
