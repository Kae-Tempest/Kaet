import { Status } from "~/enum/status";
import type { IRestaurant, ICreateRestaurant } from "~/types/IRestaurant";
import type { IReturnedData } from "~/types/IReturnedData";

export const restaurantCreation = async (sendData: ICreateRestaurant) => {
  const { data, error, status } = await useCustomFetch<
    IReturnedData<IRestaurant>
  >(`/api/restaurants`, {
    method: "POST",
    body: sendData,
  });

  if (status == Status.SUCCES) return data?.data;
  else throw error;
};
