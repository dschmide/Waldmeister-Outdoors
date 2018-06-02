<template>
  <v-layout column>
    <v-flex md6 offset-md3 xs12>
      <div class="white elevation-2">
      <v-toolbar flar dense class="light-green" dark>
      <v-toolbar-title>Login</v-toolbar-title>
      </v-toolbar>
      <div class="pl-4 pr-4 pt-2 pb-2">
        <v-text-field
              label="Displayname"
              v-model="displayname"
              @keyup.enter="login" 
        ></v-text-field>
        <br>
        <v-text-field
              label="Password"
              type="password"
              v-model="password"
              @keyup.enter="login" 
        ></v-text-field>
        <br>
        <div class="error" v-if="error">
          <ul>
            <li v-if="error.data.username">Displayname: {{ error.data.username[0] }}</li>
            <li v-if="error.data.password">Password: {{ error.data.password[0] }}</li>
            <li v-if="error.data.non_field_errors">{{ error.data.non_field_errors[0] }}</li>
          </ul>
        </div>
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
          .catch((error) => {
            // Catches and displays the error messages if necessary
            this.error = error.response;
            console.log("err");
          })
    }
  }
}
</script>

<style scoped>

.error {
  color: white;
  list-style:  none;
  text-align: left;
}

</style>
