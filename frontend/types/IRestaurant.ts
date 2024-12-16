export interface ICreateRestaurant {
    restaurant: {
        name: string;
        country: string;
        number: string;
        street: string;
        is_open: boolean;
        hourly: string | HourlyRestaurant[]
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

type HourlyRestaurant = {
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
    DayList: number[];
}