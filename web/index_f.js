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

  if (info["empty"] > 0){
    //空き有り
    if (info["empty"] > 1){
      //空き2以上 アイコン白
      var icon = "white.png";
    }else{
      //空き1　アイコン黄色
      var icon = "yellow.png";
    }
    var content = '<h1>' + info["address"] + '</h1><h2>空き:'+info["empty"]+' 予約中:'+ info["reserved"] + ' 使用中:' + info["occupied"] + '</h2><p>最新のレビュー:' + info["review_comment"] + '</p><p><form action="/cgi-bin/reserve.py" method="POST"><input type="hidden" name="sex" value="F"><input type="hidden" name="pos_id" value=' + info["pos_id"] + '><div class="buttonarea"><input type="submit" value="予約" class="btn btn-default"></div></form></p>'

  }else{
    //空き無し　アイコン赤
    var icon =   "red.png";
    var content = '<h1>' + info["address"] + '</h1><h2>空き:'+info["empty"]+' 予約中:'+ info["reserved"] + ' 使用中:' + info["occupied"] + '</h2>'
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
