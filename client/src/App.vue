<template>
  <div id="app">
    <v-app>
      <page-header />
        <main>
          <v-container fluid>
            <router-view>
            </router-view>
          </v-container>
        </main>
    </v-app>
    <!-- <img src="./assets/logo.png"> -->
  </div>
</template>

<script>
import PageHeader from '@/components/Header.vue'
import Waldmeistermap from '@/components/Waldmeistermap.vue'

export default {
  name: 'app',
  components: {
    PageHeader, Waldmeistermap
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

@import './assets/leaflet.css'
</style>
