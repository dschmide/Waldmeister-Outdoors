import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  strict: true,
  state: {
    token: null,
    user: null,
    isUserLoggedIn: false,
    toggleVegetation: true,
  },

  mutations: {
    setToken(state, token) {
      state.token = token
      if (token) {
        state.isUserLoggedIn = true
      } else {
        state.isUserLoggedIn = false
      }
    },

    setUser(state, user) {
      state.user = user
    },

    toggleVegetation(state) {
      if (state.toggleVegetation) {
        state.toggleVegetation = false
      } else {
        state.toggleVegetation = true
      }
      console.log('Vegetation Toggled ' + state.toggleVegetation);
    },

  },
  actions: {
    setToken({ commit }, token) {
      commit('setToken', token)
    },
    setUser({ commit }, user) {
      commit('setUser', user)
    },
    toggleVegetation({ commit }) {
      commit('toggleVegetation')
    }
  }
})
