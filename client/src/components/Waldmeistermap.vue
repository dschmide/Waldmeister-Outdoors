<template>
  <div id="app">
    <v-layout row justify-center>
      <v-dialog v-model="saveDialog" max-width="500px">
        <v-card>
          <v-card-title>
            <span>Create new Userarea</span>
            <v-spacer></v-spacer>
          </v-card-title>
          <v-card-text>
            <v-text-field label="Label" type="text" v-model="userAreaLabel"></v-text-field>
            Public Area:
            <input type="checkbox" id="checkbox" v-model="checked">
            <label for="checkbox"> {{ checked }}</label>
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" flat @click.stop="saveDialog=false">Close</v-btn>
            <v-btn color="primary" dark class="light-green" flat @click="save">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
    <div id='map'>
    </div>
  </div>
</template>
<script>
import AreaService from '@/services/AreaService'
import Vegetation from '@/components/data/vegetationskarte_minimal.json'

const startPoint = [47.4348826, 8.7460494];
const attributionForMap = 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> and <a href="https://maps.zh.ch">maps.zh.ch</a>'
const tileLayerURL = 'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}.{ext}'

const PolygonButtonTextIdle = 'Add'
const PolygonButtonTextEditing = 'Edit'
const ToggleVegetationButtonLabel= 'Veg'
const ToggleUserAreasLabel = "UA"

var geolocationOptions = {
  enableHighAccuracy: false,
  timeout: 60000,
  maximumAge: Infinity
};

var myGeoJsonPoly = [];
var myCoords
var PolyCoordinates

var AllUserAreas = []



