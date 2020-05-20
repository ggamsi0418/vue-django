<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-content>
      <PostDetail>
      </PostDetail>
    </v-content>

    <v-footer app dark>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainMenu from '../components/MainMenu.vue';
  import PostDetail from '../components/PostDetail.vue';


  export default {
    components: {MainMenu, PostDetail},

    data: () => ({
      drawer: false,
    }),
    created () {
      this.$vuetify.theme.dark = false
    },
  }
</script>
