import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint


def createMap():
    # Lists of all states in regions
    northeast = ['New England', 'New York', 'Pennsylvania',
                 'Midcoastal', 'Ohio', 'West Virginia']
    southeast = ['Virginia', 'Kentucky', 'Tennessee', 'North Carolina',
                 'South Carolina', 'Georgia', 'Alabama', 'Mississippi', 'Florida']
    northcentral = ['Michigan', 'Indiana', 'Illinois', 'Wisconsin',
                    'Minnesota', 'Iowa', 'North Dakota', 'South Dakota', 'Nebraska']
    southcentral = ['Missouri', 'Kansas',
                    'Arkansas', 'Oklahoma', 'Louisiana', 'Texas']
    northwest = ['Washington', 'Oregon', 'Idaho', 'Montana', 'Wyoming']
    southwest = ['California', 'Nevada', 'Utah',
                 'Colorado', 'Arizona', 'New Mexico']
    states = northeast+southeast+northcentral+southcentral+northwest+southwest

    # Create Graph and add nodes
    map = nx.Graph()
    # map.add_nodes_from(states)
    map.add_nodes_from(northeast,regions=['North','East'],value=None,isCrossed=False,isCircled=False)
    map.add_nodes_from(southeast,regions=['South','East'],value=None,isCrossed=False,isCircled=False)
    map.add_nodes_from(northcentral,regions=['North','Central'],value=None,isCrossed=False,isCircled=False)
    map.add_nodes_from(southcentral,regions=['South','Central'],value=None,isCrossed=False,isCircled=False)
    map.add_nodes_from(northwest,regions=['North','West'],value=None,isCrossed=False,isCircled=False)
    map.add_nodes_from(southwest,regions=['South','West'],value=None,isCrossed=False,isCircled=False)
    # map.add_edges_from([('',''),('',''),('',''),('',''),('','')])
    # # Add all edges (Edges are created twice between each node so I don't have to keep track of which ones I created. Networkx will simply ignore them.)
    # # New England
    # map.add_edges_from([('New England', 'New York')])
    # # New York
    # map.add_edges_from([('New York', 'New England'),
    #                     ('New York', 'Pennsylvania'), ('New York', 'Midcoastal')])
    # # Pennsylvania
    # map.add_edges_from([('Pennsylvania', 'New York'), ('Pennsylvania', 'Midcoastal'),
    #                     ('Pennsylvania', 'West Virginia'), ('Pennsylvania', 'Ohio')])
    # # Midcoastal
    # map.add_edges_from([('Midcoastal', 'New York'),
    #                     ('Midcoastal', 'Pennsylvania'), ('Midcoastal', 'Virginia')])
    # # Ohio
    # map.add_edges_from([('Ohio', 'Pennsylvania'), ('Ohio', 'West Virginia'),
    #                     ('Ohio', 'Kentucky'), ('Ohio', 'Indiana'), ('Ohio', 'Michigan')])
    # # West Virginia
    # map.add_edges_from([('West Virginia', 'Pennsylvania'), ('West Virginia',
    #                                                         'Virginia'), ('West Virginia', 'Kentucky'), ('West Virginia', 'Ohio')])
    # # Virginia
    # map.add_edges_from([('Virginia','Midcoastal'),('Virginia','West Virginia'),('Virginia','Kentucky'),('Virginia','Tennessee'),('Virginia','North Carolina')])
    # # Kentucky
    # map.add_edges_from([('Kentucky','Virginia'),('Kentucky','West Virginia'),('Kentucky','Ohio'),('Kentucky','Indiana'),('Kentucky','Illinois'),('Kentucky','Missouri'),('Kentucky','Tennessee')])
    # # Tennessee
    # map.add_edges_from([('Tennessee','North Carolina'),('Tennessee','Virginia'),('Tennessee','Kentucky'),('Tennessee','Missouri'),('Tennessee','Arkansas'),('Tennessee','Mississippi'),('Tennessee','Alabama'),('Tennessee','Georgia')])
    # # North Carolina
    # map.add_edges_from([('North Carolina','Virginia'),('North Carolina','Tennessee'),('North Carolina','South Carolina')])
    # # South Carolina
    # map.add_edges_from([('South Carolina','North Carolina'),('South Carolina','Georgia')])
    # # Georgia
    # map.add_edges_from([('Georgia','South Carolina'),('Georgia','Tennessee'),('Georgia','Alabama'),('Georgia','Florida')])
    # # Alabama
    # map.add_edges_from([('Alabama','Georgia'),('Alabama','Tennessee'),('Alabama','Mississippi'),('Alabama','Florida')])
    # # Mississippi
    # map.add_edges_from([('Mississippi','Alabama'),('Mississippi','Tennessee'),('Mississippi','Arkansas'),('Mississippi','Louisiana')])
    # # Florida
    # map.add_edges_from([('Florida','Georgia'),('Florida','Alabama')])
    # # Michigan
    # map.add_edges_from([('Michigan','Ohio'),('Michigan','Indiana'),('Michigan','Wisconsin')])
    # # Indiana
    # map.add_edges_from([('Indiana','Ohio'),('Indiana','Michigan'),('Indiana','Illinois'),('Indiana','Kentucky')])
    # # Illinois
    # map.add_edges_from([('Illinois','Indiana'),('Illinois','Wisconsin'),('Illinois','Iowa'),('Illinois','Missouri'),('Illinois','Kentucky')])
    # # Wisconsin
    # map.add_edges_from([('Wisconsin','Michigan'),('Wisconsin','Minnesota'),('Wisconsin','Iowa'),('Wisconsin','Illinois')])
    # # Minnesota
    # map.add_edges_from([('Minnesota','Wisconsin'),('Minnesota','North Dakota'),('Minnesota','South Dakota'),('Minnesota','Iowa')])
    # # Iowa
    # map.add_edges_from([('Iowa','Illinois'),('Iowa','Wisconsin'),('Iowa','Minnesota'),('Iowa','South Dakota'),('Iowa','Nebraska'),('Iowa','Missouri')])
    # # North Dakota
    # map.add_edges_from([('North Dakota','Minnesota'),('North Dakota','South Dakota'),('North Dakota','Montana')])
    # # South Dakota
    # map.add_edges_from([('South Dakota','Iowa'),('South Dakota','Minnesota'),('South Dakota','North Dakota'),('South Dakota','Montana'),('South Dakota','Wyoming'),('South Dakota','Nebraska')])
    # # Nebraska
    # map.add_edges_from([('Nebraska','Iowa'),('Nebraska','South Dakota'),('Nebraska','Wyoming'),('Nebraska','Colorado'),('Nebraska','Kansas'),('Nebraska','Missouri')])
    # # Missouri
    # map.add_edges_from([('Missouri','Kentucky'),('Missouri','Illinois'),('Missouri','Iowa'),('Missouri','Nebraska'),('Missouri','Kansas'),('Missouri','Oklahoma'),('Missouri','Arkansas'),('Missouri','Tennessee')])
    # # Kansas
    # map.add_edges_from([('Kansas','Missouri'),('Kansas','Nebraska'),('Kansas','Colorado'),('Kansas','Oklahoma')])
    # # Arkansas
    # map.add_edges_from([('Arkansas','Tennessee'),('Arkansas','Missouri'),('Arkansas','Oklahoma'),('Arkansas','Texas'),('Arkansas','Louisiana'),('Arkansas','Mississippi')])
    # # Oklahoma
    # map.add_edges_from([('Oklahoma','Arkansas'),('Oklahoma','Missouri'),('Oklahoma','Kansas'),('Oklahoma','Colorado'),('Oklahoma','New Mexico'),('Oklahoma','Texas')])
    # # Louisiana
    # map.add_edges_from([('Louisiana','Mississippi'),('Louisiana','Arkansas'),('Louisiana','Texas')])
    # # Texas
    # map.add_edges_from([('Texas','Louisiana'),('Texas','Arkansas'),('Texas','Oklahoma'),('Texas','New Mexico')])
    # # Washington
    # map.add_edges_from([('Washington','Oregon'),('Washington','Idaho')])
    # # Oregon
    # map.add_edges_from([('Oregon','Idaho'),('Oregon','Washington'),('Oregon','California'),('Oregon','Nevada')])
    # # Idaho
    # map.add_edges_from([('Idaho','Wyoming'),('Idaho','Montana'),('Idaho','Washington'),('Idaho','Oregon'),('Idaho','Nevada'),('Idaho','Utah')])
    # # Montana
    # map.add_edges_from([('Montana','North Dakota'),('Montana','Idaho'),('Montana','South Dakota')])
    # # Wyoming
    # map.add_edges_from([('Wyoming','South Dakota'),('Wyoming','Montana'),('Wyoming','Idaho'),('Wyoming','Utah'),('Wyoming','Colorado'),('Wyoming','Nebraska')])
    # # California
    # map.add_edges_from([('California','Oregon'),('California','Nevada'),('California','Arizona')])
    # # Nevada
    # map.add_edges_from([('Nevada','Utah'),('Nevada','Idaho'),('Nevada','Oregon'),('Nevada','California'),('Nevada','Arizona')])
    # # Utah
    # map.add_edges_from([('Utah','Colorado'),('Utah','Wyoming'),('Utah','Idaho'),('Utah','Nevada'),('Utah','Arizona')])
    # # Colorado
    # map.add_edges_from([('Colorado','Nebraska'),('Colorado','Wyoming'),('Colorado','Utah'),('Colorado','New Mexico'),('Colorado','Oklahoma'),('Colorado','Kansas')])
    # # Arizona
    # map.add_edges_from([('Arizona','California'),('Arizona','Nevada'),('Arizona','Utah'),('Arizona','New Mexico')])
    # # New Mexico
    # map.add_edges_from([('New Mexico','Texas'),('New Mexico','Oklahoma'),('New Mexico','Colorado'),('New Mexico','Arizona')])
    map.add_edges_from([('New Mexico', 'Oklahoma'), ('New Mexico', 'Arizona'), ('New Mexico', 'Texas'), ('New Mexico', 'Colorado'), ('Idaho', 'Montana'), ('Idaho', 'Oregon'), ('Idaho', 'Nevada'), ('Idaho', 'Washington'), ('Idaho', 'Utah'), ('Idaho', 'Wyoming'), ('California', 'Oregon'), ('California', 'Arizona'), ('California', 'Nevada'), ('Georgia', 'Alabama'), ('Georgia', 'Florida'), ('Georgia', 'South Carolina'), ('Georgia', 'Tennessee'), ('Florida', 'Alabama'), ('Texas', 'Oklahoma'), ('Texas', 'Louisiana'), ('Texas', 'Arkansas'), ('Nebraska', 'Iowa'), ('Nebraska', 'Kansas'), ('Nebraska', 'Colorado'), ('Nebraska', 'Wyoming'), ('Nebraska', 'Missouri'), ('Nebraska', 'South Dakota'), ('Montana', 'Wyoming'), ('Montana', 'North Dakota'), ('Montana', 'South Dakota'), ('Oklahoma', 'Missouri'), ('Oklahoma', 'Kansas'), ('Oklahoma', 'Colorado'), ('Oklahoma', 'Arkansas'), ('New England', 'New York'), ('Midcoastal', 'Pennsylvania'), ('Midcoastal', 'New York'), ('Midcoastal', 'Virginia'), ('West Virginia', 'Pennsylvania'), ('West Virginia', 'Ohio'), ('West Virginia', 'Kentucky'), ('West Virginia', 'Virginia'), ('Mississippi', 'Alabama'), ('Mississippi', 'Louisiana'), ('Mississippi', 'Arkansas'), ('Mississippi', 'Tennessee'), ('Pennsylvania', 'Ohio'), ('Pennsylvania', 'New York'), ('Alabama', 'Tennessee'), ('Utah', 'Wyoming'), ('Utah', 'Arizona'), ('Utah', 'Colorado'), ('Utah', 'Nevada'), ('Kentucky', 'Missouri'), ('Kentucky', 'Illinois'), ('Kentucky', 'Ohio'), ('Kentucky', 'Indiana'), ('Kentucky', 'Tennessee'), ('Kentucky', 'Virginia'), ('Washington', 'Oregon'), ('Louisiana', 'Arkansas'), ('Tennessee', 'Arkansas'), ('Tennessee', 'North Carolina'), ('Tennessee', 'Missouri'), ('Tennessee', 'Virginia'), ('Iowa', 'Minnesota'), ('Iowa', 'Wisconsin'), ('Iowa', 'Illinois'), ('Iowa', 'Missouri'), ('Iowa', 'South Dakota'), ('Wisconsin', 'Minnesota'), ('Wisconsin', 'Michigan'), ('Wisconsin', 'Illinois'), ('Oregon', 'Nevada'), ('North Dakota', 'Minnesota'), ('North Dakota', 'South Dakota'), ('Arkansas', 'Missouri'), ('Nevada', 'Arizona'), ('Michigan', 'Ohio'), ('Michigan', 'Indiana'), ('Ohio', 'Indiana'), ('South Dakota', 'Minnesota'), ('South Dakota', 'Wyoming'), ('Virginia', 'North Carolina'), ('Kansas', 'Missouri'), ('Kansas', 'Colorado'), ('South Carolina', 'North Carolina'), ('Illinois', 'Missouri'), ('Illinois', 'Indiana'), ('Wyoming', 'Colorado')])

    # forprint(list(map.edges))
    # print(map.number_of_edges())
    return map

