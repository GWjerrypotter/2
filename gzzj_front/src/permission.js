import router from './router'
import store from './store'
import { Message } from 'element-ui'
import { getToken } from '@/utils/auth' // 验权

const whiteList = ['/login'] // 不重定向白名单
router.beforeEach((to, from, next) => {
  if (getToken()) {
      if (to.path === '/login') {
        next({ path: '/' })
      } else {
      if (store.getters.roles === undefined) {
        store.dispatch('GetInfo').then(res => {
          const roles = []
          res.is_manager === true ? roles.push('deptmanager') : roles.push('normaluser')
          store.dispatch('GenerateRoutes', { roles }).then(() => {
            router.addRoutes(store.getters.addRouters)
            next({ ...to, replace: true})
          })
        }).catch((err) => {
          store.dispatch('FedLogOut').then(() => {
            Message.error(err || 'Verification failed, please login again')
            next({ path: '/' })
          })
        })
      } else {
        next()
        }
      }
  } else {
      if (whiteList.indexOf(to.path) !== -1) {
        next();
      } else {
        next('/login')
        // next(`/login?redirect=${to.path}`) // 否则全部重定向到登录页
      
      }
    }
  
})
