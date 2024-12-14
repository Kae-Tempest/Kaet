<script setup lang="ts">
import CreateRestaurant from "~/components/Modal/CreateRestaurant.vue";

const user = useCheckUser();

const showModal = ref<boolean>(false);
if (!user.value?.restaurant_id) {
    showModal.value = true;
}
</script>

<template>
    <CreateRestaurant v-if="user" v-model="showModal" v-model:user="user" />
</template>
