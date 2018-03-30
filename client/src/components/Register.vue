<template>
  <v-layout column>
    <v-flex xs6 offset-xs3>
      <div class="white elevation-2">
      <v-toolbar flar dense class="light-green" dark>
      <v-toolbar-title>Register</v-toolbar-title>
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
        <v-text-field
              label="Email"
              v-model="email"
        ></v-text-field>
        <div class="error" v-html="error" />
        <br>
        <v-btn
          dark
          class="light-green"
          @click="register"> 
          Register
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
      displayname:'',
      error: null
    }
  },
  methods: {
    async register(){
        AuthenticationSevice.register({
          email: this.email,
          password: this.password,
          username: this.displayname
        })
        .then( () => {
        // } catch (error) {
        //   this.error = error.response.data.error
        // }

          const Response = AuthenticationSevice.login({ 
            username: this.displayname, 
            password: this.password
          })
          .then( (response) => {
            this.$store.dispatch('setToken', response.data.token)
            this.$store.dispatch('setUser', this.displayname)
            this.$router.push({
              name: 'login' 
            })
            console.log(response.data)
          })
        })
      }
    }
  }
</script>

<style scoped>
.error{
   color:red;
 }

</style>
