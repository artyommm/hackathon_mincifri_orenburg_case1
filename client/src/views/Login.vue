<template>
  <div class="d-flex flex-column justify-content-center align-items-center login__container">
    <div class="login__wrapper">
      <h1 class="login__header">Вход</h1>
      <form @submit.prevent="submitHandler"
            class="d-flex flex-column needs-validation"
            :class="{
              'was-validated': isValidate
            }"
            novalidate>
        <div class="login__item">
          <label for="login" class="form-label">Адрес электронной почты</label>
          <input
              required
              minlength="3"
              id="login"
              type="text"
              class="form-control"
              placeholder="Логин"
              v-model.trim="v$.login.$model"
          >
          <div class="invalid-feedback">
            Поле логин некорректно (минимум 3 символа)
          </div>
        </div>
        <div class="login__item">
          <label for="password" class="form-label">Пароль</label>
          <input
              required
              minlength="5"
              id="password"
              type="password"
              class="form-control"
              placeholder="Пароль"
              v-model.trim="v$.password.$model"
          >
          <div class="invalid-feedback">
            Поле пароль некорректно (минимум 5 символа)
          </div>
        </div>
        <button class="btn btn-primary" type="submit">
          Вход
        </button>
  </form>
    </div>
  </div>
</template>

<script>
import {required, minLength} from '@vuelidate/validators'
import useVuelidate from "@vuelidate/core";
import axios from "axios";
import {mapMutations, mapState} from 'vuex';
const Buffer = require('buffer').Buffer;

export default {
  name: "Login",
  data() {
    return {
      v$: useVuelidate(),
      password: '',
      login: '',
      isValidate: false
    }
  },
  validations() {
    return {
      login: {
        required,
        minLength: minLength(3)
      },
      password: {
        required,
        minLength: minLength(5)
      }
    }
  },
  methods: {
    ...mapMutations({
      setAuth: 'auth/setAuth'
    }),

    async submitHandler(e) {
      this.v$.$touch()
      if (this.v$.$invalid) {
        this.isValidate = true;
        alert('Информация не корректна')
      } else {
        const username = this.v$.login.$model
        const password = this.v$.password.$model
        const token = Buffer.from(`${username}:${password}`, 'utf8').toString('base64')

        await axios.get('http://127.0.0.1:5000/api/auth/auth', {
          headers: {'Authorization': `Basic ${token}`}
        }).then(response => {
          localStorage.setItem('token', response.data.token);
          this.setAuth(true);
          this.$router.push('/');
        }).catch(error => {
          console.error('Ошибка авторизации', error)
          if (error.request.status === 401)
            alert('Пользователя не существует')
        })
      }
    }
  },
  computed: {
    ...mapState({
      isAuth: state => state.auth.isAuth
    }),
  }
}
</script>

<style scoped>
.login__wrapper {
  width: 350px;
}

.login__container {
  width: 100%;
  height: 100%;
}

.login__header {
  width: 100%;
  display: flex;
  justify-content: center;
}

.login__item {
  margin: 10px;
}
</style>