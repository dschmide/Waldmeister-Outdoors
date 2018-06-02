<template>
  <v-layout column>
    <v-flex md6 offset-md3 xs12>
      <div class="white elevation-2">
        <v-toolbar flar dense class="light-green" dark>
        <v-toolbar-title>About</v-toolbar-title>
        </v-toolbar>
        <div class="pl-4 pr-4 pt-2 pb-2">
        <v-card-media src="/static/logo.png" height='400'>
        </v-card-media>
          <div>
            <h3 class="headline mb-0">Waldmeister Outdoors</h3>
            <div>"Waldmeister Outdoors" ist ein Instrument zur Arbeit im Feld.
            <br>
            Waldmeister-Outdoors wurde als Projektarbeit im Herbssemester 2017/18 an der HSR von Daniel Schmider mit Prof. Stefan Keller als Advisor erstellt.
            <br>
            Geodaten vom Kanton Zürich werden unter Einhaltung der Nutzungsbestimmungen auf der Waldmeister Map angezeigt.
            <br>
            Die offizielle Waldmeister App dient als Hilfswerk zur Identifikation und als Nachschlagewerk für Waldstandorttypen in der Schweiz. Sie ist erhätlich unter:
            <br>
            <a href="https://itunes.apple.com/bn/app/waldmeister/id825753160?mt=8">App Store iOS App</a>
            <br>
            <a href="https://play.google.com/store/apps/details?id=bgu_schmider.waldmeister">Google Playstore für Android App</a>
            <br>
            <a href="/api/static/legende.pdf" target='_blank'>Legende als PDF anzeigen</a>
            </div>
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

.card__media__background {
  background-size: auto 100%;
}

.error{
   color:red;
 }

</style>
