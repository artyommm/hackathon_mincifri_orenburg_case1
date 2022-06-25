<template>
  <div class="basic__wrapper d-flex flex-column justify-content-center align-items-center">
    <div class="d-flex justify-content-center align-items-center">
      <search></search>
    </div>
    <div class="list__home">
      <list></list>
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
