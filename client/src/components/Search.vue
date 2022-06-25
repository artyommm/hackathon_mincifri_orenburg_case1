<template>
  <div class="search__wrapper d-flex justify-content-center">
  <form class="search">
    <div class="search__header d-flex flex-column">
      <div class="search__item">
        <select class="form-select ">
          <option selected disabled>Выберите предприятие</option>
          <option v-for="company in companies" v-bind:key="company.id" value="{{company.id}}">{{company.name}}</option>
        </select>
      </div>
      <div class="search__item">
        <select class="form-select choices-multiple" multiple>
<!--          <option selected disabled>Выберите категории</option>-->
          <option v-for="category in categories" v-bind:key="category.id" value="{{category.id}}">{{category.name}}</option>
        </select>
      </div>
      <button type="button" class="btn btn-primary">Поиск</button>
    </div>
<!--    <div class="search__footer input-group mb-3">-->
<!--      <input type="text" class="form-control" placeholder="URL" aria-describedby="button-addon2">-->
<!--      <button class="btn btn-outline-secondary" type="button" id="button-addon2">Поиск</button>-->
<!--    </div>-->
  </form>
  </div>
</template>

<script>

export default {
  name: 'Search',
  data() {
    return {
      categories: [
        {id: 1, name: 'категория 1'},
        {id: 2, name: 'категория 2'},
        {id: 3, name: 'категория 3'}
      ],
      companies: [
        {id: 1, name: 'компания 1'},
        {id: 2, name: 'компания 2'},
        {id: 3, name: 'компания 3'}
      ]
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
</style>
