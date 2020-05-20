<template>
  <v-container>
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      dark
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Settings</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Vue - Dajgno Blog App</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text href="/">Home</v-btn>
      <v-btn text href="/post_list.html">List</v-btn>
      <v-btn text href="#">Admin</v-btn>
      <v-spacer></v-spacer>

    </v-app-bar>
  </v-container>
</template>

<script>
  export default {

    data: () => ({
      drawer: false,
    }),
    
  }
</script>

