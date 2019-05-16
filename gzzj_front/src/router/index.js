import Vue from 'vue'
import Router from 'vue-router'
import login from '@/views/login/index'
import { userInfo } from 'os';

Vue.use(Router)


export const constantRouterMap = [
  { path: '/login', name: 'login', component: () => import('@/views/login/index') },
  { path: '/404', component: () => import('@/views/404'), hidden: true },

  {
    path: '/',
    component: login,
    redirect: '/login',
    meta: { title: '首页' },
    // children: [{
    //   meta: { title: '延期支付系统', icon: 'link' },
    //   path: 'home',
    //   component: () => import('@/views/dashboard/index')
    // }]
  }
]

export default new Router({
  mode: 'history',
  routes: constantRouterMap
})


export const asyncRouterMap = [
    {
      path: '/gzzjxt/',
      component: () => import('@/views/gzzj/index'),
      redirect: '/gzzjxt/index',
      meta: { roles: [ 'deptmanager', 'normaluser' ], title: '主页' },
      children: [
        { path: 'index', component: () => import('@/views/gzzj/base'),  meta:{ title: '首页' } },
        { path: 'gzzjlist', component: () => import('@/views/gzzj/gzzjtable/index'),  meta:{ title: '列表' } },
        { path: 'user', component: () => import('@/views/gzzj/user/index'),  meta: { roles: ['deptmanager'], title: '用户管理'} },
      ]
    },
    // {
    //   path : '/user/',
    //   component: () => import('@/views/gzzj/user/index'),
    //   meta: { roles: ['deptmanager'], title: '用户管理'},
    // },
    { path: '*', redirect: '/404', hidden: true }
  ]
