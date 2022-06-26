
export const publiсationsModule = {
    state: () => ({
        isSearch: false,
        cards: [],
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
                state.cards = []
            }
        },
        setPublications(state, cards) {
            if (!cards)
                state.cards = []
            state.cards = cards;
        },
    },
    namespaced:true,
}