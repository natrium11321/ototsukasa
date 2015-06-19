var map;

function initialize() {
  var univ = new google.maps.LatLng(35.712678,139.761989); //Univ of Tokyo
  var mapOptions = {
    zoom: 15,
    center: univ
  };
  map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);

  var currentInfoWindow = null;
  $.getJSON("/cgi-bin/get_info.py?sex=M",function(data){
    for (var i = 0; i < data.length ; i++){
      info = data[i];
      makeMarker(info);
    }
  })

  function makeMarker(info) {

    //トイレの状態を表すピクトグラム
    var empty ="logo/pictogram_free.svg";
    var occupied = "logo/pictogram_used.svg";
    var reserved = "logo/pictogram_reserved.svg";

    var icon;
    if (info["empty_num"] == 0){
      icon = "red.png";
    }else if(info["empty_num"] == 1){
      icon = "yellow.png";
    }else{
      icon = "white.png";
    }

    var content = '<h1>' + info["name"] + '</h1>'

    for(var i=0;i<info["toilets"].length;i++){
      if (info["toilets"][i] === "Empty"){
        content += '<img src="' + empty +'" width="30px" height="30px" alt="空き">';
      }else if (info["toilets"][i] === "Reserved") {
        content += '<img src="'+reserved+'" width="30px" height="30px" alt="予約済み">';
      }else if (info["toilets"][i] === "Occupied") {
        content += '<img src="'+occupied+'" width="30px" height="30px" alt="使用中">';
      }
    }

    content += '<p>最新のレビュー:' + info["review_comment"] + '</p>'

    //空きがあるときは予約ボタン
    if (info["empty_num"] > 0){
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
      if(currentInfoWindow){
        currentInfoWindow.close();
      }
      infowindow.open(map,marker);
      currentInfoWindow = infowindow;
    })
  };
};

google.maps.event.addDomListener(window, 'load', initialize);
