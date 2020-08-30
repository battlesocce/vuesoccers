<template>
  <div class="ody">
    <br><br><br><br>
    <div class="container-sm">
      <div v-if="!id">
    <h1 >Add player</h1></div>
    <div v-if="id">
    <h1 >Update player</h1></div>
    <br>
  <transition name="fade">
    <div class="alert alert-danger" role="alert" v-if="error">
{{ error }}
</div></transition>
<div v-if="!id">
<transition name="fade">
<div class="alert alert-success" role="alert"  v-if="savingSuccessful" >
  Player added successfully
</div>
</transition></div>
<div v-if="id">
<transition name="fade">
<div class="alert alert-success" role="alert"  v-if="savingSuccessful" >
 updated successfully
</div>
</transition></div>
    <form @submit.prevent="onSubmit">
<div class="form-group">
  <label for="usr">Name:</label>
  <input type="text"  v-model='player' maxlength="20" class="form-control" id="usr" autofocus>
</div>

<div class="form-group">
  <label for="usr">Age:</label>
  <input type="text"  v-model='age' class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">Contact:</label>
  <input type="text"  v-model='contact' class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">Player_passcode:</label>
  <input type="text"  v-model='playerpasscode' class="form-control" id="usr">
</div>


<div class="form-group">
  <label for="usr">profession:</label>
  <input type="text"  v-model='profession' class="form-control" id="usr">
</div>


<div class="form-group">
  <label for="usr">Insta_Id:</label>
  <input type="text"  v-model='instaurl' class="form-control" id="usr">
</div>



<div class="form-group">
  <label for="usr">Facebook_Id:</label>
  <input type="text"  v-model='facebookurl' class="form-control" id="usr">
</div>

<div class="form-group">
  <label for="usr">Position:</label>
  <input type="text"  v-model='position' class="form-control" id="usr">
</div>


<div class="form-group">
  <label for="usr">Description:</label>
  <input type="text"  v-model='description' class="form-control" id="usr">
</div>

      <br>
<button type="submit" class="btn btn-dark">Add</button>

    </form>
  </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: "Addplayer",
  props: {
    id: {
      type: Number,
      required: false
    }
  },
  data() {
    return {
      player: null,
      age: null,
      playerpasscode: null,
      contact: null,
      profession: null,
      facebookurl: null,
      instaurl: null,
      position: null,
      description: null,
      error: null,
      savingSuccessful: false
    }
  },
  methods: {
    onSubmit() {
      // Tell the REST API to create or update a Question Instance
      if (!this.player) {
        this.error = "You can't send an empty question!";
     this.savingSuccessful= false;
      } else if (this.player.length > 240) {
       this.savingSuccessful= false;
        this.error = "Ensure this field has no more than 240 characters!";
      } else {
        let endpoint = "/api/player/";
        let method = "POST";
        if (this.id !== undefined) {
          endpoint += `${ this.id }/`;
          method = "PUT";
        }
        apiService(endpoint, method, { player: this.player, 
                                        age: this.age,
                                        playerpasscode: this.playerpasscode,
                                        contact: this.contact,
                                        profession:this.profession,
                                        facebookurl: this.facebookurl,
                                        instaurl: this.instaurl,
                                        position: this.position,
                                        description: this.description,
                                        })
                                       .then(response => {
  console.log('SUCCESS!!');
      this.player= "";
      this.age= "";
      this.playerpasscode= "";
      this.contact= "";
      this.profession= "";
      this.facebookurl= "";
      this.instaurl= "";
      this.position= "";
      this.description= "";
      this.error="";
      this.savingSuccessful= true;
      if (this.id){
    this.$router.push({
              name: 'Userprofile',
              params: { id: response.id }
            })        }
        return response
        

})
      

      }
    }
  },
  async beforeRouteEnter(to, from, next) {
    // if the component will be used to update a question, then get the question's data from the REST API
    if (to.params.id !== undefined) {
      let endpoint = `/api/player/${ to.params.id }/`;
      let data = await apiService(endpoint);
      return next(vm => (vm.player = data.player, 
                         vm.age = data.age,
                         vm.playerpasscode = data.playerpasscode,
                         vm.contact = data.contact,
                         vm.profession = data.profession,
                         vm.facebookurl = data.facebookurl,
                         vm.instaurl = data.instaurl,
                         vm.position = data.position,
                         vm.description = data.description))
                         
} else {
      return next();
    }
  },
}
</script>