export default {
  data() {
    return {
      checked: "",
      userAreaLabel: "",
      vegetation: Vegetation,
      title: 'WaldmeisterMap',
      zoom: 13,
      center: [51.505, -0.09],
      url: "http://{s}.tile.osm.org/{z}/{x}/{y}.png",

      saveDialog: false,
      notifications: false,
      sound: true,
      widgets: false
    }
  },
  methods: {
    // This Function sends a drawn polygon to the server and closes the save dialog
    save() {
      var theArea = {
        "label": this.userAreaLabel,
        "public": !!this.checked,
        "polygon": {
          "type": "MultiPolygon",
          "coordinates": [
            [myGeoJsonPoly]
          ]
        }
      }
      AreaService.postArea(theArea);
      this.saveDialog = false;
      myGeoJsonPoly = [];
    }
  },

  // This code is executed when the Waldmeistermap.vue is mounted on the page
  async mounted() {
    //Show my location on map
    navigator.geolocation.getCurrentPosition(geoLocationSuccess, geoLocationError, geolocationOptions);
    function geoLocationSuccess(pos) {
      var crd = pos.coords;
      console.log('Your current position is:');
      console.log(`Latitude : ${crd.latitude}`);
      console.log(`Longitude: ${crd.longitude}`);
      console.log(`More or less ${crd.accuracy} meters.`);

      //Draws the circle
      L.circle([crd.latitude, crd.longitude], crd.accuracy, {color:'white',opacity:0,fillColor: 'blue',fillOpacity:.15}).addTo(map);
      L.circle([crd.latitude, crd.longitude], 10, {color:'white',opacity:1,fillColor: 'blue',fillOpacity:.7}).addTo(map);
      
    }

    function geoLocationError(err) {
      console.warn(`ERROR(${err.code}): ${err.message}`);
    }


    // init the map object
    var map = L.map('map', { editable: true }).setView(startPoint, 15),
      tilelayer = L.tileLayer(tileLayerURL, {
        attribution: attributionForMap,
        subdomains: 'abcd',
        minZoom: 0,
        maxZoom: 18,
        ext: 'png'
      }).addTo(map);

    var UserAreaGroup = L.layerGroup();

    //Geolocation and Marker 
    //Here the browser attempts to return a geolocation and asks the user for permission
    map.locate({setView: true, maxZoom: 15, enableHighAccuracy:false, timeout:60000, maximumAge:Infinity});

    //Add the Polygon Control Button for drawing Polygons on the map
    L.NewPolygonControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);
        link.href = '#';
        link.title = 'Create a new polygon';
        link.innerHTML = PolygonButtonTextIdle;
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            map.editTools.startPolygon();
          });
        container.style.display = 'block';
        map.editTools.on('editable:enabled', function(e) {
          container.style.display = 'none';
        });
        map.editTools.on('editable:disable', function(e) {
          container.style.display = 'block';
        });
        return container;
      }
    });
    map.addControl(new L.NewPolygonControl());

    //This button is shown while the user is drawing or editing a polygon
    L.AddPolygonShapeControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);

        link.href = '#';
        link.title = 'Create a new polygon';
        link.innerHTML = PolygonButtonTextEditing;
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            if (!map.editTools.currentPolygon) return;
            map.editTools.currentPolygon.editor.newShape();
          });
        container.style.display = 'none';
        map.editTools.on('editable:enabled', function(e) {
          container.style.display = 'block';
        });
        map.editTools.on('editable:disable', function(e) {
          container.style.display = 'none';
        });

        return container;
      }
    });
    map.addControl(new L.AddPolygonShapeControl());

    //This button is shown while the user is editing a polygon and can delete it
    L.AddPolygonShapeControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);

        link.href = '#';
        link.title = 'Delete the current Polygon';
        link.innerHTML = "Delete";
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            //Return the id of the currentPolygon
            console.log(map.editTools.currentPolygon)
            var idOfPoly = AllUserAreas.findIndex(function(x) { return x === map.editTools.currentPolygon; })
            console.log("foundPolyid: " + idOfPoly);
            //Delete existing polygon
            //create button to delete
            AreaService.deleteArea(idOfPoly)
            //todo: redraw all UserAreas
          });
        container.style.display = 'none';
        map.editTools.on('editable:enabled', function(e) {
          container.style.display = 'block';
        });
        map.editTools.on('editable:disable', function(e) {
          container.style.display = 'none';
        });

        return container;
      }
    });
    map.addControl(new L.AddPolygonShapeControl());

    //This button is shown while the user is editing a polygon and can update it
    L.AddPolygonShapeControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);

        link.href = '#';
        link.title = 'Update the current Polygon';
        link.innerHTML = "Update";
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            //Return the id of the currentPolygon
            console.log(map.editTools.currentPolygon)
            var idOfPoly = AllUserAreas.findIndex(function(x) { return x === map.editTools.currentPolygon; })
            console.log("foundPolyid: " + idOfPoly);
            //Delete existing polygon
            //create button to delete
            //todo: generate current polygon
            var updatedPolygon = []
            var layer = map.editTools.currentPolygon;
            console.log(map.editTools.currentPolygon)
            var point = layer.getLatLngs();

            for (var i = 0; i < point[0].length; i++) {
              updatedPolygon.push([
                point[0][i].lat,
                point[0][i].lng
              ]);
            }
            //Closes the shape by adding the first point at the end
            updatedPolygon.push([
              point[0][0].lat,
              point[0][0].lng
            ]);
            AreaService.updateArea(updatedPolygon, idOfPoly)
            //todo: redraw all UserAreas
          });
        container.style.display = 'none';
        map.editTools.on('editable:enabled', function(e) {
          container.style.display = 'block';
        });
        map.editTools.on('editable:disable', function(e) {
          container.style.display = 'none';
        });

        return container;
      }
    });
    map.addControl(new L.AddPolygonShapeControl());

    // make closure of "this"
    var self = this;

    // Creates and adds a button to toggle visibility of the VegetationsLayer
    L.GeoJsonControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);

        link.href = '#';
        link.title = 'Toggle Vegetation Layer';
        link.innerHTML = ToggleVegetationButtonLabel;
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            if (self.$store.state.toggleVegetation) {
              myGeoJsonLayer.clearLayers();
              labelGroup.clearLayers();
              self.$store.dispatch('toggleVegetation', null)
            } else {
              myGeoJsonLayer.addData(self.vegetation);
              self.$store.dispatch('toggleVegetation', null)
            }
          });
        container.style.display = 'block';
        return container;
      }
    });
    map.addControl(new L.GeoJsonControl());

    // Creates a button to toggle visibility of UserAreas
    L.UserAreasControl = L.Control.extend({
      options: {
        position: 'topleft'
      },
      onAdd: function(map) {
        var container = L.DomUtil.create('div', 'leaflet-control leaflet-bar'),
          link = L.DomUtil.create('a', '', container);

        link.href = '#';
        link.title = 'Toggle UserAreas Layer';
        link.innerHTML = ToggleUserAreasLabel;
        L.DomEvent.on(link, 'click', L.DomEvent.stop)
          .on(link, 'click', function() {
            if (self.$store.state.toggleUserAreas) {
              UserAreaGroup.clearLayers();
              self.$store.dispatch('toggleUserAreas', null)
            } else {
              DrawAllUserAreas()
              self.$store.dispatch('toggleUserAreas', null)
            }
          });
        container.style.display = 'block';
        return container;
      }
    });
    map.addControl(new L.UserAreasControl());

    //Whenever a new Polygon gets added to the map, it makes the Polygon editable
    map.on('layeradd', function(e) {
      if (e.layer instanceof L.Polygon) {
        e.layer.on('click', L.DomEvent.stop).on('click', e.layer.toggleEdit);
      }
    });

    //Whenever a Polygon gets removed from the map, disable editing
    map.on('layerremove', function(e) {
      if (e.layer instanceof L.Polygon) {
        e.layer.off('click', L.DomEvent.stop).off('click', e.layer.toggleEdit);
      }
    });

    //When attempting to draw a new Polygon, disable editing on all other active polygons
    map.editTools.on('editable:enable', function(e) {
      if (this.currentPolygon) {
        this.currentPolygon.disableEdit();
      }
      this.currentPolygon = e.layer;
      this.fire('editable:enabled');
    });

    //When the user stops drawing an active polygon, discard it
    map.editTools.on('editable:disable', function(e) {
      delete this.currentPolygon;
    });


    //This function finishes the drawing operation when the user closes the polygon shape
    map.editTools.on('editable:drawing:commit', function(e) {
      console.log("stoppedediting");
      self.saveDialog = true;
      var layer = e.layer;
      var point = layer.getLatLngs();

      for (var i = 0; i < point[0].length; i++) {
        myGeoJsonPoly.push([
          point[0][i].lat,
          point[0][i].lng
        ]);
      }
      //Closes the shape by adding the first point at the end
      myGeoJsonPoly.push([
        point[0][0].lat,
        point[0][0].lng
      ]);
    })

    //Draws the VegetationLayer
    var labelGroup = L.layerGroup();
    var myGeoJsonLayer = L.geoJSON(undefined, {
      style: function(feature){
        //This switch determines the color of the polygons for the Vegetationlayer
        //TODO; include special characters
        switch (feature.properties.EK72) {
          case '1':
            return { color: "#f2142b" };
          case '2':
            return { color: "#f20a50" };
          case '6':
            return { color: "#de3629" };
          case '7a':
            return { color: "#a45930" };
          case '7as':
            return { color: "#008e83" };
          case '7b':
            return { color: "#cb006c" };
          case '7e':
            return { color: "#c83025" };
          case '7f':
            return { color: "#6c6832" };
          case '7g':
            return { color: "#00a772" };
          case '7stern':
            return { color: "#cb006c" };
          case '8a':
            return { color: "#8c2e22" };
          case '8as':
            return { color: "#008e84" };
          case '8d':
            return { color: "#c11524" };
          case '8e':
            return { color: "#744531" };
          case '8f':
            return { color: "#644633" };
          case '8g':
            return { color: "#00a773" };
          case '8stern':
            return { color: "#c9057d" };
          case '9':
            return { color: "#9ebd4b" };
          case '10':
            return { color: "#bdc156" };
          case '10w':
            return { color: "#ece650" };
          case '11':
            return { color: "#008c4e" };

          default:
          return { color: "005800" };
        }

      },
      "weight": 0.8,
      "opacity": 0.75,
      "editable": false,

      //Draws labels for the Polygons of the Vegetationlayer
      onEachFeature: function(feature, layer) {
        var label = L.marker(layer.getBounds().getCenter(), {
          icon: L.divIcon({
            className: 'propertyLabel',
            html: feature.properties.EK72,
            iconSize: [20, 20],
            direction: 'auto'
          })
        }).addTo(labelGroup);
      }

    }).addTo(map);
    labelGroup.addTo(map);

    if (self.$store.state.toggleVegetation) {
      myGeoJsonLayer.addData(self.vegetation);
    }

    //Draws all UserAreas now
    DrawAllUserAreas();

    //This function retrieves and draws all Userareas and their labels
    async function DrawAllUserAreas(){
      self.MyAreas = (await AreaService.getAreas()).data
      var val;
      for (val of self.MyAreas) {
        var corner;
        var polygonToAdd = [];
        for (corner of val.polygon.coordinates[0][0]) {
          polygonToAdd.push(corner);
        }
        //ID test
        console.log("This UserAreas id: " + val.id)
        var poly = L.polygon([
          [
            polygonToAdd
          ]
        ],

        ).addTo(UserAreaGroup);

        //Add polygon to arraylist
        AllUserAreas[val.id] = poly;
        var idOfPoly = AllUserAreas.findIndex(function(x) { return x === poly; })
        //console.log("foundPolyid: " + idOfPoly);

        //Draws all labels for the Userareas
        if (val.public == true) {
          var label = L.marker(poly.getBounds().getCenter(), {
            icon: L.divIcon({
              className: 'AreaLabelPublic',
              html: val.label,
              iconSize: [100, 0],
              direction: 'auto',
            })
          }).addTo(UserAreaGroup);
        } else {
          var label = L.marker(poly.getBounds().getCenter(), {
            icon: L.divIcon({
              className: 'AreaLabelPrivate',
              html: val.label,
              iconSize: [100, 0],
              direction: 'auto'
            })
          }).addTo(UserAreaGroup);
        }
        UserAreaGroup.addTo(map);
      }
    };

    //MAP LEGEND
    var legend = L.control({ position: 'topright' });

    legend.onAdd = function(map) {

      var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000],
        labels = [];

      return div;
    };
    legend.addTo(map);
  }

}

</script>
<style type='text/css'>
body {
  margin: 0;
  padding: 0;
}

#map {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  width: 100%;
}

.leaflet-sidebar>.leaflet-control {
  overflow-y: hidden;
}

.propertyLabel {
  color: white;
  text-shadow: 2px 2px 2px black;
  opacity: 1;
}

.cssPolygon{
  color:green;
}
.AreaLabelPublic {
  color: green;
  text-shadow: 2px 2px 2px black;
  opacity: 1;
}

.AreaLabelPrivate {
  color: yellow;
  text-shadow: 2px 2px 2px black;
  opacity: 1;
}

div.overlay--active {
  z-index: 1000 !important
}

div.dialog__content__active {
  z-index: 1000 !important
}

</style>
<!-- <style lang="scss">
@import './assets/leaflet.css';
</style> -->
