// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuex from 'vuex'
// import store from './vuex/store'
import axios from 'axios'
// import router from './router'
import VueRouter from 'vue-router'
import iView from 'iview'

import 'iview/dist/styles/iview.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'

import Layout from './components/layout.vue'
import Home from './components/Home'
import Login from './components/login.vue'
import realTimeData from './components/real-time-data.vue'
import history from './components/history-data.vue'
import alarmhistory from './components/alarm-history.vue'
import alarmnow from './components/alarm-now.vue'
import station from './components/station.vue'
import plc from './components/plc.vue'
import group from './components/group.vue'
import variable from './components/variable.vue'
import querygroup from './components/query_group.vue'
import queryvariable from './components/query_variable.vue'
import param from './components/param.vue'
import paramval from './components/param-val.vue'
import alarminfo from './components/alarm-info.vue'
// import bread from './components/breadcrumb-view.vue'
import test from './components/test.vue'
import register from './components/register.vue'

Vue.config.productionTip = true

Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(iView)
Vue.prototype.$axios = axios
/* eslint-disable no-new */
// new Vue({`
//   el: '#app',
//   router,
//   template: '<App/>',
//   components: {App}
// })

const User = {
  template: `
    <div class="user">
        <h2>User {{ $route.params.id }}</h2>
        <router-view></router-view>
    </div>
    `
}

const UserProfile = {
  template: '<div>hello</div>'
}

const routes = [
  {
    path: '/',
    component: Layout,
    children: [
      {
        path: '/station',
        component: station
      }, {
        path: '/data',
        component: realTimeData
      }, {
        path: '/history',
        component: history
      }, {
        path: '/alarm_history',
        component: alarmhistory
      }, {
        path: '/alarm_now',
        component: alarmnow
      }, {
        path: '/plc',
        component: plc
      }, {
        path: '/group',
        component: group
      }, {
        path: '/variable',
        component: variable
      }, {
        path: '/query_group',
        component: querygroup
      }, {
        path: '/query_variable',
        component: queryvariable
      }, {
        path: '/alarm_info',
        component: alarminfo
      }, {
        path: '/param',
        component: param
      }, {
        path: '/param_val',
        component: paramval
      }, {
        path: '/',
        component: Home
      }
    ]
  }, {
    path: '/login',
    component: Login
  }, {
    path: '/user/:id',
    component: User,
    children: [
      {
        path: 'profile',
        component: UserProfile
      }
    ]
  }, {
    path: '/test',
    component: test
  }, {
    path: '/register',
    component: register
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start()
  next()
})

router.afterEach((to, from, next) => {
  iView.LoadingBar.finish()
})
// new Vue({
//   router,
//   ...App
// }).$mount('#app')

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})

// new Vue({
//   router
// }).$mount('#app')
