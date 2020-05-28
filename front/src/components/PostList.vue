<template>
<v-container>
  <v-data-table
    :headers="headers"
    :items="posts"
    :items-per-page="5"
    sort-by="id"
    class="elevation-1"
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
        <v-btn
          color="primary"
          dark
          class="mb-2"
          @click.stop="dialogOpen('post_create', null)"
        >New Item</v-btn>
        
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

  <v-dialog v-model="dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ formTitle }}</span>
        </v-card-title>
        <v-card-text>
          <v-form id="post-form" ref="postForm">
            <v-text-field label="ID" name="id" v-model="editedItem.id"/>
            <v-text-field label="Title" name="title" v-model="editedItem.title" />
            <v-text-field label="Description" name="description" v-model="editedItem.description" />
            <v-textarea outlined label="Content" name="content" v-model="editedItem.content" />
            <v-text-field label="Owner" name="owner" v-model="editedItem.owner.username" />
            <v-text-field label="Tags" name="tags" v-model="editedItem.tags" />
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="cancel">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="save">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

</v-container>
</template>

<script>
  import axios from "axios";

  axios.defaults.xsrfCookieName = "csrftoken";
  axios.defaults.xsrfHeaderName = "X-CSRFToken";
  axios.defaults.headers.common["X-Requested-With"] = "XMLHttpRequest";

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
        if (this.actionKind === "post_create") return "Create Post";
        else return "Update Post";
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
      
      dialogOpen(kind, item) {
        console.log("dialogOpen()...", kind, item);
        
        this.actionKind = kind; // CRUD 액션을 구분하기 위함

        if (kind === "post_create") {
          this.dialog = true;
          this.editedIndex = -1;
          this.editedItem = {
            owner: {}
          };
        } 
      },
      cancel() {
        console.log("cancel()...");
        this.dialog = false;
      },
      save() {
        console.log("save()...");
        this.dialog = false;
        console.log(this.actionKind)
        if (this.actionKind === "post_create") this.createPost();
        // else if (this.actionKind === "post_update") this.updatePost();
        this.actionKind = "";
      },
      createPost() {
        console.log("createPost()...");
        const postData = new FormData(document.getElementById("post-form"));
        // postData.set("owner", this.me.id);
        axios
          .post("/api/post/create/", postData)
          .then(res => {
            console.log("CREATE POST RES", res);
            this.posts.push(res.data);
          })
          .catch(err => {
            console.log("CREATE POST ERR.RESPONSE", err.response);
            alert(err.response.status + " " + err.response.statusText);
          });
      },
    }
  }
</script>