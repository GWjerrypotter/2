// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from '@/store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import locale from 'element-ui/lib/locale/lang/zh-CN' // lang i18n
import '@/permission' // permission control
Vue.config.productionTip = false
Vue.use(ElementUI, { locale })
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  mode: 'history',
  components: { App },
  template: '<App/>'
})

// router.beforeEach((to, from, next) => {
//   console.log(store.state.token)
//   // to: Route: 即将要进入的目标 路由对象
//   // from: Route: 当前导航正要离开的路由
//   // next: Function: 一定要调用该方法来 resolve 这个钩子。执行效果依赖 next 方法的调用参数。
//   const route = ['index', 'list'];
//   let isLogin = store.state.token;  // 是否登录
//   // 未登录状态；当路由到route指定页时，跳转至login
//   if (route.indexOf(to.name) >= 0) {
//     if (isLogin == null) {
//       router.push({ path: '/login', });
//     }
//   }
//   // 已登录状态；当路由到login时，跳转至home 
//   console.log(to.name)
//   localStorage.setItem('routerName', to.name)
//   if (to.name === 'login') {
//     if (isLogin != null) {
//       router.push({ path: '/gzzj', });;
//     }
//   }
//   next();
// });