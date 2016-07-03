class Node:

    def __init__(self, nodeLabel, distance):
        self.nodeLabel = nodeLabel
        self.distance = distance

    def getNodeLabel(self):
        return self.nodeLabel

    def getDistance(self):
        return self.distance

    def __repr__(self):
        return "[" + self.nodeLabel + ", %s]" % (self.distance,)