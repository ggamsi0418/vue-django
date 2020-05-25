<template>
<v-container>
  <v-data-table
    :headers="headers"
    :items="posts"
    :items-per-page="5"
    sort-by="id"
    class="elevation-1"
    @click:row="serverPage"
  >
    <template v-slot:top>
      <v-toolbar flat color="white">
        <v-toolbar-title>JB's Blog List</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-btn color="primary" dark class="mb-2" v-on="on">New Item</v-btn>
        
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn color="primary" @click="initialize">Reset</v-btn>
    </template>
  </v-data-table>
</v-container>
</template>

<script>
  import axios from "axios";

  export default {
    data: () => ({
        dialog: false,
        headers: [
            {
                text: "ID",
                align: "start",
                sortable: false,
                value: "id"
            },
            { text: "제 목", value: "title" },
            { text: "요 약", value: "description" },
            { text: "작성자", value: "owner.username" },
            { text: "수정일", value: "modify_dt" },
            { text: "Actions", value: "actions", sortable: false }
        ],
        posts: [],
        tagname: "",
        editedIndex: -1,
        editedItem: {
        owner: {}
        },
        actionKind: "",
        me: {}
  }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created () {
      this.fetchPostList();
    },

    methods: {
      fetchPostList() {
        console.log("fetchPostList()...");
        let getUrl = "";
        if (this.tagname) getUrl = `/api/post/list/?tag=${this.tagname}`;
        else getUrl = "/api/post/list/";
        axios(getUrl)
            .then(res => {
                console.log("POST GET RES", res);
                this.posts = res.data;
            })
            .catch(err => {
                console.log("POST GET ERR.RESPONSE", err.responnse);
                alert(err.responnse.status + " " + err.responnse.statusText);
            });
      },
    }
  }
</script>