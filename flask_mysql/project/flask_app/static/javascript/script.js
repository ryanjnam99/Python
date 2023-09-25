console.log("success");
// const radius = document.querySelector("#radius");
// const googleAPI = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyCvRnqTEfA4_J54fue8MTPoL6nhoDuTfRA&location=47.6192,-122.2023&radius="+radius.value+"&type=restaurant";

const googleDisplay = document.querySelector("#googleList");
function getMapData(event) {
    const radius = document.querySelector("#radius");
    const googleAPI = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyCvRnqTEfA4_J54fue8MTPoL6nhoDuTfRA&location=47.6192,-122.2023&radius="+radius.value+"&type=restaurant&minprice=3";
    event.preventDefault();
    fetch(googleAPI)
        .then(response => response.json())
        .then(mapData => 
            {   console.log(mapData.results)
                googleDisplay.innerHTML += `
                <div class="foodBox">
                    <p>Name: ${mapData.place_id}</p>
                    <p>Price: ${mapData.price_level}</p>
                    <p>Location: ${mapData.vicinity}</p>
                    <p>Rating: ${mapData.rating}</p>
                </div>`
            }
            )
        .catch(err => console.log(err))
}


// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow;
var myPlace = { lat: 47.6192, lng: -122.2023 };
var service = new google.maps.places.PlacesService(map);
service.nearbySearch({
    location: myPlace,
    radius: 1000000,
    types: ['restaurant'],
    minprice: 2,
}, callback);
initMap();
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 47.6192, lng: -122.2023 },
        zoom: 10,
    });
    infoWindow = new google.maps.InfoWindow();

    const locationButton = document.createElement("button");

    locationButton.textContent = "Pan to Current Location";
    locationButton.classList.add("custom-map-control-button");
    map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
    locationButton.addEventListener("click", () => {
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const pos = {
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    };

                    infoWindow.setPosition(pos);
                    infoWindow.setContent("Location found.");
                    infoWindow.open(map);
                    map.setCenter(pos);
                },
                () => {
                    handleLocationError(true, infoWindow, map.getCenter());
                }
            );
        } else {
            // Browser doesn't support Geolocation
            handleLocationError(false, infoWindow, map.getCenter());
        }
    });
}


// function handleLocationError(browserHasGeolocation, infoWindow, pos) {
//     infoWindow.setPosition(pos);
//     infoWindow.setContent(
//         browserHasGeolocation
//             ? "Error: The Geolocation service failed."
//             : "Error: Your browser doesn't support geolocation."
//     );
//     infoWindow.open(map);
// }

// function callback(results, status) {
//     if (status === google.maps.places.PlacesServiceStatus.OK) {
//         for (var i = 0; i < results.length; i++) {
//             createMarker(results[i]);
//         }
//     }
// }

// function createMarker(place) {
//     var placeLoc = place.geometry.location;
//     var marker = new google.maps.Marker({
//         map: map,
//         position: place.geometry.location
//     });

//     google.maps.event.addListener(marker, 'click', function () {
//         infowindow.setContent(place.name);
//         infowindow.open(map, this);
//     });
// }




