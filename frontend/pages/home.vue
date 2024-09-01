<template>
    <!--
    <div class="flex flex-cols-1 justify-center m-4">
        <div class="carousel-container m-4">
            <UCarousel ref="carouselRef" v-slot="{ item }" :items="items" :ui="{ item: 'basis-full' }"
                class="rounded-lg overflow-hidden" indicators>
                <img :src="item" class="w-full" draggable="false" />
            </UCarousel>
        </div>
    </div>
-->
</template>

<script setup lang="ts">

//  import { ref, onMounted } from 'vue';
//  
//  const items = [
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/09/REHABILITACION-INTEGRAL.2png.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/11/ORTOPEDIA-2.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/11/HOME-CARE-2.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/11/CLINICA-DEL-DOLOR-2.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/11/MEDICINA-ESPECIALIZADA-3.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2020/10/SOBRE-NOSOTROS-2.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2021/02/PERSONAL-DE-ATENCION-CAMARA.png',
//      'https://ipsglobalsafe.com/wp-content/uploads/2021/02/cama-hiperbarica-2.png',
//  
//  ];
//  
//  const carouselRef = ref();
//  
//  onMounted(() => {
//      setInterval(() => {
//          if (!carouselRef.value) return;
//  
//          if (carouselRef.value.page === carouselRef.value.pages) {
//              return carouselRef.value.select(0);
//          }
//  
//          carouselRef.value.next();
//      }, 3000);
//  });
  </script>
  
  <style scoped>
  /*
  .carousel-container {
      width: 75%;
      display: flex;
      align-items: center;
      /* Esto centrará verticalmente las imágenes
      justify-content: center;


  }
  
  
  
  .carousel-container img {
      width: 100%;
      height: 400px;
      align-items: center;
      justify-content: center;
  }

  */
</style>