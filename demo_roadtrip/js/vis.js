
(function() {
     google.maps.event.addDomListener(window, 'load', initialize);

     var CHICAGO = new google.maps.LatLng(41.850033, -87.6500523);
     var directionsView;

     function initialize() {
          directionsView = new google.maps.DirectionsRenderer();
          var map = new google.maps.Map(document.getElementById('map-canvas'),
               {
                    center: CHICAGO,
                    zoom: 7,
               });
          directionsView.setMap(map);

          $.getJSON('res/data.json', handleJSONDataLoaded);
     }

     function handleJSONDataLoaded(jsonData) {
          var points = jsonData.route.map(function(name) {
              return {location: name};
          });
                                                      
          var request = {
              origin: points.shift().location,
              destination: points.pop().location,
              waypoints: points,
              travelMode: google.maps.TravelMode.DRIVING,
          };

          var directionsService = new google.maps.DirectionsService();
          directionsService.route(request, handleRouteLoaded);
     }

     function handleRouteLoaded(result, status) {
          if (status === google.maps.DirectionsStatus.OK) {
               directionsView.setDirections(result);
          }
     }
})();
