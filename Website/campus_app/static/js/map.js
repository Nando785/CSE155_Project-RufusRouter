
function initMap(){
    // Map initialization
    var map = L.map('map').setView([37.3660, -120.4235], 17);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // // === DEBUG: PRINT ALL NODES AND THEIR COORDINATES ===
    // // Node coordinates with respective names
    // var node_coordinates = {
    //     'se2': [37.36629164813181, -120.42154490947725],
    //     'node3': [37.36720401785676, -120.42259633541109],
    //     'sre': [37.364419991461546, -120.4246884584427],
    //     'node1': [37.36514478367969, -120.42549312114717],
    //     'acs': [37.36394671167786, -120.42415738105775],
    //     'library1': [37.3659633777708, -120.42435586452486],
    //     'bsp': [37.36473975555329, -120.42364239692688],
    //     'NodeSE': [37.366010270949076, -120.42193114757539],
    //     'ssm': [37.36752377277552, -120.42220473289491],
    //     'cob1': [37.36689704756419, -120.42305231094362],
    //     'node2': [37.36650483154995, -120.42360484600069],
    //     'cob2': [37.36697806054532, -120.42417347431183],
    //     'library2': [37.36647924687576, -120.4247957468033],
    //     'ssb': [37.36771990299146, -120.42320251464845]
    // };

    // // Loop through the coordinates and add markers
    // for (var node in node_coordinates) {
    //     var coords = node_coordinates[node];
    //     var marker = L.marker(coords).addTo(map);
        
    //     // Create a popup with both the node name and coordinates
    //     var popupContent = "<strong><u>Node:</u></strong><br>" + node + "<br><strong><u>Coordinates:</u></strong><br>" + coords[0].toFixed(14) + ", " + coords[1].toFixed(14);
    //     marker.bindPopup(popupContent); // Bind the popup to the marker
    // }

    // // === DEBUG: COODRINATE CHECKER ===
    // map.on('click', function(e) { 
    //     // Get the latitude and longitude from the event object
    //     var latlng = e.latlng; 
    //     // Create a marker at the clicked location 
    //     var marker = L.marker(latlng).addTo(map); 
    //     // Create a popup with the coordinates and bind it to the marker 
    //     marker.bindPopup("Coordinates: " + latlng.lat + ", " + latlng.lng).openPopup();
    // });

    return map
}

function addPath(map, pathCoordinates){
    
    // Show line on map
    const latlngs = pathCoordinates.map(coord => [coord.latitude, coord.longitude]);
    console.log("Pushing to map: \n", latlngs)
    L.polyline(latlngs, {color: 'red'}).addTo(map);
    map.fitBounds(latlngs);
}

