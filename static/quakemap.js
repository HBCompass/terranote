<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDXY13ltRR9wS-mxSaXuyEY-F6hiGm4d4E"></script>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?libraries=visualization"></script>
<script src="https://maps.googleapis.com/maps/api/js"></script>



<script>
	var map;

	// Pull in location from database

	

 	// Pull in magnitude from database

 	function initialize() {
 	  var mapOptions = {
 	    zoom: 2,
 	    center: new google.maps.LatLng(2.8, -187.3),
 	    mapTypeId: google.maps.MapTypeId.TERRAIN
 	  };

 	  map = new google.maps.Map(document.getElementById('map_canvas'),
 	      mapOptions);

 	}


 	// Put circle marker on location
	

 	    var marker = new google.maps.Marker({
 	      position: latLng,
 	      map: map,
 	      icon: getCircle(earthquake.properties.mag)
 	    });
 	  }
 	}

 	function getCircle(magnitude) {
 	  return {
 	    path: google.maps.SymbolPath.CIRCLE,
 	    fillColor: 'red',
 	    fillOpacity: .2,
 	    scale: Math.pow(2, magnitude) / Math.PI,
 	    strokeColor: 'white',
 	    strokeWeight: .5
 	  };
}
</script>