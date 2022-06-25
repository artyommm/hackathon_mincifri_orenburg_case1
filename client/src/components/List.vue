<template>
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
      </tr>
    </tbody>
  </table>
</template>
//class="overflow-hidden" пропуск
//class="overflow-auto" скролл
<script>
import {mapState} from "vuex";

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
    })
  },
  async created() {
    this.cards = this.cards_request
  }
}
</script>

<style>
</style>
