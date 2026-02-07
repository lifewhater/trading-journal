import { createRouter, createWebHistory } from 'vue-router'
import mainChart from '@/pages/mainChart.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: mainChart}
  ],
})

export default router
