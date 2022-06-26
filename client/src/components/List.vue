<template>
  <div v-if="cards.length > 0">
    <table class="table table-striped">
      <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Предприятие</th>
        <th scope="col">Ресурс</th>
        <th scope="col">Новость</th>
        <th scope="col">Дата</th>
        <th scope="col">Ссылка</th>
        <th scope="col">Категории</th>
        <th v-if="isAuth" scope="col">Архив</th>
        <th v-if="isAuth" scope="col">Удалить</th>
      </tr>
      </thead>
      <tbody>
      <tr v-for="card in cards" v-bind:key="card.id">
        <th scope="row">{{ card.id }}</th>
        <td>{{ card.enterprise }}</td>
        <td>{{ card.information_resource }}</td>
        <td>{{ card.title }}</td>
        <td>{{ card.date_of_publication }}</td>
        <td>{{ card.publication_url }}</td>
        <td>
          <span v-for="(category, index) in card.categories" v-bind:key="index">
            {{ category.name }}
          </span>
        </td>
        <td v-if="isAuth">
          <button type="button" class="btn btn-secondary">Архив</button>
        </td>
        <td v-if="isAuth">
          <button type="button" class="btn btn-danger">
            &#9587;
          </button>
        </td>
      </tr>
      </tbody>
    </table>
  </div>
  <div v-else class="noData">
    <h1>Данных по заданным фильтрам нет( <br> перейдите во вкладку главная</h1>
  </div>
</template>
//class="overflow-hidden" пропуск
//class="overflow-auto" скролл
<script>
import {mapState} from "vuex";
import axios from "axios";

export default {
  name: 'Search',
  data() {
    return {
      cards: []
    }
  },
  computed: {
    ...mapState({
      cards_request: state => state.cards.cards,
      isSearch: state => state.cards.isSearch,
      isAuth: state => state.auth.isAuth,
      isAll: state => state.cards.isAll
    })
  },
  async created() {
    if (this.isSearch && !this.isAll)
      this.cards = this.cards_request
    if (this.isAll) {
      await axios.get('http://127.0.0.1:5000/api/search/all/')
          .then(response => {
            this.setPublications(response.data);
          }).catch(error => {
            console.error('Ошибка при запросе:', error)
          })
    }
  }
}
</script>

<style>
.noData {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>
