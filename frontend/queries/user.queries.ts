import { useMutation } from "@tanstack/vue-query";
import { updateUser } from "~/repositories/user.repository";

export const useUpdateUser = () => {
  return useMutation({
    mutationFn: updateUser,
  });
};
