import Vue from 'vue'
import Router from 'vue-router'
import Register from '@/components/Register'
import Login from '@/components/Login'
import Waldmeistermap from '@/components/Waldmeistermap'
import About from '@/components/About'


Vue.use(Router)

export default new Router({
  routes: [{
      path: '/',
      name: 'root',
      component: Waldmeistermap
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/map',
      name: 'map',
      component: Waldmeistermap
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
})
