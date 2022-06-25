<template>
  <div :class="{
    'basic__wrapper d-flex flex-column justify-content-center' : true,
    'align-items-center' : !isSearch,
    'align-items-start' : isSearch,

  }">
    <div class="d-flex justify-content-center align-items-center">
      <search></search>
    </div>
    <div class="list__home">
      <list @click="search"></list>
    </div>
  </div>
</template>

<script>
import Search from "@/components/Search";
import List from "@/components/List";

export default {
  name: 'HomeView',
  components: {
    Search, List
  },
  data() {
    return {
      isSearch: false
    }
  },
  methods: {
    search() {
      this.isSearch = true;
      console.log(111)
    }
  }
}
</script>

<style>
.basic__wrapper {
  height: 100%;
}
.list__home {
  width: 80%;
}
</style>
