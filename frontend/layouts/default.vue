<template>
  <div class="flex gap-3 bg-gray-000 border mt-4" style="height: calc(260vh - 50px) !important" @click="closeAllMenus">
    <!-- Barra lateral -->
    <div class="sidebar w-52 bg-gray-100 hidden md:block mt-4">
      <div class="py-5 text-center">
        <img src="@/assets/img/GLOBALIPS.png" alt="GLOBAL" class="object-contain w-full md:w-1/1 lg:w-1/1">
      </div>
      <div v-for="(item, index) in menuItems" :key="item.path" class="m-2">
        <UButton class="rounded-full" @click.stop="toggleChilds(index, true)" style="width: 190px; white-space: normal;"
          :to="item.path">
          <Icon :name="item.icon" style="color: white; font-size: 1.5em;" />
          {{ item.label }}
        </UButton>
        <div class="m-2" style="text-align: right;">
          <UButton style="width: 150px; white-space: normal; text-align: right;" v-for="subItem in item?.childs"
            :key="subItem.path" class="rounded-full" variant="soft" v-if="showChilds[index]" :to="subItem.path">
            <Icon :name="subItem.icon" style="color: blue; font-size: 1.5em;" />
            {{ subItem.label }}
          </UButton>
        </div>
      </div>
    </div>

    <!-- Contenido principal -->
    <div class="flex-grow bg-white rounded-lg">
      <!-- Menú a la derecha (visible en todas las pantallas) -->
      <div class="flex justify-center md:justify-end p-2 bg-gray-100 rounded-full shadow m-4">
        <div class="relative inline-block text-left bg-gray-100 flex items-center space-x-2">

          <!-- Imagen del usuario -->
          <span class="relative">
            <img src="@/assets/img/GLOBALIPS.png" alt="Usuario"
              class="rounded-full w-12 h-12 cursor-pointer border-2 border-blue-500 hover:shadow-md transition-transform transform hover:scale-105"
              @click.stop="toggleMenu" />

            <!-- Menú desplegable -->
            <transition name="fade">
              <div v-if="menuAbierto" 
                class="absolute left-1/2 transform -translate-x-1/2 md:left-auto md:transform-none md:right-0 mt-6 bg-gray-100 shadow-lg rounded-lg w-52 py-2 ring-1 ring-gray-200 z-50"
                role="menu" aria-label="User menu" @click.stop>
                <div v-for="(item, index) in menuItems" :key="item.path" class="m-2 block md:hidden">
                  <UButton class="rounded-full" @click.stop="toggleChilds(index, false)"
                    style="width: 190px; white-space: normal;" :to="item.path">
                    <Icon :name="item.icon" style="color: white; font-size: 1.5em;" />
                    {{ item.label }}
                  </UButton>
                  <div style="text-align: right;">
                    <UButton style="width: 190px; white-space: normal; text-align: right;"
                      v-for="subItem in item?.childs" :key="subItem.path" class="rounded-full" variant="soft"
                      v-if="showChilds[index]" :to="subItem.path">
                      <Icon :name="subItem.icon" style="color: blue; font-size: 1.5em;" />
                      {{ subItem.label }}
                    </UButton>
                  </div>
                </div>
                <UButton key="profile" to="profile" class="rounded-full no-style-button white-space: normal m-2"
                  style="width: 190px">

                  <Icon name="uil:user-circle" style="color: white; font-size: 1.5em;" />
                  Perfil {{ user?.username }}
                </UButton>
                <a class="block px-4 py-2 text-gray-700 hover:bg-red-100 hover:text-red-700 transition-colors justify-center"
                  @click="doLogout" role="menuitem">
                  <Icon name="uil:signout" style="color: black; font-size: 1em;" />
                  <span class="ml-2">Cerrar sesión</span>
                </a>

              </div>
            </transition>
          </span>
        </div>
      </div>

      <slot></slot>
    </div>
  </div>
  <ModalGlobal v-if="showModal" />
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import { useCookie, useRouter } from 'nuxt/app';
import { jwtDecode } from 'jwt-decode';
import { _hidden } from '#tailwind-config/theme/aria';


const showModal = ref(false);

const authUserStorage = useAuthUserStorage();
const authTokensStorage = useAuthTokensStorage();
const user = computed(() => authUserStorage.value);
const tokenCookie = useCookie('token');
const menuAbierto = ref(false);

const doLogout = () => {
  tokenCookie.value = null;
  authUserStorage.value = {};
  authTokensStorage.accessToken.value = null;
  authTokensStorage.refreshToken.value = null;
  useRouter().push('/');
};

const closeAllMenus = (event) => {
  if (!event.target.closest('.sidebar') && !event.target.closest('.relative')) {
    menuAbierto.value = false;
    for (let i = 0; i < showChilds.value.length; i++) {
      showChilds.value[i] = false;
    }
  }
};

if (!tokenCookie.value) {
  useRouter().push('/');
} else {
  let decodedToken;
  try {
    decodedToken = jwtDecode(tokenCookie.value);
    const expDT = decodedToken.exp ? new Date(decodedToken.exp * 1000) : new Date();
    const nowDT = new Date();

    if (expDT < nowDT) {
      doLogout();
    }
  } catch (e) {
    console.error(e);
    doLogout();
  }
}

const menuItems = computed(() => {
  const user = authUserStorage.value;
  if (!user) return [];
  return user.menu_items;
});

const showChilds = ref(menuItems.value ? menuItems.value.map(() => false) : []);

const toggleChilds = (index: number, closeMenu: boolean) => {
  for (let i = 0; i < showChilds.value.length; i++) {
    if (i !== index) {
      showChilds.value[i] = false;
    }
  }
  showChilds.value[index] = !showChilds.value[index];
  if (closeMenu && showChilds.value[index]) {
    menuAbierto.value = false; // Cierra el menú emergente del círculo de la imagen
  }
};

const toggleMenu = () => {
  menuAbierto.value = !menuAbierto.value;
  if (menuAbierto.value) {
    for (let i = 0; i < showChilds.value.length; i++) {
      showChilds.value[i] = false; // Cierra los otros menús desplegables
    }
  }
};
</script>

<style scoped>
body::-webkit-scrollbar {
  width: 12px;
  /* Ancho de toda la barra de desplazamiento */
}

body::-webkit-scrollbar-thumb {
  background-color: transparent;
  /* Color del botón de desplazamiento */
}

body {
  scrollbar-color: transparent orange;
  /* Color del botón de desplazamiento y la barra de desplazamiento */
}

/* Estilo para curvar los bordes superiores de la barra gris */
.sidebar {
  border-top-left-radius: 110px;
  /* Ajusta el valor según tus necesidades */
  border-top-right-radius: 110px;
  /* Ajusta el valor según tus necesidades */
}

/* Estilo para el botón sin borde ni color */
.no-style-button {
  border: none;
  background: none;
  box-shadow: none;
  padding: 0;
  margin: 0;
}
</style>
