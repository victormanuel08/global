import { createGlobalState, useStorage } from '@vueuse/core'

export const useAuthTokensStorage = createGlobalState(
  () => {
    const accessToken = ref<string | null>('')
    const refreshToken = ref<string | null>('')
    return { accessToken, refreshToken }
  })

watch(() => useAuthTokensStorage().accessToken.value, (value) => {
  console.log('accessToken changed', value)
  const tokenCookie = useCookie('token')
  tokenCookie.value = value
  console.log('tokenCookieSTORE', tokenCookie.value)
})

export const useAuthUserStorage = createGlobalState(
  () => useStorage('vm-auth-user', {
  } as any)
)