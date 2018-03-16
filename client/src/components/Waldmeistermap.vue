<template>
  <div id="app">
    <div id='map'></div>
  </div>
</template>

<script>
import AreaService from '@/services/AreaService'

export default {
  data () {
    return {
      title: 'WaldmeisterMap',
      zoom:13,
      center:[51.505, -0.09],
      url:"http://{s}.tile.osm.org/{z}/{x}/{y}.png",
    }
  },
  async mounted () {
    var startPoint = [47.4348826, 8.7460494];
    var map = L.map('map', {editable: true}).setView(startPoint, 13),
    tilelayer = L.tileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}', 
    {maxZoom: 20, 
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 18,
    ext: 'png'
    }).addTo(map);

    // try{
    //   const AreasToDisplay = AreaService.getAreas({ 
    //     })
    //     .then( (response) => {
    //       console.log(response.data)
    //     })
    //   } catch (error) {
    //     //console.log(response.error)
    //   }
    //   //console.log(response.data)
    
    L.NewPolygonControl = L.Control.extend({

        options: {
            position: 'topleft'
        },

        onAdd: function (map) {
            var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
                link = L.DomUtil.create('a', '', container);

            link.href = '#';
            link.title = 'Create a new polygon';
            link.innerHTML = 'add';
            L.DomEvent.on(link, 'click', L.DomEvent.stop)
                      .on(link, 'click', function () {
                        map.editTools.startPolygon();
                      });
            container.style.display = 'block';
            map.editTools.on('editable:enabled', function (e) {
                container.style.display = 'none';
            });
            map.editTools.on('editable:disable', function (e) {
                container.style.display = 'block';
            });
            return container;
        }
    });

    
    L.AddPolygonShapeControl = L.Control.extend({

        options: {
            position: 'topleft'
        },

        onAdd: function (map) {
            var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
                link = L.DomUtil.create('a', '', container);

            link.href = '#';
            link.title = 'Create a new polygon';
            link.innerHTML = 'edit';
            L.DomEvent.on(link, 'click', L.DomEvent.stop)
                      .on(link, 'click', function () {
                          if (!map.editTools.currentPolygon) return;
                          map.editTools.currentPolygon.editor.newShape();
                      });
            container.style.display = 'none';
            map.editTools.on('editable:enabled', function (e) {
                container.style.display = 'block';
            });
            map.editTools.on('editable:disable', function (e) {
                container.style.display = 'none';
            });

            return container;
        }
    });
    


    map.addControl(new L.NewPolygonControl());
    map.addControl(new L.AddPolygonShapeControl());

    
    map.on('layeradd', function (e) {
        if (e.layer instanceof L.Polygon) e.layer.on('click', L.DomEvent.stop).on('click', e.layer.toggleEdit);
    });
    
    map.on('layerremove', function (e) {
        if (e.layer instanceof L.Polygon) e.layer.off('click', L.DomEvent.stop).off('click', e.layer.toggleEdit);
    });

    
    map.editTools.on('editable:enable', function (e) {
        if (this.currentPolygon) this.currentPolygon.disableEdit();
        this.currentPolygon = e.layer;
        this.fire('editable:enabled');
    });

    map.editTools.on('editable:disable', function (e) {
        delete this.currentPolygon;
    });

    map.editTools.on('editable:drawing:commit', function (e) {
        console.log("stoppediting");
        console.log(this.currentPolygon);
        console.log(this.currentPolygon.editor.tools.currentPolygon._latlngs);
    })

    
    /*
  var vegetationsLayer = L.geoJson(vegetation, { 
      style: function(feature) {
            switch (feature.properties.EK72) {
                case '1': return {color: "#f2142b"};
                case '2': return {color: "#f20a50"};
                case '6': return {color: "#de3629"};
                case '7a': return {color: "#a45930"};
                case '7as': return {color: "#008e83"};
                case '7b': return {color: "#cb006c"};
                case '7e': return {color: "#c83025"};
                case '7f': return {color: "#6c6832"};
                case '7g': return {color: "#00a772"};
                case '7stern': return {color: "#cb006c"};
                case '8a': return {color: "#8c2e22"};
                case '8as': return {color: "#008e84"};
                case '8d': return {color: "#c11524"};
                case '8e': return {color: "#744531"};
                case '8f': return {color: "#644633"};
                case '8g': return {color: "#00a773"};
                case '8stern': return {color: "#c9057d"};
                case '9': return {color: "#9ebd4b"};
                case '10': return {color: "#bdc156"};
                case '10w': return {color: "#ece650"};
                case '11': return {color: "#008c4e"};
                
              }
          },
    onEachFeature: function(feature, layer) {
      var label = L.marker(layer.getBounds().getCenter(), {
        icon: L.divIcon({
          className: 'propertyLabel',
          html: feature.properties.EK72,
          iconSize: [0, 0],
          direction: 'auto'
        })
      }).addTo(map);
    }

    }).addTo(map);
      //bounding box auto
    map.fitBounds(vegetationsLayer.getBounds());

    var popup = L.popup();

    //Handle click on map
    function onMapClick(e) {
      
        popup
            .setLatLng(e.latlng)
            .setContent("You clicked the map at " + e.latlng.toString())
            .openOn(map);
            
            //map.editTools.cancelDrawing();
    }
    map.on('click', onMapClick);

    //Handle click on polygon
    var onPolyClick = function(event){
        //callFancyboxIframe('flrs.html')
        //var label = event.target.feature.properties.EK72;
        alert(event.target);
    };
    vegetationsLayer.on('click', onPolyClick);

    */

    this.MyAreas = (await AreaService.getAreas()).data

    //map.data.addGeoJson(vegetation);

    var val;
    for (val of this.MyAreas) {
      console.log(val.polygon.coordinates[0][0]);
    
    /*
    var poly = L.polygon([
      [
        val.polygon.coordinates[0][0][0],
        val.polygon.coordinates[0][0][1],
        val.polygon.coordinates[0][0][2],
        val.polygon.coordinates[0][0][3]
      ]
    ]).addTo(map);
    poly.enableEdit();
    */
    }

    
    //console.log(this.MyAreas[1].polygon.coordinates[0][0][0])

    }

  }
</script>

<style type='text/css'>
      body { margin:0; padding:0; }
      #map { position:absolute; top:0; bottom:0; right: 0; left: 0; width:100%; }
      .propertyLabel { color: white; text-shadow: 1px 1px black; opacity: 0.4;}

      @import "~assets/css/vegetationskarte_minimal.geojson";

</style>

<!-- <style lang="scss">
@import './assets/leaflet.css';
</style> -->