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
        #{'to':'node2', 'weight': NULL, 'pathName':'scholarsLane2'}
    ],
    'bsp': [
        {'to': 'acs', 'weight': 276.14, 'pathName': 'academicQuad'},
        {'to': 'se2', 'weight': 276.14, 'pathName': 'mineralKingBridge'}
    ],
    # 'se2':[
    #     {'to':'bsp', 'weight': NULL, 'pathName':'mineralKingsBridge'},
    #     {'to':'node3', 'weight': NULL, 'pathName':'anselAdamsRoad1'}
    # ],
    # 'node3':[
    #     {'to':'se2', 'weight': NULL, 'pathName':'anselAdamsRoad1'},
    #     {'to':'ssm', 'weight': NULL, 'pathName':'scholarsPlaza'},
    #     {'to':'ssb', 'weight': NULL, 'pathName':'anselAdamsRoad2'},
    #     {'to':'cob1', 'weight': NULL, 'pathName':'scholarsLane4'}
    # ],
    # 'ssm':[
    #     {'to':'node3', 'weight': NULL, 'pathName':'scholarsPlaza'}
    # ],
    # 'cob1':[
    #     {'to':'node3', 'weight': NULL, 'pathName':'scholarsLane4'},
    #     {'to':'node2', 'weight': NULL, 'pathName':'scholarsLane3'}
    # ],
    # 'node2':[
    #     {'to':'library1', 'weight': NULL, 'pathName':'scholarsLane2'},
    #     {'to':'cob1', 'weight': NULL, 'pathName':'scholarsLane3'},
    #     {'to':'cob2', 'weight': NULL, 'pathName':'ck'}
    # ],
    # 'cob2':[
    #     {'to':'library2', 'weight': NULL, 'pathName':'socialJusticePlaza1'},
    #     {'to':'node2', 'weight': NULL, 'pathName':'ck'},
    #     {'to':'ssb', 'weight': NULL, 'pathName':'socialJusticePlaza2'}
    # ],
    # 'library2':[
    #     {'to':'cob2', 'weight': NULL, 'pathName':'socialJusticePlaza1'}
    # ],
    # 'ssb':[
    #     {'to':'cob2', 'weight': NULL, 'pathName':'socialJusticePlaza2'},
    #     {'to':'node3', 'weight': NULL, 'pathName':'anselAdamsRoad2'}
    # ]
}
