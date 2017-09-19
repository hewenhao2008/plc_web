// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
// import Vuex from 'vuex'
// import store from './vuex/store'
// import axios from 'axios'
import '@/utils/init'
import router from './router'
import store from '@/store'
import iView from 'iview'
import '@/styles/global/index.scss'
// import '@/styles/iview/index.less'
import 'iview/dist/styles/iview.css'
import 'bootstrap/dist/css/bootstrap.css'
import 'font-awesome/css/font-awesome.css'

Vue.config.productionTip = true

// Vue.use(Vuex)
Vue.use(iView)
// Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  template: '<App/>',
  components: {App}
})

