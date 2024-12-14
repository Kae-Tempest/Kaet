export interface IUser {
  id: number;
  name: string;
  last_name: string;
  email: string;
  token: string;
  restaurant_id: number;
}

export interface ICreateUser {
  user: {
    name: string;
    last_name: string;
    email: string;
    password: string;
    confirm_password: string;
  };
}
