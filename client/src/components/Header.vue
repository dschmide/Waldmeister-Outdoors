<template>
  <v-toolbar fixed class="light-green" dark>
    <v-toolbar-title class=mr-4>
    <span
      class="home"
      @click="navigateTo({name: 'root'})">
      Waldmeister-Outdoors
      </span>
    </v-toolbar-title>

    <!-- TODO Goto Map
    <v-toolbar-items>
      <v-btn flat dark>
        Map
      </v-btn>
    </v-toolbar-items> -->

    <v-spacer></v-spacer>

    <!-- Routing with router-link
    <v-toolbar-items>
      <router-link to="register">
        <v-btn flat dark>
          Sign Up
        </v-btn>
      </router-link> -->

      <!-- routing with method -->
      <v-toolbar-items>
        <v-btn 
          flat 
          dark
          @click="navigateTo({name: 'about'})">
          About
        </v-btn>

      <v-btn 
          v-if="!$store.state.isUserLoggedIn"
          flat 
          dark
          @click="navigateTo({name: 'login'})">
          Login
        </v-btn>

        <v-btn 

          v-if="!$store.state.isUserLoggedIn"
          flat 
          dark
          @click="navigateTo({name: 'register'})">
          Sign Up
        </v-btn>
        <v-btn 

          v-if="$store.state.isUserLoggedIn"
          flat 
          dark
          @click="logout">
          LogOut
        </v-btn>
    </v-toolbar-items>
  </v-toolbar>
</template>

<script>
export default {
  methods: {
    navigateTo (route) {
      this.$router.push(route)
    },
    logout() {
      this.$store.dispatch('setToken', null)
      this.$store.dispatch('setUser', null)
      this.$router.push({
        name:'root'
      })
    },
    toggleGeoJson() {
      this.$store.dispatch('toggleVegetation', null)
    },
    
  }
}
</script>

<style scoped>
.home{
  cursor: pointer;
}
.home:hover {
  color: #EEEEEE;
}
</style>
