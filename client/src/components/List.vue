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
      <tr v-for="publiсation in publiсations" v-bind:key="publiсation.id">
        <th scope="row">{{ publiсation.id }}</th>
        <td>{{ publiсation.enterprise }}</td>
        <td>{{ publiсation.information_resource }}</td>
        <td>{{ publiсation.title }}</td>
        <td>{{ publiсation.date_of_publication }}</td>
        <td>{{ publiсation.publication_url }}</td>
        <td>
          <span v-for="(category, index) in publiсation.categories" v-bind:key="index">
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

export default {
  name: 'Search',
  data() {
    return {
      publiсations: [
        {
          id: 1,
          title: 'публикация 1',
          date_of_publication:'11.01.2002',
          publication_url:'http/pizdec',
          information_resource: 'blabla',
          enterprise: 'super',
          categories: [
            {id: 1, name: 'категория 1'},
            {id: 2, name: 'категория 2'}
          ]
        },
        {
          id: 2,
          title: 'публикация 2',
          date_of_publication:'11.01.2002',
          publication_url:'http/pizdec',
          information_resource: 'blabla',
          enterprise: 'super',
          categories: [
            {id: 1, name: 'категория 3'},
            {id: 2, name: 'категория 2'}
          ]
        },
        {
          id: 3,
          title: 'публикация 3',
          date_of_publication:'11.01.2002',
          publication_url:'http/pizdec',
          information_resource: 'blabla',
          enterprise: 'super',
          categories: [
            {id: 1, name: 'категория 1'},
            {id: 2, name: 'категория 3'}
          ]
        },
      ]
    }
  }
}
</script>

<style>
</style>
