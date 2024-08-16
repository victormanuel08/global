// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({

  devtools: { enabled: true },
  modules: ["@nuxt/ui", "@nuxt/icon"],
  
  imports: {
    dirs: ['stores'],
  },
  devServer: {
    host: '0.0.0.0',
    port: 3000, // Elige el puerto que desees
  },
  


  icon: {
    sizes: {
      'xl': '48px'
    }
  },
  

  compatibilityDate: "2024-07-22",
})