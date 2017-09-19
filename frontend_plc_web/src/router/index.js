import Vue from 'vue'
import Router from 'vue-router'
import iView from 'iview'

import Layout from '../components/layout.vue'
import Login from '../components/Login/index.vue'
import Home from '../components/Home'
import realTimeData from '../components/real-time-data.vue'
import history from '../components/history-data.vue'
import alarmhistory from '../components/alarm-history.vue'
import alarmnow from '../components/alarm-now.vue'
import station from '../components/station.vue'
import plc from '../components/plc.vue'
import group from '../components/group.vue'
import variable from '../components/variable.vue'
import querygroup from '../components/query_group.vue'
import queryvariable from '../components/query_variable.vue'
import param from '../components/param.vue'
import paramval from '../components/param-val.vue'
import alarminfo from '../components/alarm-info.vue'
// import bread from '../components/breadcrumb-view.vue'
import logout from '../router/logout'
import test from '../components/test.vue'
import register from '../components/register.vue'

Vue.use(Router)

const router = new Router({
  routes: [

    {
      path: '/login',
      component: Login
    }, {
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
      path: '/logout',
      component: logout
    }, {
      path: '/test',
      component: test
    }, {
      path: '/register',
      component: register
    }
  ]
})

router.beforeEach((to, from, next) => {
  iView.LoadingBar.start()
  next()
})

router.afterEach((to, from, next) => {
  iView.LoadingBar.finish()
})

export default router
