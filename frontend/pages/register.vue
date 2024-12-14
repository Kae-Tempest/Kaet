<script setup lang="ts">
import type { ICreateUser } from "~/types/IUser";
import { useRegisterQuery } from "~/queries/auth.queries";

definePageMeta({
    layout: false,
});

const sendData = ref<ICreateUser>({
    user: {
        name: "",
        last_name: "",
        email: "",
        password: "",
        confirm_password: "",
    },
});

const error = ref<Error>();
const { mutate } = useRegisterQuery();
const handleRegister = async () => {
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
            <h1 class="text-5xl text-center pb-4">Register</h1>
            <form @submit.prevent="handleRegister()" class="flex flex-col">
                <div class="text-red-500 text-center text-lg" v-if="error">
                    {{ error?.message }}
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="name">Name</label>
                    <input
                        id="name"
                        type="text"
                        class="input"
                        required
                        v-model="sendData.user.name"
                    />
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="last_name">Last Name</label>
                    <input
                        id="last_name"
                        type="text"
                        class="input"
                        required
                        v-model="sendData.user.last_name"
                    />
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="email">Email</label>
                    <input
                        id="email"
                        type="email"
                        class="input"
                        required
                        v-model="sendData.user.email"
                    />
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="password">Password</label>
                    <input
                        id="password"
                        type="password"
                        class="input"
                        required
                        minlength="6"
                        v-model="sendData.user.email"
                    />
                </div>
                <div class="flex justify-between items-center my-2 gap-2">
                    <label for="confirm_password">Confirm Password</label>
                    <input
                        id="confirm_password"
                        type="password"
                        class="input"
                        required
                        minlength="6"
                        v-model="sendData.user.confirm_password"
                    />
                </div>
                <div class="flex justify-end gap-2 items-end my-2">
                    <NuxtLink to="/login" class="opacity-65 hover:opacity-100"
                        >Already have account ?</NuxtLink
                    >
                    <UButton
                        label="Register"
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
