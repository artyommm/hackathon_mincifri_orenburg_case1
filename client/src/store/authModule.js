import axios from "axios";


export const authModule = {
    state: () => ({
        isAuth: false
    }),
    getters: {
        getAuth: state => {
            return state.isAuth
        }
    },
    mutations: {
        setAuth(state, auth) {
            state.isAuth = auth;
            if(!auth) {
                state.currentUser = []
            }
        }
    },
    actions: {
        async checkAuth({state, commit}) {
            if(localStorage.getItem('token')) {
                commit('setAuth', true)
                try {
                    const response = await axios.get('http://127.0.0.1:5000/api/user/info',  {
                        headers: {Authorization:`Bearer ${localStorage.getItem('token')}`},
                    })
                    commit('setAuth', true)
                } catch (error) {
                    alert('Проблема авторизации')
                    if (Number(error.response.status) === 409) {
                        commit('setAuth', false)
                        await this.$router.push({ name: 'login'})
                        localStorage.clear()
                    }
                } finally {
                }
            } else {
                commit('setAuth', false)
            }
        }
    },
    namespaced:true,
}