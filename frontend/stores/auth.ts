import { createGlobalState, useStorage } from '@vueuse/core'

export const useAuthState = createGlobalState(
  () => useStorage('vm-auth-token', ''), // Esto debe tener un nombre distinto en cada app si no se arma un lío
)
