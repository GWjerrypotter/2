import Vue from 'vue'
import Router from 'vue-router'
import gzzjindex from '@/views/gzzj/'
import gzzjlist from '@/views/gzzj/table/'
import gzzjcheck from '@/views/gzzj/check/'

Vue.use(Router)

export default new Router({
  
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'index',
      redirect: '/gzzj/'
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
