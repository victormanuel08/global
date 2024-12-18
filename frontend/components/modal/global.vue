<template>
    <div v-if="showModal" class="modal">
      <div class="modal-content">
        <h3>Tu sesión está a punto de expirar</h3>
        <p>Tu sesión expirará en 2 minutos. ¿Quieres extenderla?</p>
        <div class="modal-actions">
          <button @click="extendSession">Extender</button>
          <button @click="closeModal">Cerrar</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { useModal } from '~/stores/modal';
  import { useAuthTokensStorage } from '~/stores/auth';
  import { useRouter } from 'vue-router';
  
  const { showModal, setShowModal } = useModal();
  const { accessToken } = useAuthTokensStorage();
  const router = useRouter();
  
  // Método para extender la sesión
  const extendSession = async () => {
    try {
      // Realiza una solicitud al backend para extender el token
      //console.log('Extendiendo sesión...');
      await refreshToken();
      // Cierra el modal después de extender la sesión
      setShowModal(false);
    } catch (e) {
      console.error('Error al extender la sesión:', e);
    }
  };
  
  // Método para cerrar el modal sin extender la sesión
  const closeModal = () => {
    setShowModal(false);
    router.push('/'); // Redirige al login si el usuario decide no extender la sesión
  };
  </script>
  
  <style scoped>
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    text-align: center;
  }
  
  .modal-actions {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
  }
  
  button {
    padding: 10px 20px;
    cursor: pointer;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 5px;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  