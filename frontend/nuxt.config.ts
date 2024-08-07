// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxt/ui"],

  imports: {
    dirs: ['stores'],
  },

  compatibilityDate: "2024-07-22",
})