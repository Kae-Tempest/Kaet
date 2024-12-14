import { useMutation } from "@tanstack/vue-query";
import { restaurantCreation } from "~/repositories/restaurant.reposity";

export const useCreateRestaurantQuery = () => {
  return useMutation({
    mutationFn: restaurantCreation,
  });
};
