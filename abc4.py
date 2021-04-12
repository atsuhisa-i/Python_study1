class Insert(Command):
  def __init__(self, index, text):
      self.index = index
      self.text = text

  def run(self, text):
      i = self.index
      return text[:i]+self.text+text[i:]