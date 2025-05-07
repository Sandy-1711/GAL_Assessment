import { createSlice } from '@reduxjs/toolkit'

const initialState = {
    value: {
        messages: [],
    }
}
const getLocalStorage = (name) => {
    if (typeof window !== 'undefined') {
        return JSON.parse(window.localStorage.getItem(name));
    }
    return null;
};

const setLocalstorage = (name, value) => {
    window.localStorage.setItem(name, JSON.stringify(value));
}


export const chat = createSlice({
    name: "chat",
    initialState: typeof window !== 'undefined' ? getLocalStorage('chatState') || initialState : initialState,
    reducers: {
        clear: () => {
            setLocalstorage('chatState', initialState)
            return initialState;
        },
        addMessage: (state, action) => {
            if (action.payload) {
                setLocalstorage('chatState', { value: { messages: action.payload } });
                return {
                    value: {
                        messages: action.payload,
                    }
                }
            }
            else {
                return initialState
            }
        },

    },
});

export const { clear, addMessage } = chat.actions;
export default chat.reducer;