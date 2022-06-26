<template>
  <div class="basic__wrapper d-flex flex-column  align-items-center justify-content-center">
    <div class="list__home">
      <list :isSearch="isSearch"></list>
    </div>
  </div>
</template>

<script>
import List from "@/components/List";
import {mapState} from "vuex";

export default {
  name: 'ListView',
  components: {
    List
  },
  computed: {
    ...mapState({
      isSearch: state => state.cards.isSearch
    })
  }
}
</script>

<style>
.basic__wrapper {
  height: 100%;
}
.list__home {
  height: 100%;
  width: 80%;
  margin-top: 10px;
}
</style>
