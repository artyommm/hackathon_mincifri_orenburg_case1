<template>
  <div className="basic__wrapper d-flex flex-column  align-items-center justify-content-center">
    <div className="list__home">
      <list :isAll="isAll"></list>
    </div>
  </div>
</template>

<script>
import List from "@/components/List";
import {mapState} from "vuex";

export default {
  name: 'AllListView',
  components: {
    List
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth,
      isAll: state => state.cards.isAll
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
