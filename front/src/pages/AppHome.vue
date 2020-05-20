<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-content>
      <Home></Home>
    </v-content>

    <v-footer app dark>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainMenu from '../components/MainMenu.vue';
  import Home from '../components/Home.vue';


  export default {
    components: {MainMenu, Home},

    data: () => ({

    }),

    created () {
      this.$vuetify.theme.dark = false
    },
  }
</script>
