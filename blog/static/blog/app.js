const app = Vue.createApp({
    delimiters:["[[","]]"],
    data() {
        return {
            firstname: "mna",
            title: "test"
        }
    }
})

app.mount('#app')