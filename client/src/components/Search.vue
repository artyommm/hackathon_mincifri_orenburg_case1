<template>
  <div class="search__wrapper d-flex justify-content-center">
  <form class="search needs-validation" @submit.prevent="submitHandlerSearch"
        :class="{
              'was-validated': isValidate
            }"
        novalidate>
    <div class="search__header d-flex flex-column">
      <div class="search__item">
        <label for="company" class="form-label">Компании</label>
        <select required v-model="v$.company.$model" id="company" class="form-select ">
          <option selected disabled>Выберите предприятие</option>
          <option v-for="company in companies"
                  v-bind:key="company.id"
                  v-bind:value="company.id">
            {{company.name}}
          </option>
        </select>
        <div class="invalid-feedback">
          Поле компании обязательно
        </div>
      </div>
      <div class="search__item">
        <label for="category" class="form-label">Категории</label>
        <select required v-model="v$.category.$model" id="category" class="form-select">
          <option selected disabled>Выберите категории</option>
          <option v-for="category in categories"
                  v-bind:key="category.id"
                  v-bind:value="category.id">
            {{category.name}}
          </option>
        </select>
        <div class="invalid-feedback">
          Поле категории обязательно
        </div>
      </div>
      <div class="search__item">
        <label class="form-label">Промежуток времени</label>
        <div class="search__date">
          <input v-model="date_from" type="date" name='date_from' class="form-control">
          <input v-model="date_to" type="date" name='date_to' class="form-control">
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Поиск</button>
    </div>
<!--    <div class="search__footer input-group mb-3">-->
<!--      <input type="text" class="form-control" placeholder="URL" aria-describedby="button-addon2">-->
<!--      <button class="btn btn-outline-secondary" type="button" id="button-addon2">Поиск</button>-->
<!--    </div>-->
  </form>
  </div>
</template>

<script>
import axios from 'axios';
import {mapMutations} from 'vuex';
import {required} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";

export default {
  name: 'Search',
  data() {
    return {
      v$: useVuelidate(),
      categories: [],
      companies: [],
      isSearch: false,
      category: [],
      company: [],
      date_from: '',
      date_to: '',
      isValidate: false
    }
  },
  validations() {
    return {
      category: {
        required
      },
      company: {
        required
      }
    }
  },
  async created() {
    await axios.get('http://127.0.0.1:5000/api/enterprises/get_all')
        .then(response_companies => {
          this.companies = response_companies.data
        }).catch(error => {
          console.error('Ошибка при создании:', error)
        })
    await axios.get('http://127.0.0.1:5000/api/keywords/get_all')
        .then(response_categories => {
          this.categories = response_categories.data
        }).catch(error => {
          console.error('Ошибка при создании:', error)
        })
  },
  methods: {
    ...mapMutations({
      setPublications: 'cards/setPublications',
      setSearch: 'cards/setSearch'
    }),

    async submitHandlerSearch(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        this.isValidate = true;
        alert('Не все поля выбраны')
      } else {
        await axios.post('http://127.0.0.1:5000/api/search/', {
          headers: {'Content-type': 'application/json'},
          keyword: JSON.stringify(this.category),
          enterprise: JSON.stringify(this.company),
          date_from: this.date_from === '' ? null : this.date_from,
          date_to: this.date_to === '' ? null : this.date_to
        })
            .then(response => {
              this.isSearch = true;
              this.setPublications(response.data);
              this.setSearch(this.isSearch);

              this.$router.push({name: 'list'});
            }).catch(error => {
              console.error('Ошибка при отправке:', error)
            })
      }

    }
  }
}
</script>

<style>
.search__wrapper {
  width: 100%;
}
.search__header {
  margin-bottom: 15px;
}

.search {
  width: 500px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.search__item {
  margin: 10px;
}

.search__date {
  display: flex;
  justify-content: space-between;
}
</style>
