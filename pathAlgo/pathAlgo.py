import googlemaps
from Node import Node
from datetime import datetime
import sys

# start = "4144 11th Ave NE Seattle"
# addr2 = "1111 3rd Avenue Seattle"
# addr3 = "2101 N Northlake Way Seattle"
# addr4 = "401 NE Northgate Way, Seattle"
# addr5 = "698 W Raye St Seattle"
# end = "4th Ave Pine St Seattle"

start = "4144 11th Ave NE Seattle, WA 98105"
addr2 = "369 8th Ave Seattle, WA 98104"
addr3 = "2101 N Northlake Way, Seattle, WA 98103"
addr4 = "8392 31st Ave NW Seattle, WA 98117"
addr5 = "3517 E Olive St Seattle, WA 98122"
end = "4144 11th Ave NE Seattle, WA 98105"

addr = [start, addr2, addr4, addr3, addr5, end]

class Graph:

    def __init__(self, addrlist):
        self.addrlist = addrlist
        self.gmaps = googlemaps.Client(key='AIzaSyDRTW_KgBW5ysS_G3bBKbB7OasIBm6miEA')
        self.graph = {}
        self.gmapsResult = {}

    def getdata(self, mode):
        now = datetime.now()

        for i in range(1, len(self.addrlist) - 1):
            self.gmapsResult[(self.addrlist[0], self.addrlist[i])] = self.gmaps.distance_matrix(self.addrlist[0], self.addrlist[i], mode=mode, departure_time=now)

        for i in range(1, len(self.addrlist) - 1):
            for j in range(i + 1, len(self.addrlist)):
                self.gmapsResult[(self.addrlist[i], self.addrlist[j])] = self.gmaps.distance_matrix(self.addrlist[i], self.addrlist[j], mode=mode, departure_time=now)

    def makegraph(self):
        for i in range(1, len(self.addrlist) - 1):
            temp = self.gmapsResult[(self.addrlist[0], self.addrlist[i])]
            for item in temp['rows']:
                for newItem in item['elements']:
                    prevlist = []
                    if self.graph.has_key(self.addrlist[0]):
                        prevlist = self.graph[self.addrlist[0]]
                    self.graph[self.addrlist[0]] = prevlist + [Node(self.addrlist[i], (newItem['duration']['value'], newItem['distance']['value'], newItem['duration_in_traffic']['value']))]

        for i in range(1, len(self.addrlist) - 1):
            for j in range(i + 1, len(self.addrlist) - 1):
                temp = self.gmapsResult[(self.addrlist[i], self.addrlist[j])]
                for item in temp['rows']:
                    for newItem in item['elements']:
                        prevlist = []
                        if self.graph.has_key(self.addrlist[i]):
                            prevlist = self.graph[self.addrlist[i]]
                        self.graph[self.addrlist[i]] = prevlist + [Node(self.addrlist[j], (newItem['duration']['value'], newItem['distance']['value'], newItem['duration_in_traffic']['value']))]
                        if j is not len(self.addrlist) - 1:
                            prevlist = []
                            if self.graph.has_key(self.addrlist[j]):
                                prevlist = self.graph[self.addrlist[j]]
                            self.graph[self.addrlist[j]] = prevlist + [Node(self.addrlist[i], (newItem['duration']['value'], newItem['distance']['value'], newItem['duration_in_traffic']['value']))]

    def shortestPath(self):
        pathList = [self.addrlist[0]]
        visited = {}
        while len(pathList) != len(self.addrlist) - 1:
            edgesList = self.graph[pathList[len(pathList) - 1]]
            minDistance = sys.maxsize
            minNode = None
            for nextPath in edgesList:
                if nextPath.getNodeLabel() in visited:
                    continue
                if nextPath.getDistance()[1] < minDistance:
                    minDistance = nextPath.getDistance()[1]
                    minNode = nextPath.getNodeLabel()
            pathList = pathList + [minNode]
            visited[minNode] = True
        return pathList + [self.addrlist[len(self.addrlist) - 1]]


g = Graph(addr)
g.getdata("driving")
g.makegraph()
print g.shortestPath()