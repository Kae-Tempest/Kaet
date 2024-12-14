export interface ICreateRestaurant {
  restaurant: {
    name: string;
    country: string;
    number: string;
    street: string;
    is_open: boolean;
    hourly:
      | string
      | {
          open_at: {
            hours: string;
            minutes: string;
            seconds: string;
          };
          closed_at: {
            hours: string;
            minutes: string;
            seconds: string;
          };
        };
  };
}
export interface IRestaurant {
  id?: number;
  name: string;
  country: string;
  number: string;
  street: string;
  is_open: boolean;
  hourly: string;
}
