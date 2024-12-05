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
        {'to': 'NodeSE', 'weight': 276.14, 'pathName': 'mineralKingBridge'}
    ],
    'NodeSE': [
        {'to': 'cob1', 'weight': 490.52, 'pathName': 'SE1WalkWay'},
        {'to': 'se2', 'weight': 165.31, 'pathName': 'mineralKingBridge2'},
        {'to': 'bsp', 'weight': 700, 'pathName': 'mineralKingBridge'}
    ],
    'se2':[
        {'to':'NodeSE', 'weight': 165.31, 'pathName':'mineralKingBridge2'},
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

node_coordinates = {
    'se2': [37.36629164813181, -120.42154490947725],
    'node3': [37.36720401785676, -120.42259633541109],
    'sre': [37.364419991461546, -120.4246884584427],
    'node1': [37.36514478367969, -120.42549312114717],
    'acs': [37.36394671167786, -120.42415738105775],
    'library1': [37.3659633777708, -120.42435586452486],
    'bsp': [37.36473975555329, -120.42364239692688],
    'NodeSE': [37.366010270949076, -120.42193114757539],
    'ssm': [37.36752377277552, -120.42220473289491],
    'cob1': [37.36689704756419, -120.42305231094362],
    'node2': [37.36650483154995, -120.42360484600069],
    'cob2': [37.36697806054532, -120.42417347431183],
    'library2': [37.36647924687576, -120.4247957468033],
    'ssb': [37.36771990299146, -120.42320251464845]
}
