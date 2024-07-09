<template>
    <div class="modal-overlay">
      <div class="modal">

      </div>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      closeModal() {
        this.$emit('close-modal');
      }
    }
  }
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    background-color: white;
  }
  
  .modal {
    margin-top: 0;
    text-align: center;
    background-color: white;
    height: 80vh;
    width: 500px;
    padding: 60px 0;
    border-radius: 20px;
    overflow-y: auto;
    scrollbar-width: thin;
    /* Ajusta el ancho del scrollbar */
    scrollbar-color: #3532dc white;
    /* Color del scrollbar (azul y blanco) */
  }
  
  .modal::-webkit-scrollbar {
    width: 12px;
    /* Ancho del scrollbar (ajustado) */
    border-radius: 10px;
    /* Borde redondeado */
  }
  
  .modal::-webkit-scrollbar-thumb {
    background-color: #3532dc;
    /* Color del thumb (barra deslizadora) */
    border-radius: 10px;
    /* Borde redondeado */
  }
  
  .modal::-webkit-scrollbar-thumb:hover {
    background-color: #1f1d8e;
    /* Color del thumb al pasar el mouse */
    border-radius: 10px;
    /* Borde redondeado */
  }
  
  .close {
    margin: 10% 0 0 16px;
    cursor: pointer;
  }
  
  .close-img {
    width: 25px;
  }
  
  .check {
    width: 150px;
  }
  
  h6 {
    font-weight: 500;
    font-size: 28px;
    margin: 20px 0;
  }
  
  p {
    font-size: 16px;
    margin: 20px 0;
  }
  
  button {
    background-color: #3532dc;
    width: 150px;
    height: 40px;
    color: white;
    font-size: 14px;
    border-radius: 16px;
    margin-top: 0;
  }
  
  .modal-text {
    text-align: justify;
    font-size: 16px;
    margin: 20px 0;
  }
  </style>