import { useMutation } from "@tanstack/vue-query";
import { userLogin, userRegister } from "~/repositories/auth.repository";

export const useAuthQuery = () => {
  return useMutation({
    mutationFn: userLogin,
  });
};

export const useRegisterQuery = () => {
  return useMutation({
    mutationFn: userRegister,
  });
};
