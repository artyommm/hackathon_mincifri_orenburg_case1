import {createStore} from "vuex";
import {publiсationsModule} from "./publiсationsModule";
import {authModule} from "./authModule";


export default createStore({
  modules: {
    cards: publiсationsModule,
    auth: authModule
  }
})