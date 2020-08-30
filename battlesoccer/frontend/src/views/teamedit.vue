<template>
  <div class="Teamedit">
    <br><br><br><br>
    <div class="container">
    <h1 class="display-4">Team edit</h1>   
     <form @submit.prevent="onSubmit">
<br>
<div class="form-group">
  <label for="usr">Team_name:</label>
  <input type="text"  v-model='teamname' class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">Team_quotes:</label>
  <input type="text"  v-model='teamquotes' class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">Team_contact:</label>
  <input type="text"  v-model='teamcontact' class="form-control" id="usr">
</div>

      <br>
<button type="submit" class="btn btn-dark">Sumbit</button>

    </form>
    <p v-if="error" class="muted mt-2">{{ error }}</p>
  </div>
  </div>
</template>
<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Teamedit",
  props: {
    id: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      teamname: null,
      teamquotes:null,
      teamcontact:null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.teamname) {
        this.error = "You can't send an empty question!";
      } else if (this.teamname.length > 240) {
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/team/";
        let method = "POST";
        if (this.id !== undefined) {
          endpoint += `${ this.id }/`;
          method = "PUT";
        }
        apiService(endpoint, method, { teamname: this.teamname,
                                        teamquotes: this.teamquotes,
                                        teamcontact:this.teamcontact})
          .then(team => {
            this.$router.push({
              name: 'Userprofile',
              params: { id: team.id }
            })
          })
      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.id !== undefined) {
      let endpoint = `/api/team/${ to.params.id }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.teamname = data.teamname,
                        vm.teamquotes=data.teamquotes,
                        vm.teamcontact=data.teamcontact))
    } else {
      return next();
    }
  },

}
</script>
