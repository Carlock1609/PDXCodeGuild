// const url = 'https://jsonplaceholder.typicode.com/todos/1'
const url = 'https://favqs.com/api/quotes'

axios.get(url, {
    headers: {
        'Authorization': `Token token="YOUR_API_KEY"`
    }
})
.then(request => {
    // logic to work on data
    console.log(request.data)
})
.catch(error => console.log(error))

