// //INIT MAP
// let map, infoWindow;
//
// //PERSONAL VAR
//
// //END PERSONAL VARS
//
// //Init Markers
// var markersOnMap = [
//     {
//         LatLng: [{
//             lat: lat,
//             lng: lng
//         }]
//     },
//     {
//         LatLng: [{
//             lat: 19.392856,
//             lng: -99.162641
//         }]
//     },
//     {
//         LatLng: [{
//             lat: 19.393686,
//             lng: -99.170752
//         }]
//     },
//     {
//         LatLng: [{
//             lat: 19.408309,
//             lng: -99.163104
//         }]
//     },
//     {
//         LatLng: [{
//             lat: 19.396479,
//             lng: -99.173468
//         }]
//     }
// ]
//
// function addMarkerInfo() {
//     for (var i = 0; i < markersOnMap.length; i++) {
//         const marker = new google.maps.Marker({
//             position: markersOnMap[i].LatLng[0],
//             map: map
//         });
//     }
// }
//
// //Markers
//
// function initMap() {
//     map = new google.maps.Map(document.getElementById("map"), {
//         center: {lat: 39.742043, lng: -104.991531},
//         zoom: 14,
//         mapTypeId: "roadmap",
//         mapId: '73323dfcd106d471',
//         accuracy: '10',
//     });
//     addMarkerInfo();
//
//
//     //LOCALIZATION BUTTON
//     infoWindow = new google.maps.InfoWindow();
//
//     const locationButton = document.createElement("button");
//
//     locationButton.textContent = "MI UBICACION";
//     locationButton.classList.add("custom-map-control-button");
//     map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
//     locationButton.addEventListener("click", () => {
//         // Try HTML5 geolocation.
//         if (navigator.geolocation) {
//             navigator.geolocation.getCurrentPosition(
//                 (position) => {
//                     const pos = {
//                         lat: position.coords.latitude,
//                         lng: position.coords.longitude,
//                     };
//
//                     infoWindow.setPosition(pos);
//                     infoWindow.setContent("Location found.");
//                     infoWindow.open(map);
//                     map.setCenter(pos);
//                 },
//                 () => {
//                     handleLocationError(true, infoWindow, map.getCenter());
//                 }
//             );
//         } else {
//             // Browser doesn't support Geolocation
//             handleLocationError(false, infoWindow, map.getCenter());
//         }
//     });
// }
//
// function handleLocationError(browserHasGeolocation, infoWindow, pos) {
//     infoWindow.setPosition(pos);
//     infoWindow.setContent(
//         browserHasGeolocation
//             ? "Error: The Geolocation service failed."
//             : "Error: Your browser doesn't support geolocation."
//     );
//     infoWindow.open(map);
// }
//
// //ENDS GEOLOCALIZATINO BUTTON









