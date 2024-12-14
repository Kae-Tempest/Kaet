<script lang="ts" setup>
import DatePicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";
import type { ICreateRestaurant, IRestaurant } from "~/types/IRestaurant";
import type { IUser } from "~/types/IUser";
import { useCreateRestaurantQuery } from "~/queries/restaurant.queries";
import { useUpdateUser } from "~/queries/user.queries";

const showModal = defineModel({ required: true, default: false });
const user = defineModel<IUser>("user", { required: true });
const sendData = ref<ICreateRestaurant>({
    restaurant: {
        name: "",
        country: "",
        number: "",
        street: "",
        is_open: true,
        hourly: {
            open_at: {
                hours: "",
                minutes: "",
                seconds: "",
            },
            closed_at: {
                hours: "",
                minutes: "",
                seconds: "",
            },
        },
    },
});

const error = ref<Error>();
const { mutate } = useCreateRestaurantQuery();
const { mutate: userMutate } = useUpdateUser();
const handleCreateRestaurant = async () => {
    let data: ICreateRestaurant = sendData.value;
    data.restaurant.hourly = JSON.stringify(data.restaurant.hourly);
    mutate(data, {
        onSuccess: async (data) => {
            if (data?.id) {
                user.value.restaurant_id = data.id;
                // update user's restaurant_id in db
                userMutate(user.value, {
                    onSuccess: async (data) => {
                        console.log(data, "user");
                        // save new user in localStorage
                        localStorage.setItem("user", JSON.stringify(data));
                        // close modal
                        showModal.value = false;
                    },
                    onError: (err: Error) => (error.value = err),
                });
            }
        },
        onError: (err: Error) => {
            error.value = err;
        },
    });
};
</script>

<template>
    <UModal v-model="showModal" prevent-close>
        <UCard>
            <h2 class="text-2xl text-center my-2">Create you're Restaurant</h2>
            <div v-if="error" class="text-red-500 text-center text-lg">
                {{ error?.message }}
            </div>
            <form @submit.prevent="handleCreateRestaurant">
                <UFormGroup label="Name" :ui="{ wrapper: 'py-2' }">
                    <UInput
                        color="primary"
                        variant="outline"
                        placeholder="Name"
                        v-model="sendData.restaurant.name"
                        required
                    />
                </UFormGroup>
                <UFormGroup label="Country" :ui="{ wrapper: 'py-2' }">
                    <UInput
                        color="primary"
                        variant="outline"
                        placeholder="Country"
                        v-model="sendData.restaurant.country"
                        required
                    />
                </UFormGroup>
                <UFormGroup label="Street" :ui="{ wrapper: 'py-2' }">
                    <UInput
                        color="primary"
                        variant="outline"
                        placeholder="Street"
                        v-model="sendData.restaurant.street"
                        required
                    />
                </UFormGroup>
                <UFormGroup label="Number" :ui="{ wrapper: 'py-2' }">
                    <UInput
                        color="primary"
                        variant="outline"
                        placeholder="number"
                        v-model="sendData.restaurant.number"
                        required
                    />
                </UFormGroup>

                <UFormGroup
                    label="Opening Time"
                    :ui="{ container: 'flex flex-row gap-2 py-2' }"
                >
                    <DatePicker
                        v-model="sendData.restaurant.hourly.open_at"
                        time-picker
                        :is-24="false"
                        minutes-increment="5"
                        minutes-grid-increment="5"
                        :clearable="false"
                        auto-apply
                    />

                    <DatePicker
                        v-model="sendData.restaurant.hourly.closed_at"
                        time-picker
                        :is-24="false"
                        minutes-increment="5"
                        minutes-grid-increment="5"
                        :clearable="false"
                        auto-apply
                    />
                </UFormGroup>

                <div class="flex justify-end w-full mt-4">
                    <UButton label="Create" type="submit" />
                </div>
            </form>
        </UCard>
    </UModal>
</template>
