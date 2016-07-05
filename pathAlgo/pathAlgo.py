import googlemaps
from Node import Node
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDRTW_KgBW5ysS_G3bBKbB7OasIBm6miEA')

now = datetime.now()


start = "4144 11th Ave NE Seattle"
addr2 = "1111 3rd Avenue Seattle"
addr3 = "2101 N Northlake Way Seattle"
addr4 = "401 NE Northgate Way, Seattle"
addr5 = "698 W Raye St Seattle"
end = "4th Ave Pine St Seattle"

addr = [start, addr2, addr3, addr4, addr5, end]

# distance_result = gmaps.distance_matrix(addr3, addr4, mode="driving", departure_time=now)
# print distance_result
# direction_result = gmaps.directions(addr1, addr2, mode="driving", departure_time=now)
#
# print distance_result
# print direction_result


# distance_result = {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'12 mins', u'value': 723}, u'distance': {u'text': u'7.3 km', u'value': 7278}, u'duration_in_traffic': {u'text': u'10 mins', u'value': 617}, u'status': u'OK'}, {u'duration': {u'text': u'6 mins', u'value': 346}, u'distance': {u'text': u'2.4 km', u'value': 2387}, u'duration_in_traffic': {u'text': u'6 mins', u'value': 330}, u'status': u'OK'}, {u'status': u'ZERO_RESULTS'}]}], u'origin_addresses': [u'4144 11th Ave NE, Seattle, WA 98105, USA'], u'destination_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA', u'2101 N Northlake Way, Seattle, WA 98103, USA', u'4th Ave, Bridgetown, Barbados']}
# direction_result = [{u'overview_polyline': {u'points': u'gf{aHj~piVyIQkFCu@A?dA?~BAnF?hEA`I?`BAbC?bAbBBrABZITAb@?rE?~CEhAIl@GFEBCJMVAr@C|CMpAErAE~C@j\\VtGJzCRh@FrF\\dGXzAHlQXrT@rE?jA@fBHdALpCZn@NlBb@|Ad@|C~@xBz@jAp@vAjAl@l@pDdErB`ChBhBlA|@hAr@l@Tr@XbB`@p@FpCDfHBjPGdOAj@?hB?tADjCP`CXjCd@zA`@LDxAd@hD`A~@Zl@RtF`BfCr@F@LRPNhAn@p@Zx@XVPT\\|@lCjChIn@pBhC_CjEyD~AtEnApEFTl@k@'}, u'warnings': [], u'bounds': {u'northeast': {u'lat': 47.66133079999999, u'lng': -122.3165806}, u'southwest': {u'lat': 47.60681839999999, u'lng': -122.3353252}}, u'waypoint_order': [], u'summary': u'I-5 S', u'copyrights': u'Map data \xa92016 Google', u'legs': [{u'distance': {u'text': u'4.5 mi', u'value': 7277}, u'traffic_speed_entry': [], u'end_address': u'1111 3rd Ave, Seattle, WA 98101, USA', u'via_waypoint': [], u'duration_in_traffic': {u'text': u'27 mins', u'value': 1600}, u'start_address': u'4144 11th Ave NE, Seattle, WA 98105, USA', u'start_location': {u'lat': 47.6581232, u'lng': -122.3166992}, u'steps': [{u'html_instructions': u'Head <b>north</b> on <b>11th Ave NE</b> toward <b>NE 42nd St</b>', u'distance': {u'text': u'0.2 mi', u'value': 354}, u'travel_mode': u'DRIVING', u'start_location': {u'lat': 47.6581232, u'lng': -122.3166992}, u'polyline': {u'points': u'gf{aHj~piVo@AiHOkDC_A?u@A'}, u'duration': {u'text': u'1 min', u'value': 79}, u'end_location': {u'lat': 47.6613012, u'lng': -122.3165806}}, {u'html_instructions': u'Turn <b>left</b> at the 3rd cross street onto <b>NE 45th St</b>', u'distance': {u'text': u'0.3 mi', u'value': 471}, u'travel_mode': u'DRIVING', u'maneuver': u'turn-left', u'start_location': {u'lat': 47.6613012, u'lng': -122.3165806}, u'polyline': {u'points': u'cz{aHr}piV?dA?f@?vA?`@?t@?nAAfA?n@?L?`B?h@AfA?P@P?x@A^?\\?|A?V?`@?@?L?V?@?@?H?J?T?@AL?d@?D?@?H?J?B?~@'}, u'duration': {u'text': u'2 mins', u'value': 109}, u'end_location': {u'lat': 47.66133079999999, u'lng': -122.322875}}, {u'html_instructions': u'Turn <b>left</b> onto <b>5th Ave NE</b>', u'distance': {u'text': u'335 ft', u'value': 102}, u'travel_mode': u'DRIVING', u'maneuver': u'turn-left', u'start_location': {u'lat': 47.66133079999999, u'lng': -122.322875}, u'polyline': {u'points': u'iz{aH~driVb@?~@Bp@?`@B'}, u'duration': {u'text': u'1 min', u'value': 24}, u'end_location': {u'lat': 47.6604113, u'lng': -122.3229182}}, {u'html_instructions': u'Take the ramp on the <b>left</b> onto <b>I-5 S</b>', u'distance': {u'text': u'3.4 mi', u'value': 5479}, u'travel_mode': u'DRIVING', u'start_location': {u'lat': 47.6604113, u'lng': -122.3229182}, u'polyline': {u'points': u'qt{aHferiVVGBAD?BAB?F?D?\\?tCB|@Cz@?^Ad@A\\A`@CNAFANAPCPA@?@?@A@?@?@A@?@A@A@A@AJMVAXAXAbAExAGB?XAr@Cr@C^A\\?`C@~B@jXTpFHb@@tBLXB@@H?@@D?H@VBjDRfAHjERx@DzAHlQXxIBxIAl@?hC?Z?^?j@@|@Bh@DPBl@FD@bBPl@Hb@HJD^FlAZ~@X\\J~@X|Ad@bA\\t@\\`@Th@ZvAjAl@l@rCbD\\`@XZxAdBx@x@n@n@XRr@h@hAr@l@Tr@XbB`@p@FtADz@?P@R?Z?dF@P?T?TAJ?vHCr@?tBAJAF@F?N?lA?zGAlA?`@?D?H?T?D?X@nAAh@@j@BX@p@D~@HbAJ|@Lt@LtAVx@P`@NLDbA^TD~A`@hA^^LB@ZJDBf@NpBn@bCp@d@LxA`@FBF@'}, u'duration': {u'text': u'5 mins', u'value': 286}, u'end_location': {u'lat': 47.6122333, u'lng': -122.330814}}, {u'html_instructions': u'Take exit <b>165B</b> for <b>Union St</b>', u'distance': {u'text': u'0.1 mi', u'value': 191}, u'travel_mode': u'DRIVING', u'maneuver': u'ramp-right', u'start_location': {u'lat': 47.6122333, u'lng': -122.330814}, u'polyline': {u'points': u'mgraHpvsiVLRDDJH`@Vf@Vb@RLFx@XVPLLFNZ~@'}, u'duration': {u'text': u'1 min', u'value': 18}, u'end_location': {u'lat': 47.6107852, u'lng': -122.332055}}, {u'html_instructions': u'Continue onto <b>Union St</b>', u'distance': {u'text': u'0.1 mi', u'value': 231}, u'travel_mode': u'DRIVING', u'start_location': {u'lat': 47.6107852, u'lng': -122.332055}, u'polyline': {u'points': u'm~qaHj~siVX|@FN|A|El@jBn@pB'}, u'duration': {u'text': u'1 min', u'value': 55}, u'end_location': {u'lat': 47.6096839, u'lng': -122.334667}}, {u'html_instructions': u'Turn <b>left</b> onto <b>5th Ave</b>', u'distance': {u'text': u'0.1 mi', u'value': 223}, u'travel_mode': u'DRIVING', u'maneuver': u'turn-left', u'start_location': {u'lat': 47.6096839, u'lng': -122.334667}, u'polyline': {u'points': u'owqaHtntiVhC_Cz@u@nCcC'}, u'duration': {u'text': u'1 min', u'value': 63}, u'end_location': {u'lat': 47.6079746, u'lng': -122.3331043}}, {u'html_instructions': u'Turn <b>right</b> onto <b>Seneca St</b>', u'distance': {u'text': u'0.1 mi', u'value': 196}, u'travel_mode': u'DRIVING', u'maneuver': u'turn-right', u'start_location': {u'lat': 47.6079746, u'lng': -122.3331043}, u'polyline': {u'points': u'ylqaHzdtiVr@vBj@|Aj@tBb@zAFT'}, u'duration': {u'text': u'1 min', u'value': 76}, u'end_location': {u'lat': 47.6070486, u'lng': -122.3353252}}, {u'html_instructions': u'Turn <b>left</b> onto <b>3rd Ave</b><div style="font-size:0.9em">May be closed at certain times or days</div><div style="font-size:0.9em">Destination will be on the right</div>', u'distance': {u'text': u'98 ft', u'value': 30}, u'travel_mode': u'DRIVING', u'maneuver': u'turn-left', u'start_location': {u'lat': 47.6070486, u'lng': -122.3353252}, u'polyline': {u'points': u'agqaHxrtiVl@k@'}, u'duration': {u'text': u'1 min', u'value': 13}, u'end_location': {u'lat': 47.60681839999999, u'lng': -122.3351148}}], u'duration': {u'text': u'12 mins', u'value': 723}, u'end_location': {u'lat': 47.60681839999999, u'lng': -122.3351148}}]}]
# print distance_result
# print direction_result[0]['legs'][0]['steps']
#
# for item in direction_result[0]['legs'][0]['steps']:
#     for key, value in item.iteritems():
#         print key + str(": "), value
#     print "------------------------------------------"


