import Vue from 'vue'
import Router from 'vue-router'
import iView from 'iview'

import Layout from '@/app/Layout'
import Login from '@/app/Login'
import Home from '../components/Home'
import realTimeData from '@/app/realTime'
import history from '@/app/historyData'
import alarmhistory from '@/app/alarmHistory'
import alarmnow from '@/app/alarmNow'
import station from '@/app/Station'
import plc from '@/app/PLC'
import group from '@/app/Group'
import variable from '@/app/Variable'
import querygroup from '@/app/queryGroup'
import queryvariable from '@/app/queryVariable'
import param from '@/app/Param'
import paramval from '@/app/paramValue'
import alarminfo from '@/app/alarmInfo'
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
