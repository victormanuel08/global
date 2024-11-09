import { jwtDecode } from "jwt-decode";
// Esto es un middleware, este codigo se ejecuta cada vez que ud visita una nueva página. Acá se ponen las "guardias" de la app


export default defineNuxtRouteMiddleware((to) => {
  if (to.path === "/") {
    return;
  }

  const accessToken = useCookie('token') // Esto es un estado global que se almacena en LocalStorage y que contiene el JWT. 
  // Esto podría estar en una cookie pero lo podemos hacer después.

  if (!accessToken.value) {
    return navigateTo("/"); // Si no hay token, lo mandamos a la página de login.
  }

  let decodedToken: any;
  try {
    decodedToken = jwtDecode(accessToken.value);
    console.log("Tenemos token")
    if (!decodedToken || !decodedToken.exp) {
      return navigateTo("/");
    }
  } catch (e) {
    console.error(e);
    return navigateTo("/");
  }

  const expDT = new Date(decodedToken.exp * 10000);
  const nowDT = new Date();

  if (expDT < nowDT) {
    return navigateTo("/"); // Acá le decimos que si el token expiró, lo mande a la página de login
  } else {
    const CURRENT_USER_PATH = '/api/auth/users/me/'
    const useUserStorage = useAuthUserStorage()
    if (decodedToken.user_id !== useUserStorage.value.id) {
      $fetch(CURRENT_USER_PATH).then((response: any) => {
        if (response.error) {
          console.error(response.error)
          return navigateTo("/")
        }
        useUserStorage.value = response
      })
    }

  }

});
