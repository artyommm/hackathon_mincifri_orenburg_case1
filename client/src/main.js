import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vueExcelExport from "vue-excel-export";

createApp(App)
    .use(vueExcelExport)
    .use(store)
    .use(router)
    .mount('#app')
