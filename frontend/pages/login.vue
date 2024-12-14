<script setup lang="ts">
import { useAuthQuery } from "~/queries/auth.queries";

definePageMeta({
    layout: false,
});

const sendData = ref({
    email: "",
    password: "",
});

const error = ref<Error>();
const { mutate } = useAuthQuery();

const handleLogin = async () => {
    mutate(sendData.value, {
        onSuccess: async (data) => {
            localStorage.setItem("user", JSON.stringify(data));
            await navigateTo("/");
        },
        onError: (err) => {
            error.value = err;
        },
    });
};
</script>

<template>
    <div class="flex justify-center h-screen items-center">
        <section class="flex flex-col border border-blue-600 p-6 rounded w-1/3">
            <h1 class="text-5xl text-center pb-4">Login</h1>
            <form @submit.prevent="handleLogin" class="flex flex-col w-full">
                <div class="text-red-500 text-center text-lg" v-if="error">
                    {{ error?.message }}
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="email">Email</label>
                    <input
                        id="email"
                        type="email"
                        class="input"
                        v-model="sendData.email"
                    />
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="password">Password</label>
                    <input
                        id="password"
                        type="password"
                        class="input"
                        v-model="sendData.password"
                    />
                </div>
                <div class="flex justify-end gap-2 items-end my-2">
                    <NuxtLink
                        to="/register"
                        class="opacity-65 hover:opacity-100 mr-2"
                        >No Account ?</NuxtLink
                    >
                    <span class="opacity-65 hover:opacity-100 mr-4"
                        >Forgot password ?</span
                    >

                    <UButton
                        label="Login"
                        type="submit"
                        color="blue"
                        class="p-2"
                    />
                </div>
            </form>
        </section>
    </div>
</template>

<style lang="postcss" scoped>
.input {
    @apply hidden w-3/4 lg:flex items-center text-sm leading-6 text-slate-400 rounded-md ring-1 ring-slate-900/10 shadow-sm py-1.5 pl-2 pr-3 hover:ring-slate-300 dark:bg-zinc-800 dark:hover:bg-zinc-700 dark:text-zinc-50;
}
</style>
