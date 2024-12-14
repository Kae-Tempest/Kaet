<script lang="ts" setup>
const links = [
    [
        {
            label: "Reservation",
            icon: "material-symbols:book-4",
            to: "/reservation",
        },
        {
            label: "Table",
            icon: "material-symbols:table-restaurant-rounded",
            to: "/table",
        },
    ],
    [
        {
            label: "Login",
            icon: "",
            to: "/login",
        },
        {
            label: "Register",
            icon: "",
            to: "/register",
        },
    ],
];
</script>

<template>
    <div class="w-screen h-screen max-h-screen flex">
        <nav class="w-[10%] h-full border-r border-blue-600">
            <h1 class="text-4xl text-center">Kaeat</h1>
            <UVerticalNavigation
                :ui="{
                    wrapper:
                        'flex flex-col justify-between h-[calc(100vh-40px)]',
                }"
                :links="links"
            />
        </nav>
        <div class="flex-grow">
            <slot />
        </div>
    </div>
</template>
