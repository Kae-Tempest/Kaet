import type { IUser } from "~/types/IUser";

export const useCheckUser: () => Ref<IUser | null> = (): Ref<IUser | null> => {
  const user: Ref<IUser | null> = ref<IUser | null>(null);
  if (process.client) {
    const localUser = window.localStorage.getItem("user");
    if (localUser) {
      user.value = JSON.parse(localUser!).data;
    }
    if (!user || user === null || !localUser || localUser === null) {
      navigateTo("/login");
    }
    return user;
  }
  return user;
};
