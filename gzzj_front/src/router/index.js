import Vue from 'vue'
import Router from 'vue-router'
import gzzjindex from '@/views/gzzj/'
import gzzjlist from '@/views/gzzj/table/'
import gzzjcheck from '@/views/gzzj/check/'
import login from '@/views/login/'

Vue.use(Router)

export default new Router({
  
  mode: 'history',
  routes: [
    {
      path: '/login',
      name: 'login',
      component: login,
    },
    {
      path: '/',
      name: 'index',
      redirect: '/login'
    },
    {
      path: '/gzzj/',
      name: 'gzzjindex',
      component: gzzjindex,
      children: [
        { path: 'gzzjlist', component: gzzjlist, name: '工作总结列表' },
        { path: 'gzzjcheck', component: gzzjcheck, name: '工作总结列表' },
      ]
    },
  ]
})
