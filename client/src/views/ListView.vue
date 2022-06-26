<template>
  <div class="basic__wrapper d-flex flex-column  align-items-center justify-content-center">
    <div class="list__home">
      <list></list>
    </div>
  </div>
</template>

<script>
import List from "@/components/List";

export default {
  name: 'ListView',
  components: {
    List
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
