import type { IUser } from "~/types/IUser";
import { Status } from "~/enum/status";
import type { IReturnedData } from "~/types/IReturnedData";

export const updateUser = async (sendData: IUser) => {
  const { data, error, status } = await useCustomFetch<IReturnedData<IUser>>(
    `/api/users/${sendData.id}`,
    {
      method: "PATCH",
      body: { user: sendData },
    },
  );

  if (status == Status.SUCCES) return data;
  else throw error;
};
