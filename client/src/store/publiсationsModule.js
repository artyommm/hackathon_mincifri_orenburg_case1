
export const publiсationsModule = {
    state: () => ({
        isSearch: false,
        cards: [],
        allCards: [],
        isAll: false
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
        setAllCards(state, isAll) {
            state.isAll = isAll;
            if(!isAll) {
                state.allCards = []
            }
        },
        setPublications(state, cards) {
            if (!cards)
                state.cards = []
                state.cards = cards;
        },
        setAllPublications(state, cards) {
            if (!cards)
                state.cards = []
            state.allCards = cards;
        },
    },
    namespaced:true,
}