<template>
  <div v-if="cards.length > 0">
    <button type="button" @click="createXls" class="btn btn-success">
      <export-excel
          :data="json_data"
          :fields="json_fields"
          :name="file_name">
        Выгрузить в xls
      </export-excel>
    </button>
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
        <td>{{ card.keyword }}</td>
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
import {mapMutations, mapState} from "vuex";
import axios from "axios";

export default {
  name: 'Search',
  props: {
    isAll: Boolean,
    isSearch: Boolean,
  },
  data() {
    return {
      cards: [],
      file_name: '',
      json_fields: {
        'ID': 'id',
        'Наименование предприятия организации': 'enterprise',
        'Дата новости (информации)': 'date_of_publication',
        'Наименование информационного ресурса': 'information_resource',
        'Наименование заголовка новости (информации)': 'title',
        'Ссылка на новость (информацию)': 'publication_url',
        'Категория инвестиционной активности': 'keyword',
      },
      json_data: [],
      json_meta: [
        [
          {
            'key': 'charset',
            'value': 'utf-8'
          }
        ]
      ],
    }
  },
  computed: {
    ...mapState({
      cards_request: state => state.cards.cards,
      isAuth: state => state.auth.isAuth,
      all_cards: state => state.cards.allCards
    }),
  },
  async created() {
    if (this.isSearch) {
      this.cards = this.cards_request;
      const date = new Date();
      this.file_name = `${this.cards[0].enterprise}_${this.cards[0].keyword}_${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}.xls`
      this.json_data = this.cards;
    }
    if (this.isAll) {
      await axios.get('http://127.0.0.1:5000/api/publications/get_all')
          .then(response => {
            //вынести в стор
            this.setAllPublications(response.data);
            this.cards = this.all_cards;
          }).catch(error => {
            console.error('Ошибка при запросе:', error)
          })
    }
  },
  methods: {
    ...mapMutations({
      setAllPublications: 'cards/setAllPublications'
    }),
    createXls() {
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
