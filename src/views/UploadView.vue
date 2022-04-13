<script>
    import UploadForm from "../components/UploadForm.vue";
    export default {
        data() {
            return{}
        },
        components: { UploadForm }
    }
</script>
<template>
    <div class="container">
        <UploadForm />
    </div>
</template>

<style scoped>
    .container {
        display: flex;
        flex-direction: column;
    }
</style>