def drawMap(map):
    pos = {'New England':(2316,415),'New York':(2180,485),'Pennsylvania':(2100,633),'Midcoastal':(2204,707),'Ohio':(1893,704),'West Virginia':(1993,788),'Virginia':(2118,817),'Kentucky':(1849,858),'Tennessee':(1782,969), 'North Carolina':(2147,944),'South Carolina':(2050,1050), 'Georgia':(1925,1134), 'Alabama':(1760,1153), 'Mississippi':(1625,1158), 'Florida':(2028,1353),'Michigan':(1793,539), 'Indiana':(1747,728), 'Illinois':(1614,733), 'Wisconsin':(1571,468), 'Minnesota':(1376,363), 'Iowa':(1433,641), 'North Dakota':(1149,330), 'South Dakota':(1153,493), 'Nebraska':(1152,666),'Missouri':(1490,853), 'Kansas':(1235,836),'Arkansas':(1487,1050), 'Oklahoma':(1281,1020), 'Louisiana':(1495,1258), 'Texas':(1206,1245),'Washington':(394,225), 'Oregon':(324,395),'Idaho':(575,471),'Montana':(794,328), 'Wyoming':(843,550),'California':(261,815), 'Nevada':(429,693), 'Utah':(638,747),'Colorado':(905,790), 'Arizona':(605,999), 'New Mexico':(851,1045)}
    nx.draw(map,pos)
    img = mpimg.imread('mapImage.jpg')
    plt.imshow(img)
    plt.show()

    return None

