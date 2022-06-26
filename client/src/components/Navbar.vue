<template>
  <div class="navigation__wrapper d-flex flex-row-reverse">
    <nav class="navigation">
      <div
          class="d-flex justify-content-around">
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
            v-if="!isAuth"
            @click="$router.push('/login')"
            :is-active="isSelected('/login')"
        >Вход</nav-el>
        <nav-el
            v-if="isAuth"
            @click="all_list"
            :is-active="isSelected('/all_list')"
        >Публикации</nav-el>
        <nav-el
            v-if="isAuth"
            @click="update"
            :is-active="isSelected('/update')"
        >Обновить</nav-el>
        <nav-el
            v-if="isAuth"
            @click="logout"
            :is-active="isSelected('/logout')"
        >Выход</nav-el>
      </div>
    </nav>
  </div>
</template>

<script>
import NavEl from "./NavEl";
import {mapMutations, mapState} from 'vuex';

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
    ...mapMutations({
      setAuth: 'auth/setAuth',
      setSearch: 'cards/setSearch',
      setAllCards: 'cards/setAllCards'
    }),
    isSelected(href) { return this.$route.href === href },
    logout() {
      this.setAuth(false)
      this.setSearch(false)
      localStorage.clear();
      this.$router.push('/login');
    },

    update() {
      // this.setAuth(false)
      // localStorage.clear();
      // this.$router.push('/login');
    },

    all_list() {
      this.setAllCards(true);
      this.$router.push('/all_list');
    }
  },
  computed: {
    ...mapState({
      isSearch: state => state.cards.isSearch,
      isAuth: state => state.auth.isAuth
    })
  }
}
</script>

<style lang="css" scoped>

.navigation__wrapper {
  margin-top: 10px;
}

.navigation {
  width: 500px;
}
</style>