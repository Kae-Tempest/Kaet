import type { IUser, ICreateUser } from "~/types/IUser";
import { Status } from "~/enum/status";

export const userLogin = async (sendData: {
  email: string;
  password: string;
}) => {
  const { data, error, status } = await useCustomFetch<IUser>(
    `/api/users/login`,
    {
      method: "POST",
      body: { user: sendData },
    },
  );

  if (status == Status.SUCCES) return data;
  else throw error;
};

export const userRegister = async (sendData: ICreateUser) => {
  const { data, error, status } = await useCustomFetch<IUser>(
    `/api/users/register`,
    {
      method: "POST",
      body: { user: sendData },
    },
  );

  if (status == Status.SUCCES) return data;
  else throw error;
};
