import { useAuthTokensStorage } from '~/stores/auth';
import { useModal } from '~/stores/modal';  // Asegúrate de tener una store de modal para controlar su visibilidad

export default defineNuxtRouteMiddleware(async (to, from) => {
  const { accessToken } = useAuthTokensStorage();  // Accede a tu token almacenado
  const { showModal, setShowModal } = useModal();  // Utiliza la store para controlar el estado del modal

  if (!accessToken.value) {
    // Si no hay token, redirige al login
    return navigateTo('/');
  }

  // Decodificar el token para obtener la fecha de expiración
  let decodedToken;
  try {
    decodedToken = jwtDecode(accessToken.value);
    const expDT = new Date(decodedToken.exp * 1000);
    const nowDT = new Date();

    const remainingTime = expDT.getTime() - nowDT.getTime();  // Tiempo restante en milisegundos

    // Si el token va a expirar en menos de 2 minutos, mostrar el modal
    if (remainingTime <= 5 * 60 * 1000 && !showModal.value) {
      setShowModal(true);  // Muestra el modal
    }

    // Si el token ha expirado, redirige al login
    if (remainingTime <= 0) {
      return navigateTo('/');
    }

    // Si queda tiempo, puedes extender el token (si es necesario) o simplemente seguir
    if (remainingTime <= 5 * 60 * 1000) {
      // Si quieres extender el token por 10 minutos más, realiza una petición para refrescar el token
      // Aquí agregas el código que actualiza el token.

      await refreshToken();  // Asegúrate de que este método existe en tu store o lógica de token
    }

  } catch (e) {
    console.error('Error al decodificar el token:', e);
    return navigateTo('/');
  }
});
