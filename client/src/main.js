// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import vuetify from 'vuetify'
import { sync } from 'vuex-router-sync'
import 'vuetify/dist/vuetify.min.css'
import store from '@/store/store'

import Vue2Leaflet from 'vue2-leaflet';

Vue.config.productionTip = false

Vue.use(vuetify)

sync(store, router)

require('./assets/css/leaflet.js')
require('./assets/css/leaflet.css')
require('./assets/css/Leaflet.Editable.js')

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
