var map;

function initialize() {
  var univ = new google.maps.LatLng(35.712678,139.761989); //Univ of Tokyo
  var mapOptions = {
    zoom: 15,
    center: univ
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  $.getJSON("/cgi-bin/get_info.py",function(data){
    for (var i = 0; i < data.length ; i++){
      info = data[i];
      makeMarker(info);
    }
  })

};

function makeMarker(info) {

  if (info["empty"] > 0){
    //空き有り　アイコン白
    var icon = "https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=WC|FFFFFF";
    var content = '<h2>Empty:'+info["empty"]+' Reserved:'+ info["reserved"] + ' Occupied:' + info["occupied"] + '</h2><p><form action="/cgi-bin/reserve.py" method="POST"><input type="hidden" name="pos_id" value=' + info["pos_id"] + '><input type="submit" value="予約"></form></p>'

  }else{
    //空き無し　アイコン赤
    var icon =   "https://chart.googleapis.com/chart?chst=d_map_pin_icon&chld=WC|FF0000";
    var content = '<h2>Empty:'+info["empty"]+' Reserved:'+ info["reserved"] + ' Occupied:' + info["occupied"] + '</h2>'
  }

  var marker = new google.maps.Marker({
    position: new google.maps.LatLng(info["lat"],info["lng"]),
    map: map,
    icon: icon
  });


  var infowindow = new google.maps.InfoWindow({
    content: content
  });

  google.maps.event.addDomListener(marker,'click',function(){
    infowindow.open(map,marker);
  })
};

google.maps.event.addDomListener(window, 'load', initialize);
