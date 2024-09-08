<template>
    <div class="flex gap-3 bg-gray-100 border" style="height: calc(150vh - 50px) !important">
        <!-- Barra lateral -->
        <div class="w-48 bg-gray-100 hidden md:block  ">  
            <div class="py-5 text-center">
                <img src="@/assets/img/GLOBALIPS.png" alt="GLOBAL" class="object-contain w-full md:w-1/1 lg:w-1/1">
            </div>
            <div v-for="(item, index) in menuItems" :key="item.path" class="my-4">
                <UButton  class="rounded-full"  @click="toggleChilds(index)"
                    style="width: 200px; white-space: normal;" :to="item.path" >
                    <Icon :name="item.icon" style="color: white; font-size: 1.5em;" />
                    {{ item.label }}
                </UButton>
                <div class="my-2" style="text-align: right;">
                    <UButton style="width: 150px; white-space: normal; text-align: right;" 
                        v-for="subItem in item?.childs" :key="subItem.path" class="rounded-full" 
                        variant="soft" v-if="showChilds[index]" :to="subItem.path" >
                        <Icon :name="subItem.icon" style="color: blue; font-size: 1.5em;" />
                        {{ subItem.label }}
                    </UButton>
                </div>
            </div>

        </div>

        <!-- Contenido principal -->
        <div class="flex-grow bg-white  rounded-lg">
            <!-- Menú a la derecha (visible solo en pantallas grandes) -->
            <div class="p-2 bg-gray-100 rounded-full shadow m-4 text-right hidden md:block">
                {{ user.username }} {{ user.first_name }} {{ user.last_name }}
                <UButton @click="doLogout">Cerrar sesión</UButton>
            </div>

            <div class="bg-gray-100 rounded-full shadow m-2 text-center block md:hidden">
                <span v-for="(item, index) in menuItems" :key="item.path" class="p-1"
                    :style="{ marginBottom: index < menuItems.length - 1 ? '10rem' : '5' }">
                    <UButton :to="item.path" class="rounded-full"  @click="toggleChilds(index)">
                        <Icon :name="item.icon" style="color: white; font-size: 1.5em;" />
                    </UButton>
                    <span class="p-1">
                        <UButton  v-for="subItem in item?.childs" :key="subItem.path"
                            class="rounded-full"  variant="soft" v-if="showChilds[index]" :to="subItem.path">       
                            <Icon :name="subItem.icon" style="color: blue; font-size: 1.5em;" />
                        </UButton>
                    </span>
                </span>
                <UButton @click="doLogout" class="rounded-full">Salir</UButton>
            </div>

            <slot></slot>
        </div>
    </div>
</template>

<script setup lang="ts">

const authUserStorage = useAuthUserStorage()
const authTokensStorage = useAuthTokensStorage()
const user = computed(() => authUserStorage.value)
const tokenCookie = useCookie('token')

const menuItems = computed(() => {
    const user = authUserStorage.value
    if (!user) return []
    return user.menu_items
})

const loader = (path: string) => {
   // useRouter().push(path)
}

const showChilds = ref(menuItems.value ? menuItems.value.map(() => false) : []);


const toggleChilds = (index: number) => {
// aca 
    for (let i = 0; i < showChilds.value.length; i++) {
        if (i !== index) {
            showChilds.value[i] = false;
        }
    }

    showChilds.value[index] = !showChilds.value[index];
}


const doLogout = () => {
    tokenCookie.value = null
    authUserStorage.value = {}
    authTokensStorage.accessToken.value = null
    authTokensStorage.refreshToken.value = null
    useRouter().push('/')
}

</script>

<style scoped>
body::-webkit-scrollbar {
  width: 12px; /* Ancho de toda la barra de desplazamiento */
}

body::-webkit-scrollbar-thumb {
  background-color: transparent; /* Color del botón de desplazamiento */
}

body {
  scrollbar-color: transparent orange; /* Color del botón de desplazamiento y la barra de desplazamiento */
}
</style>
