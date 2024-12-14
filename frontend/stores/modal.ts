import { createGlobalState } from '@vueuse/core';

export const useModal = createGlobalState(() => {
  const showModal = ref(false); // Estado para mostrar/ocultar el modal

  const setShowModal = (value: boolean) => {
    showModal.value = value;
  };

  return { showModal, setShowModal };
});
