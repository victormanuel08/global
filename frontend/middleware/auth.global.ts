//import { jwtDecode } from "jwt-decode";
//import { useCookie } from 'nuxt/app'; // Esto es un middleware, este codigo se ejecuta cada vez que ud visita una nueva página. Acá se ponen las "guardias" de la app
//
//
//export default defineNuxtRouteMiddleware((to) => {
//  if (to.path === "/") {
//    return;
//  }
//
//  const accessToken = useCookie('token') // Esto es un estado global que se almacena en LocalStorage y que contiene el JWT. 
//  // Esto podría estar en una cookie pero lo podemos hacer después.
//
//  if (!accessToken.value) {
//    return navigateTo("/"); // Si no hay token, lo mandamos a la página de login.
//  }
//
//  let decodedToken: any;
//  try {
//    decodedToken = jwtDecode(accessToken.value);
//    console.log("Tenemos token")
//    if (!decodedToken || !decodedToken.exp) {
//      return navigateTo("/");
//    }
//  } catch (e) {
//    console.error(e);
//    return navigateTo("/");
//  }
//
//  const expDT = new Date(decodedToken.exp * 10000);
//  const nowDT = new Date();
//
//  if (expDT < nowDT) {
//    return navigateTo("/"); // Acá le decimos que si el token expiró, lo mande a la página de login
//  } else {
//    const CURRENT_USER_PATH = '/api/auth/users/me/'
//    const useUserStorage = useAuthUserStorage()
//    if (decodedToken.user_id !== useUserStorage.value.id) {
//      $fetch(CURRENT_USER_PATH).then((response: any) => {
//        if (response.error) {
//          console.error(response.error)
//          return navigateTo("/")
//        }
//        useUserStorage.value = response
//      })
//    }
//
//  }
//
//});
//

import { jwtDecode } from "jwt-decode";
import { useCookie } from 'nuxt/app';

export default defineNuxtRouteMiddleware((to) => {
  if (to.path === "/") {
    return;
  }

  const accessToken = useCookie('token');
  const refreshToken = useCookie('refresh_token');

  if (!accessToken.value) {
    return navigateTo("/");
  }

  let decodedToken;
  try {
    decodedToken = jwtDecode(accessToken.value);
    console.log("Tenemos token");
    if (!decodedToken || !decodedToken.exp) {
      return navigateTo("/");
    }
  } catch (e) {
    console.error(e);
    return navigateTo("/");
  }

  const expDT = new Date(decodedToken.exp * 1000); // Convertimos el tiempo de expiración a milisegundos
  const nowDT = new Date();
  const remainingTime = expDT.getTime() - nowDT.getTime();

  // Si queda menos de 60 segundos, renovamos el token
  if (remainingTime < 300000) {
    console.log("Token está por caducar, intentando renovarlo...");

    if (refreshToken.value) {
      $fetch("/api/auth/refresh", {
        method: "POST",
        body: { refreshToken: refreshToken.value },
      }).then((response) => {
        if (response.accessToken) {
          console.log("Token renovado exitosamente."); // Log cuando se renueva el token
          accessToken.value = response.accessToken;
          useCookie('token').value = response.accessToken;
        }
      });
    }
  } else {
    const CURRENT_USER_PATH = '/api/auth/users/me/';
    const useUserStorage = useAuthUserStorage();
    if (decodedToken.user_id !== useUserStorage.value.id) {
      $fetch(CURRENT_USER_PATH).then((response) => {
        if (response.error) {
          console.error(response.error);
          return navigateTo("/");
        }
        useUserStorage.value = response;
      });
    }
  }

  if (expDT < nowDT) {
    console.log("El token ha caducado, redirigiendo a login...");
    return navigateTo("/");
  }
});
