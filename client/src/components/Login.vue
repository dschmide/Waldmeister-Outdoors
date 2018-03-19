<template>
  <v-layout column>
    <v-flex xs6 offset-xs3>
      <div class="white elevation-2">
      <v-toolbar flar dense class="light-green" dark>
      <v-toolbar-title>Login</v-toolbar-title>
      </v-toolbar>
      <div class="pl-4 pr-4 pt-2 pb-2">
        <v-text-field
              label="Displayname"
              v-model="displayname"
        ></v-text-field>
        <br>
        <v-text-field
              label="Password"
              type="password"
              v-model="password"
        ></v-text-field>
        <br>
        <div class="error" v-html="error" />
        <br>
        <v-btn
          dark
          class="light-green"
          @click="login"> 
          Login
        </v-btn>
      </div>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import AuthenticationSevice from '@/services/AuthenticationService'
export default {
  data () {
    return {
      email:'',
      password:'',
      error: null,
      displayname:''
    }
  },
  methods: {
    async login(){
      try{
        const Response = AuthenticationSevice.login({ 
            username: this.displayname, 
            password: this.password
          })
          .then( (response) => {
            this.$store.dispatch('setToken', response.data.token)
            this.$store.dispatch('setUser', this.displayname)
            this.$router.push({
              name: 'map'
            })
            console.log(response.data)
          })
        } catch (error) {
          console.log(response.token)
        }
        //console.log(response.data)
      }
    }
  }
</script>

<style scoped>
.error{
   color:red;
 }

</style>
