<template>
  <div :class="{
    'basic__wrapper d-flex flex-column  align-items-center' : true,
    'justify-content-center ' : !isSearch,
    'justify-content-start' : isSearch,

  }">
    <div class="d-flex justify-content-center align-items-center">
      <search @updateStyle="updateStyle"></search>
    </div>
    <div class="list__home" v-if="isSearch">
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
  },
  data() {
    return {
      isSearch: false
    }
  },
  methods: {
    updateStyle(e) {
      this.isSearch = e.isSearch
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
