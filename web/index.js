var map;

function initialize() {
  var univ = new google.maps.LatLng(35.712678,139.761989); //Univ of Tokyo
  var mapOptions = {
    zoom: 15,
    center: univ
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var marker = new google.maps.Marker({
    position: univ,
    map: map,
    title:"Hello World!",
    icon: "https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=WC|FFFFFF"
  });

  var infowindow = new google.maps.InfoWindow({
    content: '<h2>The University of Tokyo.</h2><p>status:Open</p><p>rate:4.0</p><p><form action="/cgi-bin/reserve.py" method="POST"><input type="hidden" name="id" value="0"><input type="submit" value="予約"></form></p>'
  });

  google.maps.event.addListener(marker, 'click', function() {
    infowindow.open(map,marker);
  });

  var bld6 = new google.maps.Marker({
    position: new google.maps.LatLng(35.7143987,139.7612711),
    map: map,
    icon: "https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=WC|FF0000"
  });

  var bld6_window = new google.maps.InfoWindow({
    content: "<h2>Bld.6,Engineering,The University of Tokyo</h2><p>status: <font color ='FF0000'>Used</font></p><p>rate:2.5</p>"
  });

  google.maps.event.addListener(bld6, 'click', function() {
    bld6_window.open(map,bld6);
  });

  var bld14 = new google.maps.Marker({
    position: new google.maps.LatLng(35.714265, 139.75929),
    map: map,
    icon: "https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=WC|FFFF00"
  });

  var bld14_window = new google.maps.InfoWindow({
    content: "<h2>Bld.14,Engineering,The University of Tokyo</h2><p>status:<font color='FFFF00'>Reserved</font></p><p>rate:3.0</p>"
  });

  google.maps.event.addListener(bld14, 'click', function() {
    bld14_window.open(map,bld14);
  });

}

google.maps.event.addDomListener(window, 'load', initialize);
