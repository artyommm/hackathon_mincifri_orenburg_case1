<template>
  <div class="basic__wrapper d-flex flex-column  align-items-center justify-content-center">
    <div>
      <img src="@/assets/home.png" alt="OrenBoogle">
    </div>
    <div class="d-flex justify-content-center align-items-center">
      <search></search>
    </div>
  </div>
</template>

<script>
import Search from "@/components/Search";

export default {
  name: 'HomeView',
  components: {
    Search
  }
}
</script>

<style>
.basic__wrapper {
  height: 100%;
}
</style>
