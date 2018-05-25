<template>
  <v-toolbar fixed class="light-green" dark>
    <v-toolbar-title class=mr-4>
    <span
      class="home"
      @click="navigateTo({name: 'root'})">
      Waldmeister-Outdoors
      </span>
    </v-toolbar-title>

    <v-spacer></v-spacer>
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
        <div class="text-xs-center header-chip">
          <v-chip
          flat
          dark
          v-if="$store.state.isUserLoggedIn"
          >{{ this.$store.state.user }}
          </v-chip>
        </div>
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
      localStorage.removeItem("jwt")
      this.$router.push({
        name:'login'
      })
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

.header-chip{
  margin-top: 8px;
}
</style>
