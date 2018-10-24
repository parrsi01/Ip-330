/* jshint esversion: 6 */
/* jshint node: true */
'use strict';


  var teams =['Arsenal FC', 'Aston Villa FC', 'Blackburn Rovers FC','Bolton Wanderers FC','Chelsea FC','Everton FC',
'Fulham FC','Liverpool FC','Manchester City FC','Manchester United FC','Norwich City FC','Queens Park Rangers FC',
'Stoke City FC','Tottenham Hotspur FC','West Bromwich Albion FC','Wigan Athletic FC','Wolverhampton Wanderers FC',
'Hull City AFC','Burnley FC','Birmingham City FC','Leicester City FC','Southampton FC','Leeds United AFC',
'Derby County FC','Middlesbrough FC','Sheffield Wednesday FC','Watford FC','Ipswich Town FC','Nottingham Forest FC',
'Crystal Palace FC','Reading FC','Sheffield United FC','Barnsley FC','Millwall FC','Rotherham United FC',
'Bristol City FC','Huddersfield Town AFC','Brighton & Hove Albion FC','Brentford FC','West Ham United FC','AFC Bournemouth',
'Burton Albion FC','Preston North End FC'];




 function initMap() {
  //create new interactive 
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: {lat: -34.397, lng: 150.644}
  });
  var geocoder = new google.maps.Geocoder();

  //PANORAMA-------------------------------------------------------------


$.ajax({
  headers: { 'X-Auth-Token': '38cefef3d6df46c78eeb5a4bce1c075a' },
  url: `http://api.football-data.org/v2/teams`,
  dataType: 'json',
  type: 'GET',
}).done(function loop(response) {
  //var football = JSON.stringify(response);
  
  
  document.getElementById('submit').addEventListener('click', function() {
  geocodeAddress(geocoder, map, response);
  });
  

});

}



function geocodeAddress(geocoder, resultsMap, response) {
  //var address = team_address;
  var input = document.getElementById("input").value;
  //console.log(input);
  for (var i = 0; i < response.teams.length; i++){
      if (response.teams[i].name == input){
        var team_address = response.teams[i].address;
        console.log(team_address);
        document.getElementById("team_name").innerHTML = "Team Name: " + response.teams[i].name
        document.getElementById("founded").innerHTML = "Year founded: " + response.teams[i].founded;
        //console.log(response.teams[i].address);

        var img = document.createElement("img")
        img.src = `https://maps.googleapis.com/maps/api/streetview?size=600x300&location=${team_address}&heading=151.78&pitch=-0.76&key=AIzaSyDKHAeEok60rvTMF-xLx50hNvDdl3w3VDg`
        document.body.appendChild(img);

        geocoder.geocode({'address': team_address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
              map: resultsMap,
              position: results[0].geometry.location
            });
          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });

      }
    }


}
