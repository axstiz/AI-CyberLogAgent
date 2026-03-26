<template>
  <div id="app" class="min-h-screen bg-[#202020]">

    <div v-if="appStore.isAuthenticated" class="flex relative">
      <Sidebar />
      <main 
        :class="[
          'flex-1 transition-all duration-300',
          appStore.sidebarCollapsed ? 'ml-20' : 'ml-20 sm:ml-64'
        ]"
      >
        <RouterView />
      </main>
    </div>
    <div v-else>
      <RouterView />
    </div>

    <!-- Уведомления -->
    <NotificationStack />
  </div>
</template>

<script setup>
import { useAppStore } from '@/stores/app'
import { onMounted } from 'vue'
import Sidebar from '@/components/Sidebar.vue'
import NotificationStack from '@/components/NotificationStack.vue'
import websocketService from '@/services/websocket'

const appStore = useAppStore()

onMounted(() => {
  // Попытка восстановления сессии
  if (appStore.token) {
    appStore.isAuthenticated = true
  }

  // Подключение к WebSocket для получения уведомлений
  if (appStore.isAuthenticated) {
    // Пытаемся подключиться, но не показываем ошибки
    websocketService.connect().catch((error) => {
      console.warn('WebSocket connection failed:', error)
      // Не показываем уведомление, т.к. WebSocket не критичен для работы
    })

    websocketService.on('message', (data) => {
      if (data.type === 'incident') {
        appStore.addIncident(data.incident)
      }
    })

    // Убираем обработчик ошибок, чтобы не спамить уведомлениями
  }
})
</script>

<style scoped>
#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
