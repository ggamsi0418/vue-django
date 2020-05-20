<template>
  <v-app id="inspire">
    <MainMenu></MainMenu>

    <v-content>
      <PostList>
      </PostList>
    </v-content>

    <v-footer app dark>
      <span>&copy; 2020</span>
    </v-footer>
  </v-app>
</template>

<script>
  import MainMenu from '../components/MainMenu.vue';
  import PostList from '../components/PostList.vue';


  export default {
    components: {MainMenu, PostList},

    data: () => ({
      drawer: false,
    }),
    created () {
      this.$vuetify.theme.dark = false
    },
  }
</script>
