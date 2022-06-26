<template>
  <div class="navigation__wrapper d-flex flex-row-reverse">
    <nav class="navigation">
      <div class="d-flex justify-content-around">
        <nav-el
            @click="$router.push('/')"
            :is-active="isSelected('/')"
        >Главная</nav-el>
        <nav-el
            v-if="isSearch"
            @click="$router.push('/list')"
            :is-active="isSelected('/list')"
        >Запрос</nav-el>
        <nav-el
            @click="$router.push('/login')"
            :is-active="isSelected('/login')"
        >Вход</nav-el>
      </div>
    </nav>
  </div>
</template>

<script>
import NavEl from "./NavEl";
import {mapState} from "vuex";

export default {
  components: {
    NavEl
  },
  name: "Navbar",
  data() {
    return {
      burgerIsActive: false
    }
  },
  methods: {
    isSelected(href) { return this.$route.href === href },
  },
  computed: {
    ...mapState({
      isSearch: state => state.cards.isSearch
    })
  }
}
</script>

<style lang="css" scoped>

.navigation__wrapper {
  margin-top: 10px;
}

.navigation {
  width: 350px;
}
</style>