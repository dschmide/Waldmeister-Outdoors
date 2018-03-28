<template>
  <v-layout column>
    <v-flex xs6 offset-xs3>
      <div class="white elevation-2">
        <v-toolbar flar dense class="light-green" dark>
        <v-toolbar-title>About</v-toolbar-title>
        </v-toolbar>
        <div class="pl-4 pr-4 pt-2 pb-2">
        <v-card-media src="/static/logo.png" height="400px">
        </v-card-media>
          <div>
            <h3 class="headline mb-0">Waldmeister Outdoors</h3>
            <div>"Waldmeister Outdoors" ist ein Instrument zur Arbeit im Feld. Die offizielle Waldmeister App dient als Hilfswerk zur identifikation und als Nachschlagewerk für die Waldstandorttypen.</div>
          </div>
        </div>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data () {
    return {
    }
  },
  methods: {
    
  }
}
</script>

<style scoped>
.error{
   color:red;
 }

</style>
