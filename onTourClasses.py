# # class board
# init
#     create nodes
#     create edges
#     positions

# assignNumber

# showBoard

# returnAvailableStatesinRegions



# # class game
# init
#     Create Deck

# autoround
    
# manualround

# DrawCards

# Roll Dice

# Reshuffle Deck

# # class ai
# pass

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint, shuffle


class Board:
    def __init__(self):
        # Lists of all states in regions
        northeast = ['New England', 'New York', 'Pennsylvania', 'Midcoastal', 'Ohio', 'West Virginia']
        southeast = ['Virginia', 'Kentucky', 'Tennessee', 'North Carolina', 'South Carolina', 'Georgia', 'Alabama', 'Mississippi', 'Florida']
        northcentral = ['Michigan', 'Indiana', 'Illinois', 'Wisconsin', 'Minnesota', 'Iowa', 'North Dakota', 'South Dakota', 'Nebraska']
        southcentral = ['Missouri', 'Kansas', 'Arkansas', 'Oklahoma', 'Louisiana', 'Texas']
        northwest = ['Washington', 'Oregon', 'Idaho', 'Montana', 'Wyoming']
        southwest = ['California', 'Nevada', 'Utah', 'Colorado', 'Arizona', 'New Mexico']

        # Create Graph and add nodes
        self.map = nx.Graph()
        # map.add_nodes_from(states)
        self.map.add_nodes_from(northeast,regions=['North','East'],value=None,isCrossed=False,isCircled=False)
        self.map.add_nodes_from(southeast,regions=['South','East'],value=None,isCrossed=False,isCircled=False)
        self.map.add_nodes_from(northcentral,regions=['North','Central'],value=None,isCrossed=False,isCircled=False)
        self.map.add_nodes_from(southcentral,regions=['South','Central'],value=None,isCrossed=False,isCircled=False)
        self.map.add_nodes_from(northwest,regions=['North','West'],value=None,isCrossed=False,isCircled=False)
        self.map.add_nodes_from(southwest,regions=['South','West'],value=None,isCrossed=False,isCircled=False)
        self.map.add_edges_from([('New Mexico', 'Oklahoma'), ('New Mexico', 'Arizona'), ('New Mexico', 'Texas'), ('New Mexico', 'Colorado'), 
                            ('Idaho', 'Montana'), ('Idaho', 'Oregon'), ('Idaho', 'Nevada'), ('Idaho', 'Washington'), ('Idaho', 'Utah'), ('Idaho', 'Wyoming'), 
                            ('California', 'Oregon'), ('California', 'Arizona'), ('California', 'Nevada'), 
                            ('Georgia', 'Alabama'), ('Georgia', 'Florida'), ('Georgia', 'South Carolina'), ('Georgia', 'Tennessee'), 
                            ('Florida', 'Alabama'), 
                            ('Texas', 'Oklahoma'), ('Texas', 'Louisiana'), ('Texas', 'Arkansas'), 
                            ('Nebraska', 'Iowa'), ('Nebraska', 'Kansas'), ('Nebraska', 'Colorado'), ('Nebraska', 'Wyoming'), ('Nebraska', 'Missouri'), ('Nebraska', 'South Dakota'), 
                            ('Montana', 'Wyoming'), ('Montana', 'North Dakota'), ('Montana', 'South Dakota'), 
                            ('Oklahoma', 'Missouri'), ('Oklahoma', 'Kansas'), ('Oklahoma', 'Colorado'), ('Oklahoma', 'Arkansas'), 
                            ('New England', 'New York'), 
                            ('Midcoastal', 'Pennsylvania'), ('Midcoastal', 'New York'), ('Midcoastal', 'Virginia'), 
                            ('West Virginia', 'Pennsylvania'), ('West Virginia', 'Ohio'), ('West Virginia', 'Kentucky'), ('West Virginia', 'Virginia'), 
                            ('Mississippi', 'Alabama'), ('Mississippi', 'Louisiana'), ('Mississippi', 'Arkansas'), ('Mississippi', 'Tennessee'), 
                            ('Pennsylvania', 'Ohio'), ('Pennsylvania', 'New York'), 
                            ('Alabama', 'Tennessee'), 
                            ('Utah', 'Wyoming'), ('Utah', 'Arizona'), ('Utah', 'Colorado'), ('Utah', 'Nevada'), 
                            ('Kentucky', 'Missouri'), ('Kentucky', 'Illinois'), ('Kentucky', 'Ohio'), ('Kentucky', 'Indiana'), ('Kentucky', 'Tennessee'), ('Kentucky', 'Virginia'), 
                            ('Washington', 'Oregon'), 
                            ('Louisiana', 'Arkansas'), 
                            ('Tennessee', 'Arkansas'), ('Tennessee', 'North Carolina'), ('Tennessee', 'Missouri'), ('Tennessee', 'Virginia'), 
                            ('Iowa', 'Minnesota'), ('Iowa', 'Wisconsin'), ('Iowa', 'Illinois'), ('Iowa', 'Missouri'), ('Iowa', 'South Dakota'), 
                            ('Wisconsin', 'Minnesota'), ('Wisconsin', 'Michigan'), ('Wisconsin', 'Illinois'), 
                            ('Oregon', 'Nevada'), 
                            ('North Dakota', 'Minnesota'), ('North Dakota', 'South Dakota'), 
                            ('Arkansas', 'Missouri'), 
                            ('Nevada', 'Arizona'), 
                            ('Michigan', 'Ohio'), ('Michigan', 'Indiana'), 
                            ('Ohio', 'Indiana'), 
                            ('South Dakota', 'Minnesota'), ('South Dakota', 'Wyoming'), 
                            ('Virginia', 'North Carolina'), 
                            ('Kansas', 'Missouri'), ('Kansas', 'Colorado'), 
                            ('South Carolina', 'North Carolina'), 
                            ('Illinois', 'Missouri'), ('Illinois', 'Indiana'), 
                            ('Wyoming', 'Colorado')])

    def assignNumber(self, state, value):
        self.map.nodes[state]['value'] = value

    def showMap(self):
        pos = {'New England':(2316,415),'New York':(2180,485),'Pennsylvania':(2100,633),'Midcoastal':(2204,707),'Ohio':(1893,704),'West Virginia':(1993,788),'Virginia':(2118,817),'Kentucky':(1849,858),'Tennessee':(1782,969), 'North Carolina':(2147,944),'South Carolina':(2050,1050), 'Georgia':(1925,1134), 'Alabama':(1760,1153), 'Mississippi':(1625,1158), 'Florida':(2028,1353),'Michigan':(1793,539), 'Indiana':(1747,728), 'Illinois':(1614,733), 'Wisconsin':(1571,468), 'Minnesota':(1376,363), 'Iowa':(1433,641), 'North Dakota':(1149,330), 'South Dakota':(1153,493), 'Nebraska':(1152,666),'Missouri':(1490,853), 'Kansas':(1235,836),'Arkansas':(1487,1050), 'Oklahoma':(1281,1020), 'Louisiana':(1495,1258), 'Texas':(1206,1245),'Washington':(394,225), 'Oregon':(324,395),'Idaho':(575,471),'Montana':(794,328), 'Wyoming':(843,550),'California':(261,815), 'Nevada':(429,693), 'Utah':(638,747),'Colorado':(905,790), 'Arizona':(605,999), 'New Mexico':(851,1045)}
        valuesDict = nx.get_node_attributes(self.map, 'value')
        nx.draw(self.map,pos,labels=valuesDict,node_color='#ffffff')
        img = mpimg.imread('mapImage.jpg')
        plt.imshow(img)
        plt.show()

    def availableStatesInRegions(self, regions):
        availableStates = []
        for state in self.map:
            if self.map.nodes[state]['value'] == None:
                if self.map.nodes[state]['isCrossed'] == False:
                    if self.map.nodes[state]['regions'][0] in regions or self.map.nodes[state]['regions'][1] in regions:
                        print(state)

class Card:
    def __init__(self,state,region):
        self.state = state
        self.region = region

class Deck:
    def __init__(self):
        self.deck = []
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
        for card in listOfCards:
            self.deck.append(Card(card[0],card[1]))
        shuffle(self.deck)

    def setupGame(self):
        setupCards = []
        for i in range(4):
            setupCards.append(self.deck.pop(i))

def main():
    board = Board()
    deck = Deck()
    print(map)
    board.assignNumber('Utah',1)
    print(board.map.nodes['Utah'])
    board.assignNumber('Arizona',2)
    print(board.map.nodes['Arizona']['value'])
    # board.showMap()
    board.availableStatesInRegions(['West'])
    print(deck.deck[0].state)
    

if __name__ == "__main__":
    main()