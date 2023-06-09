import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
// 导入全局样式表
import './assets/css/global.css'
import TreeTable from 'vue-table-with-tree-grid'

import axios from 'axios'
// 配置请求
// 请求URL
axios.defaults.baseURL = 'http://127.0.0.1:8005/'
axios.interceptors.request.use(config => {
  config.headers.Authorization = window.sessionStorage.getItem('login_token')
  // 最后必须返回 config
  return config
})
Vue.prototype.$http = axios

Vue.config.productionTip = false

Vue.component('tree-table', TreeTable)

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
