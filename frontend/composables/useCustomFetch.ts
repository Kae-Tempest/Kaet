import type { UseFetchOptions } from "nuxt/app";

export async function useCustomFetch<T>(
  url: string | (() => string),
  options: UseFetchOptions<T> = {},
) {
  const resp = await useFetch(url, {
    ...options,
    $fetch: useNuxtApp().$customFetch,
  });

  let data = resp.data.value;
  let error = resp.error.value?.data || resp.error.value;
  let status: string = resp.status.value;

  return { data, error, status };
}
