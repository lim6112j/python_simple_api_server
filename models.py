class APIResponse:
  def __init__(self, id, routes, od, timestamp):
    self.id = id
    self.routes = routes
    self.od = od
    self.timestamp = timestamp

  def __repr__(self):
    return '<id {}>'.format(self.id)

  def serialize(self):
    return {
      'id': self.id,
      'routes': self.routes,
      'od': self.od,
      'timestamp':self.timestamp
    }
class APIRequest:
    def __init__(self, startLoc, endLoc, timestamp):
        self.startLoc = startLoc
        self.endLoc = endLoc
        self.timestamp = timestamp
    def __repr__(self):
        return '<id {}>'.format(self.startLoc)
    def serialize(self):
        return {
            'startLoc': self.startLoc,
            'endLoc': self.endLoc,
            'timestamp': self.timestamp
        }
