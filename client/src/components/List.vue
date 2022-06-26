<template>
  <div v-if="cards.length > 0">
    <button type="button" @click="createXls" class="btn btn-success xls">
      <export-excel
          :data="json_data"
          :fields="json_fields"
          :name="file_name">
        Выгрузить в xls
      </export-excel>
    </button>
<!--    <button type="button" @click="$router.go(0)" class="btn btn-danger xls">-->
<!--        Обновить таблицу-->
<!--    </button>-->
    <div class="container">
    <div class="row">
    <div class="col-12">
      <table class="table table-striped">
        <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Предприятие</th>
          <th scope="col">Ресурс</th>
          <th scope="col">Новость</th>
          <th scope="col">Дата</th>
          <th scope="col">Ссылка</th>
          <th scope="col">Категория</th>
          <th v-if="isAuth" scope="col">Удалить</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(card, index) in cards" v-bind:key="card.id">
          <th scope="row">{{ card.id }}</th>
          <td>{{ card.enterprise }}</td>
          <td>{{ card.information_resource }}</td>
          <td>{{ card.title }}</td>
          <td>{{ card.date_of_publication }}</td>
          <td><a :href="card.publication_url">
            URL
          </a></td>
          <td>{{ card.keyword }}</td>
          <td v-if="isAuth">
            <button type="button" @click="deletePublication(card.id, index)" class="btn btn-danger">
              &#9587;
            </button>
          </td>
        </tr>
        </tbody>
      </table>
    </div>
    </div>
    </div>
  </div>
  <div v-else class="noData">
    <div>
      <h1>Данных нет.</h1>
    </div>
    <div>
      <h1>Возможно, идет поиск...</h1>
    </div>
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
    isSearch: Boolean
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
            const date = new Date();
            this.file_name = `${this.cards[0].enterprise}_${this.cards[0].keyword}_${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}.xls`
            this.json_data = this.cards;
          }).catch(error => {
            console.error('Ошибка при запросе:', error)
          })
    }
  },
  methods: {
    ...mapMutations({
      setAllPublications: 'cards/setAllPublications',
      deletePublication: 'cards/deletePublication'
    }),
    //создание при нажатии, не успевает, пришлось при загрузке переносить данные в json
    createXls() {
    },
    async deletePublication(publication_id, card) {
      console.log(publication_id)
      await axios.delete(`http://127.0.0.1:5000/api/delete/${publication_id}`, {
        headers: {'Authorization': `Bearer ${localStorage.getItem('token')}`}
      })
          .then(response => {
            alert('данные удалены, обновление займет время')
            // this.deletePublication(card)
            // this.cards = this.cards_request;
            // const date = new Date();
            // this.file_name = `${this.cards[0].enterprise}_${this.cards[0].keyword}_${date.getDate()}.${date.getMonth() + 1}.${date.getFullYear()}.xls`
            // this.json_data = this.cards;
            // const data = [];
            // this.cards.map(el => {
            //   console.log(el)
            //   if (el.id !== card.id)
            //     data.push(el)
            // })
            // this.cards = data;
            // console.log(this.cards)
          }).catch(error => {
            console.error('Ошибка при запросе:', error)
          })
    }
  }
}
</script>

<style>
.xls {
  margin: 10px;
}

.noData {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%;
}
</style>
