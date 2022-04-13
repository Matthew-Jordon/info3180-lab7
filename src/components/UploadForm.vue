<template>
    <form id="uploadForm" @submit.prevent="uploadPhoto">
            <textarea name="description" cols="2" rows="4" class="form-control" placeholder="Enter description of photo"></textarea>
            <input type="file" name="photo" class="form-control">
            <input type="submit" class="btn btn-primary">
    </form>
</template>
<script>
    export default{
        data() {
            return {
                csrf_token: ''
            }
        },
        methods: {
            uploadPhoto() {
                let uploadForm = document.getElementById('uploadForm');
                let form_data = new FormData(uploadForm)
                console.log(...form_data);
                fetch('/api/upload', {
                    method: 'POST',
                    body: form_data,
                    headers: {
                        'X-CSRFToken': this.csrf_token
                    }
                }).then((response) => {
                    return response.json();
                }).then((data) => {
                    console.log(data)
                }).catch((error) => {
                    console.log(error)
                })
            },
            getCsrfToken() {
                let self = this;
                fetch('/api/csrf-token')
                .then((response)=> response.json())
                .then((data)=> {
                    console.log(data)
                    self.csrf_token = data.csrf_token
                    })
            }
        },
        created() {
            this.getCsrfToken();
        }
    }
</script>

<style scoped>

div {
    margin: 1pc;
}

</style>