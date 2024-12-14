import type { IUser } from "~/types/IUser";

export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig();
  const user = useCheckUser();
  let token: string | null;
  if (!user.value) token = null;
  else token = user.value.token;
  const $customFetch = $fetch.create({
    baseURL: config.public.apiBase,
    credentials: "include",
    headers: {
      Authorization: `Bearer ${token}`,
    },
    onRequest({ request, options, error }) {
      options.headers = new Headers({
        Authorization: `Bearer ${token}`,
      });
    },
    onResponse({ response }) {},
    onResponseError({ response, error }) {},
  });
  // Expose to useNuxtApp().$customFetch
  return {
    provide: {
      customFetch: $customFetch,
    },
  };
});
