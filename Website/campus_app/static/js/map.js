
function initMap(){
    // Map initialization
    var map = L.map('map').setView([37.3660, -120.4235], 17);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // // DEBUG: COODRINATE CHECKER
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
    L.polyline(latlngs, {color: 'red'}).addTo(map);
    map.fitBounds(latlngs);
}