# print "-----------------------------------------------------------------------------"
# for item in distance_result['rows']:
#     for newItem in item['elements']:
#         for key, value in newItem.iteritems():
#             print key + ": ", value
#         print "----------------------------------------"


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

        # self.gmapsResult = {('1111 3rd Avenue Seattle', '2101 N Northlake Way Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'14 mins', u'value': 817}, u'distance': {u'text': u'7.0 km', u'value': 7044}, u'duration_in_traffic': {u'text': u'15 mins', u'value': 928}, u'status': u'OK'}]}], u'origin_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA'], u'destination_addresses': [u'2101 N Northlake Way, Seattle, WA 98103, USA']}, ('1111 3rd Avenue Seattle', '4th Ave Pine St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'3 mins', u'value': 165}, u'distance': {u'text': u'0.6 km', u'value': 643}, u'duration_in_traffic': {u'text': u'3 mins', u'value': 166}, u'status': u'OK'}]}], u'origin_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA'], u'destination_addresses': [u'Pine St & 4th Ave, Seattle, WA 98181, USA']}, ('2101 N Northlake Way Seattle', '698 W Raye St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'10 mins', u'value': 590}, u'distance': {u'text': u'3.2 km', u'value': 3245}, u'duration_in_traffic': {u'text': u'11 mins', u'value': 651}, u'status': u'OK'}]}], u'origin_addresses': [u'2101 N Northlake Way, Seattle, WA 98103, USA'], u'destination_addresses': [u'698 W Raye St, Seattle, WA 98119, USA']}, ('4144 11th Ave NE Seattle', '2101 N Northlake Way Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'6 mins', u'value': 355}, u'distance': {u'text': u'2.4 km', u'value': 2361}, u'duration_in_traffic': {u'text': u'7 mins', u'value': 441}, u'status': u'OK'}]}], u'origin_addresses': [u'4144 11th Ave NE, Seattle, WA 98105, USA'], u'destination_addresses': [u'2101 N Northlake Way, Seattle, WA 98103, USA']}, ('4144 11th Ave NE Seattle', '401 NE Northgate Way, Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'9 mins', u'value': 515}, u'distance': {u'text': u'6.4 km', u'value': 6409}, u'duration_in_traffic': {u'text': u'8 mins', u'value': 505}, u'status': u'OK'}]}], u'origin_addresses': [u'4144 11th Ave NE, Seattle, WA 98105, USA'], u'destination_addresses': [u'401 NE Northgate Way, Seattle, WA 98125, USA']}, ('2101 N Northlake Way Seattle', '4th Ave Pine St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'14 mins', u'value': 839}, u'distance': {u'text': u'7.9 km', u'value': 7886}, u'duration_in_traffic': {u'text': u'14 mins', u'value': 850}, u'status': u'OK'}]}], u'origin_addresses': [u'2101 N Northlake Way, Seattle, WA 98103, USA'], u'destination_addresses': [u'Pine St & 4th Ave, Seattle, WA 98181, USA']}, ('1111 3rd Avenue Seattle', '698 W Raye St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'13 mins', u'value': 786}, u'distance': {u'text': u'6.5 km', u'value': 6527}, u'duration_in_traffic': {u'text': u'13 mins', u'value': 750}, u'status': u'OK'}]}], u'origin_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA'], u'destination_addresses': [u'698 W Raye St, Seattle, WA 98119, USA']}, ('4144 11th Ave NE Seattle', '1111 3rd Avenue Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'12 mins', u'value': 723}, u'distance': {u'text': u'7.3 km', u'value': 7278}, u'duration_in_traffic': {u'text': u'11 mins', u'value': 674}, u'status': u'OK'}]}], u'origin_addresses': [u'4144 11th Ave NE, Seattle, WA 98105, USA'], u'destination_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA']}, ('1111 3rd Avenue Seattle', '401 NE Northgate Way, Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'13 mins', u'value': 751}, u'distance': {u'text': u'12.1 km', u'value': 12126}, u'duration_in_traffic': {u'text': u'13 mins', u'value': 761}, u'status': u'OK'}]}], u'origin_addresses': [u'1111 3rd Ave, Seattle, WA 98101, USA'], u'destination_addresses': [u'401 NE Northgate Way, Seattle, WA 98125, USA']}, ('401 NE Northgate Way, Seattle', '698 W Raye St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'18 mins', u'value': 1056}, u'distance': {u'text': u'11.3 km', u'value': 11262}, u'duration_in_traffic': {u'text': u'18 mins', u'value': 1065}, u'status': u'OK'}]}], u'origin_addresses': [u'401 NE Northgate Way, Seattle, WA 98125, USA'], u'destination_addresses': [u'698 W Raye St, Seattle, WA 98119, USA']}, ('2101 N Northlake Way Seattle', '401 NE Northgate Way, Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'11 mins', u'value': 671}, u'distance': {u'text': u'8.0 km', u'value': 7963}, u'duration_in_traffic': {u'text': u'12 mins', u'value': 731}, u'status': u'OK'}]}], u'origin_addresses': [u'2101 N Northlake Way, Seattle, WA 98103, USA'], u'destination_addresses': [u'401 NE Northgate Way, Seattle, WA 98125, USA']}, ('401 NE Northgate Way, Seattle', '4th Ave Pine St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'14 mins', u'value': 832}, u'distance': {u'text': u'12.6 km', u'value': 12592}, u'duration_in_traffic': {u'text': u'14 mins', u'value': 821}, u'status': u'OK'}]}], u'origin_addresses': [u'401 NE Northgate Way, Seattle, WA 98125, USA'], u'destination_addresses': [u'Pine St & 4th Ave, Seattle, WA 98181, USA']}, ('698 W Raye St Seattle', '4th Ave Pine St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'14 mins', u'value': 851}, u'distance': {u'text': u'6.8 km', u'value': 6783}, u'duration_in_traffic': {u'text': u'13 mins', u'value': 802}, u'status': u'OK'}]}], u'origin_addresses': [u'698 W Raye St, Seattle, WA 98119, USA'], u'destination_addresses': [u'Pine St & 4th Ave, Seattle, WA 98181, USA']}, ('4144 11th Ave NE Seattle', '698 W Raye St Seattle'): {u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'13 mins', u'value': 771}, u'distance': {u'text': u'5.9 km', u'value': 5912}, u'duration_in_traffic': {u'text': u'13 mins', u'value': 786}, u'status': u'OK'}]}], u'origin_addresses': [u'4144 11th Ave NE, Seattle, WA 98105, USA'], u'destination_addresses': [u'698 W Raye St, Seattle, WA 98119, USA']}}

        # print self.gmapsResult
        # for key, value in self.gmapsResult.iteritems():
        #     print "%s: " % (key,)
        #     for item in value['rows']:
        #         for newItem in item['elements']:
        #             for key2, value2 in newItem.iteritems():
        #                 print key2 + ": ", value2
        #             print "----------------------------------------"

    def makegraph(self):
        for i in range(1, len(self.addrlist) - 1):
            temp = self.gmapsResult[(self.addrlist[0], self.addrlist[i])]
            for item in temp['rows']:
                for newItem in item['elements']:
                    prevlist = []
                    if self.graph.has_key(self.addrlist[0]):
                        prevlist = self.graph[self.addrlist[0]]
                    self.graph[self.addrlist[0]] = prevlist + [Node(self.addrlist[i], (newItem['duration']['text'], newItem['distance']['text'], newItem['duration_in_traffic']['text']))]

        for i in range(1, len(self.addrlist) - 1):
            for j in range(i + 1, len(self.addrlist)):
                temp = self.gmapsResult[(self.addrlist[i], self.addrlist[j])]
                for item in temp['rows']:
                    for newItem in item['elements']:
                        prevlist = []
                        if self.graph.has_key(self.addrlist[i]):
                            prevlist = self.graph[self.addrlist[i]]
                        self.graph[self.addrlist[i]] = prevlist + [Node(self.addrlist[j], (newItem['duration']['text'], newItem['distance']['text'], newItem['duration_in_traffic']['text']))]
                        if j is not len(self.addrlist) - 1:
                            prevlist = []
                            if self.graph.has_key(self.addrlist[j]):
                                prevlist = self.graph[self.addrlist[j]]
                            self.graph[self.addrlist[j]] = prevlist + [Node(self.addrlist[i], (newItem['duration']['text'], newItem['distance']['text'], newItem['duration_in_traffic']['text']))]

    def shortestPath(self):
        


g = Graph(addr)
g.getdata("driving")
g.makegraph()