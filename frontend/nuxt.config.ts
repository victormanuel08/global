// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({

  devtools: { enabled: true },
  modules: ["@nuxt/ui"],

  imports: {
    dirs: ['stores'],
  },
  devServer: {
    host: '0.0.0.0',
    port: 3000, // Elige el puerto que desees
  },


  

  compatibilityDate: "2024-07-22",
})