def getNodes(map,criteriaList):
    availableStates = []
    for criteria in criteriaList:
        for node in map:
            if node not in availableStates:
                if criteria[0] == 'regions':
                    if criteria[1] in map.node[node][criteria[0]]:
                        if map.node[node]['value'] == None and map.node[node]['isCrossed'] == False:
                            availableStates.append(node)
                else:
                    if map.node[node][criteria[0]] == criteria[1]:
                        if map.node[node]['value'] == None and map.node[node]['isCrossed'] == False:
                            availableStates.append(node)

    return availableStates

def autoRound():
    die1 = randint(0, 9)
    die2 = randint(0, 9)
    number1 = die1*10+die2
    number2 = die2*10+die1
    return number1,number2

class Card:
    def __init__(self,state,region):
        self.state = state
        self.region = region

class Deck:
    def __init__(self):
        listOfCards = [('Indiana','Central'),('Nevada','South'),('Washington','West'),
                       ('Illinois','North'),('Ohio','North'),('Arkansas','Central'),
                       ('South Dakota','Central'),('Wyoming','West'),('Virginia','East'),
                       ('Arizona','South'),('Mid Coastal','East'),('Texas','South'),
                       ('Kentucky','South'),('Wisconsin','Central'),('Nebraska','North'),
                       ('Montana','North'),('Kansas','Central'),('New York','North'),
                       ('North Carolina','East'),('Florida','East'),('Iowa','Central'),
                       ('Michigan','North'),('Minnesota','North'),('Louisiana','Central'),
                       ('Alabama','South'),('New England','East'),('Mississippi','East'),
                       ('Utah','West'),('South Carolina','East'),('Georgia','South'),
                       ('Oklahoma','South'),('Oregon','North'),('West Virginia','North'),
                       ('Pennsylvania','East'),('North Dakota','North'),('New Mexico','West'),
                       ('Colorado','South'),('Idaho','West'),('Tennessee','South'),
                       ('Missouri','South'),('California','West')]
        # for i card in enumerate(listOfCards):
        #     pass


def main():
    map = createMap()
    print(getNodes(map,[['regions','West'],['regions','West']]))
    print(autoRound())
    drawMap(map)


if __name__ == "__main__":
    main()
