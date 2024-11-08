# UC Merced full school map


#   == NODE SYNTAX: ==
#   <Node Name>: [
#       { <Edge1> },
#       { <Edge2> }
#   ]

#   == EDGE SYNTAX: ==
#   {'to': <destination node>, 'weight': <distance (feet)>, 'pathName': <edge name>}

graph = {
    'SRE': [
        {'to': 'node1', 'weight': 376.98, 'pathName': 'path2'},
        {'to': 'acs', 'weight': 201.30, 'pathName': 'path1'}
    ],
    'node1': [
        {'to': 'SRE', 'weight': 376.9, 'pathName': 'path2'},
        {'to': 'library1', 'weight': 358.09, 'pathName': 'scholarsLane1'}
    ],
    'acs': [
        {'to': 'SRE', 'weight': 201.30, 'pathName': 'path1'},
        {'to': 'bsp', 'weight': 276.14, 'pathName': 'academicQuad'}
    ],
    'library1': [
        {'to': 'node1', 'weight': 358.09, 'pathName': 'scholarsLane1'},
        {'to':'node2', 'weight': 348, 'pathName':'scholarsLane2'}
    ],
    'bsp': [
        {'to': 'acs', 'weight': 276.14, 'pathName': 'academicQuad'},
        {'to': 'se2', 'weight': 276.14, 'pathName': 'mineralKingBridge'}
    ],
    'NodeSE': [
        {'to': 'cob1', 'weight': 490.52, 'pathName': 'SE1WalkWay'},
        {'to': 'se2', 'weight': 165.31, 'pathName': 'mineralKingBridge2'},
        {'to': 'bsp', 'weight': 700, 'pathName': 'mineralKingBridge'}
    ],
    'se2':[
        {'to':'bsp', 'weight': 165.31, 'pathName':'mineralKingBridge2'},
        {'to':'node3', 'weight': 474.24, 'pathName':'anselAdamsRoad1'}
    ],
    'node3':[
        {'to':'se2', 'weight': 474.24, 'pathName':'anselAdamsRoad1'},
        {'to':'ssm', 'weight': 209.69, 'pathName':'scholarsPlaza'},
        {'to':'ssb', 'weight': 245.55, 'pathName':'anselAdamsRoad2'},
        {'to':'cob1', 'weight': 165.84, 'pathName':'scholarsLane4'}
    ],
    'ssm':[
        {'to':'node3', 'weight': 209.69, 'pathName':'scholarsPlaza'}
    ],
    'cob1':[
        {'to':'node3', 'weight': 165.84, 'pathName':'scholarsLane4'},
        {'to':'node2', 'weight': 220.18, 'pathName':'scholarsLane3'},
        {'to':'NodeSE', 'weight': 490.52, 'pathName':'SE1WalkWay'}
    ],
    'node2':[
        {'to':'library1', 'weight': 348, 'pathName':'scholarsLane2'},
        {'to':'cob1', 'weight': 220.18, 'pathName':'scholarsLane3'},
        {'to':'cob2', 'weight': 223.76, 'pathName':'ck'}
    ],
    'cob2':[
        {'to':'library2', 'weight': 255.36, 'pathName':'socialJusticePlaza1'},
        {'to':'node2', 'weight': 223.76, 'pathName':'ck'},
        {'to':'ssb', 'weight': 385.39, 'pathName':'socialJusticePlaza2'}
    ],
    'library2':[
        {'to':'cob2', 'weight': 255.36, 'pathName':'socialJusticePlaza1'}
    ],
    'ssb':[
        {'to':'cob2', 'weight': 385.39, 'pathName':'socialJusticePlaza2'},
        {'to':'node3', 'weight': 245.55, 'pathName':'anselAdamsRoad2'}
    ]
}
