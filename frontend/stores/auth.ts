import { createGlobalState, useStorage } from '@vueuse/core';

export const useAuthTokensStorage = createGlobalState(
  () => {
    const accessToken = ref<string | null>('');
    const refreshToken = ref<string | null>('');
    return { accessToken, refreshToken };
  }
);

watch(() => useAuthTokensStorage().accessToken.value, (value) => {

  const tokenCookie = useCookie('token');
  tokenCookie.value = value;
 
});

watch(() => useAuthTokensStorage().refreshToken.value, (value) => {
 
  const refreshTokenCookie = useCookie('refresh_token');
  refreshTokenCookie.value = value;
 
});

export const useAuthUserStorage = createGlobalState(
  () => useStorage('vm-auth-user', {} as any)
);

export const refreshToken = async () => {
  const { accessToken, refreshToken } = useAuthTokensStorage();
  
  try {
    // Realiza una solicitud para refrescar el token usando el refreshToken
    const response = await $fetch('/api/auth/token/refresh/', {
      method: 'POST',
      body: { refresh_token: refreshToken.value },
    });

    // Almacena el nuevo token de acceso
    accessToken.value = response.access_token;
   
  } catch (e) {
    console.error('Error al refrescar el token:', e);
    useRouter().push('/'); // Si algo falla, redirige al login
  }
};
