
export const publiсationsModule = {
    state: () => ({
        isSearch: false,
        publiсations: [],
    }),
    getters: {
        getSearch: state => {
            return state.isSearch
        }
    },
    mutations: {
        setSearch(state, search) {
            state.isSearch = search;
            if(!search) {
                state.publiсations = []
            }
        },
        setPublications(state, publications) {
            if (!publications)
                state.publications = []
            state.publications = publications;
        },
    },
    namespaced:true,
}