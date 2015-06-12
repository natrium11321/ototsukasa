var map;

function initialize() {
  var univ = new google.maps.LatLng(35.712678,139.761989); //Univ of Tokyo
  var mapOptions = {
    zoom: 15,
    center: univ
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  $.getJSON("/cgi-bin/get_info.py?sex=F",function(data){
    for (var i = 0; i < data.length ; i++){
      info = data[i];
      makeMarker(info);
    }
  })

};

function makeMarker(info) {

  //トイレの状態を表すピクトグラム
  var empty ="white.png";
  var occupied = "red.png";
  var reserved = "yellow.png";

  var icon;
  if (info["empty"] == 0){
    icon = "red.png";
  }else if(info["empty"] == 1){
    icon = "yellow.png";
  }else{
    icon = "white.png";
  }

  var content = '<h1>' + info["address"] + '</h1>'

  for (var i=0;i<info["empty"];i++){
    content += '<img src="' + empty +'" width="30px" height="30px" alt="空き">';
  }
  for (var i=0;i<info["reserved"];i++){
    content += '<img src="'+occupied+'" width="30px" height="30px" alt="予約済み">';
  }
  for (var i=0;i<info["occupied"];i++){
    content += '<img src="'+reserved+'" width="30px" height="30px" alt="使用中">';
  }
  content += '<p>最新のレビュー:' + info["review_comment"] + '</p>'

  //空きがあるときは予約ボタン
  if (info["empty"] > 0){
    content +=   '<p><form action="/cgi-bin/reserve.py" method="POST"><input type="hidden" name="sex" value="M"><input type="hidden" name="pos_id" value=' + info["pos_id"] + '><div class="buttonarea"><input type="submit" value="予約" class="btn btn-default"></div></form></p>'
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
